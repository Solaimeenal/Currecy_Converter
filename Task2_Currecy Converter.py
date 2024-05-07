import tkinter as tk
from tkinter import ttk

# Mock data for exchange rates
# In a real application, you would fetch this data from an API
exchange_rates = {
    'USD': {
        'EUR': 0.85,
        'GBP': 0.75,
        'INR': 74.5,
        'USD': 1
    },
    'EUR': {
        'USD': 1.18,
        'GBP': 0.88,
        'INR': 87.5,
        'EUR': 1
    },
    'GBP': {
        'USD': 1.34,
        'EUR': 1.14,
        'INR': 99.1,
        'GBP': 1
    },
    'INR': {
        'USD': 0.013,
        'EUR': 0.011,
        'GBP': 0.010,
        'INR': 1
    }
}

# Create the main application window
root = tk.Tk()
root.title("Currency Converter")

# Function to convert currency
def convert_currency():
    amount = float(amount_entry.get())
    base_currency = base_currency_combo.get()
    target_currency = target_currency_combo.get()

    # Calculate the converted amount
    converted_amount = amount * exchange_rates[base_currency][target_currency]

    # Display the result
    result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

# Create widgets
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=5)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

base_currency_label = tk.Label(root, text="Base Currency:")
base_currency_label.grid(row=1, column=0, padx=10, pady=5)

base_currency_combo = ttk.Combobox(root, values=list(exchange_rates.keys()))
base_currency_combo.grid(row=1, column=1, padx=10, pady=5)

target_currency_label = tk.Label(root, text="Target Currency:")
target_currency_label.grid(row=2, column=0, padx=10, pady=5)

target_currency_combo = ttk.Combobox(root, values=list(exchange_rates.keys()))
target_currency_combo.grid(row=2, column=1, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Start the application
root.mainloop()
