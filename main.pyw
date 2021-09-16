import mysql.connector as mysql 
from tkinter import * 
import tkinter.messagebox as MessageBox
from tkinter import ttk 
import os 

def save():
    kodeRS = e_KodeRS.get()
    namaRS = e_NamaRS.get()
    jumPas = e_JumPas.get()
    jumBed = e_JumBed.get()
    tanggal = e_Tanggal.get()
    waktu = e_Waktu.get()
    penginput = e_Penginput.get()

    if (kodeRS == "" or namaRS == "" or jumPas == "" or jumBed == "" or tanggal == "" or waktu == "" or penginput == ""):
        MessageBox.showinfo("Insert Status", "All Fields Are Required")
    else: 
        con = mysql.connect(host = "localhost", user = "root", password = "", database = "infors")
        cursor = con.cursor()
        cursor.execute("insert into datars values('"+ kodeRS +"','"+ namaRS +"','"+ jumPas +"', '"+ jumBed +"', '"+ tanggal +"', '"+ waktu +"', '"+ penginput +"')")
        cursor.execute("commit")

        e_KodeRS.delete(0, "end")
        e_NamaRS.delete(0, "end")
        e_JumPas.delete(0, "end")
        e_JumBed.delete(0, "end")
        e_Tanggal.delete(0, "end")
        e_Waktu.delete(0, "end")
        e_Penginput.delete(0, "end")

        MessageBox.showinfo("Insert Status", "Inserted Succesfully")
        con.close()

def delete():
    if (e_KodeRS.get() == ""):
        MessageBox.showinfo("Delete Status", "Kode RS is compolsary for delete")
    else: 
        con = mysql.connect(host = "localhost", user = "root", password = "", database = "infors")
        cursor = con.cursor()
        cursor.execute("delete from datars where KRS = '"+ e_KodeRS.get()+"' ")
        cursor.execute("commit")

        e_KodeRS.delete(0, "end")
        e_NamaRS.delete(0, "end")
        e_JumPas.delete(0, "end")
        e_JumBed.delete(0, "end")
        e_Tanggal.delete(0, "end")
        e_Waktu.delete(0, "end")
        e_Penginput.delete(0, "end")

        MessageBox.showinfo("Delete Status", "Deleted Succesfully")
        con.close()

def update():

    kodeRS = e_KodeRS.get()
    namaRS = e_NamaRS.get()
    jumPas = e_JumPas.get()
    jumBed = e_JumBed.get()
    tanggal = e_Tanggal.get()
    waktu = e_Waktu.get()
    penginput = e_Penginput.get()

    if (kodeRS == "" or namaRS == "" or jumPas == "" or jumBed == "" or tanggal == "" or waktu == "" or penginput == ""):
        MessageBox.showinfo("Update Status", "All Fields Are Required")
    else: 
        con = mysql.connect(host = "localhost", user = "root", password = "", database = "infors")
        cursor = con.cursor()
        cursor.execute("update datars set KRS = '"+ kodeRS +"', NamRS = '"+ namaRS +"', JumPas = '"+ jumPas +"', JumBed = '"+ jumBed +"', Tanggal = '"+ tanggal +"', Waktu = '"+ waktu +"', Penginput = '"+ penginput +"' where KRS = '"+ kodeRS+"'")
        cursor.execute("commit")

        e_KodeRS.delete(0, "end")
        e_NamaRS.delete(0, "end")
        e_JumPas.delete(0, "end")
        e_JumBed.delete(0, "end")
        e_Tanggal.delete(0, "end")
        e_Waktu.delete(0, "end")
        e_Penginput.delete(0, "end")

        MessageBox.showinfo("Update Status", "Updated Succesfully")
        con.close()
     
def refresh():
    root.destroy()
    os.startfile("main.pyw")

