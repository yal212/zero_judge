sun_last, sun_years = map(int, input().split())
moon_last, moon_years = map(int, input().split())

sun_right, moon_right = -sun_last, -moon_last

while sun_right < 0:
    sun_right += sun_years

while moon_right < 0:
    moon_right += moon_years

while sun_right != moon_right:
    if sun_right > moon_right:
        moon_right += moon_years
    else:
        sun_right += sun_years

print(sun_right)
