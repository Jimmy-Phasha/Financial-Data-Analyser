import pandas as pd

class FinancialAgent:
    def __init__(self):
        self.df = pd.DataFrame() #holds processed DataFrame

        #Categorization rules
        self.catefory_keywords = {
            'Savings_Transfer': ['transfer from', 'payment to investment'],
            'Groceries': ['spar', 'shoprite'],
            'Take-Out': ['pedros', 'chicken'],
            'Lunch': ['purchase auditor general'],
            'Transport': ['gautrain', 'vuyo', 'bolt'],
            'Subcriptions': ['netflix', 'microsoft', 'purchase payflex', 'rain'],
            'Family': ['to lebo', 'to sesi pheladi', 'to sechaba'],
            'savings': ['stokvel'],
            'Matita': ['bobo', "naledi's mom", 'send money app', 'naledi'],
            'Salary': ['magtape credit stansal n984auditor-general']
        }

        self.amount_category = {
            115.00: 'Monthly charges',
            8.00: 'Charges'
        }

    def load_files(self,file_paths):
        #Load and merge multiple bank statements
        dfs = [pd.read_excel(path) for path in file_paths]
        self.df = pd.concat(dfs, ignore_index=True)
    
    def clean_data(self):
        #Clean statements/df
        df= self.df.copy()

        df['CleanAmount'] = df['Amount'].astype(str)
        df['CleanAmount'] = df['CleanAmount'].str.replace('C', '', regex=False)
        df['CleanAmount'] = df['CleanAmount'].str.replace(',','',regex=False).astype(float)

        df['Credit'] = df.apply(lambda row: row['CleanAmount'] if any(x in str(row['Amount']) for x in ['C', 'Cr']) else 0, axis=1) 
        df['Debit'] = df.apply(lambda row: row['CleanAmount'] if all(x not in str(row['Amount']) for x in ['C', 'Cr']) else 0, axis=1)

        self.df = df

    def categorize_transactions(self):
        #Categorize transactions
        def categorize(row):
            desc = str(row['Description']).lower()
            amount = row['CleanAmount']

            if amount in self.amount_category:
                return self.amount_category[amount]
            
            for category, keywords in self.catefory_keywords.items():
                if any(keyword in desc for keyword in keywords):
                    return category
            
            return 'Other'
        
        self.df['Category'] = self.df.apply(categorize, axis=1)
    
    def export_to_excel(self, output_path='output.xlsx'):
        self.df.to_excel(output_path, index=False)
        print(f"Exported cleaned data to {output_path}")