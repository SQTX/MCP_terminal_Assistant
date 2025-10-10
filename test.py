# =========================================================================
# Niedziałające próby użycia iTerm2 z MCP i AppKit
# =========================================================================
# from mcp.server.fastmcp import FastMCP
# import asyncio
# import AppKit 
# import iterm2

# mcp = FastMCP("Test")

# async def run_commands_via_ssh(session, ssh_command: str, commands: list[str]):
#     """
#     Wysyła do sesji komendę SSH, a następnie kolejne komendy.
#     """
#     await session.async_send_text(ssh_command + "\n")
#     await asyncio.sleep(1)  # krótka pauza, można zamiast tego czekać na prompt

#     for cmd in commands:
#         await session.async_send_text(cmd + "\n")
#         await asyncio.sleep(0.5)


# async def ssh_run(connection, ssh_host: str, commands: list[str]):
#     """
#     Uruchamia nowe okno iTerm2, łączy się przez SSH i wysyła komendy.
#     """
#     app = await iterm2.async_get_app(connection)
#     await app.async_activate()

#     window = await iterm2.Window.async_create(connection)
#     if window is None:
#         return "❌ Nie udało się utworzyć nowego okna"

#     session = window.current_tab.current_session
#     ssh_cmd = f"ssh {ssh_host}"

#     await run_commands_via_ssh(session, ssh_cmd, commands)
#     return f"✅ Wysłano {len(commands)} komend na {ssh_host}"


# @mcp.tool()
# def run_ssh_commands(host: str, commands: list[str]) -> str:
#     """
#     Otwiera iTerm2, łączy się z hostem SSH i uruchamia listę komend.
#     Args:
#         host: adres hosta SSH np. "user@server.com"
#         commands: lista komend do uruchomienia
#     """
#     try:
#         # Upewnij się, że iTerm2 działa
#         AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm2")

#         # Uruchamiamy pętlę iTerm2 z MCP
#         result = iterm2.run_until_complete(lambda conn: ssh_run(conn, host, commands), retry=True)
#         return result
#     except Exception as e:
#         return f"❌ Błąd: {e}"


# if __name__ == "__main__":
#     mcp.run()


# from mcp.server.fastmcp import FastMCP
# import asyncio
# import AppKit
# import iterm2

# mcp = FastMCP("Test")


# async def run_commands_via_ssh(session, ssh_command: str, commands: list[str]):
#     """
#     Wysyła do sesji komendę SSH, a następnie kolejne komendy.
#     """
#     await session.async_send_text(ssh_command + "\n")
#     await asyncio.sleep(1)  # krótka pauza, można zamiast tego czekać na prompt

#     for cmd in commands:
#         await session.async_send_text(cmd + "\n")
#         await asyncio.sleep(0.5)


# async def ssh_run(connection, ssh_host: str, commands: list[str]):
#     """
#     Uruchamia nowe okno iTerm2, łączy się przez SSH i wysyła komendy.
#     """
#     app = await iterm2.async_get_app(connection)
#     await app.async_activate()

#     window = await iterm2.Window.async_create(connection)
#     if window is None:
#         return "❌ Nie udało się utworzyć nowego okna"

#     session = window.current_tab.current_session
#     ssh_cmd = f"ssh {ssh_host}"

#     await run_commands_via_ssh(session, ssh_cmd, commands)
#     return f"✅ Wysłano {len(commands)} komend na {ssh_host}"


# @mcp.tool()
# def run_hello(host: str) -> str:
#     """
#     Proste narzędzie, które w terminalu SSH wyświetli 'Hello world'.
#     Args:
#         host: adres hosta SSH np. "user@server.com"
#     """
#     try:
#         # Upewnij się, że iTerm2 działa
#         AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm2")

#         # Uruchamiamy pętlę iTerm2 z MCP
#         result = iterm2.run_until_complete(
#             lambda conn: ssh_run(conn, host, ["echo Hello world"]),
#             retry=True
#         )
#         return result
#     except Exception as e:
#         return f"❌ Błąd: {e}"


# if __name__ == "__main__":
#     mcp.run()


# import iterm2
# import AppKit
# import objc
# from mcp.server.fastmcp import FastMCP

# mcp = FastMCP("Test")

# async def run_hello_in_terminal(connection):
#     app = await iterm2.async_get_app(connection)
#     await app.async_activate()

#     window = await iterm2.Window.async_create(connection)
#     if window is None:
#         return "❌ Nie udało się utworzyć nowego okna"

#     session = window.current_tab.current_session
#     await session.async_send_text("echo Hello world\n")
#     return "✅ Wysłano komendę 'Hello world'"

# @mcp.tool()
# def run_hello() -> str:
#     try:
#         # Poprawny sposób otwarcia iTerm2 w PyObjC 9+
#         NSWorkspace = objc.lookUpClass("NSWorkspace")
#         workspace = NSWorkspace.sharedWorkspace()
#         workspace.launchApplication_("iTerm2")

#         result = iterm2.run_until_complete(run_hello_in_terminal, retry=True)
#         return result
#     except Exception as e:
#         return f"❌ Błąd: {e}"

# if __name__ == "__main__":
#     mcp.run()


# from mcp.server.fastmcp import FastMCP
# import subprocess

# mcp = FastMCP("Test")

# @mcp.tool()
# def run_hello() -> str:
#     """
#     Otwiera nowe okno iTerm2 i wypisuje 'Hello world' lokalnie, bez AppKit.
#     """
#     try:
#         # Uruchomienie iTerm2 z komendą echo Hello world
#         subprocess.run([
#             "osascript", "-e",
#             'tell application "iTerm2" to create window with default profile; '
#             'tell current window to tell current session to write text "echo Hello world"'
#         ])
#         return "✅ Wysłano komendę 'Hello world' do iTerm2"
#     except Exception as e:
#         return f"❌ Błąd: {e}"

# if __name__ == "__main__":
#     mcp.run()


# =========================================================================
# Działające, proste narzędzie MCP otwierające iTerm2 i wysyłające komendę
# =========================================================================

from mcp.server.fastmcp import FastMCP
import subprocess

mcp = FastMCP("Test")


def run_in_iterm(cmd: str):
    """
    Otwiera nowe okno iTerm2 i wysyła komendę.
    """
    applescript = f'''
    tell application "iTerm2"
        activate
        try
            set newWindow to (create window with default profile)
        on error
            -- jeśli nie da się utworzyć nowego okna, użyj aktualnego
            set newWindow to current window
        end try
        tell current session of newWindow
            write text "{cmd}"
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", applescript])


@mcp.tool()
def hello_iterm() -> str:
    """
    MCP tool: otwiera iTerm2 i wysyła 'echo Hello from AppleScript'.
    """
    try:
        run_in_iterm("echo Hello from AppleScript")
        return "✅ Komenda wysłana do iTerm2"
    except Exception as e:
        return f"❌ Błąd: {e}"


if __name__ == "__main__":
    mcp.run()