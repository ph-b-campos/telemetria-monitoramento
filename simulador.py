import socket 
import json
from time import sleep, time
from datetime import datetime
import random
from math import cos 

# Configurações da comunicação UDP
ip_destino = "127.0.0.1"
porta_destino = 20001
udp_sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

tempo_inicial = time()


print("Leitura de telemetria iniciada. Enviando dados para o receptor UDP.")
try:
    while True:
        # Simulando dados de telemetria 
        t = time() - tempo_inicial
        profundidade = 500 + 500 * cos(0.02 * t)

        temp_media = 25.0 - (profundidade * 0.023) 
        leitura_temp = round(temp_media + random.uniform(-0.05, 0.05), 2)

        pressao_base = 1.0 + (profundidade / 10.0)
        leitura_pressao = round(pressao_base + random.uniform(-0.2, 0.2), 2)

        telemetria = {
            "timestamp": datetime.now().isoformat(),
            "profundidade": round(profundidade, 2),
            "temperatura": round(leitura_temp, 2),
            "pressao": round(leitura_pressao, 2)
        }
        # Convertendo o dicionário para JSON e depois para bytes
        data_bytes = json.dumps(telemetria).encode('utf-8')
        # Enviando os dados para o receptor UDP
        udp_sender.sendto(data_bytes, (ip_destino, porta_destino))
        print(f"Dados enviados: {telemetria}")
        # Aguardando 0.5 segundos antes de enviar a próxima telemetria
        sleep(0.5)
    
except KeyboardInterrupt:
    print("\n Simulador encerrado pelo usuário.")
finally:
    udp_sender.close()