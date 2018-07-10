from tkinter import *

def btnClicke(numbers):
    global operator_1
    operator_1 += str(numbers)
    text_Input.set(operator_1)
def  btnClearDisplay():
    global operator_1
    operator_1=" "
    text_Input.set(" ")
def btnEqualsInput():
    global operator_1
    sumup = str(eval(operator_1))
    text_Input.set(sumup)
    operator_1  = " "
cal =Tk()
cal.title("Calculator")
cal.geometry('500x500')
operator_1 = " "
text_Input=StringVar()

text = Entry(cal ,font=("Courior New",12,'bold'),textvariable=text_Input,width=25,bd=5,bg='powder blue').grid(columnspan=4)
button7 = Button(cal ,padx=16,bd=8, fg="Black",font=('arial',20,'bold'),text="7",command=lambda:btnClicke(7)).grid(row=1,column=0)
button8 = Button(cal ,padx=16,bd=8, fg='RED',font=('arial',20,'bold'),text="8",command=lambda:btnClicke(8)).grid(row=1,column=1)
button9 = Button(cal ,padx=16,bd=8,fg="yellow",font=('arial',20,'bold'),text="9",command=lambda:btnClicke(9)).grid(row=1,column=2)
Addition = Button(cal ,padx=16,bd=8,fg="white",font=('arial',20,'bold'),text="Add",command=lambda:btnClicke('+')).grid(row=1,column=3)

button4 = Button(cal ,padx=16,bd=8, fg="Black",font=('arial',20,'bold'),text="4",command=lambda:btnClicke(4)).grid(row=2,column=0)
button5 = Button(cal ,padx=16,bd=8, fg='RED',font=('arial',20,'bold'),text="5",command=lambda:btnClicke(5)).grid(row=2,column=1)
button6 = Button(cal ,padx=16,bd=8,fg="yellow",font=('arial',20,'bold'),text="6",command=lambda:btnClicke(6)).grid(row=2,column=2)
Subtraction = Button(cal ,padx=16,bd=8,fg="white",font=('arial',20,'bold'),text="-",command=lambda:btnClicke("-")).grid(row=2,column=3)


button1=Button(cal ,padx=16,bd=8, fg="Black",font=('arial' ,20, 'bold'),text="1",command=lambda:btnClicke(1)).grid(row=3,column=0)
button2 = Button(cal ,padx=16,bd=8, fg='RED' ,font=('arial' ,20, 'bold'),text="2",command=lambda:btnClicke(2)).grid(row=3,column=1)
button3 = Button(cal ,padx=16,bd=8,fg="yellow",font=('arial',20,'bold'),text="3",command=lambda:btnClicke(3)).grid(row=3,column=2)
button0 =Button(cal ,padx=16,bd=8,fg="yellow",font=('arial',20,'bold'),text="0",command=lambda:btnClicke(0)).grid(row=4,column=0)

Multiplication = Button(cal ,padx=16,bd=8,fg="RED",font=('arial',20,'bold'),text="Multiply" , command= lambda:btnClicke("*")).grid(row=3, column= 3)
Division=Button(cal ,padx=16,bd=8,fg="white",font=('arial',20,'bold'),text="Division",command=lambda:btnClicke('/')).grid(row=4,column=3)
Equal=Button(cal ,padx=16,bd=8,fg='white',font=('arial' ,20, 'bold'), text="Equal",bg="powderblue" ,command=btnEqualsInput).grid(row=4,column=2)
Clear=Button(cal, padx=16,bd=8,fg='white',font=('arial',20,'bold'),text="C",bg="Black",command=btnClearDisplay).grid(row=4 ,column=1)

cal.mainloop()
