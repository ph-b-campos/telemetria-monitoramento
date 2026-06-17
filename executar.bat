@echo off
echo ===================================================
echo Iniciando o Ecossistema de Telemetria...
echo ===================================================

:: Navega dinamicamente para a pasta onde este arquivo .bat esta localizado
cd /d "%~dp0"

:: 1. Inicia a API (FastAPI) em uma nova janela
echo [1/4] Levantando a API FastAPI...
start "Backend - FastAPI" cmd /k "call venv\Scripts\activate & uvicorn main:app --reload"

:: Aguarda 3 segundos para garantir que a API subiu antes de mandar os dados
timeout /t 3 /nobreak > nul

:: 2. Inicia o Receptor UDP em uma nova janela
echo [2/4] Iniciando o Receptor de Telemetria...
start "Receptor - UDP" cmd /k "call venv\Scripts\activate & python receptor.py"

:: 3. Inicia o Simulador UDP em uma nova janela
echo [3/4] Iniciando o Simulador de Telemetria...
start "Simulador - UDP" cmd /k "call venv\Scripts\activate & python simulador.py"

:: 4. Inicia o Dashboard (Streamlit) em uma nova janela
echo [4/4] Abrindo o Painel de Controle...
start "Frontend - Streamlit" cmd /k "call venv\Scripts\activate & streamlit run dashboard.py"

echo ===================================================
echo Todos os servicos estao no ar! Pode fechar esta janela.
echo ===================================================
timeout /t 5 > nul