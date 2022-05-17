from decimal import Decimal, localcontext

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)

"""
    Примечание. Главное преимущество decimal в том, что он позволяет контролировать различные аспекты вычислений,
    такие как число знаков после запятой и округление. Что бы это сделать необходимо создать локальный контекст и 
    поменять его установки
"""
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(f'ctx.prec = 3:: {a / b}')

with localcontext() as ctx:
    ctx.prec = 50
    print(f'ctx.prec = 50:: {a / b}')
