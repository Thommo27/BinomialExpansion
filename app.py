from Factorial import fact

print('Binomial Expansion: (x + y)^n')

x = input('Input a value for x: ')
y = input('Input a value for y: ')
n = int(input('Input a value for n: '))

print('This is the binomial: ({} + {})^{}'.format(x, y, n))

xpower = n
ypower = 0
expanded = ''

for i in range (n + 1):
    ncr = fact(n) / fact(i) * fact(n-i)

    if (ypower < 1):
        expanded += ('({}{}^{})'.format(ncr, x, xpower))
    elif (ypower == 1):
        expanded += ('({}{}^{} {})'.format(ncr, x, xpower, y))
    elif (xpower < 1):
        expanded += ('({}{}^{})'.format(ncr, y, ypower))
    elif (xpower == 1):
        expanded += ('({}{}{}^{})'.format(ncr, x, y, ypower))
    else:
        expanded += '({}{}^{} {}^{})'.format(ncr, x, xpower, y, ypower)
    
    if (i == n):
        break
    elif (ncr > 0):
        expanded += ' + '
    elif (ncr < 0):
        expanded += ' - '

    xpower -= 1
    ypower += 1

print(expanded)