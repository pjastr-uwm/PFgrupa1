def fibonacci(arg):
    if not isinstance(arg, int) or arg < 0:
        raise TypeError

    if arg == 0:
        return 0
    if arg == 1:
        return 1
    return fibonacci(arg-1)+fibonacci(arg-2)
