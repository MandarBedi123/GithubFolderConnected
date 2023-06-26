import tkinter as tk
from tkinter import filedialog, messagebox


def open_file():
  file_path = filedialog.askopenfilename()
  if file_path:
    try:
      with open(file_path, 'r') as file:
        text_editor.delete('1.0', tk.END)
        text_editor.insert(tk.END, file.read())
    except Exception as e:
      messagebox.showerror('Error', str(e))
  print('The file is opened Successfully.')


def save_file():
  file_path = filedialog.asksaveasfilename(defaultextension='.txt')
  if file_path:
    try:
      with open(file_path, 'w') as file:
        file.write(text_editor.get('1.0', tk.END))
    except Exception as e:
      messagebox.showerror('Error', str(e))
  print('The file is saved Successfully.')

def copy_text():
  selected_text = text_editor.selection_get()
  text_editor.clipboard_clear()
  text_editor.clipboard_append(selected_text)
  print('The text is copied Successfully.')

def paste_text():
  text_to_paste = text_editor.clipboard_get()
  text_editor.insert(tk.INSERT, text_to_paste)
  print('The text is pasted Successfully.')

def cut_text():
  copy_text()
  text_editor.delete(tk.SEL_FIRST, tk.SEL_LAST)
  print('The text is cutted Successfully.')

def select_all():
  text_editor.tag_add(tk.SEL, '1.0', tk.END)
  print('The all text is selected Successfully.')


# Create the main window
print('The main window is created Successfully.')
root = tk.Tk()
root.title('Text Editor')

# Create a text widget
print('The text widget is created Successfully.')
text_editor = tk.Text(root)
text_editor.pack()

# Create a menu
menu_bar = tk.Menu(root)
print('The menu is created Successfully.')

# Create File menu 
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
menu_bar.add_cascade(label='File', menu=file_menu)

# Create Edit menu 
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

# Add the menu to the window
root.config(menu=menu_bar)
print('The menu is added to window Successfully.')
print('Now you can type your text.')
print('Also type the name of file with extension while saving it.')



# Start the main event loop
root.mainloop()
print('You exited Successfully.')
print('The text editor is closed Successfully.')
