def obtenha_um_numero_inteiro(frase, min=None, max=None, proibidos=None):
    digitou_corretamente = False
    
    while not digitou_corretamente:
        try:
            numero = int(input(frase))
        except ValueError:
            print("Um número inteiro devia ter sido digitado; tente novamente!")
        else:
            if min != None and numero < min:
                print("Um valor de", min, "para cima deveria ter sido digitado, tente novamente!")
            elif max != None and numero > max:
                print("Um valor de", max, "para baixo deveria ter sido digitado, tente novamente!")
            elif proibidos != None and numero in proibidos:
                print("O(s) valor(es)", proibidos, "são inaceitáveis, tente novamente!")
            else:
                digitou_corretamente = True
                
    return numero

numero = obtenha_um_numero_inteiro(
    "Digite um número: ",
    min=None,
    max=100,
    proibidos=[10, 20, 30, 40, 50, 60, 70, 80, 90]
)

print("Número válido digitado:", numero)
