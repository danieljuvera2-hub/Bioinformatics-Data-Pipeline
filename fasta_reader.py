from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
print("--- INITIATING FASTA PARSER WITH GC ANALYSIS ---")
for record in SeqIO.parse("sample_patient.fasta","fasta"):
    print("Record ID: " + record.id)
    raw_gc = gc_fraction(record.seq) * 100
    clean_gc = round(raw_gc, 2)
    print("GC Content: " + str(clean_gc) + "%")
    