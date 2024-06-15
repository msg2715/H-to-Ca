import tkinter
import tkinter.ttk
import tkinter.font
import random
import time

window = tkinter.Tk()
window.configure(bg='white')

window.title('H to Ca')
window.geometry('500x600+100+100')
window.resizable(width=False, height=False) # 창 크기 고정

elements1 = []
elements2 = ['Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
elements3 = ['K', 'Ca']

pixelVirtual = tkinter.PhotoImage(width=1, height=1)


# 제목
title_font = tkinter.font.Font(family='@HY견고딕', size=30)
title = tkinter.Label(window, text="H to Ca", font=title_font, bg='white')
title.pack()

# 버튼 (초기도 랜덤으로)
btn_text = tkinter.StringVar()

def click():
    if elements1 != []:
        print(btn_text.get())

btn_font = tkinter.font.Font(size=20)
#for i in range(1, 10):
    #exec(f"btn{i} = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, variable=btn_text, command=click)")

btn1 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn2 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn3 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn4 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn5 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn6 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn7 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn8 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)
btn9 = tkinter.Button(window, text='', font=btn_font, image=pixelVirtual, width=100, height=100, compound='c', bg='#46a', fg='white', relief='groove', bd=0, highlightthickness=0, command=click)

def newbutton():
    global elements1, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    elements1 = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F']
    for i in range(1, 10):
        r = random.choice(elements1)
        exec(f"btn{i}.config(text='{r}')")
        elements1.remove(r)

btn1.place(x=145-50, y =210-50)
btn2.place(x=250-50, y =210-50)
btn3.place(x=355-50, y =210-50)
btn4.place(x=145-50, y =315-50)
btn5.place(x=250-50, y =315-50)
btn6.place(x=355-50, y =315-50)
btn7.place(x=145-50, y =420-50)
btn8.place(x=250-50, y =420-50)
btn9.place(x=355-50, y =420-50)


# 타이머
timer_font = tkinter.font.Font(family='새굴림', size=14)
timer = tkinter.Label(window, text='0.000', font=timer_font, bg='white')
timer.pack()


# 다시하기 버튼
btn_re_font = tkinter.font.Font(family='새굴림', size=16,)
btn_re = tkinter.Label(window, text="다시하기", font=btn_re_font, fg='white', bg='#C2C2C2')
btn_re.pack()


# 만든것들 화면에 출력
window.update()
title.place(x=250-(title.winfo_width()/2), y=80-(title.winfo_height()/2))
timer.place(x=250-(timer.winfo_width()/2), y=490-(timer.winfo_height()/2))
btn_re.place(x=250-(btn_re.winfo_width()/2), y=600-btn_re.winfo_height())


# 게임중 설정
newbutton()
elements1 = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F']

start_time = time.time()


window.mainloop()