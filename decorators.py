# decorators

# tanımı : tanımlanmış olan bir fonksiyonu bozmadan fonksiyona yeni özellikler eklemeye yarar.

def decorator(f):
    def wrapper(x,y):
        f(x**2,y**2)
    return wrapper

@decorator
def toplama(x,y):
    print(x+y)

toplama(4,5)