import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

def loginwindow(title) :
    global iconbitmap
    log = Tk()
    x = log.winfo_screenwidth()/2 - w/2
    y = log.winfo_screenheight()/2 - h/2
    log.geometry("%dx%d+%d+%d"%(w,h,x,y))
    log.config(bg='#8EC0E7')
    log.title(title)
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    log.iconphoto(False,iconbitmap)
    log.option_add('*font',"'Calibri', 16")
    log.rowconfigure(0,weight=1)
    log.rowconfigure(1,weight=3)
    log.columnconfigure((0,1),weight=1)
    return log

def registerwindow(title) :
    reg = Toplevel()
    x = reg.winfo_screenwidth()/2 - w/2
    y = reg.winfo_screenheight()/2 - h/2
    reg.geometry("%dx%d+%d+%d"%(w,h,x+100,y+100))
    reg.config(bg='#8EC0E7')
    reg.title(title)
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    reg.iconphoto(False,iconbitmap)
    reg.option_add('*font',"'Calibri', 16")
    reg.rowconfigure(0,weight=3)
    reg.rowconfigure(1,weight=1)
    reg.columnconfigure((0,1),weight=1)
    return reg

def cfpassword():
    global cfpwdentry , cfpas
    w = 500
    h = 200
    cfpas = Toplevel()
    x = cfpas.winfo_screenwidth()/2 - w/2
    y = cfpas.winfo_screenheight()/2 - h/2
    cfpas.geometry("%dx%d+%d+%d"%(w,h,x+100,y+100))
    cfpas.config(bg='#8EC0E7')
    cfpas.title('Embose : Confirm Password')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    cfpas.iconphoto(False,iconbitmap)
    cfpas.option_add('*font',"'Calibri', 16")
    cfpas.rowconfigure((0,1,2),weight=1)
    cfpas.columnconfigure((0,1),weight=1)
    Label(cfpas,text="Confirm Password: ",bg='#8EC0E7',fg='#01263F').grid(row=0,column=0,columnspan=2,sticky='s')
    cfpwdentry = Entry(cfpas,width=25,justify=CENTER,textvariable=cpwdinfo)
    cfpwdentry.delete(0, END)
    cfpwdentry.insert(0,' Please confirm your password')
    cfpwdentry.config(state=DISABLED)
    cfpwdentry.bind('<Button-1>',regis5click)
    cfpwdentry.grid(row=1,column=0,columnspan=2,ipady=2,padx=5,sticky='n')
    Button(cfpas,text="Submit",width=10,command=regis, relief="flat", font=('Helvetica', 14), fg='white' , bg='#0E5692').grid(row=2,column=0,columnspan=2,ipady=2,pady=20,sticky='n')

def mainwindow(title,w,h) :
    main = Tk()
    x = main.winfo_screenwidth()/2 - w/2
    y = main.winfo_screenheight()/2 - h/2
    main.geometry("%dx%d+%d+%d"%(w,h,x,y))
    main.config(bg='#8EC0E7')
    main.title(title)
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    main.iconphoto(False,iconbitmap)
    main.option_add('*font',"'Calibri', 16")
    main.rowconfigure(0,weight=1)
    main.columnconfigure((0,1),weight=1)
    return main

def formwindow(title) :
    global formw
    formw = Toplevel()
    w = 545
    h = 700
    x = formw.winfo_screenwidth()/2 - w/2
    y = formw.winfo_screenheight()/2 - h/2
    formw.geometry("%dx%d+%d+%d"%(w,h,x,y))
    formw.config(bg='#8EC0E7')
    formw.title(title)
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    formw.iconphoto(False,iconbitmap)
    formw.option_add('*font',"'Calibri', 16")
    formw.rowconfigure(0,weight=1)
    formw.columnconfigure((0,1),weight=1)

def profilewindow(title,w,h) :
    prof = Tk()
    global womanimg , manimg
    x = prof.winfo_screenwidth()/2 - w/2
    y = prof.winfo_screenheight()/2 - h/2

    womanimg = PhotoImage(file='Image/woman.png').subsample(6,6)
    manimg = PhotoImage(file='Image/man.png').subsample(6,6)
    prof.geometry("%dx%d+%d+%d"%(w,h,x,y))
    prof.config(bg='#8EC0E7')
    prof.title(title)
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    prof.iconphoto(False,iconbitmap)
    prof.option_add('*font',"'Calibri', 16")
    prof.rowconfigure(0,weight=1)
    prof.columnconfigure((0,1),weight=1)
    return prof

def addproductwindow() :
    global addw , pname , pnameinfo , ptypeinfo , ppriceinfo , pquantityinfo , pheaderinfo , CPU , GPU , Mainboard , Ram , PSU , Cooler , HDD
    addw = Toplevel()

    pnameinfo = StringVar()
    ptypeinfo = StringVar()
    ppriceinfo = StringVar()
    pquantityinfo = StringVar()
    pheaderinfo = StringVar()

    types = ['CPU','GPU','Mainboard','Ram','PSU','Cooler','HDD']
    CPU = ['Intel I3','Intel I5','Intel I7','Intel I9','Ryzen 3','Ryzen 5','Ryzen 7','Ryzen 9']
    GPU = ['Nvidia RTX3060','Nvidia RTX3070','Nvidia RTX3080','Radeon RX 6800','Radeon RX 6900']
    Mainboard = ['For AMD','For Intel']
    Ram = ['2Gb','4Gb','8Gb','16Gb','32Gb']
    PSU = ['650W','750W','850W','1000W']
    Cooler = ['Liquid cooling','Fan']
    HDD = ['500GB','1TB','2TB','4TB']

    w = 545
    h = 700
    x = addw.winfo_screenwidth()/2 - w/2
    y = addw.winfo_screenheight()/2 - h/2
    addw.geometry("%dx%d+%d+%d"%(w,h,x,y))
    addw.config(bg='#8EC0E7')
    addw.title('Embose : Add Product')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    addw.iconphoto(False,iconbitmap)
    addw.option_add('*font',"'Calibri', 16")
    addw.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    addw.columnconfigure((0,1,2),weight=1)
    Label(addw,text='Add   Product',fg='white',bg='#01263F', font=('Helvetica 36 bold')).grid(row=0,column=0,columnspan=3,sticky='news')

    Label(addw,text="Product Name: ",bg='#8EC0E7',fg='white').grid(row=1,column=1,sticky='sw')
    pname = ttk.Combobox(addw,width=13,state=DISABLED,justify=CENTER,textvariable=pnameinfo)
    pname.grid(row=2,column=1,ipady=2,padx=5,sticky='nw')

    Label(addw,text="Product Type: ",bg='#8EC0E7',fg='white').grid(row=1,column=2,sticky='sw')
    ptype = ttk.Combobox(addw,width=13,values=types,justify=CENTER,textvariable=ptypeinfo)
    ptype.grid(row=2,column=2,ipady=2,padx=5,sticky='nw')
    ptype.bind('<<ComboboxSelected>>',pnameopen)

    Label(addw,text="Product Price: ",bg='#8EC0E7',fg='white').grid(row=3,column=1,sticky='sw')
    pprice = Entry(addw,width=15,justify=CENTER,textvariable=ppriceinfo)
    pprice.grid(row=4,column=1,ipady=2,padx=5,sticky='nw')

    Label(addw,text="Product Quantity: ",bg='#8EC0E7',fg='white').grid(row=3,column=2,sticky='sw')
    pquantity = Entry(addw,width=15,justify=CENTER,textvariable=pquantityinfo)
    pquantity.grid(row=4,column=2,ipady=2,padx=5,sticky='nw')

    Label(addw,text="Post Header: ",bg='#8EC0E7',fg='white').grid(row=5,column=1,sticky='sw')
    pheader = Entry(addw,width=36,justify=CENTER,textvariable=pheaderinfo)
    pheader.grid(row=6,column=1,ipady=2,columnspan=2,padx=5,sticky='nw')

    Button(addw,text='Submit',bg='#01263F',fg='white', font=('Helvetica 20 bold'), command=addproduct).grid(row=7,column=0,columnspan=3,sticky='s')

def myproductcheck() :
    sql = 'SELECT * FROM Market WHERE Cid = ?'
    cursor.execute(sql,[Cidnow])
    result = cursor.fetchall()
    if result :
        myproductwindow()
    else :
        messagebox.showwarning('Admin',"Don't found your product")

