from vpython import *

N = 50
size = 0.005
m = 0.01
g = vec(0, -9.8, 0)
k = 40
d = size * 2
L = 20 * size * (N-1)
t = 0
dt = 0.0005
T = 20 * dt
damp = 0.05
T0 = 10


def SpringForce(r):
    return - k*(mag(r)-d)*r/mag(r)


scene = canvas(title="slinky drop", width=250, height=600,
               range=L/3.5, center=vector(0, -4*L/7, 0), fov=0.2, align="left")
spring = [helix(pos=vector(0, -i*d, 0), axis=vector(0, -d, 0),
                radius=size * 40, coils=1, thickness=size * 4, color=color.white) for i in range(N-1)]
ground = box(pos=vector(0, -1.2*L, 0), length=L/5, width=L/5, height=L/1000)
ball = sphere(radius=size * 20, color=color.green,
              pos=vector(0, -N/2*d, 10), v=(0, 0, 0))
red_ball = sphere(radius=size * 40, color=color.red,
                  pos=vector(0, -(N-1)*d, 10), v=(0, 0, 0))

vt_graph = graph(title="V-T", xtitle="time (s)",
                 ytitle="v (m/s)", width=600, height=600, align="left")
end_curve = gcurve(color=color.red, label="end of slinky")
CM_curve = gcurve(color=color.green, label="center of mass")

ball_pos = [vector(0, -i*d, 0) for i in range(N)]
ball_v = [vector(0, 0, 0) for i in range(N)]

spring_pos = [vector(0, -i*d, 0) for i in range(N-1)]
spring_axis = [vector(0, 0, 0) for i in range(N-1)]

while True:
    rate(1/dt)

    ball_pos_CM = vector(0, 0, 0)
    vcm = vector(0, 0, 0)
    mv_total = 0.0
    m_total = 0.0

    if t >= T0:
        damp = 0
        ball_v[0] += (-SpringForce(spring_axis[0]) +
                      m*g - damp * ball_v[0]) / m * dt
        ball_pos[0] += ball_v[0] * dt

    for i in range(N-1):
        spring_pos[i] = ball_pos[i]
        spring_axis[i] = ball_pos[i+1] - ball_pos[i]

    for i in range(1, N):   # calculate force
        if i == N-1:
            ball_v[i] += (SpringForce(spring_axis[i-1]) +
                          m*g - damp*ball_v[i]) / m * dt
        else:
            ball_v[i] += (-SpringForce(spring_axis[i]) +
                          SpringForce(spring_axis[i-1]) + m*g - damp*ball_v[i]) / m * dt
            ball_pos[i] += ball_v[i] * dt

    for i in range(N-1):  # 非彈性碰撞
        if (ball_pos[i].y - ball_pos[i+1].y) <= d:
            ball_v[i] = ball_v[i+1] = (ball_v[i] + ball_v[i+1]) / 2
            ball_pos[i+1].y = ball_pos[i].y - d

    for i in range(N):  # 計算質心
        ball_pos_CM += ball_pos[i]
        mv_total += m * ball_v[i].y
        m_total += m

    ball.pos = ball_pos_CM / N
    vcm.y = mv_total/m_total
    red_ball.pos = ball_pos[N-1]

    # touch floor --> stop
    if (red_ball.pos.y <= -1.2*L+size*40) and ball_v[N-1].y < 0:
        ball_v[N-1].y = 0
        for i in range(N-1):
            ball_v[i] = vector(0, 0, 0)

    print(ball_v[N-1], vcm, t)
    if t % T < T and t % T+dt > T:
        for i in range(N-1):
            spring[i].pos = spring_pos[i]
            spring[i].axis = spring_axis[i]

    if t > T0 and t < 10.745:
        CM_curve.plot(t, vcm.y)
        end_curve.plot(t, ball_v[N-1].y)

    if t > 10.747:
        break

    t += dt
