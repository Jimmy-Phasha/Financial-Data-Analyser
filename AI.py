import pandas as pd
import re

class FinanceAgent:
    #constructor
    def __init__(self, budget):
        self.budget = budget
        self.expenses = {}

    def perceive(self, transactions):
        #Read and understand transaction data
        #df = pd.DataFrame(transactions)
        April_df = pd.read_excel("April Bank Statement.xlsx")
        March_df = pd.read_excel("March Bank statement.xlsx")
        df = pd.concat([March_df,April_df], ignore_index=True) #append the 2 dataframes

        #clean Amount column & create credit and debit columns
        df['CleanAmount'] = df['Amount'].str.replace('C','',regex=False).astype(float)
        df['Credit'] = df.apply(lambda row: row['CleanAmount'] if 'C' in row['Amount'] else 0, axis=1)
        df['Debit'] = df.apply(lambda row: row['CleanAmount'] if 'C' not in row['Amount'] else 0, axis=1)

        #drop clean amount
        df.drop(columns='CleanAmount', inplace=True)

        df['Amount'] = pd.to_numeric(df['Amount'])
        self.expenses = df.groupby('Category')['Amount'].sum().to_dict()
        return self.expenses

    def decide(self):
        #Check if you're over budget
        total_spent = sum(self.expenses.values())
        if total_spent > self.budget:
            return f"⚠️ Alert: You've overspent! Total spent: ${total_spent:.2f}"
        else:
            return f"✅ You're within budget. Total spent: ${total_spent:.2f}"

    def act(self, decision):
        #Take action based on the decision
        print(decision)

# === Example Usage ===
transactions = [
    {'Category': 'Food', 'Amount': '250'},
    {'Category': 'Transport', 'Amount': '100'},
    {'Category': 'Entertainment', 'Amount': '180'},
]

#agent = FinanceAgent(budget=500)
#state = agent.perceive(transactions)
#decision = agent.decide()
#agent.act(decision)

April_df = pd.read_excel("April Bank Statement.xlsx")
March_df = pd.read_excel("March Bank statement.xlsx")
df = pd.concat([March_df,April_df], ignore_index=True) #append the 2 dataframes
#print(df) 

#clean Amount column & create credit and debit columns
df['CleanAmount'] = df['Amount'].str.replace('C','',regex=False)
df['CleanAmount'] = df['CleanAmount'].str.replace(',','',regex=False).astype(float)
df['Credit'] = df.apply(
    lambda row: row['CleanAmount'] if any(x in str(row['Amount']) for x in ['C', 'Cr']) else 0, axis=1) 
df['Debit'] = df.apply(
    lambda row: row['CleanAmount'] if all(x not in str(row['Amount']) for x in ['C', 'Cr']) else 0, axis=1)
#drop clean amount
#df.drop(columns='CleanAmount', inplace=True)

#Categorize spending
category_keywords = { #category dictionary
    'Savings_Transfer': ['transfer from', 'payment to investment'],
    'Groceries': ['spar','shoprite'],
    'Take-Out': ['pedros','chicken'],
    'Lunch': ['purchase auditor general'],
    'Transport': ['gautrain', 'vuyo','bolt'],
    'Subcriptions': ['netflix', 'microsoft', 'purchase payflex', 'rain'],
    'Family': ['to lebo', 'to sesi pheladi', 'to sechaba'],
    'savings': ['stokvel'],
    'Matita': ['bobo' "naledi's mom",'send money app','naledi'],
    'Salary': ['magtape credit stansal n984auditor-general']    
}
amount_category = {
    115.00: 'Monthly charges',
    8.00: 'Charges'
}
#everything works fine, just need to categorize using amounts
def categorize(row):
    desc = str(row['Description']).lower()
    amount = row['CleanAmount']
    #Match by exact amount
    if amount in amount_category:
        return amount_category[amount]
    #Match using description
    for category, keywords in category_keywords.items():
        if any(keyword in desc for keyword in keywords):
            return category
    return 'Other' #default if no match

df['Category'] = df.apply(categorize, axis=1)
df.to_excel('output.xlsx')
print('done')
