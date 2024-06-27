import tkinter as tk
from tkinter import Menu, ttk, messagebox

class Dashboard:
    def __init__(self):
        self.dashboard_window = tk.Toplevel()
        self.dashboard_window.title("Supermarket POS Dashboard")

        # Configure the window to cover the whole screen
        width = self.dashboard_window.winfo_screenwidth()
        height = self.dashboard_window.winfo_screenheight()
        self.dashboard_window.geometry(f"{width}x{height}")

        # Create menu
        self.menu = Menu(self.dashboard_window)
        self.dashboard_window.config(menu=self.menu)

        # Add tabs
        self.tabControl = ttk.Notebook(self.dashboard_window)

        self.sales_tab = ttk.Frame(self.tabControl)
        self.inventory_tab = ttk.Frame(self.tabControl)
        self.customers_tab = ttk.Frame(self.tabControl)
        self.reports_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.sales_tab, text="Sales")
        self.tabControl.add(self.inventory_tab, text="Inventory")
        self.tabControl.add(self.customers_tab, text="Customers")
        self.tabControl.add(self.reports_tab, text="Reports")

        self.tabControl.pack(expand=1, fill="both")

        # Add bodies for tabs
        self.create_sales_body()
        self.create_inventory_body()
        self.create_customers_body()
        self.create_reports_body()

    def create_sales_body(self):
        # Create a frame to contain sales-related elements
        sales_frame = ttk.Frame(self.sales_tab)
        sales_frame.pack(fill="both", expand=True)

        # Sales label
        sales_label = tk.Label(sales_frame, text="Sales", font=("Arial", 16))
        sales_label.pack(pady=10)

        # Table (Treeview) for displaying sales data
        columns = ("ID", "Product", "Quantity", "Price")
        self.sales_tree = ttk.Treeview(sales_frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.sales_tree.heading(col, text=col)
        self.sales_tree.pack(fill="both", expand=True)

        # Sample sales data
        sales_data = [
            ("1", "Product A", "5", "$10"),
            ("2", "Product B", "3", "$15"),
            ("3", "Product C", "2", "$20"),
        ]
        for data in sales_data:
            self.sales_tree.insert("", tk.END, values=data)

        # Button to add new sale
        add_sale_button = tk.Button(sales_frame, text="Add Sale", command=self.add_sale)
        add_sale_button.pack(pady=10)

        # Button to delete selected sale
        delete_sale_button = tk.Button(sales_frame, text="Delete Sale", command=self.delete_sale)
        delete_sale_button.pack(pady=5)

    def add_sale(self):
        # Placeholder for adding a new sale
        product_name = "New Product"
        quantity = 1
        price = "$10"
        new_sale = (str(len(self.sales_tree.get_children()) + 1), product_name, str(quantity), price)
        self.sales_tree.insert("", tk.END, values=new_sale)
        messagebox.showinfo("Success", "New sale added!")

    def delete_sale(self):
        # Delete selected sale
        selected_item = self.sales_tree.selection()
        if selected_item:
            self.sales_tree.delete(selected_item)
            messagebox.showinfo("Success", "Sale deleted.")
        else:
            messagebox.showerror("Error", "Please select a sale to delete.")

    def run(self):
        self.dashboard_window.mainloop()

    def create_inventory_body(self):
        # Add inventory-related functionalities
        inventory_label = tk.Label(self.inventory_tab, text="Inventory")
        inventory_label.pack()

        # Add sample functionality (e.g., buttons)
        add_product_button = tk.Button(self.inventory_tab, text="Add Product", command=self.add_product)
        add_product_button.pack()

    def create_customers_body(self):
        # Add customers-related functionalities
        customers_label = tk.Label(self.customers_tab, text="Customers")
        customers_label.pack()

        # Add sample functionality (e.g., buttons)
        add_customer_button = tk.Button(self.customers_tab, text="Add Customer", command=self.add_customer)
        add_customer_button.pack()

    def create_reports_body(self):
        # Add reports-related functionalities
        reports_label = tk.Label(self.reports_tab, text="Reports")
        reports_label.pack()

        # Add sample functionality (e.g., buttons)
        generate_report_button = tk.Button(self.reports_tab, text="Generate Report", command=self.generate_report)
        generate_report_button.pack()

    def add_sale(self):
        # Create a new dialog window for adding a sale
        add_sale_window = tk.Toplevel(self.dashboard_window)
        add_sale_window.title("Add Sale")

        # Create labels and entry fields for the form
        tk.Label(add_sale_window, text="Product ID:").grid(row=0, column=0)
        product_id_entry = tk.Entry(add_sale_window)
        product_id_entry.grid(row=0, column=1)

        tk.Label(add_sale_window, text="Product Name:").grid(row=1, column=0)
        product_name_entry = tk.Entry(add_sale_window)
        product_name_entry.grid(row=1, column=1)

        tk.Label(add_sale_window, text="Quantity:").grid(row=2, column=0)
        quantity_entry = tk.Entry(add_sale_window)
        quantity_entry.grid(row=2, column=1)

        tk.Label(add_sale_window, text="Price:").grid(row=3, column=0)
        price_entry = tk.Entry(add_sale_window)
        price_entry.grid(row=3, column=1)

        # Function to add the sale to the Treeview
        def add_to_treeview():
            product_id = product_id_entry.get()
            product_name = product_name_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()
            if product_id and product_name and quantity and price:
                new_sale = (product_id, product_name, quantity, price)
                self.sales_tree.insert("", tk.END, values=new_sale)
                add_sale_window.destroy()
                messagebox.showinfo("Success", "New sale added!")
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        # Button to add the sale
        add_button = tk.Button(add_sale_window, text="Add", command=add_to_treeview)
        add_button.grid(row=4, column=0, columnspan=2)


    def add_product(self):
        # Implement add product logic here
        messagebox.showinfo("Info", "Add Product functionality")

    def add_customer(self):
        # Implement add customer logic here
        messagebox.showinfo("Info", "Add Customer functionality")

    def generate_report(self):
        # Implement generate report logic here
        messagebox.showinfo("Info", "Generate Report functionality")

def main():
    dashboard = Dashboard()
    dashboard.dashboard_window.mainloop()

if __name__ == "__main__":
    main()
