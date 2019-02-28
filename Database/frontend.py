from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    #e5.delete(0,END)
    #e5.insert(END,selected_tuple[5])

def book_selected():

   for i in list1.curselection():
       c = list1.get(i)
       backend.book(c[0],c[3])

   view_command()

def pool_selected():

   for i in list1.curselection():
       c = list1.get(i)
       backend.pool(c[0],c[3])

   view_command()

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

window=Tk()

window.wm_title("Leihnotebooks")

l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="Hersteller")
l2.grid(row=0,column=2)

l3=Label(window,text="Verfügbarkeit")
l3.grid(row=1,column=0)

l4=Label(window,text="Seriennummer")
l4.grid(row=1,column=2)

l5=Label(window, text="BAM-Nummer")
l5.grid(row=2, column=3)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

bam_text=StringVar()
e5=Entry(window, textvariable=bam_text)
e5.grid(row=3, column=3)

list1=Listbox(window,selectmode ="multiple", height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="Zeige Laptops", width=12,command=view_command)
b1.grid(row=2,column=4)

b2=Button(window,text="Suche", width=12,command=search_command)
b2.grid(row=3,column=4)

b3=Button(window,text="Hinzufügen", width=12,command=add_command)
b3.grid(row=4,column=4)

b4=Button(window,text="Eintrag ändern", width=12,command=update_command)
b4.grid(row=5,column=4)

b5=Button(window,text="Löschen", width=12,command=delete_command)
b5.grid(row=6,column=4)

b6=Button(window,text="Schließen", width=12,command=window.destroy)
b6.grid(row=7,column=4)

b7=Button(window, text="Buchen", width = 12, command = book_selected)
b7.grid(row=5, column=3)

b8=Button(window, text="Pool", width = 12, command = pool_selected)
b8.grid(row=6, column=3)

window.mainloop()
