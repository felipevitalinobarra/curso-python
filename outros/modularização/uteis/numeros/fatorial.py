def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado
    