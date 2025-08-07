import tkinter as tk
from tkinter import ttk, messagebox

class ResturantOrderManager:
    def __init__(self, root):
        self.root=root
        self.root.title("resturant Management system")
        self.menu_item={
            'FRIES MEAL':2,
            'LUANCH MEAL':2,
            'BURGER MEAL':3,
            'PIZZA MEAL':4,
            'CHEESE BURGER':2.5,
            'DRINKS':1
            
        }
        self.exchange_rate=82
        self.setup_background(root)
        frame=ttk.Frame(self.root)
        
        ttk.Label(frame,text="Welcome to Resturant Management system",
                  font=("Arial", 20, 'bold')).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.menu_labels={}
        self.menu_quantities={}
        for i, (item,price) in enumerate(self.menu_item.items(),start=1):
            label=ttk.Label(frame,
                            text=f"{item} - ${price}",
                            font={"Arial", 34}
        )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry
    