# from mcp.server.fastmcp import FastMCP
# import subprocess
# from typing import List

# mcp = FastMCP("Test-Windows")


# def run_in_terminal(commands: List[str], shell: str = "cmd"):
#     """
#     Otwiera nowe okno terminala Windows (cmd lub PowerShell) i wykonuje listę poleceń.
    
#     Args:
#         commands (List[str]): Polecenia do uruchomienia.
#         shell (str): "cmd" lub "powershell".
#     """
#     if shell == "cmd":
#         # Łączymy komendy w jeden ciąg połączony '&&' (wykona sekwencyjnie)
#         joined_commands = " && ".join(commands)
#         # /K - zostawia okno otwarte po wykonaniu
#         subprocess.Popen(["cmd.exe", "/K", joined_commands])

#     elif shell == "powershell":
#         joined_commands = "; ".join(commands)
#         # -NoExit żeby zostawić okno otwarte
#         subprocess.Popen(["powershell.exe", "-NoExit", "-Command", joined_commands])

#     else:
#         raise ValueError("shell musi być 'cmd' lub 'powershell'")


# @mcp.tool()
# def run_commands(commands: List[str], shell: str = "cmd") -> str:
#     """
#     MCP tool: przyjmuje listę poleceń i uruchamia je w CMD lub PowerShell.
    
#     Args:
#         commands (List[str]): Lista poleceń do wykonania.
#         shell (str): 'cmd' lub 'powershell'.
#     """
#     try:
#         if not commands:
#             return "⚠️ Lista poleceń jest pusta"
        
#         run_in_terminal(commands, shell)
#         return f"✅ Wysłano {len(commands)} poleceń do {shell}"
#     except Exception as e:
#         return f"❌ Błąd: {e}"


# if __name__ == "__main__":
#     mcp.run()





# ============================================
# FAJNIE DZIAŁA
# ============================================


# from mcp.server.fastmcp import FastMCP
# import subprocess
# from typing import List

# mcp = FastMCP("Test-Windows")

# def run_commands_in_background(commands: List[str], shell: str = "cmd") -> str:
#     """
#     Wykonuje listę poleceń w powłoce cmd lub powershell, zwraca output.
#     """
#     if not commands:
#         return "⚠️ Lista poleceń jest pusta"
    
#     if shell == "cmd":
#         joined_commands = " && ".join(commands)
#         # wykonanie w cmd, capture output
#         result = subprocess.run(["cmd.exe", "/c", joined_commands], capture_output=True, text=True)
#     elif shell == "powershell":
#         joined_commands = "; ".join(commands)
#         result = subprocess.run(["powershell.exe", "-Command", joined_commands], capture_output=True, text=True)
#     else:
#         return "❌ Błąd: shell musi być 'cmd' lub 'powershell'"

#     if result.returncode == 0:
#         return f"✅ Polecenia wykonane pomyślnie:\n{result.stdout}"
#     else:
#         return f"❌ Błąd wykonania:\n{result.stderr}"

# @mcp.tool()
# def run_commands(commands: List[str], shell: str = "cmd") -> str:
#     try:
#         return run_commands_in_background(commands, shell)
#     except Exception as e:
#         return f"❌ Błąd: {e}"


# if __name__ == "__main__":
#     mcp.run()




# from mcp.server.fastmcp import FastMCP
# import subprocess
# from typing import List

# mcp = FastMCP("Test-Windows")

# def run_in_terminal_live(commands: List[str], shell: str = "cmd") -> str:
#     """
#     Otwiera nowe okno terminala Windows i wykonuje polecenia na żywo (output widoczny).
    
#     Args:
#         commands (List[str]): Lista poleceń do wykonania.
#         shell (str): 'cmd' lub 'powershell'.
    
#     Zwraca komunikat potwierdzający uruchomienie.
#     """
#     if not commands:
#         return "⚠️ Lista poleceń jest pusta"
    
#     if shell == "cmd":
#         # Łączymy polecenia z '&&' aby wykonać jedno po drugim
#         joined_commands = " && ".join(commands)
#         # /K - pozostawia okno otwarte po wykonaniu
#         subprocess.Popen(["cmd.exe", "/K", joined_commands])
    
#     elif shell == "powershell":
#         joined_commands = "; ".join(commands)
#         # -NoExit - pozostawia okno otwarte po wykonaniu
#         subprocess.Popen(["powershell.exe", "-NoExit", "-Command", joined_commands])
    
#     else:
#         return "❌ Błąd: shell musi być 'cmd' lub 'powershell'"

#     return f"✅ Wysłano {len(commands)} poleceń do {shell}, nowe okno terminala powinno się otworzyć."


# @mcp.tool()
# def run_commands(commands: List[str], shell: str = "cmd") -> str:
#     try:
#         return run_in_terminal_live(commands, shell)
#     except Exception as e:
#         return f"❌ Błąd: {e}"


# if __name__ == "__main__":
#     mcp.run()





# from mcp.server.fastmcp import FastMCP
# import subprocess
# from typing import List

# # Tworzymy serwer MCP
# mcp = FastMCP("Test-Windows")

# def run_in_terminal(commands: List[str], shell: str = "cmd") -> None:
#     """
#     Otwiera nowe okno terminala i uruchamia polecenia.
#     """
#     if not commands:
#         return

#     if shell == "cmd":
#         joined_commands = " && ".join(commands)
#         subprocess.Popen(["cmd.exe", "/K", joined_commands])
#     elif shell == "powershell":
#         joined_commands = "; ".join(commands)
#         subprocess.Popen(["powershell.exe", "-NoExit", "-Command", joined_commands])
#     else:
#         raise ValueError("shell musi być 'cmd' lub 'powershell'")

# @mcp.tool()
# def execute_in_new_terminal(commands: List[str], shell: str = "cmd") -> str:
#     """
#     Odbiera polecenia, uruchamia je w nowym oknie terminala.
#     Nie zwraca wyniku, bo użytkownik widzi to w otwartym oknie.
#     """
#     try:
#         if not commands:
#             return "⚠️ Lista poleceń jest pusta"

#         run_in_terminal(commands, shell)
#         return f"✅ Otworzono nowe okno terminala i uruchomiono {len(commands)} poleceń w {shell}"
#     except Exception as e:
#         return f"❌ Błąd: {e}"

# if __name__ == "__main__":
#     mcp.run()






from mcp.server.fastmcp import FastMCP
import subprocess
from typing import List

# MCP serwer
mcp = FastMCP("Test-Windows")


import subprocess
from typing import List

def run_in_terminal(commands: List[str], shell: str = "cmd"):
    if not commands:
        return

    if shell == "cmd":
        joined = " && ".join(commands)
        command = f'start cmd.exe /K "{joined}"'
        subprocess.Popen(command, shell=True)

    elif shell == "powershell":
        joined = "; ".join(commands)
        command = f'start powershell.exe -NoExit -Command "{joined}"'
        subprocess.Popen(command, shell=True)

    else:
        raise ValueError("shell musi być 'cmd' lub 'powershell'")



@mcp.tool()
def execute_in_new_terminal(commands: List[str], shell: str = "cmd") -> str:
    """
    MCP tool: uruchamia komendy w nowym oknie terminala.
    """
    try:
        if not commands:
            return "⚠️ Podaj przynajmniej jedno polecenie"
        run_in_terminal(commands, shell)
        return f"✅ Uruchomiono terminal z {len(commands)} poleceniami"
    except Exception as e:
        return f"❌ Błąd: {e}"


if __name__ == "__main__":
    mcp.run()
