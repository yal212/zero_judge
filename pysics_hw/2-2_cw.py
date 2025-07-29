from vpython import *

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.5              #球半徑 0.5 m
height = 15.0           #球初始高度 15 m
m = 1.0                 #球質量1kg
Fg = vector(0, -m*g, 0) #重力
v0=15
theta=3*pi/180

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,height/2,0)) #設定畫面
floor = box(length=60, height=0.01, width=10, color=color.green)   #畫地板
b1 = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=10) #畫球
b1.pos = vector(0, size, 0)    #球初始位置
b1.v = vector(v0*cos(theta), v0*sin(theta), 0)           #球初速

g1 = graph(title = "theta-R plot", width=600, height=400, xtitle="theta", ytitle="R")
f1 = gcurve(color=color.red)

g2 = graph(title = "theta-T plot", width=600, height=400, xtitle="theta", ytitle="T")
f2 = gcurve(color=color.blue)

dt = 0.001 #時間間隔 0.001 秒
t = 0.0 #模擬初始時間為0秒
start_t=t
while theta<=pi:    
    rate(100/dt)    #每一秒跑 1000 次
   
   
    b1.a = Fg/m            #球的加速度
    b1.v = b1.v + b1.a*dt          #球的末速度 = 前一刻速度 + 加速度*時間間隔
    b1.pos = b1.pos + b1.v * dt    #球的末位置 = 前一刻位置 + 速度*時間間隔

    if b1.pos.y<=size:
        end_t=t
        print("T=", end_t-start_t, ",R=", b1.pos.x, ",theta=", theta*180/pi)
        f1.plot(pos=(theta*180/pi, (b1.pos.x)))
        f2.plot(pos=(theta*180/pi, end_t-start_t))
        b1.pos = vector(0, size, 0)
        theta+=3*pi/180
        b1.v = vector(v0*cos(theta), v0*sin(theta), 0)  
        start_t=t

   
   
    t = t + dt    #計時器

while True:
    x=1     #for loop to continue