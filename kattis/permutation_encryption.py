#   original code

running = True
while running:
    # int_ = list(map(int, (input().split())))
    # key_len = int_[0]
    # keys = int_[1:]
    key_len, *keys = list(map(int, (input().split())))
    if key_len != 0:
        message = list(input())

        while len(message) % key_len != 0:
            message.append(" ")

        ans = [" " for _ in range(len(message))]

        for i in range(len(message)//key_len):
            temp = message[i*key_len:(i+1)*key_len]
            for index, key in enumerate(keys):
                ans[index+i*key_len] = temp[key-1]

        print("'"+"".join(ans)+"'")
    else:
        running = False

#   better ver

running = True
while running:
    key_len, *keys = list(map(int, (input().split())))

    if key_len == 0:
        running = False

    message = list(input())

    while len(message) % key_len != 0:
        message.append(" ")

    ans = [" " for _ in range(len(message))]

    for i in range(len(message)//key_len):
        temp = message[i*key_len:(i+1)*key_len]
        for index, key in enumerate(keys):
            ans[index+i*key_len] = temp[key-1]

    print("'"+"".join(ans)+"'")

#   better ver

while True:
    key_len, *keys = list(map(int, (input().split())))

    if key_len == 0:
        break

    message = list(input())

    while len(message) % key_len != 0:
        message.append(" ")

    # ans = [" " for _ in range(len(message))]
    ans = ""

    for i in range(len(message)//key_len):
        temp = message[i*key_len:(i+1)*key_len]
        for key in keys:
            ans += temp[key-1]

    print("'"+ans+"'")
