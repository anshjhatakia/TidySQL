import tkinter as tk
import tkinter.messagebox as msgbox

select_counter = 0

reserved_word_set = set()
newline_word_set = set()
check_next_word = {"GROUP", "ORDER", "INSERT", "DELETE", 
                      "CREATE", "ALTER", "DROP", "INNER", 
                      "LEFT", "RIGHT"}
final_word_list = []

def initialize_word_sets():
    with open("reserved_words.txt", 'r') as file:
        for word in file:
            curr_word = word.strip()
            if curr_word != "\n":
                reserved_word_set.add(curr_word)
                print(curr_word)
    
    with open("newline_words.txt", 'r') as file:
        for word in file:
            curr_word = word.strip()
            if curr_word != "\n":
                newline_word_set.add(curr_word)
                print(curr_word)

def formatter_core(input_list):
    #print(input_list[0].upper()) TEST
    global select_counter #telling python to apply changes to the variable out of scope

    for word in input_list:
        if word.upper() in newline_word_set:

            if word.upper() == "SELECT":
                final_word_list.append("\n" + select_counter * "     " + word)
                select_counter += 1

            else:
                final_word_list.append("\n" + (select_counter - 1) * "     " + word)
        else:
            final_word_list.append(" " + word)

        print(final_word_list)
    
    display_list()
    
def display_list():
    for line in final_word_list:
        right_tb.insert(tk.END, line)
    


def start_formatting():
    global select_counter, final_word_list

    select_counter = 0
    final_word_list = []
    right_tb.delete("1.0", "end") #Delete current right box content

    text_content = left_tb.get("1.0", "end-1c")  # Get all text from the textbox
    #print(text_content)
    lines_list = text_content.split()  # Split text into a list of lines
    #print(lines_list)
    formatter_core(lines_list) 
    #right_tb.insert("1.0", text_content)

def copy_to_clipboard():
    root.clipboard_clear() #Clear the clipboard
    copied_text=right_tb.get("1.0", "end") #variable equal to right box content
    root.clipboard_append(copied_text) 
    msgbox.showinfo("Copy Successful", "Your tidy SQL has been copied to clipboard.")

def clear_box():
    left_tb.delete("1.0", "end")
    final_word_list = ()
    select_counter = 0

def paste():
    orig_text = root.clipboard_get()
    left_tb.insert("insert", orig_text)

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
program_name = tk.Label(root, text="TidySQL", font=("Cascadia Code", 30))
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
left_tb = tk.Text(root, height=30, width = 65, font=("Cascadia Code", 11), wrap="none")
left_tb.grid(column=0, row=3, pady = 5)
# Bind Ctrl-V to the paste function
left_tb.bind("<Control-v>", paste)

#Create right text box
right_tb = tk.Text(root, height=30, width=65, font=("Cascadia Code", 11), wrap="none")
right_tb.grid(column=2, row=3, pady=5)

#Creating scrollbars
#Left scrollbar (y)
# Create a vertical scrollbar and associate it with the left_tb text widget
scrollbar_left_y = tk.Scrollbar(root, command=left_tb.yview)
scrollbar_left_y.grid(column=1, row=3, sticky='ns')

#Right scrollbar(y)
# Create a vertical scrollbar and associate it with the right_tb text widget
scrollbar_right_y = tk.Scrollbar(root, command=right_tb.yview)
scrollbar_right_y.grid(column=3, row=3, sticky='nsw')

#Left scrollbar (x)
#Create a hotizontal scrollbar and associate it with the left_tb text widget
scrollbar_left_x = tk.Scrollbar(root, command=left_tb.xview, orient=tk.HORIZONTAL)
scrollbar_left_x.grid(column=0, row=4, sticky="ew")

#Right scrollbar (x)
#Create a horizontal scrollbar and associte it with the right_rb text widget
scrollbar_right_x = tk.Scrollbar(root, command=right_tb.xview, orient=tk.HORIZONTAL)
scrollbar_right_x.grid(column=2, row=4, sticky="ew")

# Configure the left text widget to use the scrollbars
left_tb.config(yscrollcommand=scrollbar_left_y.set, xscrollcommand=scrollbar_left_x.set)

# Configure the right text widget to use the scrollbars
right_tb.config(yscrollcommand=scrollbar_right_y.set, xscrollcommand=scrollbar_right_x.set)

#Tidy up button
tidy_up_text = tk.StringVar()
tidy_up_text.set("Tidy up")
tidy_up_button = tk.Button(root, textvariable=tidy_up_text, command=start_formatting, bg="#07611c", font=("Arial", 13))
tidy_up_button.grid(column=0, row=5)

#Clear box button
clear_box_text = tk.StringVar()
clear_box_text.set("Clear")
clear_box_button = tk.Button(root, textvariable=clear_box_text, command=clear_box, bg="#b52836", font=("Arial", 13))
clear_box_button.grid(column=0, row=6)

#Copy to clipboard button
clipboard_text= tk.StringVar()
clipboard_text.set("Copy to clipboard")
clipboard_button = tk.Button(root, textvariable=clipboard_text, command=copy_to_clipboard, bg="#c4bcbd", font=("Arial", 13))
clipboard_button.grid(column=2, row=5)

initialize_word_sets()

root.mainloop()

