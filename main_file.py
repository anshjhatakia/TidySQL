import tkinter as tk

root = tk.Tk()

# Set minimum size of the window to the current size
root.update_idletasks()
min_width = 1280
min_height = 720
root.minsize(min_width, min_height)

# Prevent columns and rows from resizing
for col in range(3):
    root.columnconfigure(col, weight=1)

for row in range(20):
    root.rowconfigure(row, weight=1)

canvas = tk.Canvas(root, width=1280, height=750)
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

#Create left text box
left_tb = tk.Text(root, height=30, width = 65, font = ("Cascadia Code", 11))
left_tb.grid(column=0, row=3, pady = 5)

#Create right text box
right_tb = tk.Text(root, height=30, width=65, font = ("Cascadia Code", 11), state="disabled")
right_tb.grid(column=2, row=3, pady=5)

#Creating scrollbars
#Left scrollbar
# Create a vertical scrollbar and associate it with the left_tb Text widget
scrollbar_left = tk.Scrollbar(root, command=left_tb.yview)
scrollbar_left.grid(column=1, row=3, sticky='ns')

#Right scrollbar
# Create a vertical scrollbar and associate it with the right_tb Text widget
scrollbar_right = tk.Scrollbar(root, command=right_tb.yview)
scrollbar_right.grid(column=3, row=3, sticky='nsw')

# Configure the left text widget to use the scrollbar
left_tb.config(yscrollcommand=scrollbar_left.set)

# Configure the right text widget to use the scrollbar
right_tb.config(yscrollcommand=scrollbar_right.set)

#Tidy up button
tidy_up_text = tk.StringVar()
tidy_up_text.set("Tidy up")
tidy_up_button = tk.Button(root, textvariable=tidy_up_text, bg="#07611c", font=("Arial", 13))
tidy_up_button.grid(column=0, row=4)

#Clear box button
clear_box_text = tk.StringVar()
clear_box_text.set("Clear")
clear_box_button = tk.Button(root, textvariable=clear_box_text, bg="#b52836", font=("Arial", 13))
clear_box_button.grid(column=0, row=5)
root.mainloop()
