from mcp.server.fastmcp import FastMCP
import subprocess
from typing import List

mcp = FastMCP("Test-Windows")


def run_in_terminal(commands: List[str], shell: str = "cmd"):
    """
    Otwiera nowe okno terminala Windows (cmd lub PowerShell) i wykonuje listę poleceń.
    
    Args:
        commands (List[str]): Polecenia do uruchomienia.
        shell (str): "cmd" lub "powershell".
    """
    if shell == "cmd":
        # Łączymy komendy w jeden ciąg połączony '&&' (wykona sekwencyjnie)
        joined_commands = " && ".join(commands)
        # /K - zostawia okno otwarte po wykonaniu
        subprocess.Popen(["cmd.exe", "/K", joined_commands])

    elif shell == "powershell":
        joined_commands = "; ".join(commands)
        # -NoExit żeby zostawić okno otwarte
        subprocess.Popen(["powershell.exe", "-NoExit", "-Command", joined_commands])

    else:
        raise ValueError("shell musi być 'cmd' lub 'powershell'")


@mcp.tool()
def run_commands(commands: List[str], shell: str = "cmd") -> str:
    """
    MCP tool: przyjmuje listę poleceń i uruchamia je w CMD lub PowerShell.
    
    Args:
        commands (List[str]): Lista poleceń do wykonania.
        shell (str): 'cmd' lub 'powershell'.
    """
    try:
        if not commands:
            return "⚠️ Lista poleceń jest pusta"
        
        run_in_terminal(commands, shell)
        return f"✅ Wysłano {len(commands)} poleceń do {shell}"
    except Exception as e:
        return f"❌ Błąd: {e}"


if __name__ == "__main__":
    mcp.run()