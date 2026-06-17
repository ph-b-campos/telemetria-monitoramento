Desenvolvimento de uma arquitetura de dados estruturada para capturar, validar e monitorar sinais de ativos físicos. O projeto simula a emissão de telemetria (profundidade, temperatura e pressão) via protocolo UDP, garantindo a integridade dos dados através de uma API em FastAPI antes da persistência em SQLite e visualização ao vivo.

Arquitetura: Pipeline de monitoramento remoto de ponta a ponta.

Ingestão: Recepção de dados de alta frequência via sockets UDP.

Processamento: Validação e limpeza de payloads em tempo real utilizando FastAPI e Pydantic.

Visualização: Desenvolvimento de painel operacional com atualização contínua e baixa latência utilizando Streamlit.