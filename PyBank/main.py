# Import required libraries
import csv    # For reading CSV files
import os     # For file path operations
 
# Define file paths for Windows using your directory structure
# Path to read the source CSV file
file_to_load = "C:\\Users\\flysc\\OneDrive\\Desktop\\python-challenge\\PyBank\Resources\\budget_data.csv"
# Path where the analysis output will be saved
file_to_output = "C:\\Users\\flysc\\OneDrive\\Desktop\\python-challenge\\PyBank\\analysis\\analysis.txt"
 
# Create the analysis directory if it doesn't exist
analysis_dir = "C:\\Users\\flysc\\OneDrive\\Desktop\\python-challenge\\PyBank\\analysis"
os.makedirs(analysis_dir, exist_ok=True)  # exist_ok=True prevents error if directory already exists
 
# Initialize variables for financial calculations
total_months = 0          # Counter for total number of months
total_net = 0            # Running sum of profit/losses
previous_profit = 0      # Store previous month's profit/loss for change calculation
changes = []             # List to store month-to-month changes
dates = []              # List to store dates corresponding to changes
greatest_increase = ["", 0]  # Store [date, amount] for greatest increase
greatest_decrease = ["", 0]  # Store [date, amount] for greatest decrease
 
# Open and read the CSV file
with open(file_to_load) as financial_data:
    # Create CSV reader object
    reader = csv.reader(financial_data)
 
    # Skip header row
    header = next(reader)
 
    # Process first row separately
    first_row = next(reader)
    total_months += 1                    # Count first month
    total_net += int(first_row[1])       # Add first month's profit/loss
    previous_profit = int(first_row[1])   # Set baseline for change calculation
 
    # Process remaining rows
    for row in reader:
        # Update basic metrics
        total_months += 1                # Count each month
        total_net += int(row[1])         # Add each profit/loss
 
        # Calculate change from previous month
        current_profit = int(row[1])
        change = current_profit - previous_profit  # Calculate month-to-month change
        changes.append(change)           # Store change in list
        dates.append(row[0])            # Store corresponding date
 
        # Check for greatest profit increase
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]    # Store date
            greatest_increase[1] = change     # Store amount
 
        # Check for greatest profit decrease
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]     # Store date
            greatest_decrease[1] = change      # Store amount
 
        # Update previous_profit for next iteration
        previous_profit = current_profit
 
# Calculate average monthly change
average_change = sum(changes) / len(changes)
 
# Create formatted output string
output_text = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net:,}\n"                  # :, adds thousands separator
    f"Average Change: ${average_change:.2f}\n"   # .2f formats to 2 decimal places
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,})\n"
)
 
# Display results in terminal
print(output_text)
 
# Save results to text file
try:
    # Open file in write mode
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output_text)
    print(f"\nResults have been written to: {file_to_output}")
except Exception as e:
    print(f"Error writing to file: {str(e)}")
 
# Verify output file creation and size
if os.path.exists(file_to_output):
    print("Output file created successfully!")
    print(f"File size: {os.path.getsize(file_to_output)} bytes")
else:
    print("Error: Output file was not created")