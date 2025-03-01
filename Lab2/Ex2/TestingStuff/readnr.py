while True:
    n=(int)(input('Cititi nr de aruncari: '))
    if n>0:
        break
    print('Nr invalid! Cititi din nou: ')

while True:
    x=(int)(input('Cititi x: '))
    if x>=1 and x<=n:
        break
    print('Nr x invalid, x trebuie sa fie 1<=x<=n, cititi din nou:')

arr = [n,x]