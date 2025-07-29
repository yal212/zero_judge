m, d = map(int, input().split())
data={1:"大吉",2:"吉",0:"普通"}
s = (m*2+d)%3
print(data[s])
# if s == 0:
#     print("普通")
# elif s == 1:
#     print("吉")
# else:
#     print("大吉")