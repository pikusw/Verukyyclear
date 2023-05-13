import os
import webbrowser
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def clear_temp_files():
    os.system('del /q %temp%\\*')
    console.insert(tk.END, "Usunięto pliki tymczasowe z systemu Windows.\n")
    os.system('del /q %userprofile%\\Downloads\\*')
    console.insert(tk.END, "Usunięto pliki pobrane z internetu.\n")

def open_google():
    webbrowser.open('https://sites.google.com/view/verukyy-browser')
    console.insert(tk.END, "Otworzono stronę do zaktualizowania tą wersje aplikacji.\n")

def clear_console():
    console.delete(1.0, tk.END)

def open_license_window():
    messagebox.showinfo("Informacje o programie", "Dziękujemy za to że masz wersje pro :)")

root = tk.Tk()
root.title('VerukyyClear (Wersja pro :> )')
root.configure(bg="#006600")
root.resizable(False, False)

frame = tk.Frame(root, bg="#006600")
frame.pack(padx=20, pady=20)

# Konsola w oknie aplikacji
console_frame = tk.Frame(root, bg="#006600")
console_frame.pack(padx=20, pady=20)
console_label = tk.Label(console_frame, text="Konsola:", font=("Arial Bold", 14), bg="#006600", fg="white")
console_label.pack()
console = scrolledtext.ScrolledText(console_frame, width=50, height=10, bg="#1f1f2e", fg="white")
console.pack()

# Przycisk do usuwania plików tymczasowych
clear_temp_btn = tk.Button(frame, text='Usuń pliki tymczasowe z systemu Windows', command=clear_temp_files)
clear_temp_btn.pack(padx=5, pady=5)

# Przycisk do otwierania strony Google
google_btn = tk.Button(frame, text='Otwórz stronę do zaktualizowania aplikacji', command=open_google)
google_btn.pack(padx=5, pady=5)

# Przycisk do otwierania okna z informacjami o programie
license_btn = tk.Button(frame, text='Informacje o programie', command=open_license_window)
license_btn.pack(padx=5, pady=5)

# Przycisk do wyczyszczenia konsoli
clear_console_btn = tk.Button(console_frame, text='Wyczyść konsolę', command=clear_console)
clear_console_btn.pack(padx=5, pady=5)

# Napis "Poland" na samym dole
poland_label = tk.Label(root, text="©Pikusw.pl - Programował=Sebastian Wanat", font=("Arial", 10), bg="#006600", fg="red")
poland_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
