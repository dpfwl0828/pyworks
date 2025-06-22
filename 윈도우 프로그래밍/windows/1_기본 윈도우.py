# 처음 만드는 윈도우 
from tkinter import *  # *은 모든 클래스, 함수를 말한다 
'''
def click():
    # print("안녕~ 파이썬!")
    lbl_result.config(text = "안녕~ 파이썬!")


root = Tk() # Tk 클래스에 인스턴스 생성
root.title("첫 윈도우")
root.geometry("250x100+850+450") # 너비가 250픽셀, 높이가 100 픽셀을 뜻함, x좌표 850 / y좌표 450

# 라벨 생성
# pack() - 가운데 배치 (한 줄을 차지한다)
Label(root, text ="Hello! Python!").pack()

#버튼 생성
# command - 함수에 명령을 내린다 
Button(root, text = "확인", command=click).pack()
# click() 은 함수인데 왜 바로 위에 클릭은 그냥 클릭만 쓰냐? 누를 때마다 실행되야 하는데
# 저걸 () 괄호를 씌우게 되면은 계속 실행되기 때문에 

# 출력 레이블 생성 
lbl_result = Label(root)
lbl_result.pack()



root.mainloop()
'''

# 레이아웃 (배치) - grid() 함수 

window = Tk()
window.title('배치-grid')
window.geometry("300x200")

Label(window, text='오늘도 좋은 하루 되세요', font=("돋움", 13)).grid(row=0, column=0)
Button(window, text="동", width=5, height=2).grid(row=1, column=0, sticky=E)
Button(window, text="서", width=5, height=2).grid(row=1, column=0, sticky=W)
Button(window, text="북", width=5, height=2).grid(row=2, column=0, sticky=N)
Button(window, text="남", width=5, height=2).grid(row=3, column=0, sticky=S)



window.mainloop()