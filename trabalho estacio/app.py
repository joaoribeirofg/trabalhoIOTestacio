import time
import random

# Simulação de leitura de dados dos sensores
def read_sensor_data():
    return random.uniform(20.0, 80.0)

# Função para monitorar o equipamento e alertar sobre falhas
def monitor_equipment():
    while True:
        sensor_value = read_sensor_data()
        print(f"Leitura do sensor: {sensor_value:.2f}")
        
        if sensor_value < 30.0:
            print("Alerta: Equipamento em falha!")
        
        time.sleep(5)

if __name__ == "__main__":
    print("Monitoramento do equipamento iniciado...")
    monitor_equipment()
