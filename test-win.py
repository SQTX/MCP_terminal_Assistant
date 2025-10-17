from mcp.server.fastmcp import FastMCP
import subprocess
from typing import List
import os
import time

mcp = FastMCP("Test-Windows")

_powershell_process = None      # PowerShell-Process variable
_session_id = str(os.getpid())  # Unique session ID based on current process ID

def ensure_powershell_window():
    """
    Creates a single PowerShell window on first call.
    """
    global _powershell_process

    #* Open first PowerShell window if not already created
    if _powershell_process is None or _powershell_process.poll() is not None:
        os.makedirs("C:\\temp\\mcp", exist_ok=True) # Create temp directory for command/output files

        #* PowerShell script to run in new window
        ps_script = f'''
        $sessionId = "{_session_id}"
        Write-Host "=== MCP PowerShell Session ===" -ForegroundColor Cyan
        Write-Host "Session ID: $sessionId" -ForegroundColor Gray
        Write-Host ""

        while ($true) {{
            $cmdFile = "C:\\temp\\mcp\\$sessionId.cmd"
            $outputFile = "C:\\temp\\mcp\\$sessionId.output"

            if (Test-Path $cmdFile) {{
                $cmd = Get-Content $cmdFile -Raw -Encoding UTF8
                Remove-Item $cmdFile

                Write-Host "PS> $cmd" -ForegroundColor Green

                # Execute command and capture output
                try {{
                    $output = Invoke-Expression $cmd 2>&1 | Out-String
                    Set-Content $outputFile -Value $output -Encoding UTF8
                    Write-Host $output
                }} catch {{
                    $errorMsg = $_.Exception.Message
                    Set-Content $outputFile -Value "ERROR: $errorMsg" -Encoding UTF8
                    Write-Host "ERROR: $errorMsg" -ForegroundColor Red
                }}

                Write-Host ""
            }}
            Start-Sleep -Milliseconds 200
        }}
        '''

        #* Start new PowerShell process in a separate window
        _powershell_process = subprocess.Popen(
            ["powershell.exe", "-NoExit", "-Command", ps_script],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

        #* Give some time for the PowerShell window to initialize
        time.sleep(1)

    return _powershell_process


def run_command(cmd: str) -> str:
    """
    Executes a command in the existing PowerShell window (Windows)
    and returns its result to the LLM client.
    The command is executed ONLY ONCE.
    """
    try:
        #* Ensure PowerShell window is running
        ensure_powershell_window()

        cmd_file = f"C:\\temp\\mcp\\{_session_id}.cmd"
        output_file = f"C:\\temp\\mcp\\{_session_id}.output"

        #* Remove existing output file if any
        if os.path.exists(output_file):
            os.remove(output_file)

        #* Save command to file
        with open(cmd_file, "w", encoding="utf-8") as f:
            f.write(cmd)

        #* Wait for output file to be created (30 seconds timeout)
        timeout = 30
        start_time = time.time()

        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                return f"Timeout during executed: {cmd}"
            time.sleep(0.1)

        #* Read output from file
        time.sleep(0.1)                     # Delay to ensure file is fully written
        with open(output_file, "r", encoding="utf-8") as f:
            output = f.read().strip()

        #* Remove output file after reading
        os.remove(output_file)

        return f"Executed: {cmd}\n\n{output}"

    except Exception as e:
        return f"Executed error '{cmd}': {e}"


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
        history.append(f"PS> {cmd}\n{output}")  # Store command and its output

    #* Return full history as single string
    return "\n\n".join(history)


#* Run MCP server
if __name__ == "__main__":
    mcp.run()