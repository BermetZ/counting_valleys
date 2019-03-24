def counting_valleys():
    s = list(input("Enter Gary's route: "))
    n = len(s)
    valleys = 0
    sea_level = 0

    for step in s:
        if step == 'U':
            sea_level += 1
            if sea_level == 0:
                valleys += 1
        elif step == 'D':
            sea_level -= 1

    print('Gary took {} steps and was in {} valleys.'.format(n, valleys))

counting_valleys()