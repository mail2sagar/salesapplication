from tkinter import *
window = Tk()

window.title("Sales Porfits and Lose")
window.geometry("500x500")

mon = ('January','February','March','April','May','June','July','August','September',
          'October','November','December')

profit = (12587478,24587947,35698725,4569755,52316956,65954673,784254589,81212549,94522358713,10233765,1125458,12583484)
print(len(profit))

max_profits = max(profit)
print(max_profits)

min_profits = min(profit)
print(min_profits)

label1 = Label(window,text="Months- Jan,Feb,Mar,Ap,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec")
label2 = Label(window,text="Profits- 178,247,325,455,556,673,789,849,913,165,158,154")

def min():
    min_profits = min(profit)
    label4["text"]+ "Minimum profit of "+str(min_profits)+" was givin in the month"+str(mon)

def max():
    min_profits = min(profit)
    label4["text"]+ "Maximum profit of "+str(max_profits)+" was givin in the month"+str(mon)



label3 = Label(window)
label4 = Label(window)

btn1 = Button(window,text="Show Max Profitable Month",command=max)
btn2 = Button(window,text="Show Min Profitable Month",command=min)

index_1 = profit.index(max_profits)
print(mon[index_1])

index_2 = profit.index(min_profits)
print(mon[index_2])

label1.place(relx=0.5,rely=0.2,anchor=CENTER)
label2.place(relx=0.5,rely=0.3,anchor=CENTER)
label3.place(relx=0.5,rely=0.6,anchor=CENTER)
label4.place(relx=0.5,rely=0.5,anchor=CENTER)

btn1.place(relx=0.5,rely=0.4,anchor=CENTER)
btn2.place(relx=0.5,rely=0.7,anchor=CENTER)

window.mainloop()