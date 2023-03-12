from tkinter import *
def mainwindow() :
    root = Tk()
    root.title("GUI5 : Class Activity of Week5")
    root.geometry("800x600")
    root.grid_columnconfigure((0,1),weight=1)
    root.grid_rowconfigure((0,3),weight=1)
    root.grid_rowconfigure((1),weight=5)
    return(root)

def layout(root) :
    top = Frame(root,bg="#3C84AB")
    top.grid(row=0,columnspan=2,sticky='news')
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)
    
    left = Frame(root,bg='#DEFCF9')
    left.grid(row=1,column=0,sticky='news')
    left.rowconfigure((0,1,2,3),weight=1)
    left.columnconfigure(0,weight=1)
    left.columnconfigure(1,weight=2)

    right = Frame(root,bg='#85CDFD')
    right.grid(row=1,column=1,sticky='news')
    right.rowconfigure((0,1,2,3),weight=1)
    right.columnconfigure(0,weight=1)
    right.columnconfigure(1,weight=2)

    bottom = Frame(root,bg="#3C84AB")
    bottom.grid(row=3,columnspan=2,sticky='news')
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure((0,1),weight=1)

    return(top,bottom,left,right)

def topside(top) :
    Label(top,text="Little Dream House by Patiphan Arphorn",font=("Garamond",23,'bold'),bg="#3C84AB",fg='white').grid(row=0)

def leftside(left) :
    cakemenu = ["Stawberry Cake\n125 B.","Cheese Cake\n110 B.","Babybloom Cake\n140 B.","Chocolate Cake\n100 B."]
    cakespy = [IntVar() for i in cakemenu]
    for i,cake in enumerate(cakemenu) :
        Label(left,image=cakelist[i],bg='#DEFCF9').grid(row=i,column=0)
        Label(left,text=cake,bg='#DEFCF9').grid(row=i,column=1,sticky=W)
        Spinbox(left,from_=0,to=100,width=10,justify="center",textvariable = cakespy[i],command=userclick).grid(row=i,column=2,sticky=E,padx=10)
    return(cakespy)

def rightside(right) :
    drinkmenu = ["Hot Latte\n80 B.","Hot Cappuccino\n70 B.","Hot Caramel Latte\n100 B."," Hot Chocolate\n90 B."]
    drinkspy = [IntVar() for i in drinkmenu]
    for i,drink in enumerate(drinkmenu) :
        Label(right,image=drinklist[i],bg='#85CDFD').grid(row=i,column=0)
        Label(right,text=drink,bg='#85CDFD').grid(row=i,column=1,sticky=W)
        Spinbox(right,from_=0,to=100,width=10,justify="center",textvariable = drinkspy[i],command=userclick).grid(row=i,column=2,sticky=E,padx=10)
    return(drinkspy)

def bottomside(bottom) :
    showcake = Label(bottom,bg="#3C84AB",textvariable = spy1)
    showcake.grid(row=0,column=0)
    showdrink = Label(bottom,bg="#3C84AB",textvariable = spy2)
    showdrink.grid(row=0,column=1)
    return(showcake,showdrink)

def userclick() :
    totalcake = 0
    totaldrink = 0
    cakeprice = [125,110,140,100]
    drinkprice = [80,70,100,90]
    for i in range(len(cakeprice)) :
        totalcake += cakespy[i].get()*cakeprice[i]
        totaldrink += drinkspy[i].get()*drinkprice[i]
    showcake['bg'] = "#DEFCF9"
    showcake['fg'] = "blue"
    spy1.set("Total cake price = %0.2f"%totalcake)
    showdrink['bg'] = "#DEFCF9"
    showdrink['fg'] = "blue"
    spy2.set("Total drink price = %0.2f"%totaldrink)

root = mainwindow()
top,bottom,left,right = layout(root)
cake1 = PhotoImage(file="image/cake1.png")
cake2 = PhotoImage(file="image/cake2.png")
cake3 = PhotoImage(file="image/cake3.png")
cake4 = PhotoImage(file="image/cake4.png")
drink1 = PhotoImage(file="image/coffee1.png")
drink2 = PhotoImage(file="image/coffee2.png")
drink3 = PhotoImage(file="image/coffee3.png")
drink4 = PhotoImage(file="image/coffee4.png")
cakelist = [cake1,cake2,cake3,cake4]
drinklist = [drink1,drink2,drink3,drink4]
spy1,spy2 = StringVar(),StringVar()
topside(top)
cakespy = leftside(left)
drinkspy = rightside(right)
showcake,showdrink = bottomside(bottom)
root.mainloop()