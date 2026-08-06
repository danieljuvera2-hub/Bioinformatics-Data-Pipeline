import pandas as pd
print("--- INITIATING RELATIONAL MERGE ---")
admin_data = {
    "Patient_ID": ["PT-001", "PT-002", "PT-003"],
    "Age": [45, 52, 38],
    "Blood_Type": ["A+", "O-", "B+"]
}
admin_df = pd.DataFrame(admin_data)
lab_data = {
    "Patient_ID": ["PT-001", "PT-002", "PT-003"],
    "Mutation": ["None", "BRCA1", "TP53"],
    "Risk_Score": [1.2, 8.5, 9.1]
}
lab_df = pd.DataFrame(lab_data)
unified_df = pd.merge(admin_df, lab_df, on="Patient_ID")
print("\n--- UNIFIED CLINICAL-GENOMIC DATABASE ---")
print(unified_df)
