import tkinter as tk

currency = {
    'gel to eur': 0.34,
    'eur to gel': 2.97,
    'gel to usd': 0.37,
    'usd to gel': 2.69,
    'eur to usd': 1.11,
    'usd to eur': 0.90
}

def show_frame(frame):
    frame.tkraise()

def submit_input():
    global amount
    amount = float(entry.get())
    if amount <= 0:
        input_label.config(text='გთხოვთ, შეიყვანეთ დადებითი რიცხვი')
    else:
        show_frame(page3)

def convert_currency(target_currency):
    conversion_key = f'{selected_base_currency.lower()} to {target_currency.lower()}'
    if conversion_key in currency:
        converted = round(currency[conversion_key] * amount, 4)
        result_label.config(text=f'კონვერტაციით მიღებული შედეგია: {converted} {target_currency}', bg='#D7C3F1')
    else:
        result_label.config(text='იგივე ვალუტაში კონვერტაცია არ ხდება.', bg='#D7C3F1')

def set_base_currency(currency):
    global selected_base_currency
    selected_base_currency = currency
    show_frame(page2)

def restart_app():
    entry.delete(0, tk.END)
    input_label.config(text='შეიყვანეთ თანხის ოდენობა:')
    result_label.config(text='')
    global amount, selected_base_currency
    amount = 0
    selected_base_currency = ''
    show_frame(page1)

root = tk.Tk()
root.resizable(False, False)
root.title("ვალუტის გაცვლითი კურსი")

container = tk.Frame(root)
container.pack(fill="both", expand=True)

page1 = tk.Frame(container, bg='#E2BBE9')
page2 = tk.Frame(container, bg='#E2BBE9')
page3 = tk.Frame(container, bg='#E2BBE9')
page4 = tk.Frame(container, bg='#E2BBE9')

for frame in (page1, page2, page3, page4):
    frame.grid(row=0, column=0, sticky='nsew')

tk.Label(page1, text='აირჩიეთ ვალუტა:', bg='#5A639C', fg='white', font=("Arial", 24)).pack(pady=20)
tk.Button(page1, text='GEL', command=lambda: set_base_currency('GEL')).pack(anchor='w', padx=10, pady=5)
tk.Button(page1, text='EUR', command=lambda: set_base_currency('EUR')).pack(anchor='w', padx=10, pady=5)
tk.Button(page1, text='USD', command=lambda: set_base_currency('USD')).pack(anchor='w', padx=10, pady=5)

input_label = tk.Label(page2, text='შეიყვანეთ თანხის ოდენობა:', bg='#7776B3', fg='white', font=("Arial", 24))
input_label.pack(pady=20)
entry = tk.Entry(page2, width=30)
entry.pack(pady=(0, 10))
tk.Button(page2, text='კონვერტაცია', command=submit_input).pack(pady=20)

tk.Label(page3, text='რომელ ვალუტაში გსურთ კონვერტაცია?', bg='#9B86BD', fg='white', font=("Arial", 24)).pack(pady=20)
tk.Button(page3, text='GEL', command=lambda: (show_frame(page4), convert_currency('GEL'))).pack(anchor='w', padx=10, pady=5)
tk.Button(page3, text='EUR', command=lambda: (show_frame(page4), convert_currency('EUR'))).pack(anchor='w', padx=10, pady=5)
tk.Button(page3, text='USD', command=lambda: (show_frame(page4), convert_currency('USD'))).pack(anchor='w', padx=10, pady=5)

result_label = tk.Label(page4, font=("Arial", 24))
result_label.pack(pady=20)

restart_button = tk.Button(page4, text='გასუფთავება', command=restart_app)
restart_button.pack(pady=20)

show_frame(page1)
root.mainloop()
