from vpython import *
 
G = 6.67*10**(-11)  #萬有引力常數
M = 6*10**24        #地球M的質量
m = 1000            #衛星m的質量
Re = 6.4*10**6      #地球半徑
H = 20*Re           #離地高度
t = 0               #時間
dt = 60             #時間精度
v0 = 1200           #衛星的初始速度
Right_pos = vector(0, 0, 0)
Left_pos = vector(0, 0, 0)
a = 0 
lap = 1
K = 0
         
def Fg(r):          #萬有引力函數
    return -G*M*m/mag(r)**2 * r/mag(r)

scene = canvas(align='left', width=500, height=500, center=vec(0,0,0), background=vec(1,1,1))  #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)  #放置物件地球
satellite = sphere(pos=vec(H,0,0), radius=0.5*Re, color=color.red, make_trail=True, v=vec(0,v0,0))  #放置物件衛星   

back = False  #作為判斷是否完成繞行一週的布林值

while mag(satellite.pos - earth.pos) >= Re:           
    rate(1000)
    r = satellite.pos - earth.pos
    satellite.a = Fg(r)/m
    satellite.v += satellite.a*dt     
    satellite.pos += satellite.v*dt  

    if not back and satellite.v.x < 0 and satellite.v.x + satellite.a.x*dt > 0:
        Left_pos = vec(satellite.pos.x, satellite.pos.y, satellite.pos.z)
    if not back and satellite.v.x > 0 and satellite.v.x + satellite.a.x*dt < 0:
        back = True
        Right_pos = vec(satellite.pos.x, satellite.pos.y, satellite.pos.z)
        T = t  #繞行週期
        t = 0
        a = mag(Right_pos - Left_pos) / 2
        
    if back: 
        K = a ** 3 / T ** 2
        print(f"圈數{lap}, K = {K}")
        lap += 1
        v0 += 200
        satellite.v = vector(0, v0, 0)
        back = False
     
    t += dt