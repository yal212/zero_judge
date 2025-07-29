from vpython import *

A = 2
N = 100
omega = 2*pi
T = 2*pi/omega
size = 0.1
x = 25
# m1 = 0.2
# m2 = 1
m1 = 1
m2 = 0.2
k = 500
d = 0.4


def SpringForce(r):
    return - k*(mag(r))*r/mag(r)


scene = canvas(title='Wave: Heavy to Light', width=1200, height=300,
               range=0.4*N/6, center=vector((N-1)*d/2, 0, 0))

ball = [sphere(radius=size, color=color.yellow, pos=vector(
    i*d, 0, 0), v=vector(0, 0, 0)) for i in range(N)]
for i in range(x, N):
    ball[i].color = color.cyan

spring = [helix(radius=size/2.0, thickness=d/15.0, pos=vector(i*d,
                0, 0), axis=vector(d, 0, 0)) for i in range(N-1)]

t, dt = 0, 0.001

while True:
    rate(1000)

    if t <= T/2:
        ball[0].pos = vector(0, A*sin(omega*t), 0)

    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos - ball[i].pos

    for i in range(1, x):
        ball[i].v += (-SpringForce(spring[i].axis) +
                      SpringForce(spring[i-1].axis))/m1*dt
        ball[i].pos += ball[i].v*dt
    # 右半部
    for i in range(x, N-1):
        ball[i].v += (-SpringForce(spring[i].axis) +
                      SpringForce(spring[i-1].axis))/m2*dt
        ball[i].pos += ball[i].v*dt

    t += dt
