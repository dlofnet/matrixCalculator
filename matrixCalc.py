from tkinter import *

# Window set up---------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry("400x200")
window.title("Matrix Calculator")


# Methods---------------------------------------------------------------------------------------------------------
def a_row():

    global ar
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
    return ar


def a_col():

    global ac
    if A5.get() != "X":
        ac = 5
    elif A4.get() != "X":
        ac = 4
    elif A3.get() != "X":
        ac = 3
    elif A2.get() != "X":
        ac = 2
    elif A1.get() != "X":
        ac = 1
    return ac


def b_row():

    global br
    if B21.get() != "X":
        br = 5
    elif B16.get() != "X":
        br = 4
    elif B11.get() != "X":
        br = 3
    elif B6.get() != "X":
        br = 2
    elif B1.get() != "X":
        br = 1
    return br


def b_col():

    global bc
    if B5.get() != "X":
        bc = 5
    elif B4.get() != "X":
        bc = 4
    elif B3.get() != "X":
        bc = 3
    elif B2.get() != "X":
        bc = 2
    elif B1.get() != "X":
        bc = 1
    return bc


def generate():
    result = Toplevel()
    result.title("Result")
    result.geometry("200x150")

    r1 = [A1.get(), A2.get(), A3.get(), A4.get(), A5.get()]
    r1 = [i for i in r1 if i != 'X']
    r1 = [eval(i) for i in r1]
    r2 = [A6.get(), A7.get(), A8.get(), A9.get(), A10.get()]
    r2 = [i for i in r2 if i != 'X']
    r2 = [eval(i) for i in r2]
    r3 = [A11.get(), A12.get(), A13.get(), A14.get(), A15.get()]
    r3 = [i for i in r3 if i != 'X']
    r3 = [eval(i) for i in r3]
    r4 = [A16.get(), A17.get(), A18.get(), A19.get(), A20.get()]
    r4 = [i for i in r4 if i != 'X']
    r4 = [eval(i) for i in r4]
    r5 = [A21.get(), A22.get(), A23.get(), A24.get(), A25.get()]
    r5 = [i for i in r5 if i != 'X']
    r5 = [eval(i) for i in r5]

    x1 = Label(result, text=str(r1), font=('Arial', 14))
    x2 = Label(result, text=str(r2), font=('Arial', 14))
    x3 = Label(result, text=str(r3), font=('Arial', 14))
    x4 = Label(result, text=str(r4), font=('Arial', 14))
    x5 = Label(result, text=str(r5), font=('Arial', 14))

    if len(r1) != 0:
        x1.pack()
    if len(r2) != 0:
        x2.pack()
    if len(r3) != 0:
        x3.pack()
    if len(r4) != 0:
        x4.pack()
    if len(r5) != 0:
        x5.pack()


def matrix_sum():
    result = Toplevel()
    result.title("Result")
    result.geometry("200x150")

    if a_row() == b_row() and a_col() == b_col():
        r1 = [A1.get(), A2.get(), A3.get(), A4.get(), A5.get()]
        r1 = [i for i in r1 if i != 'X']
        r1 = [eval(i) for i in r1]
        r2 = [A6.get(), A7.get(), A8.get(), A9.get(), A10.get()]
        r2 = [i for i in r2 if i != 'X']
        r2 = [eval(i) for i in r2]
        r3 = [A11.get(), A12.get(), A13.get(), A14.get(), A15.get()]
        r3 = [i for i in r3 if i != 'X']
        r3 = [eval(i) for i in r3]
        r4 = [A16.get(), A17.get(), A18.get(), A19.get(), A20.get()]
        r4 = [i for i in r4 if i != 'X']
        r4 = [eval(i) for i in r4]
        r5 = [A21.get(), A22.get(), A23.get(), A24.get(), A25.get()]
        r5 = [i for i in r5 if i != 'X']
        r5 = [eval(i) for i in r5]
        r6 = [B1.get(), B2.get(), B3.get(), B4.get(), B5.get()]
        r6 = [i for i in r6 if i != 'X']
        r6 = [eval(i) for i in r6]
        r7 = [B6.get(), B7.get(), B8.get(), B9.get(), B10.get()]
        r7 = [i for i in r7 if i != 'X']
        r7 = [eval(i) for i in r7]
        r8 = [B11.get(), B12.get(), B13.get(), B14.get(), B15.get()]
        r8 = [i for i in r8 if i != 'X']
        r8 = [eval(i) for i in r8]
        r9 = [B16.get(), B17.get(), B18.get(), B19.get(), B20.get()]
        r9 = [i for i in r9 if i != 'X']
        r9 = [eval(i) for i in r9]
        r10 = [B21.get(), B22.get(), B23.get(), B24.get(), B25.get()]
        r10 = [i for i in r10 if i != 'X']
        r10 = [eval(i) for i in r10]
        s1 = [sum(x) for x in zip(r1, r6)]
        s2 = [sum(x) for x in zip(r2, r7)]
        s3 = [sum(x) for x in zip(r3, r8)]
        s4 = [sum(x) for x in zip(r4, r9)]
        s5 = [sum(x) for x in zip(r5, r10)]
        x1 = Label(result, text=str(s1), font=('Arial', 14))
        x2 = Label(result, text=str(s2), font=('Arial', 14))
        x3 = Label(result, text=str(s3), font=('Arial', 14))
        x4 = Label(result, text=str(s4), font=('Arial', 14))
        x5 = Label(result, text=str(s5), font=('Arial', 14))

        if len(r1) != 0:
            x1.pack()
        if len(r2) != 0:
            x2.pack()
        if len(r3) != 0:
            x3.pack()
        if len(r4) != 0:
            x4.pack()
        if len(r5) != 0:
            x5.pack()

    else:
        np = Label(result, text='Not Possible', font=('Arial', 14))
        np.pack()


