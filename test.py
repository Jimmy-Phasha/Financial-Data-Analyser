from AI import FinancialAgent

agent = FinancialAgent()

file_paths = [
    "April Bank Statement.xlsx",
    "March Bank statement.xlsx"
]

agent.load_files(file_paths)
agent.clean_data()
agent.categorize_transactions()
agent.export_to_excel()