def myproductwindow() :
    global myp , mytree
    global intel_i3 , intel_i5 , intel_i7 , intel_i9 , ryzen_3 , ryzen_5 , ryzen_7 , ryzen_9
    global mainboard_amd , mainboard_intel
    global RTX3060 , RTX3070 , RTX3080 , RX6800 , RX6900
    global HDD4TB , HDD2TB , HDD1TB , HDD500GB
    global PSU650W , PSU750W , PSU850W , PSU1000W
    global RAM2GB , RAM4GB , RAM8GB , RAM16GB , RAM32GB
    global FANCOOLING , LIQUIDCOOLING
    myp = Toplevel()

    intel_i3 = PhotoImage(file='Cpu/INTEL_I3.png').subsample(2,2)
    intel_i5 = PhotoImage(file='Cpu/INTEL_I5.png').subsample(2,2)
    intel_i7 = PhotoImage(file='Cpu/INTEL_I7.png').subsample(2,2)
    intel_i9 = PhotoImage(file='Cpu/INTEL_I9.png').subsample(2,2)
    ryzen_3 = PhotoImage(file='Cpu/RYZEN_3.png').subsample(2,2)
    ryzen_5 = PhotoImage(file='Cpu/RYZEN_5.png').subsample(2,2)
    ryzen_7 = PhotoImage(file='Cpu/RYZEN_7.png').subsample(2,2)
    ryzen_9 = PhotoImage(file='Cpu/RYZEN_9.png').subsample(2,2)

    mainboard_amd = PhotoImage(file='Mainboard/AMDMain.png').subsample(2,2)
    mainboard_intel = PhotoImage(file='Mainboard/INTELMain.png').subsample(2,2)

    RTX3060 = PhotoImage(file='Gpu/RTX3060.png').subsample(2,2)
    RTX3070 = PhotoImage(file='Gpu/RTX3070.png').subsample(2,2)
    RTX3080 = PhotoImage(file='Gpu/RTX3080.png').subsample(2,2)
    RX6800 = PhotoImage(file='Gpu/RX6800.png').subsample(2,2)
    RX6900 = PhotoImage(file='Gpu/RX6900.png').subsample(2,2)

    HDD500GB = PhotoImage(file='HDD/HDD500GB.png').subsample(2,2)
    HDD1TB = PhotoImage(file='HDD/HDD1TB.png').subsample(2,2)
    HDD2TB = PhotoImage(file='HDD/HDD2TB.png').subsample(2,2)
    HDD4TB = PhotoImage(file='HDD/HDD4TB.png').subsample(2,2)

    PSU650W = PhotoImage(file='PSU/PSU650W.png').subsample(2,2)
    PSU750W = PhotoImage(file='PSU/PSU750W.png').subsample(2,2)
    PSU850W = PhotoImage(file='PSU/PSU850W.png').subsample(2,2)
    PSU1000W = PhotoImage(file='PSU/PSU1000W.png').subsample(2,2)

    RAM2GB = PhotoImage(file='RAM/RAM2GB.png').subsample(2,2)
    RAM4GB = PhotoImage(file='RAM/RAM4GB.png').subsample(2,2)
    RAM8GB = PhotoImage(file='RAM/RAM8GB.png').subsample(2,2)
    RAM16GB = PhotoImage(file='RAM/RAM16GB.png').subsample(2,2)
    RAM32GB = PhotoImage(file='RAM/RAM32GB.png').subsample(2,2)

    FANCOOLING = PhotoImage(file='Cooler/FANCOOLING.png').subsample(2,2)
    LIQUIDCOOLING = PhotoImage(file='Cooler/LIQUIDCOOLING.png').subsample(2,2)

    w = 850
    h = 600
    x = myp.winfo_screenwidth()/2 - w/2
    y = myp.winfo_screenheight()/2 - h/2
    myp.geometry("%dx%d+%d+%d"%(w,h,x,y))
    myp.config(bg='#8EC0E7')
    myp.title('Embose : My Product')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    myp.iconphoto(False,iconbitmap)
    myp.option_add('*font',"'Calibri', 16")
    myp.rowconfigure((0,1,2,3),weight=1)
    myp.columnconfigure((0,1,2),weight=1)
    Label(myp,text='My  Product',fg='white',bg='#01263F', font=('Helvetica 36 bold')).grid(row=0,column=0,columnspan=3,sticky='news')

    #Create Treeview
    mytree = ttk.Treeview(myp, columns=("Customer id", "Customer Name", "Product Name", "Product Type", "Product Price", "Product Quantity", "Product header"), height=20)
    #create headings
    mytree.heading('#1', text='Customer id', anchor=CENTER)
    mytree.heading('#2', text='Customer Name', anchor=CENTER)
    mytree.heading('#3', text='Product Name', anchor=CENTER)
    mytree.heading('#4', text='Product Type', anchor=CENTER)
    mytree.heading('#5', text='Product Price', anchor=CENTER)
    mytree.heading('#6', text='Product Quantity', anchor=CENTER)
    mytree.heading('#7', text='Product header', anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('#1', anchor=CENTER, width=100)
    mytree.column('#2', anchor=CENTER, width=110)
    mytree.column('#3', anchor=CENTER, width=100)
    mytree.column('#4', anchor=CENTER, width=100)
    mytree.column('#5', anchor=CENTER, width=100)
    mytree.column('#6', anchor=CENTER, width=110)
    mytree.column('#7', anchor=CENTER, width=150)
    mytree.grid(row=2, column=0,columnspan=3)

    mytree.bind('<Double-1>', mypost)

    mytree.delete(*mytree.get_children())
    sql = 'SELECT * FROM Market WHERE Cid=?'
    cursor.execute(sql,[Cidnow])
    result = cursor.fetchall()
    if result :
        for i,data in enumerate(result) :
            mytree.insert('','end',values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))

def successtoadd() :
    sql = 'INSERT INTO Market (Cid, Cname, Pname, Ptype, Pprice, Pquantity, Pheader) VALUES (?,?,?,?,?,?,?)'
    cursor.execute(sql, [Cidnow , Cnamenow , pnameinfo.get() , ptypeinfo.get() , ppriceinfo.get() , pquantityinfo.get() , pheaderinfo.get()])
    conn.commit()
    messagebox.showinfo('Admin','Successfully add product')
    addw.destroy()

def pnameopen(event) :
    if ptypeinfo.get().upper() == 'CPU' :
        pname.delete(0, END)
        pname['state'] = 'Normal'
        pname['values'] = CPU
    elif ptypeinfo.get().upper() == 'GPU' :
        pname.delete(0, END)
        pname['state'] = 'Normal'
        pname['values'] = GPU
    elif ptypeinfo.get().upper() == 'MAINBOARD' :
        pname.delete(0, END)
        pname['state'] = 'Normal'
        pname['values'] = Mainboard
    elif ptypeinfo.get().upper() == 'RAM' :
        pname.delete(0, END)
        pname['state'] = 'Normal'
        pname['values'] = Ram
    elif ptypeinfo.get().upper() == 'PSU' :
        pname.delete(0, END)
        pname['state'] = 'Normal'
        pname['values'] = PSU
    elif ptypeinfo.get().upper() == 'COOLER' :
        pname.delete(0, END)
        pname['state'] = 'Normal'
        pname['values'] = Cooler
    elif ptypeinfo.get().upper() == 'HDD' :
        pname.delete(0, END)
        pname['state'] = 'Normal'
        pname['values'] = HDD
    else :
        messagebox.showwarning('Admin','Try select type')

def changepwd():
    global oldpwdentry , newpwdentry , cfnewpwdentry , chgpwd , oldpassword , newpassword , cfnewpassword
    w = 400
    h = 300
    chgpwd = Toplevel()
    oldpassword = StringVar()
    newpassword = StringVar()
    cfnewpassword = StringVar()
    x = chgpwd.winfo_screenwidth()/2 - w/2
    y = chgpwd.winfo_screenheight()/2 - h/2
    chgpwd.geometry("%dx%d+%d+%d"%(w,h,x+100,y+100))
    chgpwd.config(bg='#01263F')
    chgpwd.title('Embose : Change Password')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    chgpwd.iconphoto(False,iconbitmap)
    chgpwd.option_add('*font',"'Calibri', 16")
    chgpwd.rowconfigure((0,1,2,3,4),weight=1)
    chgpwd.columnconfigure((0,1),weight=1)
    Label(chgpwd,text="Password: ",bg='#01263F',fg='white').grid(row=1,column=0,sticky='e')
    oldpwdentry = Entry(chgpwd,width=15,justify=CENTER,textvariable=oldpassword,bg='#8EC0E7')
    oldpwdentry.grid(row=1,column=1,ipady=2,padx=5)
    Label(chgpwd,text="New Password: ",bg='#01263F',fg='white').grid(row=2,column=0,sticky='e')
    newpwdentry = Entry(chgpwd,width=15,show='*',justify=CENTER,textvariable=newpassword,bg='#8EC0E7')
    newpwdentry.grid(row=2,column=1,ipady=2,padx=5)
    Label(chgpwd,text="Confirm Password: ",bg='#01263F',fg='white').grid(row=3,column=0,sticky='e')
    cfnewpwdentry = Entry(chgpwd,width=15,show='*',justify=CENTER,textvariable=cfnewpassword,bg='#8EC0E7')
    cfnewpwdentry.grid(row=3,column=1,ipady=2,padx=5)
    Button(chgpwd,text="Submit",width=10,command=changepassword, relief="flat", font=('Helvetica', 14), fg='white' , bg='#0E5692').grid(row=4,column=0,columnspan=2,ipady=2,pady=20,sticky='n')

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('Database/Main.db')
    cursor = conn.cursor()

def login1click(event):
    userentry.config(state=NORMAL)
    userentry.delete(0, END)
    userinfo.set('')

def login2click(event):
    pwdentry.config(state=NORMAL)
    pwdentry.delete(0, END)
    pwdentry['show']='*'
    pwdinfo.set('')

def regis1click(event) :
    usernewentry.config(state=NORMAL)
    usernewentry.delete(0, END)
    usernewinfo.set('')

def regis2click(event) :
    pwdnewentry.config(state=NORMAL)
    pwdnewentry.delete(0, END)
    pwdnewentry['show']='*'
    pwdnewinfo.set('')

def regis3click(event) :
    fnameentry.config(state=NORMAL)
    fnameentry.delete(0, END)
    fname.set('')

def regis4click(event) :
    lnameentry.config(state=NORMAL)
    lnameentry.delete(0, END)
    lname.set('')

def regis5click(event) :
    cfpwdentry.config(state=NORMAL)
    cfpwdentry.delete(0, END)
    cfpwdentry['show']='*'
    cpwdinfo.set('')

def loginlayout() :
    global userentry
    global pwdentry
    global loginframe
    
    loginframe = Frame(log,bg='white')
    loginframe.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    
    Label(loginframe,image=logo2img,bg='white').grid(row=0,column=0,columnspan=2,sticky='n')

    Label(loginframe,text="Login Page",bg='white',fg='#01263F').grid(row=2,column=0,columnspan=2,sticky='s',pady=20)
    
    Label(loginframe,text="User Name: ",bg='white',fg='#01263F').grid(row=5,column=0,sticky='e')
    userentry = Entry(loginframe,width=25,bg='#8EC0E7',justify=CENTER,textvariable=userinfo)
    userentry.delete(0,END)
    userentry.insert(0,'  Enter username')
    userentry.config(state=DISABLED)
    userentry.bind('<Button-1>',login1click)
    userentry.grid(row=5,column=1,sticky='w',ipady=2,padx=5)

    Label(loginframe,text="Password: ",bg='white',fg='#01263F').grid(row=6,column=0,sticky='ne',pady=20)
    pwdentry = Entry(loginframe,width=25,bg='#8EC0E7',justify=CENTER,textvariable=pwdinfo)
    pwdentry.delete(0,END)
    pwdentry.insert(0,'  Enter password')
    pwdentry.config(state=DISABLED)
    pwdentry.bind('<Button-1>',login2click)
    pwdentry.grid(row=6,column=1,sticky='nw',ipady=2,padx=5,pady=20)

    Button(loginframe,text="Login",width=10,command=loginclick, relief="flat", font=('Helvetica', 14), fg='white' , bg='#0E5692').grid(row=7,column=0,columnspan=2,ipady=2,pady=20,sticky='n')
    Button(loginframe,text="Exit",width=10,command=exit, relief="flat", font=('Helvetica', 14), fg='white' , bg='#0E5692').grid(row=7,column=0,ipady=2,pady=20,sticky='ne')
    Button(loginframe,text="Register",width=10,command=registerclick, relief="flat", font=('Helvetica', 14), fg='white' , bg='#0E5692').grid(row=7,column=1,ipady=2,pady=20,sticky='n')

    loginframe.grid(row=0,column=0,columnspan=2,sticky='news')
    userentry.focus_force()

