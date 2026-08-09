from Bio import SeqIO
import pandas as pd
sequence_list = []
for record in SeqIO.parse("clinical_test.fasta", "fasta"):
    sequence_list.append(record.seq)
ref_seq = sequence_list[0]
patient_seq = sequence_list[1]
if len(ref_seq) == len(patient_seq):
    print("QC Passed: Sequence length match")
    mutations = []
    for i in range(len(ref_seq)):
        if ref_seq[i] != patient_seq[i]:
            mutation_data = {
                "Position": i,
                "Reference": ref_seq[i],
                "Patient": patient_seq[i]
            }
            mutations.append(mutation_data)
    df = pd.DataFrame(mutations)
    df.to_csv("mutation_report.csv", index=False)
    print("\nSUCCESS: 'mutation_report.csv' has been generated.")

else:
    print("QC Failed: Sequences are different lengths")

