import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import Style
import sqlite3

# Andmebaasi ühendamine
conn = sqlite3.connect('epood_kkalamets')
cursor = conn.cursor()

# Funktsioon andmete kuvamiseks
def kuvada_andmed():
    # Tühjendame varasema sisu
    tekst.delete('1.0', tk.END)
    
    # Haarame kõik andmed andmebaasist
    cursor.execute('SELECT * FROM kkalamets')
    andmed = cursor.fetchall()
    
    # Kuvame andmed tkinteri tekstikastis
    for rida in andmed:
        tekst.insert(tk.END, f"ID: {rida[0]}\n"
                             f"First Name: {rida[1]}\n"
                             f"Last Name: {rida[2]}\n"
                             f"Email: {rida[3]}\n"
                             f"Car Make: {rida[4]}\n"
                             f"Car Model: {rida[5]}\n"
                             f"Car Year: {rida[6]}\n"
                             f"Car Price: {rida[7]}\n"
                             f"---------------------------------\n")

# Funktsioon uue andmerea lisamiseks
def lisa_andmed():
    # Haarame kasutaja sisestatud andmed
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    car_make = entry_car_make.get()
    car_model = entry_car_model.get()
    car_year = entry_car_year.get()
    car_price = entry_car_price.get()
    
    # Lisame uue andmerea andmebaasi
    cursor.execute("INSERT INTO kkalamets (first_name, last_name, email, car_make, car_model, car_year, car_price) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, email, car_make, car_model, car_year, car_price))
    
    # Kinnitame andmebaasi muudatused
    conn.commit()
    
    # Tühjendame sisestusväljad
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_car_make.delete(0, tk.END)
    entry_car_model.delete(0, tk.END)
    entry_car_year.delete(0, tk.END)
    entry_car_price.delete(0, tk.END)
    
    # Värskendame andmete kuvamist
    kuvada_andmed()

# Funktsioon andmete kustutamiseks
def kustuta_andmed():
    # Haarame kasutaja valitud andme ID
    valitud_andme_id = entry_kustuta_id.get()
    
    # Kustutame andmebaasist valitud andme ID-ga rea
    cursor.execute("DELETE FROM kkalamets WHERE id=?", (valitud_andme_id,))
    
    # Kinnitame andmebaasi muudatused
    conn.commit()
    
    # Tühjendame sisestusväli
    entry_kustuta_id.delete(0, tk.END)
def kustuta_kinnitus():
    # Kinnituse küsimine kasutajalt
    vastus = messagebox.askyesno("Kustuta andmed", "Kas olete kindel, et soovite andmed kustutada?")
    if vastus:
        # Kui kasutaja kinnitab, siis kustuta andmed
        kustuta_andmed()
    else:
        # Kui kasutaja ei kinnita, siis ei tee midagi
        return

def otsi_andmed():
# Haarame kasutaja sisestatud otsingusõna
    otsingusona = entry_otsingusona.get()
    cursor.execute("SELECT * FROM kkalamets WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? "
               "OR car_make LIKE ? OR car_model LIKE ? OR car_year LIKE ? OR car_price LIKE ?",
               (f'%{otsingusona}%', f'%{otsingusona}%', f'%{otsingusona}%',
                f'%{otsingusona}%', f'%{otsingusona}%', f'%{otsingusona}%', f'%{otsingusona}%'))
    andmed = cursor.fetchall()
    tekst.delete('1.0', tk.END)
    for rida in andmed:
        tekst.insert(tk.END, f"ID: {rida[0]}\n"
                         f"First Name: {rida[1]}\n"
                         f"Last Name: {rida[2]}\n"
                         f"Email: {rida[3]}\n"
                         f"Car Make: {rida[4]}\n"
                         f"Car Model: {rida[5]}\n"
                         f"Car Year: {rida[6]}\n"
                         f"Car Price: {rida[7]}\n"
                         f"---------------------------------\n")
root = tk.Tk()
root.title("Andmebaasi haldamine")
style = Style(theme='darkly')
style.configure('TLabel', font=('Helvetica', 14))
style.configure('TEntry', font=('Helvetica', 14))
tekst = tk.Text(root, height=20, width=80)
tekst.pack(pady=10)
nupp_kuva_andmed = tk.Button(root, text="Kuva andmed", command=kuvada_andmed)
nupp_kuva_andmed.pack()
label_first_name = tk.Label(root, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(root)
entry_first_name.pack()

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(root)
entry_last_name.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_car_make = tk.Label(root, text="Car Make:")
label_car_make.pack()
entry_car_make = tk.Entry(root)
entry_car_make.pack()

label_car_model = tk.Label(root, text="Car Model:")
label_car_model.pack()
entry_car_model = tk.Entry(root)
entry_car_model.pack()

label_car_year = tk.Label(root, text="Car Year:")
label_car_year.pack()
entry_car_year = tk.Entry(root)
entry_car_year.pack()

label_car_price = tk.Label(root, text="Car Price:")
label_car_price.pack()
entry_car_price = tk.Entry(root)
entry_car_price.pack()
nupp_lisa_andmed = tk.Button(root, text="Lisa andmed", command=lisa_andmed)
nupp_lisa_andmed.pack()

label_kustuta_id = tk.Label(root, text="Sisesta ID, mida kustutada:")
label_kustuta_id.pack()
entry_kustuta_id = tk.Entry(root)
entry_kustuta_id.pack()

nupp_kustuta_andmed = tk.Button(root, text="Kustuta andmed", command=kustuta_kinnitus)
nupp_kustuta_andmed.pack()

label_otsingusona = tk.Label(root, text="Sisesta otsingusõna:")
label_otsingusona.pack()
entry_otsingusona = tk.Entry(root)
entry_otsingusona.pack()

nupp_otsi_andmed = tk.Button(root, text="Otsi andmed", command=otsi_andmed)
nupp_otsi_andmed.pack()

root.mainloop()