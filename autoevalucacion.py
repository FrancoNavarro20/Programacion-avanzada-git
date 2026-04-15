
def proteger_division(funcion):
        def envoltura(a, b):
            if b == 0:
              print("No se puede dividir por cero")
              return None
            return funcion(a, b)
        return envoltura


@proteger_division
def dividir(a, b):
   return a / b

   
print(dividir(10, 2))
print(dividir(10, 0))