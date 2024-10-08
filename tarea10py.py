def SumaRecursiva(Numero):
    if(Numero <= 9):
        return Numero
    else:
        return SumaRecursiva(Numero // 10) + Numero % 10
    
def SumaIterativa(Numero):
    Suma = 0
    while Numero > 9:
        Suma += Numero % 10
        Numero //= 10
    return Numero + Suma

print("""\nEste programa tiene la capacidad de Sumar todos los digitos que se ingrese a la variable
      EJEMPLO: 1+2+3+4 = 10""")

NumIng = int(input("\nPor favor, ingrese  un numero: "))

print(f"\nLa suma de {NumIng} con la SumaRecursiva es:  {SumaRecursiva(NumIng)}")
print(f"\nLa suma de {NumIng} con la SumaIterativa es:  {SumaIterativa(NumIng)}")







