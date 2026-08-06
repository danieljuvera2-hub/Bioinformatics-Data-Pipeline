nombre = input("¿Cuál es tu nombre de operador?: ")
peso_actual = float(input("Introduce tu peso actual en kg: "))
fatiga = int(input("Del 1 al 10, ¿cuál es tu nivel de fatiga muscular hoy?: "))
proteina_objetivo = peso_actual * 2.0
print("\n--- INFORME DE SISTEMA ---")
print("Operador: " + nombre)
print("Objetivo diario de proteína: " + str(proteina_objetivo) + " gramos.")
if fatiga >= 8:
    print("Directiva: DESCANSO O RECUPERACIÓN ACTIVA. Riesgo de lesión detectado.")
elif fatiga >= 5:
    print("Directiva: ENTRENAMIENTO MODERADO. Mantén los pasos del último bloque. ")
else:
    print("Directiva: SOBRECARGA PROGRESIVA. Sistema nervioso óptimo, busca nuevos RPs. ")
print("Estado: Ejecución completada")
print("\n--- MÓDULO DE INGESTA ---")
numero_comidas = int(input("¿Cuántas comidas planeas hacer hoy?: "))
proteina_total_ingerida = 0.0 #Empezamos el dia con 0 gramos
for i in range(numero_comidas):
    gramos = float(input("Introduce los gramos de proteína de la comida " + str(i + 1) + ": "))
    proteina_total_ingerida = proteina_total_ingerida + gramos
print("\n--- BALANCE FINAL ---")
print("Proteína ingerida: " + str(proteina_total_ingerida) + "g / Objetivo: " + str(proteina_objetivo) + "g")
if proteina_total_ingerida >= proteina_objetivo:
    print("Estado: OBJETIVO NUTRICIONAL CUMPLIDO. Crecimiento muscular asegurado.")
else:
    faltan = proteina_objetivo - proteina_total_ingerida
    print("Estado: DÉFICIT DETECTADO. Te faltan " + str(faltan) + " gramos . Hazte un batido")