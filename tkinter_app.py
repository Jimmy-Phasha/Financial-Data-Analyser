import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from AI import FinancialAgent

agent = FinancialAgent()

def upload_and_process():
    file_paths = filedialog.askopenfilenames(filetypes = [("Excel Files", ".xlsx")]) #list of all excel sheets
    if not file_paths:
        return #User cancelled or file_paths list is empty
    
    try:
        agent.load_files(file_paths)
        agent.clean_data()
        agent.categorize_transactions()
        output_path = agent.export_to_excel()

        messagebox.showinfo("Success", f"Files processed and saved to: \n{output_path}") #pop up message if successful
    except Exception as e:
        messagebox.showerror("Error", str(e)) #error handling

#Build UI
root = tk.Tk()
root.title("Financial Data Analyzer")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Segoe UI", 11), padding=10)
style.configure("TLabel", font=("Segoe UI", 12))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True) #lets frame grow as it resizes and more things are added.

ttk.Label(main_frame, text="Financial Data Analyzer", style="Header.TLabel").pack(pady=(0, 20))
ttk.Label(main_frame, text="Select bank statement files (Excel format):").pack()

ttk.Button(main_frame, text="Upload & Process", command=upload_and_process).pack(pady=10)

root.mainloop()