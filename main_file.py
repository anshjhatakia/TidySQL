import tkinter as tk

root = tk.Tk()

# Set minimum size of the window to the current size
root.update_idletasks()
root.minsize(1280, 720)

# Prevent columns and rows from resizing
for col in range(3):
    root.columnconfigure(col, weight=1)

for row in range(20):
    root.rowconfigure(row, weight=1)

canvas = tk.Canvas(root, width=1280, height=720)
canvas.grid(columnspan=3, rowspan=20)

# Display Program Name
program_name = tk.Label(root, text="TidySQL", font=("Arial", 30))
program_name.grid(columnspan=3, row=0)

# Tell user to paste unformatted code into box
paste_code_message = tk.Label(root, text="Please paste your unformatted SQL code into the box below.", 
                              font = ("Arial", 12))
paste_code_message.grid(column=0, row=1)

#Formatted code below message
fcb_message = tk.Label(root, text="Copy your formatted SQL code from the textbox below.", 
                       font = ("Arial", 12))
fcb_message.grid(column=2, row=1)
root.mainloop()
