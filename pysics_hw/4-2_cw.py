from vpython import *
 
G = 6.67*10**(-11)  #萬有引力常數
M = 6*10**24        #地球M的質量
m = 1000            #衛星m的質量
Re = 6.4*10**6      #地球半徑
H = 20*Re           #離地高度
t = 0               #時間
dt = 30             #時間精度
v0 = 1200           #衛星的初始速度
N = 20              #分割一個週期為N等分
         
def Fg(r):          #萬有引力函數
    return -G*M*m/mag(r)**2 * r/mag(r)

scene = canvas(align='left', width=500, height=500, center=vec(0,0,0), background=vec(1,1,1))  #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)  #放置物件地球
satellite = sphere(pos=vec(H,0,0), radius=0.5*Re, color=color.red, make_trail=True, retain = 100, v=vec(0,v0,0))  #放置物件衛星   

gd = graph(align='left', width=500, height=500, 
         title='時間區間內的掃略面積', xtitle='t', ytitle='dA', ymin = 0,
         foreground=color.black, background=color.white)     
f1 = gcurve(color=color.red)    #graph線條顏色

back = False  #作為判斷是否完成繞行一週的布林值

A = 0

while mag(satellite.pos - earth.pos) >= Re:           
    rate(1000)
    r = satellite.pos - earth.pos
    satellite.a = Fg(r)/m
    satellite.v += satellite.a*dt     
    satellite.pos += satellite.v*dt  

    if not back and satellite.v.x > 0 and satellite.v.x + satellite.a.x*dt < 0:
        back = True
        Right_pos = vec(satellite.pos.x, satellite.pos.y, satellite.pos.z)
        T = t  #繞行週期
        
    if back and int(((t/T)*N)%2) == 1:
        line_mark = cylinder(radius = Re/10, color=vector(0.5,0.5,0.5))  #畫細線
        line_mark.pos = earth.pos
        line_mark.axis = satellite.pos - earth.pos
    
    #dA為一個時間精度內，連心線的掃略面積
    dA = mag(cross(r, satellite.v*dt))/2
        
    if back: 
        A += dA  #累加面積
        if t%(T/N) > (t+dt)%(T/N):  #抓出每個等分的結束時刻
            print(A)           #在每個等分結束前將面積打印在terminal
            f1.plot(pos=(t,A)) #將該等分累加的面積畫到graph
            A = 0              #每個等分結束時將累加面積歸零
     
    t+=dt