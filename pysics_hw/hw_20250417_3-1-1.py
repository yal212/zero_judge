from vpython import *
g = vector(0,0,0)       #重力加速度(依各情況給定重力場)
size = 0.8              #球半徑
k = 100                 #彈力係數
m1 = 5.0                #球1的質量
m2 = 5.0                #球2的質量
d = 15*size             #球1與球2的間距
L0=d

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/ mag(r)

#畫面設定
scene = canvas(width=600, height=600, center = vector(d/2,1.5*d,0), background = vector(1,1,1), range=25)
#物件設定
spring = helix(radius = size/2, coils = 15, color = color.white, thickness = size/5)  #畫彈簧
ball_1 = sphere(radius = size, color=color.blue, make_trail=True)                     #畫球1
ball_2 = sphere(radius = size, color=color.green, make_trail=True)                    #畫球2
ball_cm = sphere(radius = size/3, color=color.red, make_trail=True)                   #畫質心標記紅點

ball_1.pos = vector(0, size, 0)  #球1初始位置       
ball_2.pos = vector(d, size, 0)  #球2初始位置
ball_1.v = vector(0, 10, 0)      #球1初速 
ball_2.v = vector(0, 0, 0)       #球2初速

spring.pos = ball_1.pos                #彈簧頭端位置
spring.axis = ball_2.pos - ball_1.pos  #彈簧軸方向

energy_graph=graph(title="E-T", xtitle="T", ytitle="E", fast=False)
Ek_curve=gcurve(graph=energy_graph, color=color.blue, label="Ek")   #動能
Ug_curve=gcurve(graph=energy_graph, color=color.green, label="Ug")  #重力位能
Es_curve=gcurve(graph=energy_graph, color=color.yellow, label="Es") #彈力位能
Et_curve=gcurve(graph=energy_graph, color=color.red, label="Et")    #總能

t = 0
dt = 0.001

while True:
    rate(1000)
    
    r=spring.axis

    ball_1.v += ( m1*g - SpringForce( spring.axis, d ) ) /m1*dt
    ball_1.pos = ball_1.pos + ball_1.v*dt

    ball_2.v += (m2*g + SpringForce(spring.axis, d))/m2*dt
    ball_2.pos = ball_2.pos + ball_2.v*dt

    spring.pos=ball_1.pos
    spring.axis = ball_2.pos - ball_1.pos           #彈簧的軸方向，由頭端指向尾端的距離向量

    cm=(m1*ball_1.pos+m2*ball_2.pos)/(m1+m2)
    ball_cm.pos=cm

    Ek = 0.5*m1*mag2(ball_1.v)+0.5*m2*mag2(ball_2.v)    #動能
    Ug=m1*g.y*ball_1.pos.y+m2*g.y*ball_2.pos.y          #重力位能
    Es=0.5*k*(mag(r)-L0)**2                             #彈力位能
    Et=Ek+Ug+Es                                         #總能

    Ek_curve.plot(t, Ek)
    Ug_curve.plot(t, Ug)
    Es_curve.plot(t, Es)
    Et_curve.plot(t, Et)

    t += dt                  #計時器

    print((ball_1.v+ball_2.v)/2)

while True:
    x=0