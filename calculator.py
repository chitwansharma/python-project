from tkinter import *
import math as m
font = ('verdana', 15, 'bold')
# creating function
def buttonclicked(event):
    print("button clicked")
    b = event.widget
    text = b['text']
    print(text)
    if text == "=":
        ex = textField.get()
        result = eval(ex)
        textField.delete(0, END)
        textField.insert(0, result)
        return;
    textField.insert(END, text)

def allclear():
    textField.delete(0, END)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


obj = Tk()
obj.title("CALCULATOR")
obj.geometry("400x500")
# heading label
heading = Label(obj, text="CALCULATOR", font=font)
heading.pack(side=TOP)
textField = Entry(obj, font=font, justify=CENTER)
textField.pack(side=TOP, padx=10, pady=10, fil=X)
# adding button
buttonframe = Frame(obj)
buttonframe.pack(side=TOP)
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        b = Button(buttonframe, text=str(temp), font=font, width=5, activebackground="black", activeforeground="pink")
        b.grid(row=i, column=j, padx=5, pady=5)
        temp = temp + 1
        b.bind('<Button-1>', buttonclicked)
bzer0 = Button(buttonframe, text="0", font=font, width=5, activebackground="black", activeforeground="pink")
bzer0.grid(row=3, column=0, padx=5, pady=5)
bzer0.bind('<Button-1>', buttonclicked)
bdot = Button(buttonframe, text=".", font=font, width=5, activebackground="black", activeforeground="pink")
bdot.grid(row=3, column=1, padx=5, pady=5)
bdot.bind('<Button-1>', buttonclicked)
bequ = Button(buttonframe, text="=", font=font, width=5, activebackground="black", activeforeground="pink")
bequ.grid(row=3, column=2, padx=5, pady=5)
bequ.bind('<Button-1>', buttonclicked)
bplus = Button(buttonframe, text="+", font=font, width=5, activebackground="black", activeforeground="pink")
bplus.grid(row=0, column=3, padx=5, pady=5)
bplus.bind('<Button-1>', buttonclicked)
bminus = Button(buttonframe, text="-", font=font, width=5, activebackground="black", activeforeground="pink")
bminus.grid(row=1, column=3, padx=5, pady=5)
bminus.bind('<Button-1>', buttonclicked)
bmul = Button(buttonframe, text="*", font=font, width=5, activebackground="black", activeforeground="pink")
bmul.grid(row=2, column=3, padx=5, pady=5)
bmul.bind('<Button-1>', buttonclicked)
bdiv = Button(buttonframe, text="/", font=font, width=5, activebackground="black", activeforeground="pink")
bdiv.grid(row=3, column=3, padx=5, pady=5)
bdiv.bind('<Button-1>', buttonclicked)
bclear = Button(buttonframe, font=font, text="<<--", width=11, activebackground="black", activeforeground="pink",
                command=clear)
bclear.grid(row=4, column=0, columnspan=2)
ballclear = Button(buttonframe, text="AC", font=font, width=11, activebackground="black", activeforeground="pink",
                   command=allclear)
ballclear.grid(row=4, column=2, columnspan=2)


#################################SCIENTIFIC CALCULATOR CODING ##############################################
scFrame = Frame(obj)
sqroot = Button(scFrame, text="sqrt", font=font, width=5, activebackground="black", activeforeground="pink")
sqroot.grid(row=0, column=0, padx=5, pady=5)
power = Button(scFrame, text="^", font=font, width=5, activebackground="black", activeforeground="pink")
power.grid(row=0, column=1, padx=5, pady=5)
fact = Button(scFrame, text="!", font=font, width=5, activebackground="black", activeforeground="pink")
fact.grid(row=0, column=2, padx=5, pady=5)
torad = Button(scFrame, text="toRAD", font=font, width=5, activebackground="black", activeforeground="pink")
torad.grid(row=0, column=3, padx=5, pady=5)
todeg = Button(scFrame, text="toDEG", font=font, width=5, activebackground="black", activeforeground="pink")
todeg.grid(row=1, column=0, padx=5, pady=5)
sin = Button(scFrame, text="sin", font=font, width=5, activebackground="black", activeforeground="pink")
sin.grid(row=1, column=1, padx=5, pady=5)
cos = Button(scFrame, text="cos", font=font, width=5, activebackground="black", activeforeground="pink")
cos.grid(row=1, column=2, padx=5, pady=5)
tan = Button(scFrame, text="tan", font=font, width=5, activebackground="black", activeforeground="pink")
tan.grid(row=1, column=3, padx=5, pady=5)

simplecal=True
#functions
def btnclick(event):
    print("button")
    btnclick=event.widget
    text=btnclick['text']
    print(text)
    es=textField.get()
    result=''
    if text == "toRAD":
        print("cal rad")
        result = str(m.radians(float(es)))
    elif text == "toDEG":
        print("cal deg")
        result = str(m.degrees(float(es)))
    elif text == "tan":
        print("cal tan")
        result=str(m.tan(float(es)))
    elif text == "sin":
        print("cal sin")
        result = str(m.sin(float(es)))
    elif text == "cos":
        print("cal cos")
        result = str(m.cos(float(es)))
    elif text == "^":
        print("cal power")
        result = str(m.pow(float(es)))
    elif text == "!":
        print("cal fact")
        result = str(m.factorial(float(es)))
    elif text == "sqrt":
        print("cal sqareroot")
        result = str(m.sqrt(float(es)))
    textField.delete(0, END)
    textField.insert(0, result)
def click():
    global simplecal
    if simplecal:
        buttonframe.pack_forget()
        #add frame
        scFrame.pack(side=TOP)
        buttonframe.pack(side=TOP)
        simplecal=False

    else:
        print("simple calc")
        scFrame.pack_forget()
        simplecal=True

#binding buttons
sqroot.bind('<Button-1>', btnclick)
power.bind('<Button-1>', btnclick)
todeg.bind('<Button-1>', btnclick)
torad.bind('<Button-1>', btnclick)
sin.bind('<Button-1>', btnclick)
cos.bind('<Button-1>', btnclick)
tan.bind('<Button-1>', btnclick)
fact.bind('<Button-1>', btnclick)
menubar = Menu(obj)
mode = Menu(menubar,tearoff = 0)
mode.add_command(label="SCIENTIFIC CALCULATOR",command=click)
menubar.add_cascade(label="mode",menu=mode)
obj.config(menu=menubar)


obj.mainloop()