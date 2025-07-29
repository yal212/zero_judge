from vpython import *
import random

# 初始參數設定
N = 12  # 質點個數
m = 1  # 質點質量
w = 25  # 方盒邊長
size = 1.2  # 球半徑
k = 50  # 彈力常數
t = 0  # 初始時間
dt = 0.0005  # 時間精度


def is_valid_position(x, y, positions, min_distance):
    for pos in positions:
        dx = x - pos[0]
        dy = y - pos[1]
        if (dx*dx + dy*dy) < min_distance*min_distance:
            return False
    return True


# 隨機初始位置和速度，確保球不重疊
positions = []
x = []
y = []
for i in range(N):
    while True:
        new_x = random.uniform(-w/2 + size, w/2 - size)
        new_y = random.uniform(-w/2 + size, w/2 - size)
        if is_valid_position(new_x, new_y, positions, 2*size):
            positions.append((new_x, new_y))
            x.append(new_x)
            y.append(new_y)
            break

vx = [random.uniform(-5, 5) for i in range(N)]  # 各質點x方向初速
vy = [random.uniform(-5, 5) for i in range(N)]  # 各質點y方向初速


def Fs(r, L):  # 彈力
    if mag(r) < L:  # Only apply force when balls are overlapping
        return - k*(mag(r)-L) * r/mag(r)
    return vec(0, 0, 0)


# 物件設定
scene = canvas(width=500, height=500, background=vec(1, 1, 1), center=vec(
    0, 0, 0), forward=vec(0, 0, -1), range=15, fov=0.004, align='left')
ball = [sphere(pos=vec(x[i], y[i], 0), v=vec(vx[i], vy[i], 0), a=vec(
    0, 0, 0), radius=size, color=color.blue) for i in range(N)]
v_arrow = [arrow(pos=ball[i].pos, axis=ball[i].v, color=color.blue)
           for i in range(N)]

# 設定牆面
wall_Right = box(pos=vec(w/2, 0, 0), length=0.1, height=w,
                 width=w, color=color.red, opacity=0.3)
wall_Left = box(pos=vec(-w/2, 0, 0), length=0.1, height=w,
                width=w, color=color.red, opacity=0.3)
wall_Up = box(pos=vec(0, w/2, 0), length=w, height=0.1,
              width=w, color=color.red, opacity=0.3)
wall_Down = box(pos=vec(0, -w/2, 0), length=w, height=0.1,
                width=w, color=color.red, opacity=0.3)

# 數據繪圖設定
energy_graph = graph(title="Energy vs Time", xtitle="Time (s)",
                     ytitle="Energy (J)", ymin=0, width=500, height=500, align='right')
K_curve = gcurve(color=color.orange, label="Kinetic Energy")

while True:
    rate(1/dt)

    # First calculate all forces
    forces = [vec(0, 0, 0) for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):  # check each pair once
            r = ball[j].pos - ball[i].pos
            L = size * 2  # distance when interacting
            if mag(r) < L:
                # spring force
                force = Fs(r, L)
                forces[i] -= force
                forces[j] += force

                overlap = L - mag(r)
                if overlap > 0:
                    n = r/mag(r)
                    ball[i].pos -= (overlap/2) * n
                    ball[j].pos += (overlap/2) * n

                    # Elastic collision velocity update
                    v_rel = ball[j].v - ball[i].v
                    v_rel_n = dot(v_rel, n)
                    if v_rel_n < 0:  # Only if moving toward each other
                        # Update velocities for elastic collision
                        ball[i].v += v_rel_n * n
                        ball[j].v -= v_rel_n * n

    # Update positions and velocities
    K = 0
    for i in range(N):
        # Update acceleration
        ball[i].a = forces[i]/m

        # Update velocity
        ball[i].v += ball[i].a*dt

        # Update position
        ball[i].pos += ball[i].v*dt

        # Calculate kinetic energy
        K += 0.5*m*mag(ball[i].v)**2

        # Update velocity arrow
        v_arrow[i].pos = ball[i].pos
        v_arrow[i].axis = ball[i].v

        # Wall collisions
        # Right wall
        if ball[i].pos.x + size >= w/2 and ball[i].v.x > 0:
            ball[i].v.x = -ball[i].v.x
            ball[i].pos.x = w/2 - size
        # Left wall
        if ball[i].pos.x - size <= -w/2 and ball[i].v.x < 0:
            ball[i].v.x = -ball[i].v.x
            ball[i].pos.x = -w/2 + size
        # Upper wall
        if ball[i].pos.y + size >= w/2 and ball[i].v.y > 0:
            ball[i].v.y = -ball[i].v.y
            ball[i].pos.y = w/2 - size
        # Lower wall
        if ball[i].pos.y - size <= -w/2 and ball[i].v.y < 0:
            ball[i].v.y = -ball[i].v.y
            ball[i].pos.y = -w/2 + size

    # Plot kinetic energy
    K_curve.plot(t, K)
    t += dt
