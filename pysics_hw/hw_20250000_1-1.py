from vpython import *

size = 0.1

scene = canvas(width=0, height=0, center=vector(
    2.5, 0, 0), background=vector(0, 0, 0))
# 設定物件視窗的顯示畫面與背景

ball = sphere(radius=size, color=color.yellow, pos=vector(
    0, 0, 0), v=vector(0, 0, 0), a=vec(5.0, 0, 0))

g1 = graph(title="x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.blue)

g2 = graph(title="v-t plot", width=600, height=400, xtitle="t", ytitle="v")
f2 = gcurve(color=color.red)

g3 = graph(title="a-t plot", width=600, height=400, xtitle="t", ytitle="a")
f3 = gcurve(color=color.green)
# 設定函數圖的畫面
# 設定函數圖中線條的特性，這裡只設定顏色

dt = 0.001
t = 0.0

while t < 6:

    if t < 2 and t+dt > 2:
        ball.a.x = -5

    rate(1/dt)
    t = t+dt
    ball.pos = ball.pos + ball.v*dt
    ball.v += ball.a*dt
    f1.plot(pos=(t, ball.pos.x))
    f2.plot(pos=(t, ball.v.x))
    f3.plot(pos=(t, ball.a.x))  # 每一個迴圈畫一個點描出線條，x軸為時間，y軸為位

    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0:
        print("time at turning point:", t)
        print("turning point", ball.pos)
        print("v at turning point", ball.v)
