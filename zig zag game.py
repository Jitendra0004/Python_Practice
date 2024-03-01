import time

spaces = 0
space_increase = True

while True:
    print('  ' * spaces, end='')
    print('******')

    time.sleep(0.1)

    if space_increase is True:
        spaces += 1
        if spaces >= 6:
            space_increase = False
    else:
            spaces -= 1
            if spaces == 0:
                space_increase = True