def registerclick() :
    global regframe , reg , usernewentry , pwdnewentry , fnameentry , lnameentry
    w = 800
    h = 500
    reg = registerwindow('Embose : Register')


    regframe = Frame(reg,bg='#8EC0E7')
    regframe.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    regframe.columnconfigure((0,1,2),weight=1)

    Label(regframe,image=regisimg,bg='#8EC0E7').grid(row=0,column=0,columnspan=3,sticky='news')
    
    Label(regframe,text="Username: ",bg='#8EC0E7',fg='#01263F').grid(row=1,column=1,sticky='sw')
    usernewentry = Entry(regframe,width=25,justify=CENTER,textvariable=usernewinfo)
    usernewentry.grid(row=2,column=1,ipady=2,padx=5,sticky='nw')
    usernewentry.bind('<KeyPress-space>',space)
    usernewentry.delete(0,END)
    usernewentry.insert(0,'           Enter username')
    usernewentry.config(state=DISABLED)
    usernewentry.bind('<Button-1>',regis1click)

    Label(regframe,text="Password: ",bg='#8EC0E7',fg='#01263F').grid(row=1,column=2,sticky='sw')
    pwdnewentry = Entry(regframe,width=25,justify=CENTER,textvariable=pwdnewinfo)
    pwdnewentry.grid(row=2,column=2,ipady=2,padx=5,sticky='nw')
    pwdnewentry.bind('<KeyPress-space>',space)
    pwdnewentry.delete(0,END)
    pwdnewentry.insert(0,'           Enter password')
    pwdnewentry.config(state=DISABLED)
    pwdnewentry.bind('<Button-1>',regis2click)

    Label(regframe,text="Firstname: ",bg='#8EC0E7',fg='#01263F').grid(row=3,column=1,sticky='sw')
    fnameentry = Entry(regframe,width=25,justify=CENTER,textvariable=fname)
    fnameentry.grid(row=4,column=1,ipady=2,padx=5,sticky='nw')
    fnameentry.bind('<KeyPress-space>',space)
    fnameentry.delete(0,END)
    fnameentry.insert(0,'           Enter firstname')
    fnameentry.config(state=DISABLED)
    fnameentry.bind('<Button-1>',regis3click)

    Label(regframe,text="Lastname: ",bg='#8EC0E7',fg='#01263F').grid(row=3,column=2,sticky='sw')
    lnameentry = Entry(regframe,width=25,justify=CENTER,textvariable=lname)
    lnameentry.grid(row=4,column=2,ipady=2,padx=5,sticky='nw')
    lnameentry.bind('<KeyPress-space>',space)
    lnameentry.delete(0,END)
    lnameentry.insert(0,'           Enter lastname')
    lnameentry.config(state=DISABLED)
    lnameentry.bind('<Button-1>',regis4click)

    Label(regframe,text="Gender: ",bg='#8EC0E7',fg='#01263F').grid(row=5,column=1,sticky='sw')
    Radiobutton(regframe,image=manimg,text="Male",bg='#8EC0E7',fg='#000',variable=genderinfo,value='Male').grid(row=6,column=1,padx=10,sticky='n')
    Radiobutton(regframe,image=womanimg,text="Female",bg='#8EC0E7',fg='black',variable=genderinfo,value='Female').grid(row=6,column=2,sticky='nw')
    genderinfo.set('Male')

    Button(regframe,text="Exit",width=10,command=Exittologin, relief="flat", font=('Helvetica', 14), fg='white' , bg='#0E5692').grid(row=7,column=1,ipady=2,pady=20,sticky='n')
    Button(regframe,text="Register",width=10,command=checkentry, relief="flat", font=('Helvetica', 14), fg='white' , bg='#0E5692').grid(row=7,column=2,ipady=2,pady=20,sticky='nw')

    regframe.grid(row=0,column=0,columnspan=2,sticky='news')
    reg.mainloop()

def space(event) :
    messagebox.showwarning('Admin:',"Please don't press space")
    regframe.destroy()
    reg.destroy()
    registerclick()

def checkentry() :
    sql = 'SELECT * FROM Customer WHERE Cusername = ?'
    cursor.execute(sql,[usernewinfo.get()])
    result = cursor.fetchall()
    if result : 
        messagebox.showwarning('Admin:','This username is already in use.')
        usernewentry.focus_force()
    else :
        if usernewinfo.get() == "" or usernewinfo.get() == '           Enter username':
            messagebox.showwarning("ADMIN:","Please enter username")
            usernewentry.focus_force()
        else:
            if pwdnewinfo.get() ==  "" or pwdnewinfo.get() ==  "           Enter password":
                messagebox.showwarning("ADMIN","Please enter password")
                pwdnewentry.focus_force()
            else :
                if fname.get() == "" or fname.get() == "           Enter firstname":
                    messagebox.showwarning("ADMIN:","Please enter firstname")
                    fnameentry.focus_force()
                else :
                    if lname.get() == "" or lname.get() == "           Enter lastname":
                        messagebox.showwarning("ADMIN:","Please enter lastname")
                        lnameentry.focus_force()
                    else:
                        cfpassword()

def regis() :
    if cpwdinfo.get() == pwdnewinfo.get() :
        sql = 'SELECT * FROM Customer'
        cursor.execute(sql)
        result = cursor.fetchall()
        Addid=0
        for i,data in enumerate(result) :
            Addid+=1
        Cid = 'CEM' + str(Addid)

        sql = 'INSERT INTO Customer (Cid, Cusername, Cpassword, Cfname, Clname, Cgender, Cbalance) VALUES (?,?,?,?,?,?,?)'
        cursor.execute(sql, [Cid,usernewinfo.get(),pwdnewinfo.get(),fname.get(),lname.get(),genderinfo.get(),0])
        conn.commit()
        messagebox.showinfo('Admin','Registration Success')
        cfpas.destroy()
    else :
        messagebox.showwarning('Admin','Confirm Password Failed')
        cfpwdentry.focus_force()

def Exittologin() :
    usernewinfo.set('')
    pwdnewinfo.set('')
    cpwdinfo.set('')
    fname.set('')
    lname.set('')
    regframe.destroy()
    reg.destroy()

