while True:
    n = raw_input('Enter num: ')
    try:
        n = int(n)
        break
    except ValueError:
        print('Enter the right number!')
        continue
