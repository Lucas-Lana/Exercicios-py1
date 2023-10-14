# Exercício 1: Imprimir "Olá Mundo"
def Exercício_1():
    print("Olá Mundo")
    print("----------//----------")

# Exercício 2: Capturar nome, idade e peso do usuário
def Exercício_2():
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite o seu peso: "))
    print(f'O seu nome é {nome}\nSua idade é {idade}\nSeu peso é {peso}')
    print("----------//----------")

# Exercício 3: Calcular o sucessor e o antecessor de um número
def Exercício_3():
    print("O programa irá calcular o sucessor e antecessor do número fornecido por você\n")
    n = int(input("Digite um número: "))
    sucessor = n + 1
    antecessor = n - 1
    print(f'O sucessor de {n} é {sucessor}, e seu antecessor é {antecessor}')
    print("----------//----------")

# Exercício 4: Calcular o dobro, triplo e raiz quadrada de um número
def Exercício_4():
    print("O programa irá calcular o dobro, triplo e raiz quadrada de um número fornecido pelo usuário\n")
    n = int(input("Digite um número: "))
    dobro = n * 2
    triplo = n * 3
    raiz = n ** (1/2)
    print(f'O número escolhido foi {n}, seu dobro é {dobro}, seu triplo é {triplo} e sua raiz quadrada é {raiz}')
    print("----------//----------")

# Exercício 5: Calcular a idade com base no ano de nascimento e ano atual
def Exercício_5():
    print("O programa irá calcular a idade do usuário com base no ano de nascimento e ano atual\n")
    ano_nascimento = int(input("Digite o ano em que nasceu: "))
    ano_atual = int(input("Informe em que ano estamos: "))
    idade = ano_atual - ano_nascimento
    print(f'Você possui {idade} anos')
    print("----------//----------")

# Exercício 6: Calcular o preço de um produto com desconto de 25%
def Exercício_6():
    print("O programa irá calcular o preço de um produto com desconto de 25%\n")
    preco = float(input("Digite o preço do produto: "))
    preco_com_desconto = preco * 0.75  # Aplicando desconto de 25%
    print(f'O preço atualizado do produto é R${preco_com_desconto}')
    print("----------//----------")

# Exercício 7: Calcular o salário após um aumento de 75%
def Exercício_7():
    print("O programa irá calcular o salário após um aumento de 75%\n")
    salario = float(input("Digite o valor do seu salário: "))
    salario_com_aumento = salario * 1.75  # Aumento de 75%
    print(f'Seu salário após o aumento ficou em R${salario_com_aumento}')
    print("----------//----------")

# Exercício 8: Calcular a tabuada do número recebido
def Exercício_8():
    print("O programa irá calcular a tabuada de um número fornecido pelo usuário\n")
    n =  int(input("Digite um número: "))
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print("----------//----------")

# Exercício 9: Comparações de tipos de dados
def Exercício_9():
    print("O programa irá comparar os tipos de dados fornecidos pelo usuário\n")
    dado1 = input("Digite o que quiser, seja uma palavra, um número inteiro ou um número fracionado: ")
    dado2 = input("Digite o que quiser, seja uma palavra, um número inteiro ou um número fracionado: ")

    try:
        dado1 = int(dado1)  # Tenta converter para int
    except ValueError:
        try:
            dado1 = float(dado1)  # Tenta converter para float
        except ValueError:
            pass  # Mantém o dado como string

    try:
        dado2 = int(dado2)  # Tenta converter para int
    except ValueError:
        try:
            dado2 = float(dado2)  # Tenta converter para float
        except ValueError:
            pass  # Mantém o dado como string

    if type(dado1) == type(dado2):
        print(f'Os tipos de dados fornecidos são iguais')
    else:
        print("Os tipos de dados fornecidos não são iguais")
    print("----------//----------")

