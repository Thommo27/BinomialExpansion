def fact(num):
    if (num == 0):
        value = 1
    else:
        i = 1
        value = 1
        while (i <= num):
            value *= i
            i += 1
    return(value)