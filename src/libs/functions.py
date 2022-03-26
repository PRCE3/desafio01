import random
import time
import numpy as np


class MonitoraCaldeira:
    
    def __init__(self, delay_verificacao=60):
        self.sensor_temperatura = False
        self.list_temperatura_capturada = []
        self.delay_verificacao = delay_verificacao

    def captura_temperatura(self):
        for _ in range(self.delay_verificacao):
            temperatura = random.uniform(15, 35)   # Simula temperatura capturada da caldeira
            print(f"[INFO] -> Temperatura capturada na caldeira: {round(temperatura, 2)}°C")
            self.list_temperatura_capturada.append(temperatura)
            time.sleep(1)

    def calcula_media_temperatura(self):
        self.temperatura_caldeira = round(np.median(self.list_temperatura_capturada), 2) # Calcula a média da temperatura capturada dentro o intervalo definido
    
    def executa_monitoracao(self):
        self.captura_temperatura()
        self.calcula_media_temperatura()

        if float(self.temperatura_caldeira) >= 25:
            self.sensor_temperatura = True
