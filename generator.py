import pandas as pd
import numpy as np

# Define sample data
start_date = pd.Timestamp('2022-01-01')
end_date = pd.Timestamp('2022-12-31')
num_transactions = 1000

transaction_ids = range(1, num_transactions+1)
transaction_dates = pd.date_range(start_date, end_date, periods=num_transactions)
transaction_times = [pd.Timestamp.now().strftime('%H:%M:%S') for i in range(num_transactions)]
transaction_amounts = np.random.choice([1000, 5000, 10000, 20000, 50000], size=num_transactions, p=[0.6, 0.1, 0.1, 0.1, 0.1])
bank_names = ['HDFC Bank', 'ICICI Bank', 'State Bank of India', 'Axis Bank', 'Kotak Mahindra Bank']
account_names = ['Arun Patel', 'Neha Sharma', 'Suresh Gupta', 'Priya Singh', 'Manoj Shah', 'John Doe', 'Jane Doe', 'David Smith', 'Emma Johnson', 'Isabella Davis']
foreign_names = ['Robert Smith', 'Maria Hernandez', 'Mohamed Ali', 'Katrina Nguyen', 'Yoshiro Tanaka', 'Emily Park', 'Lucas Lee', 'Sophie Kim', 'William Chen', 'Yuna Lee']
transaction_receivers = [f"{np.random.choice(bank_names)}/{np.random.choice(transaction_ids)}/{np.random.choice(account_names+foreign_names)}" for i in range(num_transactions)]
transaction_types = np.random.choice(['Bank Transfer', 'Money Transfer', 'College Fees', 'Hospital Fees'], size=num_transactions, p=[0.7, 0.2, 0.01, 0.09])

# Set frequency for college fees and hospital fees
college_fees_indices = np.random.choice(num_transactions, size=3, replace=False, p=[1/num_transactions]*num_transactions)
hospital_fees_indices = np.random.choice(num_transactions, size=30, replace=False, p=[1/num_transactions]*num_transactions)

# Set transaction type for college fees and hospital fees
transaction_types[college_fees_indices] = 'College Fees'
transaction_types[hospital_fees_indices] = 'Hospital Fees'

# Create DataFrame
df = pd.DataFrame({
    'transactionID': transaction_ids,
    'date': transaction_dates,
    'time': transaction_times,
    'amount': transaction_amounts,
    'receiver\'s info': transaction_receivers,
    'transaction type': transaction_types
})

# Add 'sender's info' column with N/A values
df['sender\'s info'] = 'N/A'

# Save DataFrame to xlsx file
df.to_excel('sample_transactions.xlsx', index=False)
