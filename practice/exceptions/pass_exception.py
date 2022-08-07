import my_exceptions


def raise_exception(exception: my_exceptions.X):
    raise exception('raise exception msg')

raise_exception(my_exceptions.Y)Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# def raise_except/ion(exception: Exception):
#     raise exception('momo')

# raise_exception(exception)