def loginclick() :
    if userinfo.get() == "":
        messagebox.showwarning("ADMIN:","Please enter Username")
        userentry.focus_force()
    else:
        sql = "select * from Customer where Cusername=?" 
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            if pwdinfo.get() ==  "":
                messagebox.showwarning("ADMIN","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from Customer where Cusername=? AND Cpassword=?"
                cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
                result = cursor.fetchone()
                if result:
                    messagebox.showinfo("ADMIN","Login successfully")
                    log.destroy()
                    Embose() #load mainframe
                else:
                    messagebox.showwarning("ADMIN","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showwarning("ADMIN","Username not found\nPlease register before login")    

def Embose() :
    global topframe , typeselect , CPU , GPU , Mainboard , Ram , PSU , Cooler , HDD , Sh , types , logo2img , mainframe , productclaimimg , mainframe , main , manimg , womanimg
    global intel_i3 , intel_i5 , intel_i7 , intel_i9 , ryzen_3 , ryzen_5 , ryzen_7 , ryzen_9
    global mainboard_amd , mainboard_intel
    global RTX3060 , RTX3070 , RTX3080 , RX6800 , RX6900
    global HDD4TB , HDD2TB , HDD1TB , HDD500GB
    global PSU650W , PSU750W , PSU850W , PSU1000W
    global RAM2GB , RAM4GB , RAM8GB , RAM16GB , RAM32GB
    global FANCOOLING , LIQUIDCOOLING
    w = 950
    h = 790
    main = mainwindow('Embose : Main',w,h)
    logoimg = PhotoImage(file='Image/Logo.png')
    logo2img = PhotoImage(file='Image/Logo2.png').subsample(2,2)
    regisimg = PhotoImage(file='Image/Register.png')
    womanimg = PhotoImage(file='Image/woman.png').subsample(6,6)
    manimg = PhotoImage(file='Image/man.png').subsample(6,6)
    iconbitmapimg = PhotoImage(file='Image/Iconbitmap.png')

    intel_i3 = PhotoImage(file='Cpu/INTEL_I3.png').subsample(2,2)
    intel_i5 = PhotoImage(file='Cpu/INTEL_I5.png').subsample(2,2)
    intel_i7 = PhotoImage(file='Cpu/INTEL_I7.png').subsample(2,2)
    intel_i9 = PhotoImage(file='Cpu/INTEL_I9.png').subsample(2,2)
    ryzen_3 = PhotoImage(file='Cpu/RYZEN_3.png').subsample(2,2)
    ryzen_5 = PhotoImage(file='Cpu/RYZEN_5.png').subsample(2,2)
    ryzen_7 = PhotoImage(file='Cpu/RYZEN_7.png').subsample(2,2)
    ryzen_9 = PhotoImage(file='Cpu/RYZEN_9.png').subsample(2,2)

    mainboard_amd = PhotoImage(file='Mainboard/AMDMain.png').subsample(2,2)
    mainboard_intel = PhotoImage(file='Mainboard/INTELMain.png').subsample(2,2)

    RTX3060 = PhotoImage(file='Gpu/RTX3060.png').subsample(2,2)
    RTX3070 = PhotoImage(file='Gpu/RTX3070.png').subsample(2,2)
    RTX3080 = PhotoImage(file='Gpu/RTX3080.png').subsample(2,2)
    RX6800 = PhotoImage(file='Gpu/RX6800.png').subsample(2,2)
    RX6900 = PhotoImage(file='Gpu/RX6900.png').subsample(2,2)

    HDD500GB = PhotoImage(file='HDD/HDD500GB.png').subsample(2,2)
    HDD1TB = PhotoImage(file='HDD/HDD1TB.png').subsample(2,2)
    HDD2TB = PhotoImage(file='HDD/HDD2TB.png').subsample(2,2)
    HDD4TB = PhotoImage(file='HDD/HDD4TB.png').subsample(2,2)

    PSU650W = PhotoImage(file='PSU/PSU650W.png').subsample(2,2)
    PSU750W = PhotoImage(file='PSU/PSU750W.png').subsample(2,2)
    PSU850W = PhotoImage(file='PSU/PSU850W.png').subsample(2,2)
    PSU1000W = PhotoImage(file='PSU/PSU1000W.png').subsample(2,2)

    RAM2GB = PhotoImage(file='RAM/RAM2GB.png').subsample(2,2)
    RAM4GB = PhotoImage(file='RAM/RAM4GB.png').subsample(2,2)
    RAM8GB = PhotoImage(file='RAM/RAM8GB.png').subsample(2,2)
    RAM16GB = PhotoImage(file='RAM/RAM16GB.png').subsample(2,2)
    RAM32GB = PhotoImage(file='RAM/RAM32GB.png').subsample(2,2)

    FANCOOLING = PhotoImage(file='Cooler/FANCOOLING.png').subsample(2,2)
    LIQUIDCOOLING = PhotoImage(file='Cooler/LIQUIDCOOLING.png').subsample(2,2)

    typeselect = StringVar()

    mainframe = Frame(main,bg='#8EC0E7')
    mainframe.rowconfigure((0,1),weight=1)
    mainframe.rowconfigure(2,weight=10)
    mainframe.columnconfigure((0,1),weight=1)
    
    topframe = Frame(mainframe,bg='#8EC0E7')
    topframe.rowconfigure((0,1),weight=1)
    topframe.columnconfigure((0,1,2,3,4),weight=1)
    topframe.grid(row=0,column=0,columnspan=2,sticky='news')

    Label(topframe,bg='#8EC0E7').grid(row=0,column=1,rowspan=2,columnspan=3,sticky='news')

    types =  [ 'COOLER' , 'CPU' , 'GPU' , 'HDD' , 'MAINBOARD' , 'RAM' , 'PSU' ]
    CPU = ['Intel I3','Intel I5','Intel I7','Intel I9','Ryzen 3','Ryzen 5','Ryzen 7','Ryzen 9']
    GPU = ['Nvidia RTX3060','Nvidia RTX3070','Nvidia RTX3080','Radeon RX 6800','Radeon RX 6900']
    Mainboard = ['For AMD','For Intel']
    Ram = ['2Gb','4Gb','8Gb','16Gb','32Gb']
    PSU = ['650W','750W','850W','1000W']
    Cooler = ['Liquid cooling','Fan']
    HDD = ['500GB','1TB','2TB','4TB']

    Sh = Label(topframe, width=45, text='Searching Here',bg='white')
    Sh.grid(row=0,column=1,columnspan=3,padx=10,sticky='we')
    Sh.bind('<Button-1>',Comboshow)

    fbs = Label(topframe,text='Feedback',bg='#44ADE2',fg='white', font=('Helvetica', 20))
    fbs.grid(row=1,column=1,padx=10,sticky='news')
    fbs.bind('<Button-1>',Feedbackshow)
    pdc = Label(topframe,text='Product Claim',bg='#44ADE2',fg='white', font=('Helvetica', 20))
    pdc.grid(row=1,column=2,padx=10,sticky='news')
    pdc.bind('<Button-1>',claimform)
    logout = Label(topframe,text='Log Out',bg='#44ADE2',fg='white', font=('Helvetica', 20))
    logout.grid(row=1,column=3,padx=10,sticky='news')
    logout.bind('<Button-1>',quitnow)

    sql = 'SELECT * FROM Customer WHERE Cusername=?'
    cursor.execute(sql,[userinfo.get()])
    result = cursor.fetchone()

    global Cidnow
    Cidnow = result[0]

    if result[5] == 'Male' :
        x = Label(topframe,image=manimg,bg='#8EC0E7')
        x.grid(row=0,column=4,padx=10,sticky='news')
        x.bind('<Button-1>',profileconfig)
        Label(topframe,text='Account Name\n'+result[3]+' '+result[4],bg='#8EC0E7',fg='white').grid(row=1,column=4,padx=10,sticky='new')
    elif result[5] == 'Female' :
        x = Label(topframe,image=womanimg,bg='#8EC0E7')
        x.grid(row=0,column=4,padx=10,sticky='news')
        x.bind('<Button-1>',profileconfig)
        Label(topframe,text='Account Name\n'+result[3]+' '+result[4],bg='#8EC0E7',fg='white').grid(row=1,column=4,padx=10,sticky='new')

    Label(topframe,image=iconbitmapimg,bg='#8EC0E7').grid(row=0,column=0,rowspan=2,padx=10,sticky='news')

    #Mid
    midframe = Frame(mainframe,bg='#01263F')
    midframe.rowconfigure(0,weight=1)
    midframe.columnconfigure(0,weight=1)
    midframe.grid(row=1,column=0,columnspan=2,sticky='ews')
    Label(midframe,text='PRODUCT CATEGORY',bg='#01263F',fg='white', font=('Helvetica 40 bold')).grid(row=0,column=0,sticky='news')

    cartimg = PhotoImage(file='Image/cart.png').subsample(3,3)
    cpuimg = PhotoImage(file='Image/cpu.png').subsample(3,3)
    mainboardimg = PhotoImage(file='Image/mainboard.png').subsample(3,3)
    ramimg = PhotoImage(file='Image/ram.png').subsample(3,3)
    gpuimg = PhotoImage(file='Image/gpu.png').subsample(3,3)
    harddiskimg = PhotoImage(file='Image/harddisk.png').subsample(3,3)
    coolerimg = PhotoImage(file='Image/cooler.png').subsample(3,3)
    psuimg = PhotoImage(file='Image/psu.png').subsample(3,3)
    promo1 = PhotoImage(file='Image/Promotion_button.png').subsample(3,3)
    marketimg = PhotoImage(file='Image/Market.png').subsample(3,3)
    productclaimimg = PhotoImage(file='Image/ProductClaim.png').subsample(2,2)

    #Bottom
    bottomframe = Frame(mainframe,bg='#0C4870')
    bottomframe.rowconfigure((0,1,2),weight=1)
    bottomframe.columnconfigure((0,1,2,3),weight=1)
    bottomframe.grid(row=2,column=0,columnspan=2,sticky='news')

    cpulabel = Label(bottomframe,image=cpuimg,bg='white')
    cpulabel.grid(row=0,column=0,pady=10)
    cpulabel.bind('<Button-1>',marketcpu)

    mainboardlabel = Label(bottomframe,image=mainboardimg,bg='white')
    mainboardlabel.grid(row=0,column=1,pady=10)
    mainboardlabel.bind('<Button-1>',marketmainboard)

    ramlabel = Label(bottomframe,image=ramimg,bg='white')
    ramlabel.grid(row=0,column=2,pady=10)
    ramlabel.bind('<Button-1>',marketram)

    psulabel = Label(bottomframe,image=psuimg,bg='white')
    psulabel.grid(row=0,column=3,pady=10)
    psulabel.bind('<Button-1>',marketpsu)

    coolerlabel = Label(bottomframe,image=coolerimg,bg='white')
    coolerlabel.grid(row=1,column=0,pady=10)
    coolerlabel.bind('<Button-1>',marketcooler)

    gpulabel = Label(bottomframe,image=gpuimg,bg='white')
    gpulabel.grid(row=1,column=1,pady=10)
    gpulabel.bind('<Button-1>',marketgpu)

    hddlabel = Label(bottomframe,image=harddiskimg,bg='white')
    hddlabel.grid(row=1,column=2,pady=10)
    hddlabel.bind('<Button-1>',markethdd)

    marketlabel = Label(bottomframe,image=marketimg,bg='white')
    marketlabel.grid(row=1,column=3,pady=10)
    marketlabel.bind('<Button-1>',marketall)

    cartlabel = Label(bottomframe,image=cartimg,bg='#0C4870')
    cartlabel.grid(row=2,column=3,sticky='ne',padx=20,pady=10)
    cartlabel.bind('<Button-1>',checkcart)

    mainframe.grid(row=0,column=0,columnspan=2,sticky='news')

    main.mainloop()

def Feedbackshow(event) :
    global fbs
    fbs = Toplevel()

    w = 600
    h = 650
    x = fbs.winfo_screenwidth()/2 - w/2
    y = fbs.winfo_screenheight()/2 - h/2
    fbs.geometry("%dx%d+%d+%d"%(w,h,x,y))
    fbs.config(bg='#8EC0E7')
    fbs.title('Embose : Feedback')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    fbs.iconphoto(False,iconbitmap)
    fbs.option_add('*font',"'Calibri', 16")
    fbs.rowconfigure((0,1,2,3),weight=1)
    fbs.columnconfigure((0,1,2),weight=1)

    Label(fbs,text='Feedback everyone',fg='white',bg='#01263F', font=('Helvetica 36 bold')).grid(row=0,column=0,columnspan=3,sticky='new')
    #Create Treeview
    mytree = ttk.Treeview(fbs, columns=("No", "Feed"), height=25)
    #create headings
    mytree.heading('#1', text='No', anchor=CENTER)
    mytree.heading('#2', text='Feedback', anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('#1', anchor=CENTER, width=50)
    mytree.column('#2', anchor=CENTER, width=500)
    mytree.grid(row=2, column=0,columnspan=3)

    mytree.delete(*mytree.get_children())
    sql = 'SELECT * FROM Feedback'
    cursor.execute(sql)
    result = cursor.fetchall()
    if result :
        for i,data in enumerate(result) :
            mytree.insert('','end',values=(i,data[0]))

def marketcpu(event) :
    showmarket('CPU')

def marketgpu(event) :
    showmarket('GPU')

def marketpsu(event) :
    showmarket('PSU')

def marketcooler(event) :
    showmarket('Cooler')

def markethdd(event) :
    showmarket('HDD')

def marketram(event) :
    showmarket('Ram')

def marketmainboard(event) :
    showmarket('Mainboard')

def marketall(event) :
    showmarket('Market')

def showmarket(typeinput) :
    global marketf , mytree , headerget
    marketf = Toplevel()

    w = 750
    h = 600
    x = marketf.winfo_screenwidth()/2 - w/2
    y = marketf.winfo_screenheight()/2 - h/2
    marketf.geometry("%dx%d+%d+%d"%(w,h,x,y))
    marketf.config(bg='#8EC0E7')
    marketf.title('Embose : Market')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    marketf.iconphoto(False,iconbitmap)
    marketf.option_add('*font',"'Calibri', 16")
    marketf.rowconfigure((0,1,2,3),weight=1)
    marketf.columnconfigure((0,1,2),weight=1)
    Label(marketf,text=typeinput.upper(),fg='white',bg='#01263F', font=('Helvetica 36 bold')).grid(row=0,column=0,columnspan=3,sticky='news')

    #Create Treeview
    mytree = ttk.Treeview(marketf, columns=('NO',"Header", "Quantity", "Price"), height=20)
    #create headings
    mytree.heading('#1', text='', anchor=CENTER)
    mytree.heading('#2', text='Header', anchor=CENTER)
    mytree.heading('#3', text='Quantity', anchor=CENTER)
    mytree.heading('#4', text='Price', anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('#1', anchor=CENTER, width=20)
    mytree.column('#2', anchor=CENTER, width=500)
    mytree.column('#3', anchor=CENTER, width=100)
    mytree.column('#4', anchor=CENTER, width=100)
    mytree.grid(row=2, column=0,columnspan=3)

    mytree.bind('<Double-1>', postshow)

    if typeinput.upper() == 'CPU' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Ptype=?'
        cursor.execute(sql,[typeinput])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput.upper() == 'GPU' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Ptype=?'
        cursor.execute(sql,[typeinput])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput.upper() == 'PSU' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Ptype=?'
        cursor.execute(sql,[typeinput])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput.upper() == 'MAINBOARD' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Ptype=?'
        cursor.execute(sql,[typeinput])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput.upper() == 'RAM' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Ptype=?'
        cursor.execute(sql,[typeinput])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput.upper() == 'HDD' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Ptype=?'
        cursor.execute(sql,[typeinput])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput.upper() == 'COOLER' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Ptype=?'
        cursor.execute(sql,[typeinput])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput.upper() == 'MARKET' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market'
        cursor.execute(sql)
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))

def profileconfig(event) :
    global womanimg , manimg , profileimg , prof
    main.destroy()
    w = 600
    h = 790
    prof = profilewindow('Embose : Profile Config',w,h)
    
    womanimg = PhotoImage(file='Image/woman.png').subsample(4,4)
    manimg = PhotoImage(file='Image/man.png').subsample(4,4)
    profileimg = PhotoImage(file='Image/profile.png')

    profileframe = Frame(prof,bg='#01263F')
    profileframe.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    profileframe.columnconfigure((0,1,2,3),weight=1)

    Label(profileframe,image=profileimg,bg='#8EC0E7').grid(row=0,column=0,columnspan=4,sticky='news')

    sql = 'SELECT * FROM Customer WHERE Cusername=?'
    cursor.execute(sql,[userinfo.get()])
    result = cursor.fetchone()

    global Cidnow , Cnamenow
    Cidnow = result[0]
    Cnamenow = result[3]+' '+result[4]

    if result[5] == 'Male' :
        Label(profileframe,image=manimg,bg='#01263F').grid(row=1,column=0,columnspan=4,sticky='ews')
    elif result[5] == 'Female' :
        Label(profileframe,image=womanimg,bg='#01263F').grid(row=1,column=0,columnspan=4,sticky='ews')

    Label(profileframe,text='CustomerID :',bg='#01263F',fg='white',font=('Helvetica 18 bold')).grid(row=2,column=0,columnspan=2,padx=5,sticky='e')
    Label(profileframe,text=result[0],bg='#01263F',fg='white',font=('Helvetica 18 bold')).grid(row=2,column=2,padx=5,sticky='w')

    Label(profileframe,text='Username :',bg='#01263F',fg='white',font=('Helvetica 18 bold')).grid(row=3,column=0,padx=5,sticky='e')
    Label(profileframe,text=result[1],bg='#01263F',fg='white',font=('Helvetica 18 bold')).grid(row=3,column=1,sticky='w')

    Label(profileframe,text='Password :',bg='#01263F',fg='white',font=('Helvetica 18 bold')).grid(row=3,column=1,columnspan=2,padx=5)
    Label(profileframe,text='******',bg='#01263F',fg='white',font=('Helvetica 18 bold')).grid(row=3,column=2,columnspan=2)

    Button(profileframe,text='Change Password',width=19,relief=FLAT,bg='#44ADE2',fg='white',font=('Helvetica 18 bold'),command=changepwd).grid(row=5,rowspan=2,column=0,columnspan=2,sticky='e',padx=5,pady=20)
    Button(profileframe,text='Exit',width=12,relief=FLAT,bg='#44ADE2',fg='white',font=('Helvetica 18 bold'),command=exittomain).grid(row=5,column=2,rowspan=2,columnspan=2,padx=5,sticky='w',pady=20)
    Button(profileframe,text='My Product sale',width=19,relief=FLAT,bg='#44ADE2',fg='white',font=('Helvetica 18 bold'),command=myproductcheck).grid(row=6,column=0,columnspan=2,sticky='es',padx=5,pady=5)
    Button(profileframe,text='Feedback',width=12,relief=FLAT,bg='#44ADE2',fg='white',font=('Helvetica 18 bold'),command=feedback).grid(row=6,column=2,columnspan=2,padx=5,sticky='ws',pady=5)
    Button(profileframe,text='Add Product for sale',width=32,relief=FLAT,bg='#44ADE2',fg='white',font=('Helvetica 18 bold'),command=addproductwindow).grid(row=7,column=0,columnspan=4,pady=3,sticky='n')

    profileframe.grid(row=0,column=0,columnspan=2,sticky='news')

def feedback() :
    global feedp , feedinfo
    feedp = Toplevel()
    feedinfo = StringVar()

    w = 600
    h = 200
    x = feedp.winfo_screenwidth()/2 - w/2
    y = feedp.winfo_screenheight()/2 - h/2
    feedp.geometry("%dx%d+%d+%d"%(w,h,x,y))
    feedp.config(bg='#8EC0E7')
    feedp.title('Embose : Feedback')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    feedp.iconphoto(False,iconbitmap)
    feedp.option_add('*font',"'Calibri', 16")
    feedp.rowconfigure((0,1,2,3),weight=1)
    feedp.columnconfigure((0,1,2),weight=1)

    Label(feedp,text='Feedback',fg='white',bg='#01263F', font=('Helvetica 36 bold')).grid(row=0,column=0,columnspan=3,sticky='new')
    Feedbackentry = Entry(feedp,width=45,justify=LEFT,textvariable=feedinfo)
    Feedbackentry.grid(row=1,column=0,columnspan=3,ipady=10)
    Button(feedp,text='Submit',width=15,relief=FLAT,bg='#01263F',fg='white',font=('Helvetica 18 bold'),command=upfeedback).grid(row=2,column=0,columnspan=3,sticky='s')

def upfeedback() :
    sql = 'INSERT INTO Feedback (Ftext) VALUES (?)'
    cursor.execute(sql,[feedinfo.get()])
    messagebox.showinfo('Admin','Update feedback success.')
    conn.commit()
    feedp.destroy()

def addproduct() :
    if pnameinfo.get() == '' or ptypeinfo.get() == '' or ppriceinfo.get() == '' or pquantityinfo.get() == '' or pheaderinfo.get() == '' :
        messagebox.showwarning('Admin','Please complete the information.')
    elif ptypeinfo.get().upper() == 'CPU' :
        if pnameinfo.get() == 'Intel I3' or pnameinfo.get() == 'Intel I5' or pnameinfo.get() ==  'Intel I7' or pnameinfo.get() ==  'Intel I9' or pnameinfo.get() ==  'Ryzen 3' or pnameinfo.get() ==  'Ryzen 5' or pnameinfo.get() == 'Ryzen 7' or pnameinfo.get() == 'Ryzen 9' :
            successtoadd()
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    elif ptypeinfo.get().upper() == 'GPU' :
        if pnameinfo.get() == 'Nvidia RTX3060' or pnameinfo.get() == 'Nvidia RTX3070' or pnameinfo.get() == 'Nvidia RTX3080' or pnameinfo.get() == 'Radeon RX 6800' or pnameinfo.get() == 'Radeon RX 6900' :
            successtoadd()
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    elif ptypeinfo.get().upper() == 'MAINBOARD' :
        if pnameinfo.get() == 'For AMD' or pnameinfo.get() == 'For Intel' :
            successtoadd()
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    elif ptypeinfo.get().upper() == 'RAM' :
        if pnameinfo.get() == '2Gb' or pnameinfo.get() == '4Gb' or pnameinfo.get() == '8Gb' or pnameinfo.get() == '16Gb' or pnameinfo.get() == '32Gb' :
            successtoadd()
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    elif ptypeinfo.get().upper() == 'PSU' :
        if pnameinfo.get() == '650W' or pnameinfo.get() == '750W' or pnameinfo.get() == '850W' or pnameinfo.get() == '1000W' :
            successtoadd()
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    elif ptypeinfo.get().upper() == 'COOLER' :
        if pnameinfo.get() == 'Liquid cooling' or pnameinfo.get() == 'Fan' :
            successtoadd()
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    elif ptypeinfo.get().upper() == 'HDD' :
        if pnameinfo.get() == '500GB' or pnameinfo.get() == '1TB' or pnameinfo.get() == '2TB' or pnameinfo.get() == '4TB' :
            successtoadd()
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    else :
        messagebox.showwarning('Admin','Please complete the information.')

def changepassword() :
    sql = 'SELECT * FROM Customer WHERE Cid=?'
    cursor.execute(sql,[Cidnow])
    result = cursor.fetchone()
    print(result)
    if cfnewpassword.get() == newpassword.get() :
        if oldpassword.get() != newpassword.get() :
            if oldpassword.get() == str(result[2]) :
                sql = 'UPDATE Customer SET Cpassword=? WHERE Cid=?'
                cursor.execute(sql, [newpassword.get(),Cidnow])
                conn.commit()
                messagebox.showinfo('Admin','Change password success')
                chgpwd.destroy()
            else :
                messagebox.showwarning('Admin','Old password failed')
                oldpwdentry.delete(0, END)
                oldpwdentry.focus_force()
        else :
            messagebox.showwarning('Admin','Use new password')
            newpwdentry.delete(0, END)
            newpwdentry.focus_force()
    else :
        messagebox.showwarning('Admin','Confirm password failed')
        cfnewpwdentry.delete(0, END)
        cfnewpwdentry.focus_force()

def quitnow(event) :
    global main , log , userinfo , pwdinfo, usernewinfo , pwdnewinfo , cpwdinfo , fname , lname , genderinfo , logoimg , logo2img , regisimg , womanimg , manimg
    main.destroy()
    w = 800
    h = 500
    log = loginwindow('Embose : Login')
    userinfo = StringVar()
    pwdinfo = StringVar()

    usernewinfo = StringVar()
    pwdnewinfo = StringVar()
    cpwdinfo = StringVar()
    fname = StringVar()
    lname = StringVar()
    genderinfo = StringVar()

    logoimg = PhotoImage(file='Image/Logo.png')
    logo2img = PhotoImage(file='Image/Logo2.png')
    regisimg = PhotoImage(file='Image/Register.png')
    womanimg = PhotoImage(file='Image/woman.png').subsample(6,6)
    manimg = PhotoImage(file='Image/man.png').subsample(6,6)
    loginlayout()

def exittomain() :
    prof.destroy()
    Embose()

def Comboshow(event) :
    Sh.destroy()
    Combo = ttk.Combobox(topframe, width = 18, values=types, justify=CENTER, textvariable=typeselect)
    Combo.set("Select Type")
    Combo.grid(row=0,column=1,columnspan=2,padx=10,sticky='w')
    Combo.bind('<<ComboboxSelected>>',Comboshow2)

def Comboshow2(event) :
    global brandselect
    brandselect = StringVar()
    if typeselect.get() == '' :
        messagebox.showwarning('Admin','Please try selected')
    elif typeselect.get().upper() == 'CPU' :
        Combo2 = ttk.Combobox(topframe, width = 18, values=CPU, justify=CENTER, textvariable=brandselect)
        Combo2.set("Select Type")
        Combo2.grid(row=0,column=2,columnspan=2,padx=20,sticky='e')
        Combo2.bind('<<ComboboxSelected>>',cpubrand)
    elif typeselect.get().upper() == 'GPU' :
        Combo2 = ttk.Combobox(topframe, width = 18, values=GPU, justify=CENTER, textvariable=brandselect)
        Combo2.set("Select Type")
        Combo2.grid(row=0,column=2,columnspan=2,padx=20,sticky='e')
        Combo2.bind('<<ComboboxSelected>>',gpubrand)
    elif typeselect.get().upper() == 'MAINBOARD' :
        Combo2 = ttk.Combobox(topframe, width = 18, values=Mainboard, justify=CENTER, textvariable=brandselect)
        Combo2.set("Select Type")
        Combo2.grid(row=0,column=2,columnspan=2,padx=20,sticky='e')
        Combo2.bind('<<ComboboxSelected>>',mainboardbrand)
    elif typeselect.get().upper() == 'RAM' :
        Combo2 = ttk.Combobox(topframe, width = 18, values=Ram, justify=CENTER, textvariable=brandselect)
        Combo2.set("Select Type")
        Combo2.grid(row=0,column=2,columnspan=2,padx=20,sticky='e')
        Combo2.bind('<<ComboboxSelected>>',rambrand)
    elif typeselect.get().upper() == 'PSU' :
        Combo2 = ttk.Combobox(topframe, width = 18, values=PSU, justify=CENTER, textvariable=brandselect)
        Combo2.set("Select Type")
        Combo2.grid(row=0,column=2,columnspan=2,padx=20,sticky='e')
        Combo2.bind('<<ComboboxSelected>>',psubrand)
    elif typeselect.get().upper() == 'COOLER' :
        Combo2 = ttk.Combobox(topframe, width = 18, values=Cooler, justify=CENTER, textvariable=brandselect)
        Combo2.set("Select Type")
        Combo2.grid(row=0,column=2,columnspan=2,padx=20,sticky='e')
        Combo2.bind('<<ComboboxSelected>>',coolerbrand)
    elif typeselect.get().upper() == 'HDD' :
        Combo2 = ttk.Combobox(topframe, width = 18, values=HDD, justify=CENTER, textvariable=brandselect)
        Combo2.set("Select Type")
        Combo2.grid(row=0,column=2,columnspan=2,padx=20,sticky='e')
        Combo2.bind('<<ComboboxSelected>>',hddbrand)
    else :
        messagebox.showwarning('Admin','Please try selected')

def cpubrand(event) :
    searchbrand('CPU')

def gpubrand(event) :
    searchbrand('GPU')

def rambrand(event) :
    searchbrand('Ram')

def mainboardbrand(event) :
    searchbrand('Mainboard')

def psubrand(event) :
    searchbrand('PSU')

def coolerbrand(event) :
    searchbrand('Cooler')

def hddbrand(event) :
    searchbrand('HDD')

def searchbrand(typeinput) :
    global searchf , mytree , headerget
    searchf = Toplevel()

    w = 750
    h = 600
    x = searchf.winfo_screenwidth()/2 - w/2
    y = searchf.winfo_screenheight()/2 - h/2
    searchf.geometry("%dx%d+%d+%d"%(w,h,x,y))
    searchf.config(bg='#8EC0E7')
    searchf.title('Embose : Market')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    searchf.iconphoto(False,iconbitmap)
    searchf.option_add('*font',"'Calibri', 16")
    searchf.rowconfigure((0,1,2,3),weight=1)
    searchf.columnconfigure((0,1,2),weight=1)
    Label(searchf,text=typeinput,fg='white',bg='#01263F', font=('Helvetica 36 bold')).grid(row=0,column=0,columnspan=3,sticky='news')

    #Create Treeview
    mytree = ttk.Treeview(searchf, columns=('NO',"Header", "Quantity", "Price"), height=20)
    #create headings
    mytree.heading('#1', text='', anchor=CENTER)
    mytree.heading('#2', text='Header', anchor=CENTER)
    mytree.heading('#3', text='Quantity', anchor=CENTER)
    mytree.heading('#4', text='Price', anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('#1', anchor=CENTER, width=20)
    mytree.column('#2', anchor=CENTER, width=500)
    mytree.column('#3', anchor=CENTER, width=100)
    mytree.column('#4', anchor=CENTER, width=100)
    mytree.grid(row=2, column=0,columnspan=3)

    mytree.bind('<Double-1>', postshow)

    if typeinput == 'CPU' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Pname=?'
        cursor.execute(sql,[brandselect.get()])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput == 'GPU' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Pname=?'
        cursor.execute(sql,[brandselect.get()])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput == 'PSU' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Pname=?'
        cursor.execute(sql,[brandselect.get()])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput == 'Mainboard' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Pname=?'
        cursor.execute(sql,[brandselect.get()])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput == 'Ram' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Pname=?'
        cursor.execute(sql,[brandselect.get()])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput == 'HDD' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Pname=?'
        cursor.execute(sql,[brandselect.get()])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))
    elif typeinput == 'Cooler' :
        headerget = []
        mytree.delete(*mytree.get_children())
        sql = 'SELECT * FROM Market WHERE Pname=?'
        cursor.execute(sql,[brandselect.get()])
        result = cursor.fetchall()
        if result :
            for i,data in enumerate(result) :
                Header = '['+data[3]+'] ['+data[2]+'] '+data[6]
                headerget.insert(i, data[6])
                mytree.insert('','end',values=(i,Header,data[5],data[4]))

def mypost(event) :
    global mypos
    mypos = Toplevel()
    mpost = mytree.item(mytree.focus(), 'values')
    protype = mpost[3]
    proname = mpost[2]
    cusid = mpost[0]
    proquan = mpost[5]
    headershow = mpost[6]

    w = 1000
    h = 500
    x = mypos.winfo_screenwidth()/2 - w/2
    y = mypos.winfo_screenheight()/2 - h/2
    mypos.geometry("%dx%d+%d+%d"%(w,h,x,y))
    mypos.config(bg='#8EC0E7')
    mypos.title('Embose : My Product')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    mypos.iconphoto(False,iconbitmap)
    mypos.option_add('*font',"'Calibri', 16")
    mypos.rowconfigure((0,1,2),weight=1)
    mypos.columnconfigure((0,1),weight=1)

    sql = 'SELECT * FROM Customer WHERE Cid=?'
    cursor.execute(sql,[cusid])
    result = cursor.fetchone()

    Label(mypos,bg='#01263F').grid(row=0,column=0,columnspan=2,sticky='news')

    if result[5] == 'Male' :
        Label(mypos,image=manimg,bg='#01263F').grid(row=0,pady=10,column=0,padx=10)
        Label(mypos,text='['+protype+'] ['+proname+'] '+headershow,bg='#01263F',fg='white', font=('Helvetica 20 bold')).grid(row=0,pady=10,column=1,padx=10)
    elif result[5] == 'Female' :
        Label(mypos,image=womanimg,bg='#01263F').grid(row=0,pady=10,column=0,padx=10)
        Label(mypos,text='['+protype+'] ['+proname+'] '+headershow,bg='#01263F',fg='white', font=('Helvetica 20 bold')).grid(row=0,pady=10,column=1,padx=10)

    if protype.upper() == 'CPU' :
        if proname == 'Intel I3' or proname == 'Intel I5' or proname ==  'Intel I7' or proname ==  'Intel I9' or proname ==  'Ryzen 3' or proname ==  'Ryzen 5' or proname == 'Ryzen 7' or proname == 'Ryzen 9' :
            if proname == 'Intel I3' :
                Label(possh,image=intel_i3,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                #Button(mypos,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='s')
            elif proname == 'Intel I5' :
                Label(mypos,image=intel_i5,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Intel I7' :
                Label(mypos,image=intel_i7,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Intel I9' :
                Label(mypos,image=intel_i9,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Ryzen 3' :
                Label(mypos,image=ryzen_3,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Ryzen 5' :
                Label(mypos,image=ryzen_5,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Ryzen 7' :
                Label(mypos,image=ryzen_7,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Ryzen 9' :
                Label(mypos,image=ryzen_9,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
    elif protype.upper() == 'GPU' :
        if proname == 'Nvidia RTX3060' or proname == 'Nvidia RTX3070' or proname == 'Nvidia RTX3080' or proname == 'Radeon RX 6800' or proname == 'Radeon RX 6900' :
            if proname == 'Nvidia RTX3060' :
                Label(mypos,image=RTX3060,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Nvidia RTX3070' :
                Label(mypos,image=RTX3070,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Nvidia RTX3080' :
                Label(mypos,image=RTX3080,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Radeon RX 6800' :
                Label(mypos,image=RX6800,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Radeon RX 6900' :
                Label(mypos,image=RX6900,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
    elif protype.upper() == 'MAINBOARD' :
        if proname == 'For AMD' or proname == 'For Intel' :
            if proname == 'For AMD' :
                Label(mypos,image=mainboard_amd,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'For Intel' :
                Label(mypos,image=mainboard_intel,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
    elif protype.upper() == 'RAM' :
        if proname == '2Gb' or proname == '4Gb' or proname == '8Gb' or proname == '16Gb' or proname == '32Gb' :
            if proname == '2Gb' :
                Label(mypos,image=RAM2GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '4Gb' :
                Label(mypos,image=RAM4GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '8Gb' :
                Label(mypos,image=RAM8GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '16Gb' :
                Label(mypos,image=RAM16GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '32Gb' :
                Label(mypos,image=RAM32GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
    elif protype.upper() == 'PSU' :
        if proname == '650W' or proname == '750W' or proname == '850W' or proname == '1000W' :
            if proname == '650W' :
                Label(mypos,image=PSU650W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '750W' :
                Label(mypos,image=PSU750W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '850W' :
                Label(mypos,image=PSU850W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '1000W' :
                Label(mypos,image=PSU1000W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
    elif protype.upper() == 'COOLER' :
        if proname == 'Liquid cooling' or proname == 'Fan' :
            if proname == 'Liquid cooling' :
                Label(mypos,image=LIQUIDCOOLING,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == 'Fan' :
                Label(mypos,image=FANCOOLING,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
    elif protype.upper() == 'HDD' :
        if proname == '500GB' or proname == '1TB' or proname == '2TB' or proname == '4TB' :
            if proname == '500GB' :
                Label(mypos,image=HDD500GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '1TB' :
                Label(mypos,image=HDD1TB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '2TB' :
                Label(mypos,image=HDD2TB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
            elif proname == '4TB' :
                Label(mypos,image=HDD4TB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(mypos,text='Product Type : '+protype,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,sticky='nw')
                Label(mypos,text='Product Name : '+proname,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=30,padx=10,sticky='nw')
                Label(mypos,text='Product Quantity : '+proquan,bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')

def postshow(event) :
    global possh
    possh = Toplevel()
    mpost = mytree.item(mytree.focus(), 'values')
    numberpost = int(mpost[0])
    sql = 'SELECT * FROM Market WHERE Pheader=?'
    cursor.execute(sql,[headerget[numberpost]])
    result = cursor.fetchone()

    protype = result[3]
    proname = result[2]
    cusid = result[0]
    proquan = result[5]
    headershow = result[6]

    w = 800
    h = 400
    x = possh.winfo_screenwidth()/2 - w/2
    y = possh.winfo_screenheight()/2 - h/2
    possh.geometry("%dx%d+%d+%d"%(w,h,x,y))
    possh.config(bg='#8EC0E7')
    possh.title('Embose : Product')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    possh.iconphoto(False,iconbitmap)
    possh.option_add('*font',"'Calibri', 16")
    possh.rowconfigure((0,1,2),weight=1)
    possh.columnconfigure((0,1),weight=1)

    sql = 'SELECT * FROM Customer WHERE Cid=?'
    cursor.execute(sql,[cusid])
    result = cursor.fetchone()

    Label(possh,bg='#01263F').grid(row=0,column=0,columnspan=2,sticky='news')

    if result[5] == 'Male' :
        Label(possh,image=manimg,bg='#01263F').grid(row=0,pady=10,column=0,padx=10)
        Label(possh,text=headershow,bg='#01263F',fg='white', font=('Helvetica 20 bold')).grid(row=0,pady=10,column=1,padx=10,sticky='w')
    elif result[5] == 'Female' :
        Label(possh,image=womanimg,bg='#01263F').grid(row=0,pady=10,column=0,padx=10)
        Label(possh,text=headershow,bg='#01263F',fg='white', font=('Helvetica 20 bold')).grid(row=0,pady=10,column=1,padx=10,sticky='w')

    if protype.upper() == 'CPU' :
        if proname == 'Intel I3' or proname == 'Intel I5' or proname ==  'Intel I7' or proname ==  'Intel I9' or proname ==  'Ryzen 3' or proname ==  'Ryzen 5' or proname == 'Ryzen 7' or proname == 'Ryzen 9' :
            if proname == 'Intel I3' :
                Label(possh,image=intel_i3,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Intel I5' :
                Label(possh,image=intel_i5,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Intel I7' :
                Label(possh,image=intel_i7,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Intel I9' :
                Label(possh,image=intel_i9,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Ryzen 3' :
                Label(possh,image=ryzen_3,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Ryzen 5' :
                Label(possh,image=ryzen_5,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Ryzen 7' :
                Label(possh,image=ryzen_7,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Ryzen 9' :
                Label(possh,image=ryzen_9,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
    elif protype.upper() == 'GPU' :
        if proname == 'Nvidia RTX3060' or proname == 'Nvidia RTX3070' or proname == 'Nvidia RTX3080' or proname == 'Radeon RX 6800' or proname == 'Radeon RX 6900' :
            if proname == 'Nvidia RTX3060' :
                Label(possh,image=RTX3060,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Nvidia RTX3070' :
                Label(possh,image=RTX3070,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Nvidia RTX3080' :
                Label(possh,image=RTX3080,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Radeon RX 6800' :
                Label(possh,image=RX6800,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Radeon RX 6900' :
                Label(possh,image=RX6900,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
    elif protype.upper() == 'MAINBOARD' :
        if proname == 'For AMD' or proname == 'For Intel' :
            if proname == 'For AMD' :
                Label(possh,image=mainboard_amd,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'For Intel' :
                Label(possh,image=mainboard_intel,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
    elif protype.upper() == 'RAM' :
        if proname == '2Gb' or proname == '4Gb' or proname == '8Gb' or proname == '16Gb' or proname == '32Gb' :
            if proname == '2Gb' :
                Label(possh,image=RAM2GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '4Gb' :
                Label(possh,image=RAM4GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '8Gb' :
                Label(possh,image=RAM8GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '16Gb' :
                Label(possh,image=RAM16GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '32Gb' :
                Label(possh,image=RAM32GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
    elif protype.upper() == 'PSU' :
        if proname == '650W' or proname == '750W' or proname == '850W' or proname == '1000W' :
            if proname == '650W' :
                Label(possh,image=PSU650W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '750W' :
                Label(possh,image=PSU750W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '850W' :
                Label(possh,image=PSU850W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '1000W' :
                Label(possh,image=PSU1000W,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
    elif protype.upper() == 'COOLER' :
        if proname == 'Liquid cooling' or proname == 'Fan' :
            if proname == 'Liquid cooling' :
                Label(possh,image=LIQUIDCOOLING,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == 'Fan' :
                Label(possh,image=FANCOOLING,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
    elif protype.upper() == 'HDD' :
        if proname == '500GB' or proname == '1TB' or proname == '2TB' or proname == '4TB' :
            if proname == '500GB' :
                Label(possh,image=HDD500GB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '1TB' :
                Label(possh,image=HDD1TB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '2TB' :
                Label(possh,image=HDD2TB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')
            elif proname == '4TB' :
                Label(possh,image=HDD4TB,bg='#8EC0E7').grid(row=2,column=0,padx=10,sticky='nw')
                Label(possh,text='Product Type : %s'%(protype),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,padx=10,pady=30,sticky='nw')
                Label(possh,text='Product Name : %s'%(proname),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=60,padx=10,sticky='nw')
                Label(possh,text='Product Quantity : %s'%(proquan),bg='#8EC0E7',font=('Helvetica 16 bold'),fg='white').grid(row=2,column=1,pady=90,padx=10,sticky='nw')
                Button(possh,text='Add to cart',width=20,bg='#01263F',fg='white',font=('Helvetica 16 bold'),command=addtocart).grid(row=2,column=1,padx=10,pady=30,sticky='sw')

def addtocart() :
    mpost = mytree.item(mytree.focus(), 'values')
    numberpost = int(mpost[0])
    sql = 'SELECT * FROM Market WHERE Pheader=?'
    cursor.execute(sql,[headerget[numberpost]])
    result = cursor.fetchone()

    proid = result[0]
    protype = result[3]
    proname = result[2]
    proprice = result[4]
    proquan = result[5]
    headershow = result[6]
    if proquan > 0:
        if proid == Cidnow :
            messagebox.showwarning('Admin','This is your product.')
            possh.destroy()
        else :
            sql = 'SELECT * FROM Cart WHERE Cid=? And Ptype=? And Pname=? And Pheader=?'
            cursor.execute(sql,[Cidnow,protype,proname,headershow])
            result = cursor.fetchone()
            if result :
                if result[4] < proquan :
                    proquan2 = result[4] + 1
                    sql = 'UPDATE Cart SET Cid=?, Ptype=?, Pname=?, Pheader=?, Pquantity=?, Pprice=? WHERE Pheader=?'
                    cursor.execute(sql,[Cidnow,protype,proname,headershow,proquan2,proprice,headershow])
                    messagebox.showinfo('Admin','Add product success')
                    conn.commit()
                    possh.destroy()
                else :
                    messagebox.showwarning('Admin','Product not enough.')
                    possh.destroy()
            else :
                proquan = 1
                sql = 'INSERT INTO Cart (Cid, Ptype, Pname, Pheader, Pquantity, Pprice) VALUES (?,?,?,?,?,?)'
                cursor.execute(sql,[Cidnow,protype,proname,headershow,proquan,proprice])
                messagebox.showinfo('Admin','Add product success')
                conn.commit()
                possh.destroy()
    else :
        messagebox.showwarning('Admin','Product not enough')
        possh.destroy()

def checkcart(event) :
    sql = 'SELECT * FROM Cart WHERE Cid=?'
    cursor.execute(sql,[Cidnow])
    result = cursor.fetchone()
    if result :
        cart()
    else :
        messagebox.showwarning('Admin',"Don't found cart")

def cart() :
    global cartp
    cartp = Toplevel()

    w = 800
    h = 600
    x = cartp.winfo_screenwidth()/2 - w/2
    y = cartp.winfo_screenheight()/2 - h/2
    cartp.geometry("%dx%d+%d+%d"%(w,h,x,y))
    cartp.config(bg='#8EC0E7')
    cartp.title('Embose : Cart')
    iconbitmap = PhotoImage(file='Image/Iconbitmap.png')
    cartp.iconphoto(False,iconbitmap)
    cartp.option_add('*font',"'Calibri', 16")
    cartp.rowconfigure((0,1,2,3,4,5),weight=1)
    cartp.columnconfigure((0,1,2),weight=1)

    sql = 'SELECT * FROM Cart WHERE Cid=?'
    cursor.execute(sql,[Cidnow])
    result = cursor.fetchall()
    Label(cartp,text='Cart',fg='white',bg='#01263F', font=('Helvetica 36 bold')).grid(row=0,column=0,columnspan=3,sticky='new')

    for i,data in enumerate(result) :
        sum = int(data[4]) * int(data[5])
        x1 = Entry(cartp,width=45,justify=CENTER,bg='#8EC0E7')
        x1.delete(0,END)
        x1.insert(0,data[1]+' '+data[2]+'     amount : '+str(data[4])+'   Price : '+str(sum))
        x1.config(state=DISABLED)
        x1.grid(row=i+2,column=0,ipady=2,padx=5,sticky='e')
    Button(cartp,text='Buy',font=('Helvetica 20 bold'),width=15,fg='white',bg='#01263F',command=buyall).grid(row=i+3, column=0, columnspan=3)

    if i == 0 or i > 0:
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(0)).grid(row=2, column=1)
    if i == 1 or i > 1 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(1)).grid(row=3, column=1)
    if i == 2 or i > 2 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(2)).grid(row=4, column=1)
    if i == 3 or i > 3 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(3)).grid(row=5, column=1)
    if i == 4 or i > 4 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(4)).grid(row=6, column=1)
    if i == 5 or i > 5 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(5)).grid(row=7, column=1)
    if i == 6 or i > 6 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(6)).grid(row=8, column=1)
    if i == 7 or i > 7 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(7)).grid(row=9, column=1)
    if i == 8 or i > 8 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(8)).grid(row=10, column=1)
    if i == 9 or i > 9 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(9)).grid(row=11, column=1)
    if i == 10 or i > 10 :
        Button(cartp,text='delete',fg='white',bg='#01263F',command=lambda:delete(10)).grid(row=12, column=1)

def delete(input) :
    sql = 'SELECT * FROM Cart WHERE Cid=?'
    cursor.execute(sql,[Cidnow])
    result = cursor.fetchall()
    for i,data in enumerate(result) : 
        if i == input :
            sql = 'DELETE FROM Cart WHERE Cid=? And Ptype=? And Pname=?'
            messagebox.showinfo('Admin',"Delete Success.")
            cursor.execute(sql, [Cidnow,data[1],data[2]])
            conn.commit()
            cartp.destroy()

def buyall() :
    sql = 'SELECT * FROM Cart WHERE Cid=?'
    cursor.execute(sql,[Cidnow])
    result = cursor.fetchall()
    for i in result :
        if result :
            sql = 'SELECT * FROM Market WHERE Pname=? And Ptype=? And Pheader=?'
            cursor.execute(sql,[i[2],i[1],i[3]])
            result2 = cursor.fetchall()
            for x in result2 :
                if result2 :
                    newquantity = x[5] - i[4]
                    print(newquantity)
                    sql = 'UPDATE Market SET Pquantity=? WHERE Ptype=? And Pname=? And Pheader=?'
                    cursor.execute(sql,[newquantity,x[3],x[2],x[6]])
                    conn.commit()

    sql = 'DELETE FROM Cart WHERE Cid=?'
    cursor.execute(sql, [Cidnow])
            
    conn.commit()
    messagebox.showinfo('Admin',"Buy Success.")
    cartp.destroy()

def claimform(event) :
    global claimframe
    formwindow('Embose : Product Claim',)
    claimframe = Frame(formw,bg='white')
    claimframe.rowconfigure(0,weight=1)
    claimframe.rowconfigure(1,weight=4)
    claimframe.columnconfigure((0,1),weight=1)
    Label(claimframe,image=logo2img,bg='#8EC0E7').grid(row=0,column=0,columnspan=2,sticky='news')
    Label(claimframe,image=productclaimimg,bg='white').grid(row=1,column=0,columnspan=2,sticky='new')

    Button(claimframe,text='Claim form',width=10,bg='#44ADE2',relief=FLAT,fg='white',command=claimproduct).grid(row=1,column=0,columnspan=2,sticky='s',pady=10)

    claimframe.grid(row=0,column=0,columnspan=2,sticky='news')

def claimproduct() :
    global cfnameinfo , clnameinfo , ccidinfo , cptype , cpname , claimproductform , claimid , claimpname , CPU2 , GPU2 , Mainboard2 , Ram2 , PSU2 , Cooler2 , HDD2
    cfnameinfo = StringVar()
    clnameinfo = StringVar()
    ccidinfo = StringVar()
    cptype = StringVar()
    cpname = StringVar()

    CPU2 = ['Intel I3','Intel I5','Intel I7','Intel I9','Ryzen 3','Ryzen 5','Ryzen 7','Ryzen 9']
    GPU2 = ['Nvidia RTX3060','Nvidia RTX3070','Nvidia RTX3080','Radeon RX 6800','Radeon RX 6900']
    Mainboard2 = ['For AMD','For Intel']
    Ram2 = ['2Gb','4Gb','8Gb','16Gb','32Gb']
    PSU2 = ['650W','750W','850W','1000W']
    Cooler2 = ['Liquid cooling','Fan']
    HDD2 = ['500GB','1TB','2TB','4TB']

    claimframe.destroy()
    claimproductform = Frame(formw,bg='#8EC0E7')
    claimproductform.rowconfigure(0,weight=2)
    claimproductform.rowconfigure((1,2,3,4,5,6,7,8,9,10,11,12,13),weight=1)
    claimproductform.columnconfigure((0,1),weight=1)
    Label(claimproductform,image=logo2img,bg='#8EC0E7').grid(row=0,column=0,columnspan=2,sticky='news')

    Label(claimproductform,text='Product Claim Form',bg='#01263F',fg='white',font=('Helvetica 38 bold')).grid(row=1,column=0,columnspan=2,sticky='news')

    Label(claimproductform,text="First Name: ",bg='#8EC0E7',fg='#01263F').grid(row=2,column=0,padx=40,sticky='ws')
    claimfname = Entry(claimproductform,width=17,justify=CENTER,textvariable=cfnameinfo)
    claimfname.grid(row=3,column=0,ipady=2,padx=40,sticky='wn')

    Label(claimproductform,text="Last Name: ",bg='#8EC0E7',fg='#01263F').grid(row=2,column=1,padx=40,sticky='ws')
    claimlname = Entry(claimproductform,width=17,justify=CENTER,textvariable=clnameinfo)
    claimlname.grid(row=3,column=1,ipady=2,padx=40,sticky='wn')

    Label(claimproductform,text="Customer ID: ",bg='#8EC0E7',fg='#01263F').grid(row=4,column=0,padx=40,sticky='ws')
    claimid = Entry(claimproductform,width=17,justify=CENTER,textvariable=ccidinfo)
    claimid.grid(row=5,column=0,ipady=2,padx=40,sticky='wn')

    Label(claimproductform,text="Product Type: ",bg='#8EC0E7',fg='#01263F').grid(row=4,column=1,padx=40,sticky='ws')
    claimtype = ttk.Combobox(claimproductform,width=17, values=types,justify=CENTER,textvariable=cptype)
    claimtype.grid(row=5,column=1,ipady=2,padx=40,sticky='wn')
    claimtype.bind('<<ComboboxSelected>>',clnameopen)

    Label(claimproductform,text="Product Name: ",bg='#8EC0E7',fg='#01263F').grid(row=6,column=0,padx=160,columnspan=2,sticky='ws')
    claimpname = ttk.Combobox(claimproductform,width=35,state=DISABLED,justify=CENTER,textvariable=cpname)
    claimpname.grid(row=7,column=0,columnspan=2,ipady=2,padx=160,sticky='wn')

    Button(claimproductform,text='Back',width=12,bg='#01263F',font=('Helvetica 16 bold'),relief=FLAT,fg='white',command=backtoclaimnote).grid(row=8,column=0,pady=10,padx=15,sticky='se')
    Button(claimproductform,text='Accept',width=12,bg='#01263F',font=('Helvetica 16 bold'),relief=FLAT,fg='white',command=accepttoclaim).grid(row=8,column=1,pady=10,padx=15,sticky='sw')

    claimproductform.grid(row=0,column=0,columnspan=2,sticky='news')

def clnameopen(event) :
    if cptype.get().upper() == 'CPU' :
        claimpname.delete(0, END)
        claimpname['state'] = 'Normal'
        claimpname['values'] = CPU2
    elif cptype.get().upper() == 'GPU' :
        claimpname.delete(0, END)
        claimpname['state'] = 'Normal'
        claimpname['values'] = GPU2
    elif cptype.get().upper() == 'MAINBOARD' :
        claimpname.delete(0, END)
        claimpname['state'] = 'Normal'
        claimpname['values'] = Mainboard2
    elif cptype.get().upper() == 'RAM' :
        claimpname.delete(0, END)
        claimpname['state'] = 'Normal'
        claimpname['values'] = Ram2
    elif cptype.get().upper() == 'PSU' :
        claimpname.delete(0, END)
        claimpname['state'] = 'Normal'
        claimpname['values'] = PSU2
    elif cptype.get().upper() == 'COOLER' :
        claimpname.delete(0, END)
        claimpname['state'] = 'Normal'
        claimpname['values'] = Cooler2
    elif cptype.get().upper() == 'HDD' :
        claimpname.delete(0, END)
        claimpname['state'] = 'Normal'
        claimpname['values'] = HDD2
    else :
        messagebox.showwarning('Admin','Try select type')

def backtoclaimnote() :
    formw.destroy()
    claimform(0)

def accepttoclaim() :
    sql = 'SELECT * FROM Customer where Cid=?'
    cursor.execute(sql,[ccidinfo.get().upper()])
    result = cursor.fetchall()
    if result :
        if cptype.get() == '' or cpname.get() == '' or ccidinfo.get() == '' or cfnameinfo.get() == '' or clnameinfo.get() == '' :
            messagebox.showwarning('Admin','Please complete the information.')
        elif cptype.get().upper() == 'CPU' :
            if cpname.get() == 'Intel I3' or cpname.get() == 'Intel I5' or cpname.get() ==  'Intel I7' or cpname.get() ==  'Intel I9' or cpname.get() ==  'Ryzen 3' or cpname.get() ==  'Ryzen 5' or cpname.get() == 'Ryzen 7' or cpname.get() == 'Ryzen 9' :
                successtoclaim()
            else :
                messagebox.showwarning('Admin','Please complete the information.')
        elif cptype.get().upper() == 'GPU' :
            if cpname.get() == 'Nvidia RTX3060' or cpname.get() == 'Nvidia RTX3070' or cpname.get() == 'Nvidia RTX3080' or cpname.get() == 'Radeon RX 6800' or cpname.get() == 'Radeon RX 6900' :
                successtoclaim()
            else :
                messagebox.showwarning('Admin','Please complete the information.')
        elif cptype.get().upper() == 'MAINBOARD' :
            if cpname.get() == 'For AMD' or cpname.get() == 'For Intel' :
                successtoclaim()
            else :
                messagebox.showwarning('Admin','Please complete the information.')
        elif cptype.get().upper() == 'RAM' :
            if cpname.get() == '2Gb' or cpname.get() == '4Gb' or cpname.get() == '8Gb' or cpname.get() == '16Gb' or cpname.get() == '32Gb' :
                successtoclaim()
            else :
                messagebox.showwarning('Admin','Please complete the information.')
        elif cptype.get().upper() == 'PSU' :
            if cpname.get() == '650W' or cpname.get() == '750W' or cpname.get() == '850W' or cpname.get() == '1000W' :
                successtoclaim()
            else :
                messagebox.showwarning('Admin','Please complete the information.')
        elif cptype.get().upper() == 'COOLER' :
            if cpname.get() == 'Liquid cooling' or cpname.get() == 'Fan' :
                successtoclaim()
            else :
                messagebox.showwarning('Admin','Please complete the information.')
        elif cptype.get().upper() == 'HDD' :
            if cpname.get() == '500GB' or cpname.get() == '1TB' or cpname.get() == '2TB' or cpname.get() == '4TB' :
                successtoclaim()
            else :
                messagebox.showwarning('Admin','Please complete the information.')
        else :
            messagebox.showwarning('Admin','Please complete the information.')
    else :
        messagebox.showwarning('Admin',"Don't found customer ID")
        claimid.focus_force()

def successtoclaim() :
    sql = 'INSERT INTO Productclaim (Firstname, Lastname, CustomerID, Producttype, Productname) VALUES (?,?,?,?,?)'
    cursor.execute(sql, [cfnameinfo.get() , clnameinfo.get() , ccidinfo.get() , cptype.get() , cpname.get()])
    conn.commit()
    messagebox.showinfo('Admin','Successfully claim')
    formw.destroy()

w = 800 #width of application
h = 500 #height of application

createconnection()
log = loginwindow('Embose : Login')

userinfo = StringVar()
pwdinfo = StringVar()

usernewinfo = StringVar()
pwdnewinfo = StringVar()
cpwdinfo = StringVar()
fname = StringVar()
lname = StringVar()
genderinfo = StringVar()

logoimg = PhotoImage(file='Image/Logo.png')
logo2img = PhotoImage(file='Image/Logo2.png')
regisimg = PhotoImage(file='Image/Register.png')
womanimg = PhotoImage(file='Image/woman.png').subsample(6,6)
manimg = PhotoImage(file='Image/man.png').subsample(6,6)

loginlayout()

log.mainloop()
cursor.close() #close cursor
conn.close() #close database connection