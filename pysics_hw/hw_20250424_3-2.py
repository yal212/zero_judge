from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.8          
k = 10000              #彈簧力常數 10000 N/m
m1=5.0
m2=5.0
L=8

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=800, height=600, center=vector(0, 0, 0), background=color.black, range=30)#設定畫面
center=sphere(radius=size/5, color=color.yellow)
ball_1 = sphere(radius = size,  color=color.red, make_trail = True)#畫球
ball_2 = sphere(radius = size,  color=color.green, make_trail = True)#畫球
rod_1=helix(radius=0.01, coils=150, color=color.white, thickness=0.1)
rod_2=helix(radius=0.01, coils=150, color=color.white, thickness=0.1)

energy_graph=graph(title="E-t", xtitle="t", ytitle="E", fast=False)
E_red_curve=gcurve(graph=energy_graph, color=color.red, label="E_red")
E_green_curve=gcurve(graph=energy_graph, color=color.green, label="E_green")
Et_curve=gcurve(graph=energy_graph, color=color.blue, label="E_total")

ball_1.pos=vector(-L, 0, 0)
ball_2.pos=vector(-2*L, 0, 0)
ball_1.v=vector(0, 0, 0)
ball_2.v=vector(0, 0, 0)

rod_1.pos=center.pos
rod_2.pos=ball_1.pos
rod_1.axis=ball_1.pos-center.pos
rod_2.axis=ball_2.pos-ball_1.pos

dt = 0.001    #時間間隔
t = 0.0       #初始時間

while True:
    rate(1000)
    
    r1=rod_1.axis
    r2=rod_2.axis

    F_spring_1=SpringForce(r1, L)
    F_spring_2=SpringForce(r2, L)

    F1=vector(0, -m1*g, 0)+F_spring_1-F_spring_2
    F2=vector(0, -m2*g, 0)+F_spring_2

    ball_1.v+=F1/m1*dt
    ball_1.pos+=ball_1.v*dt

    ball_2.v+=F2/m2*dt
    ball_2.pos+=ball_2.v*dt

    rod_1.pos=center.pos
    rod_2.pos=ball_1.pos
    rod_1.axis=ball_1.pos-center.pos
    rod_2.axis=ball_2.pos-ball_1.pos

    Ek1=0.5*m1*mag2(ball_1.v)
    Ek2=0.5*m2*mag2(ball_2.v)
    U1=m1*g*ball_1.pos.y
    U2=m2*g*ball_2.pos.y
    Es1=0.5*k*(mag(r1)-L)**2
    Es2=0.5*k*(mag(r2)-L)**2

    E_red=Ek1+U1+Es1
    E_green=Ek2+U2+Es2
    E_total=E_red+E_green

    E_red_curve.plot(t, E_red)
    E_green_curve.plot(t, E_green)
    Et_curve.plot(t, E_total)

    t+=dt

while True:
    x=0



