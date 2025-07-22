import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


def calculate_age(year_var, month_var, day_var, result_var):
    """Compute age using the provided variables and update result_var."""
    try:
        birth_date = date(
            int(year_var.get()),
            int(month_var.get()),
            int(day_var.get())
        )
        today = date.today()
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future")
            return
        diff = relativedelta(today, birth_date)
        result_var.set(f"Age: {diff.years} years, {diff.months} months, {diff.days} days")
    except ValueError:
        messagebox.showerror("Error", "Invalid date")


def create_gui():
    root = tk.Tk()
    root.title("Age Calculator")

    year_var = tk.StringVar()
    month_var = tk.StringVar()
    day_var = tk.StringVar()
    result_var = tk.StringVar()

    main = ttk.Frame(root, padding=10)
    main.grid()

    ttk.Label(main, text="Year").grid(column=0, row=0, sticky="w")
    ttk.Entry(main, textvariable=year_var, width=10).grid(column=1, row=0)

    ttk.Label(main, text="Month").grid(column=0, row=1, sticky="w")
    ttk.Entry(main, textvariable=month_var, width=10).grid(column=1, row=1)

    ttk.Label(main, text="Day").grid(column=0, row=2, sticky="w")
    ttk.Entry(main, textvariable=day_var, width=10).grid(column=1, row=2)

    calc_cmd = lambda: calculate_age(year_var, month_var, day_var, result_var)
    ttk.Button(main, text="Calculate", command=calc_cmd).grid(column=0, row=3, columnspan=2, pady=5)

    ttk.Label(main, textvariable=result_var).grid(column=0, row=4, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
