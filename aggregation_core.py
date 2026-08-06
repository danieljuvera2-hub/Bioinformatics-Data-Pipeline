import pandas as pd
print("--- INITIATING COHORT AGGREGATION ---")
clinical_data = {
    "Patient_ID": ["PT-001", "PT-002", "PT-003", "PT-004", "PT-005", "PT-006"],
    "Mutation": ["BRCA1", "TP53", "BRCA1", "None", "TP53", "BRCA1"],
    "Age": [ 45, 52, 38, 61, 48, 42],
    "Risk_Score": [8.5, 9.1, 7.2, 1.2, 8.8, 7.9]
}
df = pd.DataFrame(clinical_data)
cohort_analysis = df.groupby("Mutation")[["Age", "Risk_Score"]].mean()
print("\n--- CLINICAL COHORT ANALYSIS (MEAN VALUES) ---")
print(cohort_analysis)
