# data-pipeline-audit

A Python project that monitors data files, fixes basic formatting issues, and logs errors.

### Project Overview
This repository contains a simple, lightweight Python project built to automate **data quality checking, formatting, and error logging**. 

It simulates the real-world tasks of a **Junior Data Engineer / Support Engineer** by monitoring daily data files, catching workflow errors, and isolating corrupted records for quick triage.

### Core Features
* **File Verification:** Automatically checks if the daily data file has arrived on time.
* **Schema Standardization:** Fixes basic formatting issues by automatically converting column headers to lowercase to prevent system crashes.
* **Error Logging & Isolation:** Scans data for missing critical values (like `invoice_id`) and safely extracts bad records into a separate file (`error_log.csv`) for review.

### Built With
* Python 3.x
* Pandas Library

### How To Run
1. Place your data file in the root directory and name it `client_transactions.csv`.
2. Run the script using the terminal: `python pipeline_audit.py`
3. Check the console for live operational logs, and open `verified_production_ready.csv` to see the cleaned output.
