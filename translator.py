codon_table = {
    "AUG": "Methionine (START)",
    "UUU": "Phenylalanine",
    "GCA": "Alanine",
    "UAG": "STOP (Chain Termination)"     
}  
print("\n--- INITIATING FULL SEQUENCE TRANSLATION ---")
mrna_sequence = ["AUG", "UUU", "GCA", "UUU", "UAG"]
protein_chain = ""
for codon in mrna_sequence:
    amino_acid = codon_table[codon]
    protein_chain = protein_chain + amino_acid + " - "
print("Raw mRNA sequence: " + str(mrna_sequence))
print("Synthesized Protein: " + protein_chain)