def matrix_diff():
    result = Toplevel()
    result.title("Result")
    result.geometry("200x150")

    if a_row() == b_row() and a_col() == b_col():
        r1 = [A1.get(), A2.get(), A3.get(), A4.get(), A5.get()]
        r1 = [i for i in r1 if i != 'X']
        r1 = [eval(i) for i in r1]
        r2 = [A6.get(), A7.get(), A8.get(), A9.get(), A10.get()]
        r2 = [i for i in r2 if i != 'X']
        r2 = [eval(i) for i in r2]
        r3 = [A11.get(), A12.get(), A13.get(), A14.get(), A15.get()]
        r3 = [i for i in r3 if i != 'X']
        r3 = [eval(i) for i in r3]
        r4 = [A16.get(), A17.get(), A18.get(), A19.get(), A20.get()]
        r4 = [i for i in r4 if i != 'X']
        r4 = [eval(i) for i in r4]
        r5 = [A21.get(), A22.get(), A23.get(), A24.get(), A25.get()]
        r5 = [i for i in r5 if i != 'X']
        r5 = [eval(i) for i in r5]
        r6 = [B1.get(), B2.get(), B3.get(), B4.get(), B5.get()]
        r6 = [i for i in r6 if i != 'X']
        r6 = [eval(i) for i in r6]
        r7 = [B6.get(), B7.get(), B8.get(), B9.get(), B10.get()]
        r7 = [i for i in r7 if i != 'X']
        r7 = [eval(i) for i in r7]
        r8 = [B11.get(), B12.get(), B13.get(), B14.get(), B15.get()]
        r8 = [i for i in r8 if i != 'X']
        r8 = [eval(i) for i in r8]
        r9 = [B16.get(), B17.get(), B18.get(), B19.get(), B20.get()]
        r9 = [i for i in r9 if i != 'X']
        r9 = [eval(i) for i in r9]
        r10 = [B21.get(), B22.get(), B23.get(), B24.get(), B25.get()]
        r10 = [i for i in r10 if i != 'X']
        r10 = [eval(i) for i in r10]
        s1 = [e1 - e2 for (e1, e2) in zip(r1, r6)]
        s2 = [e1 - e2 for (e1, e2) in zip(r2, r7)]
        s3 = [e1 - e2 for (e1, e2) in zip(r3, r8)]
        s4 = [e1 - e2 for (e1, e2) in zip(r4, r9)]
        s5 = [e1 - e2 for (e1, e2) in zip(r5, r10)]
        x1 = Label(result, text=str(s1), font=('Arial', 14))
        x2 = Label(result, text=str(s2), font=('Arial', 14))
        x3 = Label(result, text=str(s3), font=('Arial', 14))
        x4 = Label(result, text=str(s4), font=('Arial', 14))
        x5 = Label(result, text=str(s5), font=('Arial', 14))

        if len(r1) != 0:
            x1.pack()
        if len(r2) != 0:
            x2.pack()
        if len(r3) != 0:
            x3.pack()
        if len(r4) != 0:
            x4.pack()
        if len(r5) != 0:
            x5.pack()

    else:
        np = Label(result, text='Not Possible', font=('Arial', 14))
        np.pack()