def show():

    con = mysql.connect(host = "localhost", user = "root", password = "", database = "infors")
    cursor = con.cursor()
    cursor.execute("select * from datars")

    newTree = ttk.Treeview()
    
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=newTree.yview)
    newTree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill = "y")


    # Jumlah Kolomnya
    newTree['columns'] = ('krs', 'namars', 'jumpas', 'jumbed', 'tanggal', 'waktu', 'penginput')

    newTree.column('krs', width = 100, minwidth = 100)
    newTree.column('namars', width = 100, minwidth = 100)
    newTree.column('jumpas', width = 100, minwidth = 100)
    newTree.column('jumbed', width = 100, minwidth = 100)
    newTree.column('tanggal', width = 100, minwidth = 100)
    newTree.column('waktu', width = 100, minwidth = 100)
    newTree.column('penginput', width = 100, minwidth = 100)

    newTree.heading('krs', text = "Kode RS")
    newTree.heading('namars', text = "Nama RS")
    newTree.heading('jumpas', text = "Pasien Covid")
    newTree.heading('jumbed', text = "Bed Tersedia")
    newTree.heading('tanggal', text = "Tanggal Input")
    newTree.heading('waktu', text = "Waktu Input")
    newTree.heading('penginput', text = "Penginput")

    i = 0
    for ro in cursor:
        newTree.insert('', i, text = "", values = (ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
        i += 1

    newTree.place(x = 600, y = 180)
    
root = Tk()
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event:root.attributes("-fullscreen", False))
root.config(bg="#3b8bf6")

# Label 
Judul = Label(root, text = "PROGRAM INPUT DATA RUMAH SAKIT PASIEN \nCOVID", font=("Arial", 48), bg ="#e5e7eb")
Judul.place(x = 20, y = 10)

KodeRS = Label(root, text = "Kode RS", font= ("Helevatica", 24), bg="#e5e7eb")
KodeRS.place(x = 20, y = 250)

NamaRS = Label(root, text = "Nama RS", font= ("Helevatica", 24), bg="#e5e7eb")
NamaRS.place(x = 20, y = 350)

JumPas = Label(root, text = "Pasien Covid", font= ("Helevatica", 24))
JumPas.place(x = 20, y = 450)

JumBed = Label(root, text = "Bed Tersisa", font= ("Helevatica", 24))
JumBed.place(x = 20, y = 550)

Tanggal = Label(root, text = "Tanggal", font= ("Helevatica", 24))
Tanggal.place(x = 20, y = 650)

Waktu = Label(root, text = "Waktu", font= ("Helevatica", 24))
Waktu.place(x = 20, y = 700)

Penginput = Label(root, text = "Penginput", font= ("Helevatica", 24))
Penginput.place(x = 20, y = 800)

logo = PhotoImage(file = "C:/_data/_Ahsan/New_Data_3Nov_2020/Belajar Coding/003 - Python/009 - Python Project For LePKom/003 - Aplikasi INput RS/Kemenkes_logo.png")
logoKemenkes = Label(root, image= logo)
logoKemenkes.place(x = 750, y = 550)

# Entry

e_KodeRS = Entry()
e_KodeRS.place(x = 300, y = 250)

e_NamaRS = Entry()
e_NamaRS.place(x = 300, y = 350)

e_JumPas = Entry()
e_JumPas.place(x = 300, y = 450)

e_JumBed = Entry()
e_JumBed.place(x = 300, y = 550)

e_Tanggal = Entry()
e_Tanggal.place(x = 300, y = 650)

e_Waktu = Entry()
e_Waktu.place(x = 300, y = 700)

e_Penginput = Entry()
e_Penginput.place(x = 300, y = 800)

# Button 

Save = Button(root, text = "    SAVE     ", font= ("Helevatica", 24), bg = "white", command = save)
Save.place(x = 1300, y = 450)

Delete = Button(root, text = "  DELETE  ", font= ("Helevatica", 24), bg = "white", command = delete)
Delete.place(x = 1300, y = 520)

Update = Button(root, text = "  UPDATE ", font= ("Helevatica", 24), bg = "white", command = update)
Update.place(x = 1300, y = 590)

Refresh = Button(root, text = "REFRESH", font= ("Helevatica", 24), bg = "white", command= refresh)
Refresh.place(x = 1300, y = 660)

Exit = Button(root, text = "     EXIT    ", font= ("Helevatica", 24), bg = "white", command= root.destroy)
Exit.place(x = 1300, y = 730)

show()

root.mainloop()