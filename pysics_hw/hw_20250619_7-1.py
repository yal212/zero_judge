from vpython import *

A = 0.05  # 振幅
N = 100  # 介質個數
size = 0.2  # 介質的大小
m1 = 0.1  # 單個介質的質量
m2 = 0.4
k = 4000.0  # 每一小段彈簧的彈力常數
d = 0.4  # 介質之間的初始間隔
L = d*(N-1)  # 繩子總長
t, dt = 0, 0.0005  # 初始時間，時間精度
T = 100*dt  # 更新畫面的時間間隔
damp = 0.01  # 質點受阻力係數


def SpringForce(r):  # 彈力
    return - k*(mag(r))*r/mag(r)


mu = N*m1/L  # 繩子線密度
Fs = mag(SpringForce(vec(d, 0, 0)))  # 繩子張力
v_wave = sqrt(Fs/mu)  # 繩波波速
# lambda_wave = L
lambda_wave = 4*L / 2  # 繩波波長
f = v_wave/lambda_wave  # 強迫振動頻率
omega = 2*pi*f  # 強迫振角頻率

scene = canvas(title='Standing Wave', width=1000, height=300,
               range=L/6, center=vector((N-1)*d/2, 0, 0))
ball = [sphere(radius=size, color=color.yellow, pos=vector(
    i*d, 0, 0), v=vector(0, 0, 0)) for i in range(N)]  # 畫球

# 各質點的位置與速度
for i in range(N):
    if i < 50:
        ball[i].color = color.yellow
    else:
        ball[i].color = color.cyan

ball_pos = [vector(i*d, 0, 0) for i in range(N)]
ball_v = [vector(0, 0, 0) for i in range(N)]
# 各彈簧的位置與軸方向
spring_pos = [vector(i*d, 0, 0) for i in range(N-1)]
spring_axis = [vector(d, 0, 0) for i in range(N-1)]

energy_graph = graph(title="Energy", xtitle="time",
                     ytitle="displacement^2", width=1000, height=250)
A_curve = gcurve(color=color.orange)

while True:
    rate(1/dt)

    ball_pos[0] = vector(0, A*sin(omega*t), 0)  # 質點1的強迫運動

    for i in range(N-1):
        spring_pos[i] = ball_pos[i]
        spring_axis[i] = ball_pos[i+1] - ball_pos[i]

    for i in range(1, N):
        if i == N-1:
            if i < 50:
                m = m1
            else:
                m = m2
            ball_v[-1] += SpringForce(spring_axis[-1])/m*dt
            ball_pos[-1] += ball_v[-1]*dt
            ball_pos[-1].x = (N-1)*d
            # ball_pos[-1] = vector((N-1)*d, A*sin(omega*t), 0)

        else:
            if i < 50:
                m = m1
            else:
                m = m2
            ball_v[i] += (-SpringForce(spring_axis[i]) +
                          SpringForce(spring_axis[i-1]) - damp*ball_v[i])/m*dt
            ball_pos[i] += ball_v[i]*dt

    sum_A = 0  # 位移加總量值
    for i in range(N):
        sum_A += ball_pos[i].y**2  # 取各質點y方向位移進行加總
    A_curve.plot(t, sum_A)  # 繪製隨時間關係圖

    if t % T < T and t % T+dt > T:  # 畫圖，每隔T秒更新一次畫面
        for i in range(N):
            ball[i].pos = vec(ball_pos[i].x, ball_pos[i].y, ball_pos[i].z)

    t += dt
