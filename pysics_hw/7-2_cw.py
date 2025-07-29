from vpython import *

A = 0.05  # 振幅
N = 50  # 介質個數
size = 0.2  # 介質的大小
m = 0.1  # 單個介質的質量
g = vec(0, -9.8, 0)  # 環境重力場
k = 50000.0  # 每一小段彈簧的彈力常數
d = 0.4  # 介質之間的初始間隔
L = d*(N-1)  # 繩子總長
t, dt = 0, 0.001  # 初始時間，時間精度
T = 50*dt  # 更新畫面的時間間隔
damp = 0.2  # 質點受阻力係數


def SpringForce(r):  # 彈力
    return - k*(mag(r)-d)*r/mag(r)


scene = canvas(title='Catenary', width=1000, height=600, range=L/2,
               center=vector((N-1)*d/2-L/5, -L/10, 0), background=color.white, fov=0.2)
ball = [sphere(radius=size, color=vec(0.5, 0.5, 0.5), pos=vector(
    i*d, 0, 0), v=vector(0, 0, 0)) for i in range(N)]  # 畫球

# 各質點的位置與速度
ball_pos = [vector(i*d, 0, 0) for i in range(N)]
ball_v = [vector(0, 0, 0) for i in range(N)]
# 各彈簧的位置與軸方向
spring_pos = [vector(i*d, 0, 0) for i in range(N-1)]
spring_axis = [vector(d, 0, 0) for i in range(N-1)]

# 畫作用力箭頭
F_Left_arr = arrow(color=color.blue, opacity=0.5, shaftwidth=L/50)
F_Right_arr = arrow(color=color.green, opacity=0.5, shaftwidth=L/50)
Fg_arr = arrow(color=color.red, opacity=0.5, shaftwidth=L/50)
X = 0.1  # 箭頭縮放比例

# 畫合力三角形確認箭頭
F_Left_arr_check = arrow(color=color.blue, opacity=0.5, shaftwidth=L/50)
F_Right_arr_check = arrow(color=color.green, opacity=0.5, shaftwidth=L/50)
Fg_arr_check = arrow(color=color.red, opacity=0.5, shaftwidth=L/50)

# 畫力的延伸線
F_Left_line = cylinder(radius=L/50/10, color=F_Left_arr.color, opacity=0.5)
F_Right_line = cylinder(radius=L/50/10, color=F_Right_arr.color, opacity=0.5)
Fg_line = cylinder(radius=L/50/10, color=Fg_arr.color, opacity=0.5)


while True:
    rate(1/dt)

    for i in range(N-1):
        spring_pos[i] = ball_pos[i]
        spring_axis[i] = ball_pos[i+1] - ball_pos[i]

    for i in range(1, N-1):
        ball_v[i] += (-SpringForce(spring_axis[i]) +
                      SpringForce(spring_axis[i-1]) + m*g - damp*ball_v[i])/m*dt
        ball_pos[i] += ball_v[i]*dt

    if t % T < T and t % T+dt > T:  # 畫圖，每隔T秒更新一次畫面
        for i in range(N):
            ball[i].pos = ball_pos[i]

    ball_pos_CM = vec(0, 0, 0)  # 每個迴圈歸零質心位置
    for i in range(N):
        ball_pos_CM += ball_pos[i]/N  # 計算質心位置

    if t % T < T and t % T+dt > T:  # 畫圖，每隔T秒更新一次畫面
        for i in range(N):
            ball[i].pos = ball_pos[i]

        # Forces
        F_left = SpringForce(spring_axis[0])
        F_right = -SpringForce(spring_axis[N-2])
        Fg_total = N * m * g

        # Main arrows
        F_Left_arr.pos = ball_pos[0]
        F_Left_arr.axis = X * F_left

        F_Right_arr.pos = ball_pos[N-1]
        F_Right_arr.axis = X * F_right

        Fg_arr.pos = ball_pos_CM
        Fg_arr.axis = X * Fg_total

        # Extension lines
        LINE = 2
        F_Left_line.pos = F_Left_arr.pos
        F_Left_line.axis = -F_Left_arr.axis*LINE

        F_Right_line.pos = F_Right_arr.pos
        F_Right_line.axis = -F_Right_arr.axis*LINE

        Fg_line.pos = Fg_arr.pos
        Fg_line.axis = Fg_arr.axis*LINE

        # Vector triangle check
        F_Left_arr_check.pos = vec(0, 0, 0)
        F_Left_arr_check.axis = X * F_left

        F_Right_arr_check.pos = F_Left_arr_check.pos + F_Left_arr_check.axis
        F_Right_arr_check.axis = X * F_right

        Fg_arr_check.pos = F_Right_arr_check.pos + F_Right_arr_check.axis
        Fg_arr_check.axis = X * Fg_total

        triangle_origin = vector(-L/3, -L/2, 0)

        # Triangle check
        F_Left_arr_check.pos = triangle_origin
        F_Left_arr_check.axis = X * F_left

        F_Right_arr_check.pos = F_Left_arr_check.pos + F_Left_arr_check.axis
        F_Right_arr_check.axis = X * F_right

        Fg_arr_check.pos = F_Right_arr_check.pos + F_Right_arr_check.axis
        Fg_arr_check.axis = X * Fg_total

    t += dt
