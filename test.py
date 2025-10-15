# # =========================================================================
# # Niedziałające próby użycia iTerm2 z MCP i AppKit
# # =========================================================================
# # from mcp.server.fastmcp import FastMCP
# # import asyncio
# # import AppKit 
# # import iterm2

# # mcp = FastMCP("Test")

# # async def run_commands_via_ssh(session, ssh_command: str, commands: list[str]):
# #     """
# #     Wysyła do sesji komendę SSH, a następnie kolejne komendy.
# #     """
# #     await session.async_send_text(ssh_command + "\n")
# #     await asyncio.sleep(1)  # krótka pauza, można zamiast tego czekać na prompt

# #     for cmd in commands:
# #         await session.async_send_text(cmd + "\n")
# #         await asyncio.sleep(0.5)


# # async def ssh_run(connection, ssh_host: str, commands: list[str]):
# #     """
# #     Uruchamia nowe okno iTerm2, łączy się przez SSH i wysyła komendy.
# #     """
# #     app = await iterm2.async_get_app(connection)
# #     await app.async_activate()

# #     window = await iterm2.Window.async_create(connection)
# #     if window is None:
# #         return "❌ Nie udało się utworzyć nowego okna"

# #     session = window.current_tab.current_session
# #     ssh_cmd = f"ssh {ssh_host}"

# #     await run_commands_via_ssh(session, ssh_cmd, commands)
# #     return f"✅ Wysłano {len(commands)} komend na {ssh_host}"


# # @mcp.tool()
# # def run_ssh_commands(host: str, commands: list[str]) -> str:
# #     """
# #     Otwiera iTerm2, łączy się z hostem SSH i uruchamia listę komend.
# #     Args:
# #         host: adres hosta SSH np. "user@server.com"
# #         commands: lista komend do uruchomienia
# #     """
# #     try:
# #         # Upewnij się, że iTerm2 działa
# #         AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm2")

# #         # Uruchamiamy pętlę iTerm2 z MCP
# #         result = iterm2.run_until_complete(lambda conn: ssh_run(conn, host, commands), retry=True)
# #         return result
# #     except Exception as e:
# #         return f"❌ Błąd: {e}"


# # if __name__ == "__main__":
# #     mcp.run()


# # from mcp.server.fastmcp import FastMCP
# # import asyncio
# # import AppKit
# # import iterm2

# # mcp = FastMCP("Test")


# # async def run_commands_via_ssh(session, ssh_command: str, commands: list[str]):
# #     """
# #     Wysyła do sesji komendę SSH, a następnie kolejne komendy.
# #     """
# #     await session.async_send_text(ssh_command + "\n")
# #     await asyncio.sleep(1)  # krótka pauza, można zamiast tego czekać na prompt

# #     for cmd in commands:
# #         await session.async_send_text(cmd + "\n")
# #         await asyncio.sleep(0.5)


# # async def ssh_run(connection, ssh_host: str, commands: list[str]):
# #     """
# #     Uruchamia nowe okno iTerm2, łączy się przez SSH i wysyła komendy.
# #     """
# #     app = await iterm2.async_get_app(connection)
# #     await app.async_activate()

# #     window = await iterm2.Window.async_create(connection)
# #     if window is None:
# #         return "❌ Nie udało się utworzyć nowego okna"

# #     session = window.current_tab.current_session
# #     ssh_cmd = f"ssh {ssh_host}"

# #     await run_commands_via_ssh(session, ssh_cmd, commands)
# #     return f"✅ Wysłano {len(commands)} komend na {ssh_host}"


# # @mcp.tool()
# # def run_hello(host: str) -> str:
# #     """
# #     Proste narzędzie, które w terminalu SSH wyświetli 'Hello world'.
# #     Args:
# #         host: adres hosta SSH np. "user@server.com"
# #     """
# #     try:
# #         # Upewnij się, że iTerm2 działa
# #         AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm2")

# #         # Uruchamiamy pętlę iTerm2 z MCP
# #         result = iterm2.run_until_complete(
# #             lambda conn: ssh_run(conn, host, ["echo Hello world"]),
# #             retry=True
# #         )
# #         return result
# #     except Exception as e:
# #         return f"❌ Błąd: {e}"


# # if __name__ == "__main__":
# #     mcp.run()


# # import iterm2
# # import AppKit
# # import objc
# # from mcp.server.fastmcp import FastMCP

# # mcp = FastMCP("Test")

# # async def run_hello_in_terminal(connection):
# #     app = await iterm2.async_get_app(connection)
# #     await app.async_activate()

# #     window = await iterm2.Window.async_create(connection)
# #     if window is None:
# #         return "❌ Nie udało się utworzyć nowego okna"

# #     session = window.current_tab.current_session
# #     await session.async_send_text("echo Hello world\n")
# #     return "✅ Wysłano komendę 'Hello world'"

