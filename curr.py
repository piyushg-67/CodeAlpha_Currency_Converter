from currency_converter import CurrencyConverter
import tkinter as tk
a = CurrencyConverter()


window = tk.Tk()
window.geometry("500x360")

def clicked():
    amount= int(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    data= a.convert(amount,cur1,cur2)
    l5=tk.Label(window,text=data).place(x=230, y= 300)


l1=tk.Label(window,text="Currency Converter", font= "Times 23 bold").place(x=5,y=5)
l2=tk.Label(window,text="Enter Amount here:", font= "Times 15 bold").place(x=7, y=75)
e1=tk.Entry(window)

l3= tk.Label(window,text="Enter Currency here:", font= "Times 15 bold").place(x=7, y=140)
e2=tk.Entry(window)

l4= tk.Label(window,text="Enter req. Currency:",font="Times 15 bold").place(x=7,y=200)
e3= tk.Entry(window)

b1=tk.Button(window, text="Click",command=clicked).place(x=230,y=240)

e1.place(x=185,y=80)
e2.place(x=200,y=145)
e3.place(x=195,y=207)  


window.mainloop()






