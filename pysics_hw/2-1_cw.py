from vpython import *

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.5              #球半徑 0.5 m
height = 15.0           #球初始高度 15 m
m = 1.0                 #球質量1kg
Fg = vector(0, -m*g, 0) #重力
damp=0.1

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,height/2,0)) #設定畫面
floor = box(length=50, height=0.01, width=10, color=color.green)   #畫地板
b1 = sphere(pos=vector(-10, size, 0), radius = size, color=color.red, make_trail= True, trail_type="points", interval=100) #畫球
b2 = sphere(pos=vector(-10, size, 0), radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=100)
#ball.pos = vector(0, height, 0)    #球初始位置
b1.v = vector(5, 8, 0)           #球初速
b2.v = vector(5, 8, 0)

dt = 0.001 #時間間隔 0.001 秒
t = 0.0 #模擬初始時間為0秒

while True:    
    rate(1/dt)    #每一秒跑 1000 次
    t = t + dt    #計時器
   
    AirResistance = - damp * b1.v
    b1.a = (Fg+AirResistance)/m            #球的加速度
    b1.v = b1.v + b1.a*dt          #球的末速度 = 前一刻速度 + 加速度*時間間隔
    b1.pos = b1.pos + b1.v * dt    #球的末位置 = 前一刻位置 + 速度*時間間隔
    if b1.pos.y <= size:    #條件：球心高度小於球半徑且速度沿-y軸
        b1.v.y = -b1.v.y    #條件成立則球的速度加一負號表示反彈

    b2.a = Fg/m            #球的加速度
    b2.v = b2.v + b2.a*dt          #球的末速度 = 前一刻速度 + 加速度*時間間隔
    b2.pos = b2.pos + b2.v * dt    #球的末位置 = 前一刻位置 + 速度*時間間隔
    if b2.pos.y <= size:    #條件：球心高度小於球半徑且速度沿-y軸
        b2.v.y = -b2.v.y
       
