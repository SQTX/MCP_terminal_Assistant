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






# from mcp.server.fastmcp import FastMCP
# import subprocess
# from typing import List

# # MCP serwer
# mcp = FastMCP("Test-Windows")


# import subprocess
# from typing import List

# def run_in_terminal(commands: List[str], shell: str = "cmd"):
#     if not commands:
#         return

#     if shell == "cmd":
#         joined = " && ".join(commands)
#         command = f'start cmd.exe /K "{joined}"'
#         subprocess.Popen(command, shell=True)

#     elif shell == "powershell":
#         joined = "; ".join(commands)
#         command = f'start powershell.exe -NoExit -Command "{joined}"'
#         subprocess.Popen(command, shell=True)

#     else:
#         raise ValueError("shell musi być 'cmd' lub 'powershell'")



# @mcp.tool()
# def execute_in_new_terminal(commands: List[str], shell: str = "cmd") -> str:
#     """
#     MCP tool: uruchamia komendy w nowym oknie terminala.
#     """
#     try:
#         if not commands:
#             return "⚠️ Podaj przynajmniej jedno polecenie"
#         run_in_terminal(commands, shell)
#         return f"✅ Uruchomiono terminal z {len(commands)} poleceniami"
#     except Exception as e:
#         return f"❌ Błąd: {e}"


# if __name__ == "__main__":
#     mcp.run()


# ====================================================================================
# Nowa wersja z odbieraniem STDOUT oraz wykonywaniem wszystkiego w 1 oknie terminala
# ====================================================================================
# from mcp.server.fastmcp import FastMCP
# import subprocess
# from typing import List
# import os
# import tempfile

# mcp = FastMCP("Test-Windows")

# # Przechowujemy PID procesu PowerShell dla sesji
# _powershell_process = None

# def ensure_powershell_window():
#     """
#     Tworzy jedno okno PowerShell przy pierwszym wywołaniu
#     i zapamiętuje proces dla kolejnych poleceń.
#     """
#     global _powershell_process
    
#     if _powershell_process is None or _powershell_process.poll() is not None:
#         # Tworzymy nazwany pipe dla komunikacji
#         pipe_name = f"mcp_powershell_{os.getpid()}"
        
#         # Uruchamiamy PowerShell, który nasłuchuje poleceń
#         ps_script = f'''
#         $pipeName = "{pipe_name}"
#         while ($true) {{
#             if (Test-Path "C:\\temp\\$pipeName.cmd") {{
#                 $cmd = Get-Content "C:\\temp\\$pipeName.cmd" -Raw
#                 Remove-Item "C:\\temp\\$pipeName.cmd"
#                 Write-Host "Wykonuję: $cmd" -ForegroundColor Green
#                 Invoke-Expression $cmd
#             }}
#             Start-Sleep -Milliseconds 500
#         }}
#         '''
        
#         _powershell_process = subprocess.Popen(
#             ["powershell.exe", "-NoExit", "-Command", ps_script],
#             creationflags=subprocess.CREATE_NEW_CONSOLE
#         )
    
#     return _powershell_process

# def run_command(cmd: str) -> str:
#     """
#     Uruchamia komendę w istniejącym oknie PowerShell (Windows)
#     i zwraca jej wynik do klienta LLM.
#     """
#     try:
#         # 1️⃣ Uruchom komendę i zbierz output
#         result = subprocess.run(
#             ["powershell.exe", "-Command", cmd],
#             capture_output=True,
#             text=True,
#             timeout=30
#         )
#         output = (result.stdout + "\n" + result.stderr).strip()
        
#         # 2️⃣ Wyślij komendę do istniejącego okna PowerShell
#         process = ensure_powershell_window()
#         pipe_name = f"mcp_powershell_{os.getpid()}"
        
#         # Zapisz komendę do pliku tymczasowego
#         os.makedirs("C:\\temp", exist_ok=True)
#         with open(f"C:\\temp\\{pipe_name}.cmd", "w", encoding="utf-8") as f:
#             f.write(cmd)
        
#         # 3️⃣ Zwróć wynik do LLM
#         return f"✅ Uruchomiono: {cmd}\n\n{output}"
        
#     except subprocess.TimeoutExpired:
#         return f"⏱️ Timeout podczas wykonywania: {cmd}"
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
#         history.append(f"PS> {cmd}\n{output}")
    
#     return "\n\n".join(history)

# if __name__ == "__main__":
#     mcp.run()

from mcp.server.fastmcp import FastMCP
import subprocess
from typing import List
import os
import time

mcp = FastMCP("Test-Windows")

# Przechowujemy PID procesu PowerShell dla sesji
_powershell_process = None
_session_id = str(os.getpid())

def ensure_powershell_window():
    """
    Tworzy jedno okno PowerShell przy pierwszym wywołaniu.
    """
    global _powershell_process
    
    if _powershell_process is None or _powershell_process.poll() is not None:
        # Tworzymy katalog na komunikację
        os.makedirs("C:\\temp\\mcp", exist_ok=True)
        
        # Skrypt PowerShell, który czeka na polecenia i wyświetla ich output
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
                
                # Wykonaj polecenie i zapisz output
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
        
        _powershell_process = subprocess.Popen(
            ["powershell.exe", "-NoExit", "-Command", ps_script],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        
        # Daj chwilę na uruchomienie
        time.sleep(1)
    
    return _powershell_process

def run_command(cmd: str) -> str:
    """
    Uruchamia komendę w istniejącym oknie PowerShell (Windows)
    i zwraca jej wynik do klienta LLM.
    Polecenie wykonywane jest TYLKO RAZ.
    """
    try:
        # Upewnij się, że okno PowerShell istnieje
        ensure_powershell_window()
        
        cmd_file = f"C:\\temp\\mcp\\{_session_id}.cmd"
        output_file = f"C:\\temp\\mcp\\{_session_id}.output"
        
        # Usuń stary output jeśli istnieje
        if os.path.exists(output_file):
            os.remove(output_file)
        
        # Zapisz komendę do pliku
        with open(cmd_file, "w", encoding="utf-8") as f:
            f.write(cmd)
        
        # Czekaj na output (max 30 sekund)
        timeout = 30
        start_time = time.time()
        
        while not os.path.exists(output_file):
            if time.time() - start_time > timeout:
                return f"⏱️ Timeout podczas wykonywania: {cmd}"
            time.sleep(0.1)
        
        # Odczytaj wynik
        time.sleep(0.1)  # Krótkie opóźnienie dla pewności zapisu
        with open(output_file, "r", encoding="utf-8") as f:
            output = f.read().strip()
        
        # Usuń plik z outputem
        os.remove(output_file)
        
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
        history.append(f"PS> {cmd}\n{output}")
    
    return "\n\n".join(history)

if __name__ == "__main__":
    mcp.run()