while True:
    try:
        age = int(input(('what is your age?')))
        10/age
        raise ValueError('hey cut it out')
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ops..... Error msg: {err}')
        
    except:
        print('please check your input.')
    else:
        break
    finally:
        # finally is always run (even though execute the break above)
        print('ok iam finally done')
