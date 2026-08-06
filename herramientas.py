def analizar_paciente(secuencia):
    if secuencia == "GGGG":
        return "⚠️ ALERTA BIOLÓGICA"
    else:
        return "✅ Limpio"
print("--- INICIANDO DIAGNÓSSTICO RÁPIDO ---")
informe_1 = analizar_paciente("ATCG")
informe_2 = analizar_paciente("GGGG")
informe_3 = analizar_paciente("TTTA")
print("Paciente 1: " + informe_1)
print("Paciente 2: " + informe_2)
print("Paciente 3: " + informe_3)

def contar_guaninas(secuencia):
    total_g = 0
    for base in secuencia:
        if base == "G":
            total_g = total_g + 1
    return total_g
print( "\n--- ANÁLISIS DE CONTENIDO GENÉTICO ---")
cantidad_1 = contar_guaninas("ATCG")
cantidad_2 = contar_guaninas("GGGG")
cantidad_3 = contar_guaninas("GATC-GATC-GATC")
print("Guaninas de la muestra 1: " + str(cantidad_1))
print("Guaninas de la muestra 2: " + str(cantidad_2))
print("Guaninas de la muestra 3: " + str(cantidad_3))


def escuadron_rastreador(secuencia, letra_objetivo):
    total_encontrado = 0
    for base in secuencia:
        if base == letra_objetivo:
            total_encontrado = total_encontrado + 1
    return total_encontrado
print("\n--- ESCÁNER UNIVERSAL ACTIVADO ---")
genoma_paciente = "AATCG-GATCG-AATTCG"
total_adeninas = escuadron_rastreador(genoma_paciente, "A")
total_timinas = escuadron_rastreador(genoma_paciente, "T")
print("Analizando genoma: " + genoma_paciente)
print("Adeninas (A) detectadas: " + str(total_adeninas))
print("Timinas (T) detectadas: " + str(total_timinas))

print("\n--- INITIATING GC CONTENT ANALYSIS ---")
def calculate_gc_percentage(sequence):
    total_length = len(sequence)
    gc_count = 0
    for base in sequence:
        if base == "G" or base == "C":
            gc_count = gc_count +1
    raw_percentage = (gc_count / total_length) * 100
    percentage = round(raw_percentage, 2)
    return percentage
patient_dna = "ATCGGC"
final_result = calculate_gc_percentage(patient_dna)
print("Analyzing DNA sequence: " + patient_dna)
print("GC content percentage: " + str(final_result) + "%")
        