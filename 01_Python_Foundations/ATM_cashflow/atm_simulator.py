import csv

def process_atm_logs():
    # 1. State Initialization
    # We must track this OUTSIDE the loop so it remembers the total
    machine_balance = 10000 

    try:
        with open("atm_transactions.csv", 'r', encoding='utf-8-sig') as f_input, \
             open("atm_report.csv", 'w', newline='') as f_output:
            
            reader = csv.DictReader(f_input)
            
            # Define output headers
            fieldnames = ['TxnID', 'Type', 'Amount', 'Result', 'Machine_Balance_After']
            writer = csv.DictWriter(f_output, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                txn_id = row['TxnID']
                txn_type = row['Type']
                raw_amount = row['Amount']
                
                # --- LOGIC START ---

                # Step 1: Validate the Amount (Handle "invalid" or "-100")
                try:
                    amount = int(raw_amount)
                    if amount <= 0:
                        raise ValueError("Negative amount") # Force an error for negatives
                except ValueError:
                    # If conversion fails or amount is negative, mark error and SKIP math
                    writer.writerow({
                        'TxnID': txn_id,
                        'Type': txn_type,
                        'Amount': raw_amount,
                        'Result': "ERROR: Invalid Amount",
                        'Machine_Balance_After': machine_balance
                    })
                    continue # Skip to the next transaction immediately!

                # Step 2: Process Valid Transactions
                result_status = "Unknown" # Default placeholder

                if txn_type == 'Deposit':
                    machine_balance += amount
                    result_status = "Success"

                elif txn_type == 'Withdraw':
                    # Step 3: The Insufficient Funds Check
                    if machine_balance >= amount:
                        machine_balance -= amount
                        result_status = "Success"
                    else:
                        result_status = "Failed: Insufficient Funds"
                
                # Step 4: Write the final result for this row
                writer.writerow({
                    'TxnID': txn_id,
                    'Type': txn_type,
                    'Amount': amount,
                    'Result': result_status,
                    'Machine_Balance_After': machine_balance
                })

        print("✅ ATM Simulation Complete. Check 'atm_report.csv'.")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_atm_logs()