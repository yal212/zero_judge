from vpython import *

G = 6.67*10**(-11)  #萬有引力常數
M = 6*10**24        #地球M的質量
m = 1000            #衛星m的質量
Re = 6.4*10**6      #地球半徑
H = 20*Re           #離地高度
t = 0               #時間
dt = 60             #時間精度

def Fg(r):          #萬有引力函數
    return -G*M*m/mag(r)**2 * r/mag(r)

scene = canvas(align='left', width=500, height=500, center=vec(0,0,0), background=vec(0.6,0.8,0.8))     #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)                                       #放置物件地球
satellite = sphere(pos=vec(H,0,0), radius=0.5*Re, color=color.red, make_trail=True, retain=50)          #放置物件衛星
satellite.v = vec(0,1000,0)      #衛星的初始速度

gd = graph(align='left', width=500, height=500,                  #設定F-r繪圖視窗
            title='E紅色、K綠色、Ug藍色', xtitle='t', ytitle='E',
            foreground=color.black, background=color.white)    
f1 = gcurve(color=color.red)
f2 = gcurve(color=color.green)
f3 = gcurve(color=color.blue) #graph線條顏色
F0 = G*M*m/Re**2                                                 #地球表面重力強度

while mag(satellite.pos - earth.pos) >= Re:        #執行迴圈
    rate(1000)
    r = satellite.pos - earth.pos      #地球指向衛星的距離向量
    satellite.a = Fg(r)/m              #衛星的加速度
    satellite.v += satellite.a*dt      #衛星的速度
    satellite.pos += satellite.v*dt    #衛星的位置

    K= 0.5*m*mag(satellite.v)**2
    Ug = -G*M*m/mag(satellite.pos-earth.pos)    #重力位能一般形式
    E =K+Ug
   
    f1.plot(pos=(t, E))  #依數據繪圖
    f2.plot(pos=(t, K))
    f3.plot(pos=(t, Ug))
   
    t += dt          #計時器