def matrix_prod():
    result = Toplevel()
    result.title("Result")
    result.geometry("200x150")

    if a_col() == b_row():
        r1 = [A1.get(), A2.get(), A3.get(), A4.get(), A5.get()]
        r1 = [i for i in r1 if i != 'X']
        r1 = [eval(i) for i in r1]
        r2 = [A6.get(), A7.get(), A8.get(), A9.get(), A10.get()]
        r2 = [i for i in r2 if i != 'X']
        r2 = [eval(i) for i in r2]
        r3 = [A11.get(), A12.get(), A13.get(), A14.get(), A15.get()]
        r3 = [i for i in r3 if i != 'X']
        r3 = [eval(i) for i in r3]
        r4 = [A16.get(), A17.get(), A18.get(), A19.get(), A20.get()]
        r4 = [i for i in r4 if i != 'X']
        r4 = [eval(i) for i in r4]
        r5 = [A21.get(), A22.get(), A23.get(), A24.get(), A25.get()]
        r5 = [i for i in r5 if i != 'X']
        r5 = [eval(i) for i in r5]
        c1 = [B1.get(), B6.get(), B11.get(), B16.get(), B21.get()]
        c1 = [i for i in c1 if i != 'X']
        c1 = [eval(i) for i in c1]
        c2 = [B2.get(), B7.get(), B12.get(), B17.get(), B22.get()]
        c2 = [i for i in c2 if i != 'X']
        c2 = [eval(i) for i in c2]
        c3 = [B3.get(), B8.get(), B13.get(), B18.get(), B23.get()]
        c3 = [i for i in c3 if i != 'X']
        c3 = [eval(i) for i in c3]
        c4 = [B4.get(), B9.get(), B14.get(), B19.get(), B24.get()]
        c4 = [i for i in c4 if i != 'X']
        c4 = [eval(i) for i in c4]
        c5 = [B5.get(), B10.get(), B15.get(), B20.get(), B25.get()]
        c5 = [i for i in c5 if i != 'X']
        c5 = [eval(i) for i in c5]

        s1 = []
        s2 = []
        s3 = []
        s4 = []
        s5 = []

        s1.append(sum([a * b for a, b in zip(r1, c1)]))
        s1.append(sum([a * b for a, b in zip(r1, c2)]))
        s1.append(sum([a * b for a, b in zip(r1, c3)]))
        s1.append(sum([a * b for a, b in zip(r1, c4)]))
        s1.append(sum([a * b for a, b in zip(r1, c5)]))
        s2.append(sum([a * b for a, b in zip(r2, c1)]))
        s2.append(sum([a * b for a, b in zip(r2, c2)]))
        s2.append(sum([a * b for a, b in zip(r2, c3)]))
        s2.append(sum([a * b for a, b in zip(r2, c4)]))
        s2.append(sum([a * b for a, b in zip(r2, c5)]))
        s3.append(sum([a * b for a, b in zip(r3, c1)]))
        s3.append(sum([a * b for a, b in zip(r3, c2)]))
        s3.append(sum([a * b for a, b in zip(r3, c3)]))
        s3.append(sum([a * b for a, b in zip(r3, c4)]))
        s3.append(sum([a * b for a, b in zip(r3, c5)]))
        s4.append(sum([a * b for a, b in zip(r4, c1)]))
        s4.append(sum([a * b for a, b in zip(r4, c2)]))
        s4.append(sum([a * b for a, b in zip(r4, c3)]))
        s4.append(sum([a * b for a, b in zip(r4, c4)]))
        s4.append(sum([a * b for a, b in zip(r4, c5)]))
        s5.append(sum([a * b for a, b in zip(r5, c1)]))
        s5.append(sum([a * b for a, b in zip(r5, c2)]))
        s5.append(sum([a * b for a, b in zip(r5, c3)]))
        s5.append(sum([a * b for a, b in zip(r5, c4)]))
        s5.append(sum([a * b for a, b in zip(r5, c5)]))

        s1 = [i for i in s1 if i != 0]
        s2 = [i for i in s2 if i != 0]
        s3 = [i for i in s3 if i != 0]
        s4 = [i for i in s4 if i != 0]
        s5 = [i for i in s5 if i != 0]

        x1 = Label(result, text=str(s1), font=('Arial', 14))
        x2 = Label(result, text=str(s2), font=('Arial', 14))
        x3 = Label(result, text=str(s3), font=('Arial', 14))
        x4 = Label(result, text=str(s4), font=('Arial', 14))
        x5 = Label(result, text=str(s5), font=('Arial', 14))

        if len(r1) != 0:
            x1.pack()
        if len(r2) != 0:
            x2.pack()
        if len(r3) != 0:
            x3.pack()
        if len(r4) != 0:
            x4.pack()
        if len(r5) != 0:
            x5.pack()

    else:
        np = Label(result, text='Not Possible', font=('Arial', 14))
        np.pack()


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
generate = Button(window, text='Generate', width=11, font=('Arial', 15), command=generate)
add = Button(window, text=' + ', width=5, font=('Arial', 15), command=matrix_sum)
subtract = Button(window, text=' - ', width=5, font=('Arial', 15), command=matrix_diff)
multiply = Button(window, text=' x ', width=5, font=('Arial', 15), command=matrix_prod)
clear = Button(window, text='Clear', width=5, font=('Arial', 15), command=clear)

# GUI set up------------------------------------------------------------------------------------------------------------
title = Label(window, text='Matrix Calculator', font=('Arial', 20, 'bold'))

# Griding---------------------------------------------------------------------------------------------------------------
title.grid(row=0, column=1, columnspan=11)
A.grid(row=3, column=0)
B.grid(row=3, column=6)

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

window.mainloop()
