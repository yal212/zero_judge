from vpython import *

A = 0.2  # 振幅
N = 50  # 介質個數
omega = 2*pi*3  # 振動角頻率
T = 2*pi/omega  # 週期
size = 0.1  # 介質的大小
m = 0.1  # 介質的質量
k = 500.0  # 每一小段彈簧的彈力常數
d = 0.4  # 介質之間的初始間隔


def SpringForce(r):  # 彈力
    return - k*(mag(r))*r/mag(r)


scene = canvas(title='Spring Wave', width=1200, height=300,
               range=0.4*50/6, center=vector((N-1)*d/2, 0, 0))

# 建立物件，注意彈簧比球數量少1
ball = [sphere(radius=size, color=color.yellow, pos=vector(
    i*d, 0, 0), v=vector(0, 0, 0)) for i in range(N)]
spring = [helix(radius=size/2.0, thickness=d/15.0, pos=vector(i*d,
                0, 0), axis=vector(d, 0, 0)) for i in range(N-1)]

t, dt = 0, 0.001  # 初始時間，時間精度

while True:
    rate(1000)

    if t <= T/2:
        ball[0].pos = vector(0, A*sin(omega*t), 0)

    # 在球與球之間放入彈簧
    # from index 0 to 49, the elements are 0,1, 2, 3, 4,... , 48, totally 49 springs
    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos - ball[i].pos

    # 計算每一個球受相鄰兩條彈簧的彈力
    # from index 1 to 50, the elements are 1, 2, 3, 4,... , 49
    for i in range(1, N):
        if i == N-1:
            ball[-1].v += SpringForce(spring[-1].axis)/m*dt  # 最後一個球
        else:
            ball[i].v += (-SpringForce(spring[i].axis) +
                          SpringForce(spring[i-1].axis))/m*dt  # 非最後且非第一個的球

        ball[i].pos += ball[i].v*dt
        ball[-1].pos = vector((N-1)*d, 0, 0)

    t += dt
