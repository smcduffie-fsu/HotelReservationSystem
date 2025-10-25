import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ---------------------------------------------------------------------
# THEME STYLING
# ---------------------------------------------------------------------
PRIMARY_BG = "#1E2A38"     # Deep navy background
CARD_BG = "#FFFFFF"        # White card surfaces
ACCENT_BLUE = "#3A7CA5"    # Modern blue accents
TEXT_DARK = "#2D2D2D"
SUCCESS_GREEN = "#00A86B"
INFO_BLUE = "#005BBB"

root = tk.Tk()
root.title("Hotel Reservation System - HRS")
root.geometry("780x500")
root.configure(bg=PRIMARY_BG)

style = ttk.Style()
style.theme_use("clam")

style.configure("TNotebook", background=PRIMARY_BG, borderwidth=0)
style.configure("TNotebook.Tab",
                font=("Segoe UI", 11, "bold"),
                padding=[10, 8],
                background=ACCENT_BLUE,
                foreground="#FFFFFF")
style.map("TNotebook.Tab",
          background=[("selected", CARD_BG)],
          foreground=[("selected", ACCENT_BLUE)])

style.configure("TLabel", background=CARD_BG, foreground=TEXT_DARK, font=("Segoe UI", 10))
style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                padding=6,
                background=ACCENT_BLUE,
                foreground="white")
style.map("TButton",
          background=[("active", "#32708A")])

# ---------------------------------------------------------------------
# Notebook Tabs
# ---------------------------------------------------------------------
tabs = ttk.Notebook(root)
tab_reservation = ttk.Frame(tabs)
tab_checkout = ttk.Frame(tabs)
tabs.add(tab_reservation, text="Make Reservation")
tabs.add(tab_checkout, text="Guest Checkout")
tabs.pack(expand=True, fill="both", padx=8, pady=8)

# ---------------------------------------------------------------------
# CARD containers
# ---------------------------------------------------------------------
def create_card(parent):
    card = tk.Frame(parent, bg=CARD_BG, bd=0, relief="flat")
    card.pack(padx=40, pady=25, fill="both", expand=True)
    return card

res_card = create_card(tab_reservation)
chk_card = create_card(tab_checkout)

# ---------------------------------------------------------------------
# TAB 1: MAKE RESERVATION
# ---------------------------------------------------------------------
title_res = tk.Label(res_card, text="STAFF MAKES A RESERVATION",
                     font=("Segoe UI", 16, "bold"), bg=CARD_BG, fg=ACCENT_BLUE)
title_res.grid(row=0, column=0, columnspan=2, pady=(10, 20))

fields = [
    ("Guest Name:", 1),
    ("Email:", 2),
    ("Phone:", 3),
    ("Check-In (YYYY-MM-DD):", 4),
    ("Check-Out (YYYY-MM-DD):", 5)
]

inputs = {}

for text, row in fields:
    label = tk.Label(res_card, text=text, font=("Segoe UI", 10, "bold"),
                     bg=CARD_BG, fg=TEXT_DARK)
    label.grid(row=row, column=0, sticky="w", pady=6)
    entry = ttk.Entry(res_card, width=32)
    entry.grid(row=row, column=1, sticky="w")
    inputs[text] = entry

# Dropdown fields
tk.Label(res_card, text="Reservation Type:", font=("Segoe UI", 10, "bold"),
         bg=CARD_BG, fg=TEXT_DARK).grid(row=6, column=0, sticky="w", pady=6)
res_type = ttk.Combobox(res_card,
                        values=["PREPAID", "SIXTY_DAY_ADVANCE", "CONVENTIONAL", "INCENTIVE"],
                        font=("Segoe UI", 10))
res_type.grid(row=6, column=1, sticky="w")
res_type.current(0)

tk.Label(res_card, text="Room Type:", font=("Segoe UI", 10, "bold"),
         bg=CARD_BG, fg=TEXT_DARK).grid(row=7, column=0, sticky="w", pady=6)
room_type = ttk.Combobox(res_card,
                         values=["Single", "Double", "Suite"],
                         font=("Segoe UI", 10))
room_type.grid(row=7, column=1, sticky="w")
room_type.current(0)

result_res = tk.Label(res_card, text="", bg=CARD_BG, fg=SUCCESS_GREEN,
                      font=("Segoe UI", 10, "bold"))
result_res.grid(row=9, column=0, columnspan=2, pady=12)

def create_reservation():
    name = inputs["Guest Name:"].get().strip()
    email = inputs["Email:"].get().strip()
    ci = inputs["Check-In (YYYY-MM-DD):"].get().strip()
    co = inputs["Check-Out (YYYY-MM-DD):"].get().strip()

    if not (name and email and ci and co):
        messagebox.showerror("Missing Info", "Please fill in all required fields.")
        return

    try:
        ci_date = datetime.strptime(ci, "%Y-%m-%d")
        co_date = datetime.strptime(co, "%Y-%m-%d")
        if co_date <= ci_date:
            messagebox.showerror("Date Error", "Check-out must be after check-in.")
            return
    except:
        messagebox.showerror("Format Error", "Invalid date format.")
        return

    result_res.config(
        text=f"✅ Reservation created!\n{name} | {res_type.get()} | {room_type.get()}"
    )

ttk.Button(res_card, text="Create Reservation", command=create_reservation)\
    .grid(row=8, column=0, columnspan=2, pady=10)

# ---------------------------------------------------------------------
# TAB 2: CHECKOUT
# ---------------------------------------------------------------------
title_chk = tk.Label(chk_card, text="GUEST CHECKOUT",
                     font=("Segoe UI", 16, "bold"), bg=CARD_BG, fg=ACCENT_BLUE)
title_chk.grid(row=0, column=0, columnspan=2, pady=(10, 20))

chk_fields = [
    ("Guest Name:", 1),
    ("Room Number:", 2),
    ("Total Due ($):", 3)
]

chk_inputs = {}

for text, row in chk_fields:
    label = tk.Label(chk_card, text=text, font=("Segoe UI", 10, "bold"),
                     bg=CARD_BG, fg=TEXT_DARK)
    label.grid(row=row, column=0, sticky="w", pady=6)
    entry = ttk.Entry(chk_card, width=20)
    entry.grid(row=row, column=1, sticky="w")
    chk_inputs[text] = entry

tk.Label(chk_card, text="Payment Method:", font=("Segoe UI", 10, "bold"),
         bg=CARD_BG, fg=TEXT_DARK).grid(row=4, column=0, sticky="w", pady=6)
payment_method = ttk.Combobox(chk_card,
                              values=["Credit Card", "Debit Card", "Cash"],
                              font=("Segoe UI", 10))
payment_method.grid(row=4, column=1, sticky="w")
payment_method.current(0)

result_chk = tk.Label(chk_card, text="", bg=CARD_BG, fg=INFO_BLUE,
                      font=("Segoe UI", 10, "bold"))
result_chk.grid(row=6, column=0, columnspan=2, pady=12)

def process_checkout():
    name = chk_inputs["Guest Name:"].get()
    room = chk_inputs["Room Number:"].get()
    total = chk_inputs["Total Due ($):"].get()
    
    if not (name and room and total):
        messagebox.showerror("Missing Info", "Please fill in all fields.")
        return

    result_chk.config(
        text=f"✔️ Checkout complete\n{name} | Room {room}\nPaid: {payment_method.get()}"
    )

ttk.Button(chk_card, text="Process Checkout", command=process_checkout)\
    .grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
