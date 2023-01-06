from tkinter import *

# Window set up---------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry("400x200")
window.title("Matrix Calculator")


# Test commands---------------------------------------------------------------------------------------------------------
def test():
    ar = 0
    ac = 0

    if A5.get() != "X":
        ac = 5
    elif A4.get() != "X":
        ac = 4
    elif A3.get() != "X":
        ac = 3
    elif A2.get() != "X":
        ac = 2

    if A21.get() != "X":
        ar = 5
    elif A16.get() != "X":
        ar = 4
    elif A11.get() != "X":
        ar = 3
    elif A6.get() != "X":
        ar = 2
    elif A1.get() != "X":
        ar = 1
        ac = 1

    print("Matrix size is", ar, "x", ac)


def clear():
    A1.delete(0, END)
    A2.delete(0, END)
    A3.delete(0, END)
    A4.delete(0, END)
    A5.delete(0, END)
    A6.delete(0, END)
    A7.delete(0, END)
    A8.delete(0, END)
    A9.delete(0, END)
    A10.delete(0, END)
    A11.delete(0, END)
    A12.delete(0, END)
    A13.delete(0, END)
    A14.delete(0, END)
    A15.delete(0, END)
    A16.delete(0, END)
    A17.delete(0, END)
    A18.delete(0, END)
    A19.delete(0, END)
    A20.delete(0, END)
    A21.delete(0, END)
    A22.delete(0, END)
    A23.delete(0, END)
    A24.delete(0, END)
    A25.delete(0, END)

    B1.delete(0, END)
    B2.delete(0, END)
    B3.delete(0, END)
    B4.delete(0, END)
    B5.delete(0, END)
    B6.delete(0, END)
    B7.delete(0, END)
    B8.delete(0, END)
    B9.delete(0, END)
    B10.delete(0, END)
    B11.delete(0, END)
    B12.delete(0, END)
    B13.delete(0, END)
    B14.delete(0, END)
    B15.delete(0, END)
    B16.delete(0, END)
    B17.delete(0, END)
    B18.delete(0, END)
    B19.delete(0, END)
    B20.delete(0, END)
    B21.delete(0, END)
    B22.delete(0, END)
    B23.delete(0, END)
    B24.delete(0, END)
    B25.delete(0, END)

    A1.insert(0, "X")
    A2.insert(0, "X")
    A3.insert(0, "X")
    A4.insert(0, "X")
    A5.insert(0, "X")
    A6.insert(0, "X")
    A7.insert(0, "X")
    A8.insert(0, "X")
    A9.insert(0, "X")
    A10.insert(0, "X")
    A11.insert(0, "X")
    A12.insert(0, "X")
    A13.insert(0, "X")
    A14.insert(0, "X")
    A15.insert(0, "X")
    A16.insert(0, "X")
    A17.insert(0, "X")
    A18.insert(0, "X")
    A19.insert(0, "X")
    A20.insert(0, "X")
    A21.insert(0, "X")
    A22.insert(0, "X")
    A23.insert(0, "X")
    A24.insert(0, "X")
    A25.insert(0, "X")

    B1.insert(0, "X")
    B2.insert(0, "X")
    B3.insert(0, "X")
    B4.insert(0, "X")
    B5.insert(0, "X")
    B6.insert(0, "X")
    B7.insert(0, "X")
    B8.insert(0, "X")
    B9.insert(0, "X")
    B10.insert(0, "X")
    B11.insert(0, "X")
    B12.insert(0, "X")
    B13.insert(0, "X")
    B14.insert(0, "X")
    B15.insert(0, "X")
    B16.insert(0, "X")
    B17.insert(0, "X")
    B18.insert(0, "X")
    B19.insert(0, "X")
    B20.insert(0, "X")
    B21.insert(0, "X")
    B22.insert(0, "X")
    B23.insert(0, "X")
    B24.insert(0, "X")
    B25.insert(0, "X")


# Matrix inputs---------------------------------------------------------------------------------------------------------
A = Label(window, text='A =', font=('Arial', 12, 'italic'))

A1 = Entry(window, width=3, font=('Helvetica', 11))
A2 = Entry(window, width=3, font=('Helvetica', 11))
A3 = Entry(window, width=3, font=('Helvetica', 11))
A4 = Entry(window, width=3, font=('Helvetica', 11))
A5 = Entry(window, width=3, font=('Helvetica', 11))
A6 = Entry(window, width=3, font=('Helvetica', 11))
A7 = Entry(window, width=3, font=('Helvetica', 11))
A8 = Entry(window, width=3, font=('Helvetica', 11))
A9 = Entry(window, width=3, font=('Helvetica', 11))
A10 = Entry(window, width=3, font=('Helvetica', 11))
A11 = Entry(window, width=3, font=('Helvetica', 11))
A12 = Entry(window, width=3, font=('Helvetica', 11))
A13 = Entry(window, width=3, font=('Helvetica', 11))
A14 = Entry(window, width=3, font=('Helvetica', 11))
A15 = Entry(window, width=3, font=('Helvetica', 11))
A16 = Entry(window, width=3, font=('Helvetica', 11))
A17 = Entry(window, width=3, font=('Helvetica', 11))
A18 = Entry(window, width=3, font=('Helvetica', 11))
A19 = Entry(window, width=3, font=('Helvetica', 11))
A20 = Entry(window, width=3, font=('Helvetica', 11))
A21 = Entry(window, width=3, font=('Helvetica', 11))
A22 = Entry(window, width=3, font=('Helvetica', 11))
A23 = Entry(window, width=3, font=('Helvetica', 11))
A24 = Entry(window, width=3, font=('Helvetica', 11))
A25 = Entry(window, width=3, font=('Helvetica', 11))

