import main_printing
import main_VARSET
from time import *
from tkinter import *
from keyboard import *
from simacro_info import *
title = "SIMacro"
win = Tk()
win.geometry("150x200")
win.title(title)
btn2 = Button(win)
btn2.config(width=20, height=2)
btn2.config(text="창 닫기")
btn2.pack(side="bottom")
btn = Button(win)
btn.config(width=20, height=2)
btn.config(text="매크로 실행")
btn.pack(side="bottom")
ent = Entry(win)
ent.config(width=20)
scale = Scale(win)
scale.config(from_=2000, to=1)
scale.config(width=40)
scale.pack(side="left")
lab = Label(win)
lab.config(text=versionCODE)
lab.pack(side="top")
def macro():
    a = ent.get()
    main_printing.printingCHECK(2)
    sleep(main_VARSET.activedela)
    main_printing.printingCHECK(3)
    for i in range(scale.get()):
        write(a, main_VARSET.wrddela, True, None)
        sleep(main_VARSET.dela)
        press('enter')
    main_printing.printingCHECK(4)
def removeGUI():
    main_printing.printingCHECK(0)
    win.quit()
ent.pack(side="bottom")
btn.config(command=macro)
btn2.config(command=removeGUI)
def macroGUI():
    main_printing.printingCHECK(1)
    win.mainloop()