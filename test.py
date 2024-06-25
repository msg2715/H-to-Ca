import tkinter

window = tkinter.Tk()

window.geometry("300x300")

def hello(msg):
    print(msg)

text = 'ag'
btn1 = tkinter.Button(window, text='', command=hello(text))
btn1.pack()


window.mainloop()

"""
이 코드를 실행시키면 ag가 print되지만 버튼을 누를 때 ag가 프린트되지 않는다.
그 이유는 command에 hello라는 함수를 전달한것이 아니라
command에 hello(text)함수가 실행되고 반환된 값을 command에 전달했기 때문이다.
따라서 버튼을 눌렀을 때 hello(text)가 실행되게 하려면 lambda를 사용해야한다.
command=lambda:hello(text)
"""