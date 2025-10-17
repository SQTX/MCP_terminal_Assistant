# Lokalny serwer MCP z PowerShell (Windows)

## Opis projektu

Serwer MCP (Model Context Protocol) umożliwiający interakcję LLM z terminalem PowerShell na Windows. Pozwala na automatyczne wykonywanie poleceń systemowych i operacji w dedykowanym oknie terminala.

## Wymagania wstępne

- **System operacyjny:** Windows 10/11
- **Python:** 3.8 lub nowszy
- **PowerShell:** 5.1 lub nowszy (wbudowany w Windows)
- **UV:** package manager dla Pythona

## Instalacja UV

Oficjalna dokumentacja UV: [Instalacja UV](https://docs.astral.sh/uv/getting-started/installation/)


## Proces inicjowania serwera

### 1. Przygotowanie struktury projektu

Utwórz katalog projektu i przejdź do niego:

```powershell
mkdir mcp-powershell-server
cd mcp-powershell-server
```

### 2. Inicjalizacja projektu z UV

Utwórz nowy projekt Python używając UV:

```powershell
uv init
```

### 3. Utworzenie wirtualnego środowiska (.venv)

UV automatycznie utworzy środowisko wirtualne przy pierwszym użyciu, ale możesz je również utworzyć ręcznie:

```powershell
uv venv
```

To polecenie utworzy katalog `.venv` z izolowanym środowiskiem Python.

### 4. Aktywacja środowiska wirtualnego

W PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

W CMD:

```cmd
.venv\Scripts\activate.bat
```

Po aktywacji powinieneś zobaczyć `(.venv)` przed znakiem zachęty w terminalu.

**Uwaga:** Jeśli napotkasz błąd związany z polityką wykonywania skryptów w PowerShell, wykonaj:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 5. Instalacja zależności

Zainstaluj pakiet MCP z dodatkami CLI za pomocą UV:
```powershell
uv add mcp[cli]
```
To polecenie:
* Automatycznie utworzy środowisko wirtualne (jeśli nie istnieje)
* Zainstaluje pakiet mcp z dodatkowymi narzędziami CLI
* Utworzy/zaktualizuje plik pyproject.toml z zależnościami
* Wygeneruje plik uv.lock z zamrożonymi wersjami pakietów

### 6. Utworzenie pliku serwera

Skopiuj kod serwera do pliku `server.py` w katalogu projektu. W PowerShell:

```powershell
New-Item -Path "server.py" -ItemType File
```

Lub w CMD:

```cmd
type nul > server.py
```

Następnie otwórz plik w edytorze tekstowym (np. Notepad, VS Code) i wklej pełny kod serwera.

### 7. Struktura projektu

Po wykonaniu powyższych kroków struktura projektu powinna wyglądać następująco:

```
mcp-powershell-server/
├── .venv/              # Wirtualne środowisko Python
├── server.py           # Główny plik serwera MCP
├── requirements.txt    # Lista zależności (opcjonalnie)
└── README.md          # Ten plik
```

## Uruchomienie serwera

### Metoda 1: Bezpośrednie uruchomienie

Tryb deweloperski pozwala na szybkie testowanie serwera z automatycznym przeładowaniem:

```powershell
mcp dev server.py
```
To polecenie:

* Uruchamia serwer w trybie deweloperskim
* Automatycznie przeładowuje serwer po zmianach w kodzie
* Wyświetla szczegółowe logi debugowania
* Idealny do rozwoju i testowania

### Metoda 2: Instalacja do Claude Desktop

Aby zintegrować serwer z aplikacją Claude Desktop, użyj:

```powershell
mcp install server.py
```

To polecenie:
- Instaluje serwer MCP do Claude Desktop
- Automatycznie aktualizuje plik konfiguracyjny Claude
- Serwer będzie dostępny w aplikacji Claude jako narzędzie

**Lokalizacja pliku konfiguracyjnego Claude:**
`%APPDATA%\Claude\claude_desktop_config.json`

## Funkcjonalność

Serwer udostępnia narzędzie `run_interactive`, które:

1. **Tworzy dedykowane okno PowerShell** przy pierwszym wywołaniu
2. **Wykonuje polecenia systemowe** w kolejności
3. **Przechwytuje wyniki** (stdout i stderr)
4. **Wyświetla polecenia w PowerShell** dla wizualizacji
5. **Zwraca historię wykonania** do klienta LLM
