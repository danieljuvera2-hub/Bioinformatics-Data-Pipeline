import pandas as pd
print("\n--- INITIATING EXTERNAL DATA IMPORT ---")
imported_data = pd.read_csv("clean_patient_report.csv")
print("\n--- EXTERNAL FILE SUCCESSFULLY LOADED ---")
print(imported_data)
print("\n--- INITIATING DATA SANITIZATION ---")
dirty_clinical_data = {
    "Patient_ID": ["PT-005", "PT-006", "PT-007", "PT-008", "PT-009"],
    "Age": [45, 52, None, 38, 61],
    "Tumor_Size": [2.4, None, 1.1, 4.5, None]
}
dirty_df = pd.DataFrame(dirty_clinical_data)
print("Raw Corrupted Data:")
print(dirty_df)
print("\n--- MISSING DATA DIAGNOSTIC REPORT ---")
print(dirty_df.isnull().sum())
cleaned_df = dirty_df.dropna()
print("\n--- SANITIZED DATAFRAME (INCOMPLETE RECORDS PURGED) ---")
print(cleaned_df)
print("\n--- INITIATING DATA IMPUTATION ---")
average_tumor_size = dirty_df["Tumor_Size"].mean()
average_tumor_size = round(average_tumor_size,2)
print("Calculated Mean Tumor Size: " + str(average_tumor_size) + " cm")
dirty_df["Tumor_Size"] = dirty_df["Tumor_Size"].fillna(average_tumor_size)
print("\n--- SANITIZED DATAFRAME (RECORDS REPAIRED) ---")
print(dirty_df)