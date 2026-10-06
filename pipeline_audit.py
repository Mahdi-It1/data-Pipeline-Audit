import os
import pandas as pd
from datetime import datetime

def process_daily_logs(input_source):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] 🚀 Initiating workflow pipeline audit for: {input_source}")
    
    # Verify file delivery
    if not os.path.exists(input_source):
        print(f"[{timestamp}] ❌ CRITICAL: Input stream unavailable. Operational failure.")
        return False
        
    try:
        # Load incoming data
        raw_data = pd.read_csv(input_source)
        print(f"[{timestamp}] 🟢 Connection secure. Processing {len(raw_data)} active records.")
        
        # Standardize headers to prevent pipeline crashes
        raw_data.columns = raw_data.columns.str.lower()
        
        # Check for missing transaction IDs
        if 'invoice_id' in raw_data.columns:
            corrupted_records = raw_data[raw_data['invoice_id'].isnull()]
            
            if not corrupted_records.empty:
                print(f"[{timestamp}] ⚠️ WARNING: Detected {len(corrupted_records)} anomalous records.")
                # Isolate corrupted data for triage
                corrupted_records.to_csv("error_log.csv", index=False)
                print(f"[{timestamp}] 📝 Anomalies isolated to 'error_log.csv'.")
        
        # Filter clean records
        verified_data = raw_data.dropna(subset=['invoice_id'])
        
        # Save output for downstream systems
        final_destination = "verified_production_ready.csv"
        verified_data.to_csv(final_destination, index=False)
        print(f"[{timestamp}] ✅ Optimization complete. Output dispatched to '{final_destination}'.")
        return True
        
    except Exception as error_message:
        print(f"[{timestamp}] ❌ Pipeline broken due to unexpected runtime error: {str(error_message)}")
        return False

if __name__ == "__main__":
    process_daily_logs("client_transactions.csv")