# Exercício 10: Aluguel de carro
def Exercício_10():
    print("O programa irá calcular o valor a ser pago pelo aluguel de um carro\n")
    distancia = float(input("Foram percorridos quantos Km pelo carro: "))
    dias = int(input("Com quantos dias foi alugado o carro: "))
    valor_diaria = 60
    valor_km = 0.15
    valor_total = dias * valor_diaria + distancia * valor_km
    print(f'O valor a ser pago pelo aluguel do carro é R${valor_total}')
    print("----------//----------")
    
# Exercício 11: Cálculo de idade
def Exercicio_11():
    print("O programa irá calcular a idade do usuário em meses, dias, horas, minutos e segundos\n")
    idade = int(input("Digite sua idade: "))
    meses = idade*12
    dias = idade*365
    print(f'Com {idade} anos, você já viveu {meses} meses, já viveu cerca de {dias} dias.0')
    print(f'Além, viveu aproximadamente {dias*24} horas, {dias*24*60} minutos e {dias*24*60*60} segundos')
    print("----------//----------")

# Exercício 12: Prize Poll
def Exercício_12():
    print("O programa irá calcular a divisão de um prêmio em três partes\n")
    prêmio = int(input("Digite o valor total para a premiação: "))
    primeiro = prêmio * 0.46
    segundo = prêmio * 0.32
    terceiro = ((prêmio - primeiro) - segundo)
    print(f'O 1º lugar receberá R${primeiro}\nO 2º Lugar receberá R${segundo}\nO 3º Lugar receberá R${terceiro}')
    print("----------//----------")

# Exercício 13: Conversão de temperatura
def Exercício_13():
    print("O programa realiza a conversão de temperatura de graus Celsius para graus Fahrenheit.\n")
    temperatura = int(input("Digite a temperatura em graus Celsius: "))
    conversão = temperatura * (9 / 5) + 32
    print(f'A conversão de {temperatura}º Celsius em graus Fahrenheit é de {conversão}º')
    print("----------//----------")

# Exercício 14: Média de notas
def Exercício_14():
    print("O programa calcula a média de quatro notas fornecidas pelo usuário.\n")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))
    print(f'A média das quatro notas é {(nota1 + nota2 + nota3 + nota4) / 4}')
    print("----------//----------")

def Exercício_14_2():
    print("O programa calcula a média de quatro notas fornecidas pelo usuário.\n")
    n1, n2, n3, n4 = input("Escreva 4 notas, separadas por vírgula: ").split(",")
    soma = float(n1) + float(n2) + float(n3) + float(n4)
    print(f'A média das quatro notas é {soma / 4}')
    print("----------//----------")

# Exercício 15: Área de parede
def Exercício_15():
    print("O programa calcula a área de uma parede e determina a quantidade de tinta necessária para pintá-la completamente.\n")
    altura, largura = input("Escreva a altura e a largura da parede, separadas por vírgula: ").split(",")
    area = float(altura) * float(largura)
    print(f'Sabendo que um litro de tinta pinta 2m², para que a parede seja totalmente pintada será necessário {area / 2} litros de tinta')
    print("----------//----------")

def Exercício_15_2():
    print("O programa calcula a área de uma parede e determina a quantidade de tinta necessária para pintá-la completamente.\n")
    altura = float(input("Escreva a altura da parede: "))
    largura = float(input("Escreva a largura da parede: "))
    print(f'Sabendo que um litro de tinta pinta 2m², para que a parede seja totalmente pintada será necessário {(largura * altura) / 2} litros de tinta')
    print("----------//----------")


# Executa todas as funções
def ALL():
    Exercício_1()
    Exercício_2()
    Exercício_3()
    Exercício_4()
    Exercício_5()
    Exercício_6()
    Exercício_7()
    Exercício_8()
    Exercício_9()
    Exercício_10()
    Exercicio_11()
    Exercício_12()
    Exercício_13()
    Exercício_14()
    Exercício_14_2()
    Exercício_15()
    Exercício_15_2()


# Execução dos programas
# para executar um programa é necessário somente digitar o nome da função    
# Exemplo:
ALL()