# # @mcp.tool()
# # def run_hello() -> str:
# #     try:
# #         # Poprawny sposób otwarcia iTerm2 w PyObjC 9+
# #         NSWorkspace = objc.lookUpClass("NSWorkspace")
# #         workspace = NSWorkspace.sharedWorkspace()
# #         workspace.launchApplication_("iTerm2")

# #         result = iterm2.run_until_complete(run_hello_in_terminal, retry=True)
# #         return result
# #     except Exception as e:
# #         return f"❌ Błąd: {e}"

# # if __name__ == "__main__":
# #     mcp.run()


# # from mcp.server.fastmcp import FastMCP
# # import subprocess

# # mcp = FastMCP("Test")

# # @mcp.tool()
# # def run_hello() -> str:
# #     """
# #     Otwiera nowe okno iTerm2 i wypisuje 'Hello world' lokalnie, bez AppKit.
# #     """
# #     try:
# #         # Uruchomienie iTerm2 z komendą echo Hello world
# #         subprocess.run([
# #             "osascript", "-e",
# #             'tell application "iTerm2" to create window with default profile; '
# #             'tell current window to tell current session to write text "echo Hello world"'
# #         ])
# #         return "✅ Wysłano komendę 'Hello world' do iTerm2"
# #     except Exception as e:
# #         return f"❌ Błąd: {e}"

# # if __name__ == "__main__":
# #     mcp.run()


# # =========================================================================
# # Działające, proste narzędzie MCP otwierające iTerm2 i wysyłające komendę
# # =========================================================================

# # from mcp.server.fastmcp import FastMCP
# # import subprocess

# # mcp = FastMCP("Test")


# # def run_in_iterm(cmd: str):
# #     """
# #     Otwiera nowe okno iTerm2 i wysyła komendę.
# #     """
# #     applescript = f'''
# #     tell application "iTerm2"
# #         activate
# #         try
# #             set newWindow to (create window with default profile)
# #         on error
# #             -- jeśli nie da się utworzyć nowego okna, użyj aktualnego
# #             set newWindow to current window
# #         end try
# #         tell current session of newWindow
# #             write text "{cmd}"
# #         end tell
# #     end tell
# #     '''
# #     subprocess.run(["osascript", "-e", applescript])


# # @mcp.tool()
# # def hello_iterm() -> str:
# #     """
# #     MCP tool: otwiera iTerm2 i wysyła 'echo Hello from AppleScript'.
# #     """
# #     try:
# #         run_in_iterm("echo Hello from AppleScript")
# #         return "✅ Komenda wysłana do iTerm2"
# #     except Exception as e:
# #         return f"❌ Błąd: {e}"


# # if __name__ == "__main__":
# #     mcp.run()


# # from mcp.server.fastmcp import FastMCP
# # import subprocess

# # mcp = FastMCP("Test")


# # def run_in_iterm(commands: list[str]):
# #     """
# #     Otwiera nowe okno iTerm2 i wysyła kolejne komendy po kolei.
# #     """
# #     # Budujemy sekwencję poleceń do AppleScript
# #     script_lines = []
# #     for cmd in commands:
# #         script_lines.append(f'write text "{cmd}"')
# #     joined_commands = "\n".join(script_lines)

# #     applescript = f'''
# #     tell application "iTerm2"
# #         activate
# #         try
# #             set newWindow to (create window with default profile)
# #         on error
# #             -- jeśli nie da się utworzyć nowego okna, użyj aktualnego
# #             set newWindow to current window
# #         end try
# #         tell current session of newWindow
# #             {joined_commands}
# #         end tell
# #     end tell
# #     '''
# #     subprocess.run(["osascript", "-e", applescript])


# # @mcp.tool()
# # def hello_iterm() -> str:
# #     """
# #     MCP tool: otwiera iTerm2 i wysyła kilka komend jedna po drugiej.
# #     """
# #     try:
# #         run_in_iterm([
# #             "echo Pierwsza komenda",
# #             "pwd",
# #             "ls -l",
# #             "echo ✅ Wszystkie komendy wykonane"
# #         ])
# #         return "✅ Sekwencja poleceń wysłana do iTerm2"
# #     except Exception as e:
# #         return f"❌ Błąd: {e}"


# # if __name__ == "__main__":
# #     mcp.run()



# # =========================================================================
# # Last version: narzędzie MCP przyjmujące listę poleceń i wysyłające je do iTerm2
# # =========================================================================

# # from mcp.server.fastmcp import FastMCP
# # import subprocess
# # from typing import List

# # mcp = FastMCP("Test")


# # def run_in_iterm(commands: List[str]):
# #     """
# #     Otwiera nowe okno iTerm2 i wysyła kolejne komendy po kolei.
# #     """
# #     script_lines = []
# #     for cmd in commands:
# #         script_lines.append(f'write text "{cmd}"')
# #     joined_commands = "\n".join(script_lines)

