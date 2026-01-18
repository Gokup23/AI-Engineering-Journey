import csv

INPUT_FILE = 'raw_trades.csv'
REPORT_FILE = 'verified_trades.csv'
LOG_FILE = 'audit.log'

def audit_portfolio():
    print("--- STARTING ---")

    valid_trade_count = 0
    total_portfolio_value = 0

    #Opening all 3 files using context manager
    with open(INPUT_FILE,'r') as f_in, \
         open(REPORT_FILE,'w') as f_out, \
         open(LOG_FILE,'w') as f_log:
        
        reader = csv.DictReader(f_in)

        #settin up Dictwriter
        fieldnames = reader.fieldnames +['Total_Value']
        writer = csv.DictWriter(f_out , fieldnames=fieldnames)
        writer.writeheader()

        #looping through each transaction
        for row_num,row in enumerate(reader, start=2): # 1 is header
            ticker = row['Ticker']

            try:
                price = float(row['Price'])
                qty = int(row['Quantity'])

                # Logical Check: Quantity cannot be negative
                if qty < 0:
                    raise ValueError(f"Negative Quantity: {qty}")
                
                # Calculate Value
                trade_value = price * qty
                total_portfolio_value += trade_value

                # Update the row dictionary with new data
                row['Total_Value'] = f"{trade_value:.2f}"
                #Even though trade_value is a float in Python, it must become text when written to CSV.
                
                # Write to clean CSV
                writer.writerow(row)
                valid_trade_count += 1
                print(f"Line {row_num}: Processed {ticker}")

                # 5. Exception Handling
            except ValueError as e:
                # Catches 'invalid_price', 'N/A', or our raised Negative Logic
                error_msg = f"Line {row_num} Error ({ticker}): {e}\n"
                f_log.write(error_msg)
                print(f"Line {row_num}: Rejected ({e})")

    print(f"\n--- AUDIT COMPLETE ---")
    print(f"Valid Trades: {valid_trade_count}")
    print(f"Total Value: ${total_portfolio_value:,.2f}")
    print(f"Check '{REPORT_FILE}' for data and '{LOG_FILE}' for errors.")

if __name__ == "__main__":
    audit_portfolio()
'''“Is this file being run directly?”

YES → run the code below

NO → skip it'''
