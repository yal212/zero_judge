from vpython import *

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.12              #球半徑 (real basketball size)
height = 2.1           #球初始高度 (typical release height)
m = 0.6                 #球質量
Fg = vector(0, -m*g, 0) #重力
v0=9.0                 #初始速度 (adjusted for better shot success)
theta=3*pi/180

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,height/2,0)) #設定畫面
floor = box(length=60, height=0.01, width=10, color=color.green)   #畫地板
r=ring(pos=vector(6.75, 3.05, 0), axis=vector(0, 1, 0), radius = 0.26, thickness = 0.016, color=color.orange)
b1 = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=1) #畫球
b1.pos = vector(0, height, 0)    #球初始位置
b1.v = vector(v0*cos(theta), v0*sin(theta), 0)           #球初速
show_angle = label(pos=vector(0,-7*size,0), box = False, height = 20, color=color.yellow)

dt = 0.001 #時間間隔 0.001 秒
t = 0.0 #模擬初始時間為0秒

while theta <= pi/2:    
    rate(1000)    #每一秒跑 1000 次
    
    shot_complete = False
    success_detected = False
    b1.pos = vector(0, height, 0)
    b1.v = vector(v0*cos(theta), v0*sin(theta), 0)
    
    # Simulate this shot until it hits the ground
    while b1.pos.y > size and not shot_complete:
        rate(1000)  # Run simulation faster
        
        b1.a = Fg/m            #球的加速度
        b1.v = b1.v + b1.a*dt          #球的末速度 = 前一刻速度 + 加速度*時間間隔
        b1.pos = b1.pos + b1.v * dt    #球的末位置 = 前一刻位置 + 速度*時間間隔

        # Check if ball is approaching the ring area
        if b1.pos.x > 6.5 and b1.pos.x < 7.0 and b1.pos.y > 2.8 and b1.pos.y < 3.3 and not success_detected:
            horizontal_distance = abs(b1.pos.x - r.pos.x)            # Calculate horizontal distance from ball center to ring center
            vertical_distance = abs(b1.pos.y - r.pos.y)            # Calculate vertical distance from ball center to ring center
            if horizontal_distance < 0.1 and vertical_distance < 0.1:            # If ball is directly above the ring within certain tolerance
                print(f"Shot went in at theta = {theta/pi*180:.1f} degrees, v0 = {v0:.1f} m/s")                # Print data once per successful shot
                success_detected = True
                
        t = t + dt    #計時器
    
    show_angle.text = 'theta = ' + str(round(theta/pi*180,0)) + ' deg'    # Update angle for next shot
    theta += 1*pi/180

while True:
    x=1     #for loop to continue