import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# create a list of dates for the past year
date_list = [datetime.now() - timedelta(days=x) for x in range(365)]

# create a list of times for each date
time_list = [datetime.now().replace(hour=np.random.randint(0, 23), minute=np.random.randint(0, 59),
                                    second=np.random.randint(0, 59), microsecond=0) for _ in range(365)]

# create a list of transaction types
transaction_type = ['Bank Transfer', 'Money Transfer', 'College Fees', 'Hospital Fees']

# create a list of receiver names
receiver_names = ['SBI Bank/123456789/John Doe', 'KotakMahindra Bank/987654321/Jane Smith', 'Axis Bank/456789123/Mohammed Khan',
                  'HDFC Bank/654321987/Wei Chen', 'PDCC Bank/321654987/Lisa Patel', 'Pune Bank/789456123/Julia Kim']

# create a list of payment amounts
payment_amounts = np.random.normal(5000, 2000, len(date_list)).round(2)

# create a list of payment recipients
payment_recipients = np.random.choice(receiver_names, len(date_list))

# create a list of transaction IDs
transaction_ids = ['TRX'+str(i+1) for i in range(len(date_list))]

# create a dataframe from the above lists
df = pd.DataFrame({
    'Date': [d.date() for d in date_list],
    'Time': [t.time() for t in time_list],
    'transactiontype': np.random.choice(transaction_type, len(date_list)),
    'receiveInfo': payment_recipients,
    'amount': payment_amounts,
    'transactionID': transaction_ids,
})

# save the dataframe to an xlsx file
df.to_excel('transactions.xlsx', index=False)
