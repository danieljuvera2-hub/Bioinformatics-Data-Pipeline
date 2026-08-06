import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
print("--- INITIATING CAPSTONE PIPELINE ---")
processed_records = []
for record in SeqIO.parse("cohort_data.fasta", "fasta"):
    dna_length = len(record.seq)
    gc_content = round(gc_fraction(record.seq) * 100, 2)
    patient_data = {
        "Patient_ID": record.id,
        "Sequence_Length": dna_length,
        "GC_Content": gc_content
    }
    processed_records.append(patient_data)
final_df = pd.DataFrame(processed_records)
print("\n--- FINAL CLINICAL DATAFRAME ---")
print(final_df)
final_df.to_csv("cohort_analysis_report.csv", index=False)
print("\nSUCCESS: 'cohort_analysis_report.csv' generated for clinical review.")