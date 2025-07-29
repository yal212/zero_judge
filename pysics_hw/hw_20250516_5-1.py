from vpython import *
M = [0.1, 0.5, 3]
N = len(M)
size = [1, 2, 3]
Y = [18, 14.5, 9]
ball_color = [color.green, color.blue, color.red]
t = 0
dt = 0.0005
k = 100
g = 9.8

scene = canvas(width=250, height=600, background=vec(1, 1, 1),
               center=vec(0, 60, 10), forward=vec(0, 0, -1),
               range=30, fov=0.004, align='left')

ball = [sphere(pos=vec(0, Y[i], 0),
               v=vec(0, 0, 0),
               a=vec(0, 0, 0),
               radius=size[i],
               color=ball_color[i]) for i in range(N)]

ground = box(pos=vec(0, 0, 0),
             length=30,
             width=30,
             height=0.1,
             color=vec(0.5, 0.5, 0.5),
             opacity=0.3)

energy_graph = graph(title="Energy vs Time",
                     xtitle="Time (s)",
                     ytitle="Energy (J)",
                     width=600,
                     height=580,
                     align='left',
                     ymax=400, ymin=0)
E_curve = gcurve(color=color.black, label="Mechanical Energy")
K_curve = gcurve(color=color.orange, label="Kinetic Energy")
Ug_curve = gcurve(color=color.blue, label="Gravitational Potential Energy")
Us_curve = gcurve(color=color.red, label="Spring Potential Energy")


def Fs(r, L):  # 彈力函數
    return - k*(mag(r)-L) * r/mag(r)


while True:
    rate(1/dt)
    Us = 0
    for i in range(N):
        force = vector(0, 0, 0)
        for j in range(N):
            r = ball[j].pos - ball[i].pos   # ball 向量
            L = size[i] + size[j]
            if i != j and mag(r) <= L:  # for ball to not stack on each other
                force += -Fs(r, L)
                Us += (0.5*k*(mag(r)-L)**2)/2

        ball[i].a = force/M[i] + vector(0, -g, 0)   # caculate ball a

    K = 0
    Ug = 0
    for i in range(N):  # caculate K, Ug
        ball[i].v += ball[i].a*dt
        ball[i].pos += ball[i].v*dt
        K += 0.5*M[i]*mag(ball[i].v)**2
        Ug += M[i]*g*ball[i].pos.y

        if ball[i].pos.y <= size[i] and ball[i].v.y < 0:  # bounce when touches ground
            ball[i].v.y = -ball[i].v.y
    E = K + Ug + Us
    E_curve.plot(t, E)
    K_curve.plot(t, K)
    Us_curve.plot(t, Us)
    Ug_curve.plot(t, Ug)
    t += dt
