from tkinter import *
root = Tk()
root.title("Fibonacci Sum")
root.geometry("400x400")
entry=Entry(root)
label_series=Label(root, text="Fibonacci Series: ")
label_sum=Label(root)
def Fibonacci():
    num=entry.get()
    first_no=0
    second_no=1
    sum=0
    counter=1
    sum2=0
    while counter <= num:
        label_series["text"]+=str(sum)
        label_sum["text"]="Sum of all the number = "+str(sum2)
        counter = counter+1
        first_no=second_no
        second_no=sum
        sum = first_no +second_no
        sum2=sum2+sum

btn = Button(root, text="Show Fibonacci Numbers", command=Fibonacci)
btn.pack()
entry.pack()
label_series.pack()
label_sum.pack()
root.mainloop()