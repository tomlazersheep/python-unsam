# Ejercicio 10.12: Envolviendo a Fibonacci
# Como vimos, la implementación recursiva inmediata del cálculo del número de Fibonacci 
# (F(n) = F(n-1) + F_(n-2), F(0) = 0, F(1)= 1) es ineficiente porque muchas de las ramas calculan 
# reiteradamente los mismos valores.

# Escribí una función fibonacci(n) que calcule el n-ésimo número de Fibonacci de forma recursiva pero que utilice 
# un diccionario para almacenar los valores ya computados y no computarlos más de una vez.

# Observación: Será necesario implementar una función wrapper (es decir, una función que envuelva a otra) 
# para cumplir con la firma de la función pedida. Podés trabajar en un script en blanco o completar el siguiente código.

def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            res = dict_fibo[n]
        else:
          if n == 0:
            dict_fibo[n] = 0
          elif n == 1:
            dict_fibo[n] = 1
          else:
            res = fibonacci_aux(n - 1,dict_fibo) + fibonacci_aux(n - 2,dict_fibo)
        return  res,dict_fibo

    
    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F 