# #     applescript = f'''
# #     tell application "iTerm2"
# #         activate
# #         try
# #             set newWindow to (create window with default profile)
# #         on error
# #             -- jeśli nie da się utworzyć nowego okna, użyj aktualnego
# #             set newWindow to current window
# #         end try
# #         tell current session of newWindow
# #             {joined_commands}
# #         end tell
# #     end tell
# #     '''
# #     subprocess.run(["osascript", "-e", applescript])


# # @mcp.tool()
# # def run_commands(commands: List[str]) -> str:
# #     """
# #     MCP tool: przyjmuje listę poleceń i wysyła je do iTerm2.
# #     Niech cigi znaków w polceniu wyznaczone będą przez pojedyczny cudzysłów (`'`).
    
# #     Args:
# #         commands (List[str]): Lista poleceń do wykonania w iTerm2.
# #     """
# #     try:
# #         if not commands:
# #             return "⚠️ Lista poleceń jest pusta"
        
# #         run_in_iterm(commands)
# #         return f"✅ Wysłano {len(commands)} poleceń do iTerm2"
# #     except Exception as e:
# #         return f"❌ Błąd: {e}"


# # if __name__ == "__main__":
# #     mcp.run()

# #* =========================================================================
# #* Wersja z uruchamianiem komend w oknach terminala i zwracaniem outputu do LLM
# #* =========================================================================
# from mcp.server.fastmcp import FastMCP
# import subprocess
# from typing import List

# mcp = FastMCP("Test")

# def run_command(cmd: str) -> str:
#     """
#     Uruchamia komendę w nowym oknie iTerm2 (macOS)
#     i zwraca jej wynik do klienta LLM.
#     """
#     try:
#         # 1️⃣ Uruchom komendę w tle i zbierz output
#         result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
#         output = (result.stdout + "\n" + result.stderr).strip()

#         # 2️⃣ Otwórz nowe okno iTerm2 z tą samą komendą
#         subprocess.Popen([
#             "osascript", "-e",
#             f'''
#             tell application "iTerm"
#                 create window with default profile
#                 tell current session of current window
#                     write text "{cmd}"
#                 end tell
#                 activate
#             end tell
#             '''
#         ])

#         # 3️⃣ Zwróć wynik do LLM
#         return f"✅ Uruchomiono: {cmd}\n\n{output.strip()}"
#     except Exception as e:
#         return f"❌ Błąd uruchamiania '{cmd}': {e}"

# @mcp.tool()
# def run_interactive(commands: List[str]) -> str:
#     """
#     MCP tool: uruchamia listę poleceń po kolei.
#     Po każdym poleceniu zwraca wynik, który może być analizowany przez LLM
#     w celu wygenerowania następnego polecenia.
#     """
#     history = []
#     for cmd in commands:
#         output = run_command(cmd)
#         history.append(f"$ {cmd}\n{output}")
#     return "\n\n".join(history)

# if __name__ == "__main__":
#     mcp.run()


#* =========================================================================
#* Wersja wykca polecenia w pojedynczym oknie terminala i zwracaniem outputu do LLM
#* =========================================================================
from mcp.server.fastmcp import FastMCP
import subprocess
from typing import List

mcp = FastMCP("Test")

# Przechowujemy ID okna iTerm2 dla sesji
_iterm_window_id = None

def ensure_iterm_window():
    """
    Tworzy jedno okno iTerm2 przy pierwszym wywołaniu
    i zapamiętuje jego ID dla kolejnych poleceń.
    """
    global _iterm_window_id
    
    if _iterm_window_id is None:
        script = '''
        tell application "iTerm"
            set newWindow to (create window with default profile)
            set windowID to id of newWindow
            activate
            return windowID
        end tell
        '''
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True
        )
        _iterm_window_id = result.stdout.strip()
    
    return _iterm_window_id

def run_command(cmd: str) -> str:
    """
    Uruchamia komendę w istniejącym oknie iTerm2 (macOS)
    i zwraca jej wynik do klienta LLM.
    """
    try:
        # 1️⃣ Uruchom komendę i zbierz output
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = (result.stdout + "\n" + result.stderr).strip()

        # 2️⃣ Wyślij komendę do istniejącego okna iTerm2
        window_id = ensure_iterm_window()
        
        # Escape cudzysłowów w komendzie
        escaped_cmd = cmd.replace('"', '\\"').replace("'", "\\'")
        
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

        # 3️⃣ Zwróć wynik do LLM
        return f"✅ Uruchomiono: {cmd}\n\n{output}"
    except Exception as e:
        return f"❌ Błąd uruchamiania '{cmd}': {e}"

@mcp.tool()
def run_interactive(commands: List[str]) -> str:
    """
    MCP tool: uruchamia listę poleceń po kolei.
    Po każdym poleceniu zwraca wynik, który może być analizowany przez LLM
    w celu wygenerowania następnego polecenia.
    """
    history = []
    for cmd in commands:
        output = run_command(cmd)
        history.append(f"$ {cmd}\n{output}")
    return "\n\n".join(history)

if __name__ == "__main__":
    mcp.run()