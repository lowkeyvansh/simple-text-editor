import tkinter as tk
from tkinter import filedialog

current_file = None

def setup_window():
    root = tk.Tk()
    root.title("Simple Text Editor")
    root.geometry("600x400")
    return root

def create_text_area(root):
    text_area = tk.Text(root, wrap="word")
    text_area.pack(fill="both", expand=True)
    return text_area

def create_menu(root, text_area):
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    
    file_menu.add_command(label="New", command=lambda: new_file(text_area))
    file_menu.add_command(label="Open", command=lambda: open_file(text_area))
    file_menu.add_command(label="Save", command=lambda: save_file(text_area))
    file_menu.add_command(label="Save As", command=lambda: save_as_file(text_area))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

def new_file(text_area):
    global current_file
    current_file = None
    text_area.delete(1.0, tk.END)

def open_file(text_area):
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file(text_area):
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        save_as_file(text_area)

def save_as_file(text_area):
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def main():
    root = setup_window()
    text_area = create_text_area(root)
    create_menu(root, text_area)
    root.mainloop()

if __name__ == "__main__":
    main()
