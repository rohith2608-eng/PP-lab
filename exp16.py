import tkinter as tk

def calculate():
    total = 0
    credits = [4, 4, 3, 4]
    grades = [g.get() for g in grade_entries]
    grade_points = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'F': 0}
    
    total_credit = sum(credits)
    weighted = sum(grade_points.get(grades[i], 0) * credits[i] for i in range(4))
    sgpa = weighted / total_credit if total_credit else 0
    
    total_label.config(text=f"Total credit: {total_credit}")
    sgpa_label.config(text=f"SGPA: {sgpa:.2f}")

root = tk.Tk()
root.title("MARKSHEET")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root).grid(row=0, column=1)
tk.Label(root, text="Reg.No").grid(row=0, column=2)
tk.Entry(root).grid(row=0, column=3)
tk.Label(root, text="Roll.No").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

headers = ["Srl.No", "Subject", "Grade", "Sub Credit"]
for i, h in enumerate(headers):
    tk.Label(root, text=h, relief="ridge", width=12).grid(row=2, column=i)

subjects = ["PYTHON", "JAVA", "HTML", "OOPS"]
credits  = [4, 4, 3, 4]
grade_entries = []

for i, (sub, cr) in enumerate(zip(subjects, credits)):
    tk.Label(root, text=str(i+1)).grid(row=3+i, column=0)
    tk.Label(root, text=sub).grid(row=3+i, column=1)
    e = tk.Entry(root, width=10)
    e.grid(row=3+i, column=2)
    grade_entries.append(e)
    tk.Label(root, text=str(cr)).grid(row=3+i, column=3)

tk.Button(root, text="Submit", bg="green", fg="white",
          command=calculate).grid(row=7, column=1, pady=10)

total_label = tk.Label(root, text="Total credit: ")
total_label.grid(row=8, column=1, columnspan=2)
sgpa_label  = tk.Label(root, text="SGPA: ")
sgpa_label.grid(row=9, column=1, columnspan=2)

root.mainloop()
