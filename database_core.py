import pandas as pd
print("\n--- INITIATING PANDAS ENGINE ---")
raw_clinical_data = {
    "Patient_ID": ["PT-001", "PT-002", "PT-003", "PT-004"],
    "Target_Gene": ["BRCA1", "TP53", "EGFR", "BRCA1"],
    "Expression_Level": [4.2, 1.1, 8.9, 5.5],
    "Risk_Status": ["High", "Low", "Critical", "High"]
}
df= pd.DataFrame(raw_clinical_data)
print("\n--- CLINICAL DATAFRAME MOUNTED ---")
print(df)
print("\n--- EXECUTING VECTORIZED QUERIES ---")
average_expression = df["Expression_Level"].mean()
print("Average Gene Expression: " + str(average_expression))
critical_patients = df[df["Risk_Status"] == "Critical"]
print("\nIsolating Critical Risk Patients:")
print(critical_patients)
print("\n--- GENERATING TARGETED REPORT ---")
targeted_report = df[["Patient_ID", "Target_Gene"]]
print("Clean Patient and Gene Data:")
print(targeted_report)
print("\n--- INITIATING DATA EXPORT ---")
targeted_report.to_csv("clean_patient_report.csv", index=False)
print("SUCCESS: 'clean_patient_report.csv' has been created in your workspace.")
