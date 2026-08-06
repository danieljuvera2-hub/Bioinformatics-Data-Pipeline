print("--- SISTEMA DE SECUENCIACIÓN INICIADO ---")
registro_adn = []
numero_muestras = int(input("¿Cuántas muestras biológicas vas a ingresar hoy?: "))
for i in range(numero_muestras):
    secuencia = input("Introduce la cadena de ADN del paciente " + str(i + 1) + ": ")
    registro_adn.append(secuencia)
print("\n--- INFORME DE LA BASE DE DATOS ---")
print("Total de pacientes registrados: " + str(len(registro_adn)))
print("Datos puros almacenados: " + str(registro_adn))
print("Estado: Servidor cerrado")


print("\n--- ESCÁNER DE MUTACIONES ACTIVADO ---")
total_mutaciones = 0
for muestra in registro_adn:
    if muestra == "GGGG":
        print("⚠️ ALERTA BIOLÓGICA: Mutación 'GGGG' detectada en el paciente.")
        total_mutaciones = total_mutaciones + 1
    else:
        print("✅ Paciente sano. Secuencia limpia: " + muestra)
print("\n--- INFORME EPIDEMÓLOGICO FINAL ---")
print("Total de mutaciones críticas detectadas en el lote: " + str(total_mutaciones))
print("Estado: Análisis completado. Desconectando sistemas.")
