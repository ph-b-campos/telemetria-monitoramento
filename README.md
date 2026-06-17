# Desenvolvimento de uma arquitetura de dados estruturada para capturar, validar e monitorar leitura de sensores. 
Este projeto implementa um ecossistema completo de telemetria. Na camada de ingestão, um script em Python atua como um equipamento físico em campo, emitindo pacotes de dados sintéticos de temperatura, pressão e profundidade via sockets UDP. Esses pacotes são interceptados por receptor e enviados para uma API, responsável por validar a integridade e o formato dos dados. Após a validação, os dados são persistidos de forma segura em um banco de dados SQLite. Para o monitoramento da operação, uma interface em Streamlit consome o banco de dados de forma assíncrona, permitindo a visualização contínua e em tempo real do perfil de mergulho assim que os dados são escritos.

Arquitetura: Pipeline de monitoramento remoto de ponta a ponta.

Ingestão: Recepção de dados de alta frequência via sockets UDP.

Processamento: Validação e limpeza de payloads em tempo real utilizando FastAPI e Pydantic.

Visualização: Desenvolvimento de painel operacional com atualização contínua e baixa latência utilizando Streamlit.