B = Label(window, text='B =', font=('Arial', 12, 'italic'))

B1 = Entry(window, width=3, font=('Helvetica', 11))
B2 = Entry(window, width=3, font=('Helvetica', 11))
B3 = Entry(window, width=3, font=('Helvetica', 11))
B4 = Entry(window, width=3, font=('Helvetica', 11))
B5 = Entry(window, width=3, font=('Helvetica', 11))
B6 = Entry(window, width=3, font=('Helvetica', 11))
B7 = Entry(window, width=3, font=('Helvetica', 11))
B8 = Entry(window, width=3, font=('Helvetica', 11))
B9 = Entry(window, width=3, font=('Helvetica', 11))
B10 = Entry(window, width=3, font=('Helvetica', 11))
B11 = Entry(window, width=3, font=('Helvetica', 11))
B12 = Entry(window, width=3, font=('Helvetica', 11))
B13 = Entry(window, width=3, font=('Helvetica', 11))
B14 = Entry(window, width=3, font=('Helvetica', 11))
B15 = Entry(window, width=3, font=('Helvetica', 11))
B16 = Entry(window, width=3, font=('Helvetica', 11))
B17 = Entry(window, width=3, font=('Helvetica', 11))
B18 = Entry(window, width=3, font=('Helvetica', 11))
B19 = Entry(window, width=3, font=('Helvetica', 11))
B20 = Entry(window, width=3, font=('Helvetica', 11))
B21 = Entry(window, width=3, font=('Helvetica', 11))
B22 = Entry(window, width=3, font=('Helvetica', 11))
B23 = Entry(window, width=3, font=('Helvetica', 11))
B24 = Entry(window, width=3, font=('Helvetica', 11))
B25 = Entry(window, width=3, font=('Helvetica', 11))

clear()

# Buttons---------------------------------------------------------------------------------------------------------------
generate = Button(window, text='Generate', width=11, font=('Arial', 15))
add = Button(window, text=' + ', width=5, font=('Arial', 15))
subtract = Button(window, text=' - ', width=5, font=('Arial', 15))
multiply = Button(window, text=' x ', width=5, font=('Arial', 15))
clear = Button(window, text='Clear', width=5, font=('Arial', 15), command=clear)

test = Button(window, text="test", command=test)

# GUI set up------------------------------------------------------------------------------------------------------------
title = Label(window, text='Matrix Calculator', font=('Arial', 20, 'bold'))

# Griding---------------------------------------------------------------------------------------------------------------
title.grid(row=0, column=1, columnspan=11)

A.grid(row=3, column=0)
A1.grid(row=1, column=1)
A2.grid(row=1, column=2)
A3.grid(row=1, column=3)
A4.grid(row=1, column=4)
A5.grid(row=1, column=5)
A6.grid(row=2, column=1)
A7.grid(row=2, column=2)
A8.grid(row=2, column=3)
A9.grid(row=2, column=4)
A10.grid(row=2, column=5)
A11.grid(row=3, column=1)
A12.grid(row=3, column=2)
A13.grid(row=3, column=3)
A14.grid(row=3, column=4)
A15.grid(row=3, column=5)
A16.grid(row=4, column=1)
A17.grid(row=4, column=2)
A18.grid(row=4, column=3)
A19.grid(row=4, column=4)
A20.grid(row=4, column=5)
A21.grid(row=5, column=1)
A22.grid(row=5, column=2)
A23.grid(row=5, column=3)
A24.grid(row=5, column=4)
A25.grid(row=5, column=5)

B.grid(row=3, column=6)
B1.grid(row=1, column=7)
B2.grid(row=1, column=8)
B3.grid(row=1, column=9)
B4.grid(row=1, column=10)
B5.grid(row=1, column=11)
B6.grid(row=2, column=7)
B7.grid(row=2, column=8)
B8.grid(row=2, column=9)
B9.grid(row=2, column=10)
B10.grid(row=2, column=11)
B11.grid(row=3, column=7)
B12.grid(row=3, column=8)
B13.grid(row=3, column=9)
B14.grid(row=3, column=10)
B15.grid(row=3, column=11)
B16.grid(row=4, column=7)
B17.grid(row=4, column=8)
B18.grid(row=4, column=9)
B19.grid(row=4, column=10)
B20.grid(row=4, column=11)
B21.grid(row=5, column=7)
B22.grid(row=5, column=8)
B23.grid(row=5, column=9)
B24.grid(row=5, column=10)
B25.grid(row=5, column=11)

generate.grid(row=6, column=0, columnspan=4)
clear.grid(row=6, column=4, columnspan=2)
add.grid(row=6, column=6, columnspan=2)
subtract.grid(row=6, column=8, columnspan=2)
multiply.grid(row=6, column=10, columnspan=2)


test.grid(row=7, column=0)

window.mainloop()
