from vpython import *

G = 6.67*10**(-11)  #萬有引力常數
M = 6*10**24        #地球M的質量
m = 1000            #衛星m的質量
Re = 6.4*10**6      #地球半徑
H = 20*Re           #離地高度
t = 0               #時間
dt = 60             #時間精度
v0=1200

def Fg(r):          #萬有引力函數
    return -G*M*m/mag(r)**2 * r/mag(r)

scene = canvas(align='left', width=500, height=500, center=vec(0,0,0), background=vec(0.6,0.8,0.8))     #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)                                       #放置物件地球
satellite = sphere(pos=vec(H,0,0), radius=0.5*Re, color=color.red, make_trail=True, retain=50)          #放置物件衛星
satellite.v = vec(0,1000,0)      #衛星的初始速度
F2 = sphere(pos=vector(0, 0, 0), radius=Re/3, color=color.red)
line1 = cylinder(radius=Re/10, color=color.black)
line2 = cylinder(radius=Re/10, color=color.black)

gd = graph(align='left', width=500, height=500,                  #設定F-r繪圖視窗
            title='衛星至兩焦點距離與時間的關係', xtitle='t/T', ytitle='(PF1 + PF2)/a',
            foreground=color.black, background=color.white, ymin=0.01)     
f1 = gcurve(color=color.red)                        #graph線條顏色
back = False
F0 = G*M*m/Re**2                                                 #地球表面重力強度

while mag(satellite.pos - earth.pos) >= Re:        #執行迴圈
    rate(1000)
    r = satellite.pos - earth.pos      #地球指向衛星的距離向量
    satellite.a = Fg(r)/m              #衛星的加速度
    satellite.v += satellite.a*dt      #衛星的速度
    satellite.pos += satellite.v*dt    #衛星的位置
    
    if not back and satellite.v.x > 0 and satellite.v.x + satellite.a.x*dt < 0:
        back = True
        Right_pos = vec(satellite.pos.x, satellite.pos.y, satellite.pos.z)
        T = t
        print(Right_pos)
    if not back and satellite.v.x < 0 and satellite.v.x + satellite.a.x*dt > 0:
        Left_pos = vec(satellite.pos.x, satellite.pos.y, satellite.pos.z)
        print(Left_pos)
    if not back and satellite.v.y > 0 and satellite.v.y + satellite.a.y*dt < 0:
        Up_pos = vec(satellite.pos.x, satellite.pos.y, satellite.pos.z)
        print(Up_pos)
    if not back and satellite.v.y < 0 and satellite.v.y + satellite.a.y*dt > 0:
        Down_pos = vec(satellite.pos.x, satellite.pos.y, satellite.pos.z)
        print(Down_pos)

    

    if back:  #如果達成繞行一周

        a = mag(Right_pos - Left_pos)/2  #半長軸
        b = mag(Up_pos - Down_pos)/2     #半短軸
        c = sqrt(a**2 - b**2)            #偏心距

        if abs(Right_pos.x) > abs(Left_pos.x):   #右端點距離地球較遠
            F2_pos = earth.pos + vec(2*c,0,0)    #另一焦點在地球右側
            F2.pos = F2_pos
        elif abs(Right_pos.x) < abs(Left_pos.x): #左端點距離地球較遠
            F2_pos = earth.pos - vec(2*c,0,0)    #另一焦點在地球左側
            F2.pos = F2_pos

        line1.pos = earth.pos  #更新衛星至地球的連心線
        line1.axis = satellite.pos - earth.pos

        line2.pos = F2.pos     #更新衛星至焦點2的連心線
        line2.axis = satellite.pos - F2.pos

        f1.plot(pos=(t/T, (mag(line1.axis) + mag(line2.axis))/a))  #將衛星與兩焦點距離和對時間的數據以graph繪圖

    t += dt          #計時器

while True:
    x=0