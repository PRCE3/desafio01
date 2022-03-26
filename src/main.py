from libs.functions import MonitoraCaldeira


def main():
    print("\n============================================================")
    print("       [INFO] -> Sistema de monitoramento Caldeira")
    print("============================================================\n")
    print("[INFO] -> Iniciando monitoramento...")
    instance = MonitoraCaldeira()
    instance.executa_monitoracao()
    print(f"[INFO] -> Média da temperatura em {instance.delay_verificacao} segundos: {instance.temperatura_caldeira}°C")
    if instance.sensor_temperatura:
        print("[INFO] -> Caldeira Desativada!!! Por gentileza, direcionar o técnico responsável.")

if __name__ == "__main__":
    main()
