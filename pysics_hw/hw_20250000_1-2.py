from vpython import *

size = 0.1

scene = canvas(width=600, height=400, center=vector(
    2.5, 0, 0), background=vector(0, 0, 0))
# 設定物件視窗的顯示畫面與背景，寬為600畫素、高為400畫素
# center為畫面中心，background為背景顏色

x = arrow(pos=vector(0, 0, 0), axis=vector(
    1, 0, 0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0, 0, 0), axis=vector(
    0, 1, 0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0, 0, 0), axis=vector(
    0, 0, 1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=size, color=color.yellow, pos=vector(
    0, 0, 0), v=vector(3.0, 0, 0), a=vec(-1.0, -0.5, 0))

dt = 0.001
t = 0.0

while t < 4:

    rate(1/dt)
    t = t+dt

    plot_t = t % 0.4  # 用餘數除法設定畫圖計時器，t累加至超過T後歸零
    if plot_t + dt >= 0.4 and plot_t < 0.4:  # 用條件判斷設定畫圖時間點
        arrow(color=color.green, pos=ball.pos,
              axis=ball.v, shaftwidth=0.05)  # 畫速度箭頭
        arrow(color=color.red, pos=ball.pos,
              axis=ball.a, shaftwidth=0.05)  # 畫加速度箭頭
        sphere(color=color.yellow, pos=ball.pos, radius=size)  # 畫球

    ball.pos = ball.pos + ball.v*dt
    ball.v += ball.a*dt

    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0:
        print("time at turning point:", t)
        print("turning point", ball.pos)
        print("v at turning point", ball.v)
