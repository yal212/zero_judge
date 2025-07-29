from vpython import *
import math

g=9.8                 #重力加速度 9.8 m/s^2
size=0.5              #球半徑 0.5 m
height=15.0           #球初始高度 15 m
m=1.0                 #球質量1kg
Fg=vector(0, -m*g, 0) #重力
damp=0.1
k=damp
t=0
dt=0.01

v0=vector(8, 20, 0)           #球初速
a0=vector(0, -g, 0)

scene=canvas(width=700, height=700,x=0, y=0, center=vector(20,height/2,0)) #設定畫面
floor=box(length=80, height=0.01, width=40, color=color.green)   #畫地板
b1=sphere(pos=vector(0, size+1, 0), radius=size, color=color.red, v=v0, a=a0, make_trail=True, trail_type="points", interval=1) #畫球
b2=sphere(pos=vector(0, size, 0), radius=size, color=color.yellow, v=v0, a=a0, make_trail=True, trail_type="points", interval=1)
b3=sphere(pos=vector(0, size, 0), radius=size, color=color.green, v=v0, a=a0, make_trail=True, trail_type="points", interval=1)

while b1.pos.y>=0 or b2.pos.y>=0:
    rate(1000)

    if b1.pos.y>=0:
        b1.pos+=b1.v*dt
        b1.v+=b1.a*dt
    if b2.pos.y>=0:
        b2.pos+=b2.v*dt 
        b2.v+=b2.a*dt+b2.v*-k/m*dt 
    
    t+=dt
t=0
while b3.pos.y>=0:
    rate(1000)

    b3.pos=vector(b3.v.x*(1-exp(-k*t))/k, -g*t/k+(k*b3.v.y+g)*(1-exp(-k*t))/k**2, 0)

    t+=dt


while True:
    x=1     #for loop to continue