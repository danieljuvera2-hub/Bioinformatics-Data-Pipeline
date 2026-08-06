# Bioinformatics Data Pipeline

## Overview
This repository contains an automated, end-to-end data engineering pipeline for genomic analysis. It processes raw patient data, calculates biological metrics, and structures the output into clinical reports.

## Core Technologies
* **Python 3**
* **Pandas:** Used for relational database merging, missing data imputation, and cohort aggregation (`groupby`).
* **Biopython (`SeqIO`, `SeqUtils`):** Used for Central Dogma operations (transcription/translation) and parsing raw FASTA files.

## Pipeline Architecture
1. **Data Ingestion:** Imports and sanitizes clinical administrative data.
2. **Biological Processing:** Parses `.fasta` files and calculates GC content using Biopython.
3. **Synthesis:** Fuses the genomic metrics with demographic data into a unified Pandas DataFrame.
4. **Export:** Generates a structured `.csv` report ready for clinical review.