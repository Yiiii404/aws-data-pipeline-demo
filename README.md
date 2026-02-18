# AWS Data Pipeline Demo

## Project Overview
This project simulates a production-style data engineering workflow, including data extraction, transformation, and loading using Python.

## Architecture
Raw Data (CSV)
→ Data Cleaning (Pandas)
→ Processed Data Output
→ Ready for Cloud Storage (AWS S3)

## Tools & Technologies
- Python
- Pandas
- AWS S3 (conceptual)
- SQL
- ETL pipeline design

## ETL Process
1. Extract raw data from source
2. Perform data validation and cleaning
3. Remove null values and duplicates
4. Save processed data for downstream analytics

## How to Run

```bash
python etl.py
