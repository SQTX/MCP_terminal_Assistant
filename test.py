from mcp.server.fastmcp import FastMCP
import subprocess
from typing import List

mcp = FastMCP("Test")

_iterm_window_id = None # iTerm2-Window-ID variable

def ensure_iterm_window():
    """
    Creates a single iTerm2 window on first call
    and remembers its ID for subsequent commands.
    """
    global _iterm_window_id

    #* Open first iTerm window if not already created
    if _iterm_window_id is None:
        #* Communication with iTerm via AppleScript, open new window and get its ID
        apple_script = '''
        tell application "iTerm"
            set newWindow to (create window with default profile)
            set windowID to id of newWindow
            activate
            return windowID
        end tell
        '''

        result = subprocess.run(
            ["osascript", "-e", apple_script],
            capture_output=True,
            text=True
        )

        _iterm_window_id = result.stdout.strip()

    return _iterm_window_id



def run_command(cmd: str) -> str:
    """
    Executes a command in the existing iTerm2 window (macOS)
    and returns its result to the LLM client.
    """
    try:
        #* Run command and capture output
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = (result.stdout + "\n" + result.stderr).strip() # Capture both stdout and stderr into single string

        #* Send command to iTerm2 window
        window_id = ensure_iterm_window()

        #* Convert characters to escaped format
        escaped_cmd = cmd.replace('"', '\\"').replace("'", "\\'")

        #* Send asynchronous AppleScript command to iTerm2
        subprocess.Popen([
            "osascript", "-e",
            f'''
            tell application "iTerm"
                tell first window whose id is {window_id}
                    tell current session
                        write text "{escaped_cmd}"
                    end tell
                end tell
            end tell
            '''
        ])

        #* Return output to LLM
        return f"Executed: {cmd}\n\n{output}"
    except Exception as e:
        return f"Executed error: '{cmd}': {e}"


@mcp.tool()
def run_interactive(commands: List[str]) -> str:
    """
    MCP tool: executes commands one by one.
    After each command returns the result, which can be analyzed by the LLM
    to generate the next command.
    """
    history = []    # All results history

    #* Run each command and collect outputs
    for cmd in commands:
        output = run_command(cmd)               # Execute command and get output
        history.append(f"$ {cmd}\n{output}")    # Store command and its output

    #* Return full history as single string
    return "\n\n".join(history)


#* Run MCP server
if __name__ == "__main__":
    mcp.run()