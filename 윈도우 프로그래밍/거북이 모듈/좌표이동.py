import turtle as t 
import time # sleep 함수 
import random 

# 좌표 이동 - turtle.goto(x, y)

t.shape("turtle")
# t.up() # 펜 올리기 
t.speed(0) # 0부터 10까지 있다 // 0이 제일 빠른 속도 
# t.goto(200, 0) # x좌표 : 200, y좌표 : 0

# t.goto(0, 200)
'''
# 직선 그리기 
t.down() # 펜 내리기 
t.goto(-200, 0) 
t.goto(200, 0)
# 중앙에서 왼쪽으로 200만큼 가고 오른쪽으로 200 가기 
'''
'''
# 사각형 그리기 
t.goto(0, 0)
time.sleep(1)
t.goto(-100, 0)
time.sleep(1)
t.goto(-100, -100)
time.sleep(1)
t.goto(0, -100)
time.sleep(1)
t.goto(0, 0)
'''
# 랜덤 위치 지정

x = random.randint(-250, 250)
y = random.randint(-250, 250)

# t.up()
# t.goto(x, y)

# 마음대로 걷는 거북이
# 거북이의 머리 방향(각도) - 랜덤
n = 200 # 반복 횟수 
for i in range(n):
    ang = random.randint(1, 360)
    t.setheading(ang) 
    t.forward(50)









t.mainloop()