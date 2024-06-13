import tkinter
import tkinter.ttk
import tkinter.font
import random

window = tkinter.Tk()

window.title('H to Ca')
window.geometry('500x600+100+100')

elements1 = []
elements2 = ['Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
elements3 = ['K', 'Ca']

pixelVirtual = tkinter.PhotoImage(width=1, height=1)


# 제목
title_font = tkinter.font.Font(family='@HY견고딕', size=30)
title = tkinter.Label(window, text="H to Ca", font=title_font)
title.grid(row=0, column=0)


# 버튼 (초기도 랜덤으로)
for i in range(1, 10):
    exec(f"btn{i} = tkinter.Button(window, text='')")

btn1 = tkinter.Button(window, text='', image=pixelVirtual)

def newbutton():
    global elements1, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    elements1 = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F']
    for i in range(1, 10):
        r = random.choice(elements1)
        exec(f"btn{i}.config(text='{r}')")
        elements1.remove(r)

btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=3, column=1)
btn8.grid(row=3, column=2)
btn9.grid(row=3, column=3)


# 타이머
timer_font = tkinter.font.Font(family='새굴림', size=14)
timer = tkinter.Label(window, text='0.000', font=timer_font)
timer.grid(row=4, column=1)


# 다시하기 버튼
btn_re = tkinter.Button(window, text="다시하기")
btn_re.grid(row=5, column=1)


# 게임중 설정
newbutton()


window.mainloop()