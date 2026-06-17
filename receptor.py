# importando bibliotecas
import socket
import json
import requests

# definindo o endereço de comunicação
local_ip = "127.0.0.1"
local_port = 20001
buffer_size = 1024

# URL da nossa futura API que irá receber os dados e armazenar no banco de dados
api_url = "http://127.0.0.1:8000/api/v1/telemetria"

# Criação do socket UDP usando IPV4 e protocolo de datagrama
udp_receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Configura o socket para receber nessa porta e nesse ip local
udp_receiver.bind((local_ip, local_port))

print("Receptor UDP pronto para receber dados.")

while True:
    try:
        # Desempacotamento direto da mensagem e do endereço do cliente.
        message, address = udp_receiver.recvfrom(buffer_size)
        
        # Decodifica a mensagem e converte para json.
        mensagem_str = message.decode('utf-8')
        payload = json.loads(mensagem_str)
        
        # Enriquecendo o payload original com os dados de rede.
        payload["ip_origem"] = address[0]
        payload["porta_origem"] = address[1]
        
        # Exibe a mensagem recebida e o endereço do cliente.
        print(f"Mensagem do Cliente: {payload}")
        print(f"Endereço do Cliente: {address}")

        # Enviar dados para a API (com timeout de 1 segundo para não travar o loop).
        response = requests.post(api_url, json=payload, timeout=1.0)
        
        # Recebe a resposta da API e imprime o status.
        print(f"Dados Enviados para a API.\nResposta: {response.status_code}\n")
        
    except json.JSONDecodeError:
        print("O dado recebido não é um JSON válido.")
    except requests.exceptions.RequestException as e:
        print(f" Falha de comunicação com a API ou timeout. ({e})")