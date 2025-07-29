from vpython import*

m = [1, 1, 1, 1, 1]               #各質點質量
N = len(m)                        #質點個數
x = [-20, -17, -5, -2, 1]         #各質點x方向位置
v = [5, 5, 0, 0, 0]               #各質點x方向初速
ball_color = [color.blue]*len(m)  #各質點的顏色
size = 1.2   #球半徑
k = 50       #彈力常數
t = 0        #初始時間
dt = 0.0005  #時間精度

def Fs(r): #彈力
    return - k*(mag(r)-2*size) * r/mag(r)

def ElasticCollision(v1, v2, r1, r2, m1, m2):  
    v1_col = v1 - (2*m2/(m1+m2)) * dot((v1-v2), (r1-r2)) * (r1-r2)/mag(r1-r2)**2
    v2_col = v2 - (2*m1/(m1+m2)) * dot((v2-v1), (r2-r1)) * (r2-r1)/mag(r2-r1)**2 
    return (v1_col, v2_col)

#物件設定
scene = canvas(width=800, height=250, background=vec(1,1,1), center=vec(5,0,10), forward=vec(0,0,-1), range=10, fov=0.004)

ball = [sphere(pos=vector(x[i], 0, 0), v=vector(v[i], 0, 0), a=vector(0, 0, 0), radius=size, color=ball_color[i]) for i in range(N)]
v_arrow = [arrow(pos=vector(x[i], 0, 0), axis=vector(v[i], 0, 0), color=ball_color[i]) for i in range(N)]

#數據繪圖設定
energy_graph = graph(title="Energy vs Time", xtitle="Time (s)", ytitle="Energy (J)", width=800, height=250, ymin=0.01)
K_curve = gcurve(color=color.orange, label="Kinetic Energy")

while True:
    rate(1/dt)
    Us = 0  #每次主迴圈歸零彈力位能
    for i in range(N):  #第1層迴圈
        force = vec(0,0,0)   #每次歸零第1層迴圈的作用力
        for j in range(N):  #第2層迴圈
            if i != j and mag(ball[i].pos - ball[j].pos) <= 2*size and dot(ball[i].pos-ball[j].pos, ball[i].v-ball[j].v) < 0:
                ball[i].v , ball[j].v = ElasticCollision(ball[i].v, ball[j].v, ball[i].pos, ball[j].pos, m[i], m[j])

    K = 0
    for i in range(N):
        ball[i].pos += ball[i].v*dt  #更新球的位置
        v_arrow[i].pos = ball[i].pos #更新速度箭頭位置
        v_arrow[i].axis = ball[i].v  #更新速度箭頭軸方向
        K += 0.5*m[i]*mag(ball[i].v)**2  #計算動能
    
    #能量計算與數據繪圖

    K_curve.plot(t, K)

    t += dt