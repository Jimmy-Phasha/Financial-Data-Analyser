# 📊 Financial Data Analyzer – Desktop App

**Financial Data Analyzer** is a Python-based Windows desktop application that helps users process and analyze their personal financial data. 
The app allows users to upload monthly bank statements, which are then cleaned and categorized using AI-powered logic. The result is a structured Excel file ready for Power BI dashboards or further analysis.

---

## ✨ Features

📂 Upload one or more Excel (.xlsx) bank statement files
🧹 Automatically cleans and standardizes transaction data
🏷️ Categorizes transactions using keyword-based rules
📤 Exports a clean, categorized version to Excel
📊 Designed for integration with Power BI dashboards
💻 User-friendly interface built with Tkinter

---

## 🚀 Tech Stack

- **Python** – Core logic and data processing
- **Tkinter** – GUI framework
- **Pandas** – Data manipulation and cleaning
- **OpenPyXL / XlsxWriter** – Excel generation
- **Power BI** – Visualization (external dashboard)

---

## ⚙️ How It Works

1. Launch the application on tkinter.py.
2. Click the **Upload & Process** button.
3. Select your Excel bank statement files.
4. The app loads, cleans, and categorizes the transactions.
5. The processed data is exported to an Excel file.
6. Use the exported file to create reports and dashboards in Power BI or other tools.

---

## 🛠 Installation & Usage

- Python 3.8 or higher installed on your machine.
- Required Python packages: pandas, openpyxl


### Install dependencies
```bash
pip install pandas openpyxl

git clone https://github.com/Jimmy-Phasha/Financial-Data-Analyzer.git
python tkinter.py
