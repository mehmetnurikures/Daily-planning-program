from tkinter import*
from tkinter.font import Font

root = Tk()
root.title('Codemy.com - Todo List!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

# Define our font
my_font =Font(
    family="Brush Scipt MT",
    size = 30,
    weight= "bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame,
    font=my_font,
    width=40,
    height=10,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
    )
my_list.pack()

stuff = ["* Sabah saat 07.30'da yataktan kalk"," *Hava güzelse sabah yürüyüşüne çık", 
"* Evde ekmek yok ise veya canın çektiyse simit al",
"* Terlediysen duşunu al veya doğrudan kahvaltıyı hazırla",
"* Günlük yapılacak işleri planla","* Akademik çalışmalarını yap",
"* Bilgisayar çalışmalarına başla",
"* Tenis için planlama yap"]

# ceklistte yer alacak islerin listeye eklenmesi.

for item in stuff:
    my_list.insert(END,item)

#create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

#add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#create entry box to add list
my_entry=Entry(root, font=("Arial",24))
my_entry.pack(pady=20)

#create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#some functions

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)
    
def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg = "#dedede")
    #Get rid of selection button    
    my_list.selection_clear(0,END)

def uncross_item():
     my_list.itemconfig(
        my_list.curselection(),
        fg = "#646464")
    #Get rid of selection button    
     my_list.selection_clear(0,END)

#Add some buttons
delete_button = Button(button_frame,text="Delete Item",command = delete_item)
add_button = Button(button_frame,text="Add Item",command = add_item)
cross_off_button = Button(button_frame,text="Cross off Item",command = cross_off_item)
uncross_button = Button(button_frame,text="Uncross Item",command = uncross_item)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
cross_off_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3,padx=20)


root.mainloop()

