# controllers.py

import sqlite3

def get_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def add_product(name, price, quantity):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    conn.close()

def update_product(id, name, price, quantity):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET name=?, price=?, quantity=? WHERE id=?', (name, price, quantity, id))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id=?', (id,))
    conn.commit()
    conn.close()
