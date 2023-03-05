while True:
    try:
        number = int(input('what is you\'r favorite number?'))
        print(18/number)
    except ValueError:
        print('Make sure you entered a number')
    except ZeroDivisionError:
        print('Don\'t pick a zero')
    except():
        break
    finally:
        print('loop complete')