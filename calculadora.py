#CALCULADORA
import math

#operação
print("ESCOLHA A OPERAÇÃO:")
print()
print("+ - soma")
print("- - subtração")
print("* - multiplicação")
print("/ - divisão")
print("% - porcentagem")
print("! - fatorial")
print("&2 - raiz quadrada")
print("&3 - raiz cubica")
print("md - media")
print("p - potencia")
print("r3 - regra de 3")
print("1 - equação de 1° grau")
print("2 - equação de 2° grau")
print("@ - bhaskara")
print("j - juros simples")
print("jc - juros compostos")
print("s2 - sistema linear 2 linhas")
print("s3 - sistema linear 3 linhas")
print("log - logaritmo")
print("trig - seno, cos, tan")
print("a - area de formas geométricas")
print("v - volume de formas geométricas")
print()
escolha = input("digite sua escolha: ")
print()

if escolha == "+" or escolha == "-" or escolha == "*" or escolha == "md":
    numeros = []
    
    while True:
        n = input("Digite um número (ou 'sair' para parar): ")
        if n.lower() == 'sair':
            break
        try:
            numeros.append(float(n))
        except ValueError:
            print("Por favor, digite um número válido!")
    

    if len(numeros) < 2:
        print("Você precisa de pelo menos 2 números!")
    else:
        if escolha == "+":
            resultado = sum(numeros)  
            print(f"Resultado: {resultado}")

        elif escolha == "-":
            resultado = numeros[0]
            for num in numeros[1:]:
                resultado -= num
            print(f"Resultado: {resultado}")

        elif escolha == "*":
            resultado = 1
            for num in numeros:
                resultado *= num
            print(f"Resultado: {resultado}")
        elif escolha == "md":
            resultado = sum(numeros) / len(numeros)
            print(f"Média: {resultado}")

elif escolha == "/":
    n1 = float(input("escolha um numero: "))
    n2 = float(input("escolha outro numero: "))
    resultado = (n1/n2)
    print(resultado)
    
elif escolha == "%":
    valor = float(input("escolha o valor: "))
    porcentagem = float(input("escolha a porcentagem: "))
    resultado = (valor*porcentagem) / 100
    print(resultado)

elif escolha == "!":
    n = int(input("escolha um numero inteiro: "))
    if n < 0:
        print("Erro: Não existe fatorial de números negativos.")
    else:
        resultado = math.factorial(n)
        print(resultado)

elif escolha == "&2":
    raiz2 = int(input("escolha um numero inteiro: "))
    resultado = raiz2 ** 0.5
    print(resultado)

elif escolha == "&3":
    raiz3 = int(input("escolha um numero inteiro: "))
    resultado = raiz3 ** 1/3
    print(resultado)

elif escolha == "p":
    base = float(input("escolha a base"))
    expoente = float(input("escolha o expoente"))
    resultado = base ** expoente
    print(resultado)

elif escolha == "r3":
    print("Regra de 3: a/b = x/c")
    a = float(input("digite 'a': "))
    b = float(input("digite 'b': "))
    c = float(input("digite 'c': "))
    if b == 0:
        print("Erro: b não pode ser zero!")
    else:
        x = (a * c) / b
        print(f"x = ({a} * {c}) / {b} = {x}")

elif escolha == "1":
    a = float(input("escolha o valor de A: "))
    b = float(input("escolha o valor de B: "))
    c = float(input("escolha o valor de C: "))
    
    if a == 0:
        if b == c:
            print("infinitas soluções")
        else:
            print("Sem solução real")
    else:
        x = (c - b) / a
        print(x)

elif escolha == "@":
    a = float(input("escolha o valor de A: "))
    b = float(input("escolha o valor de B: "))
    c = float(input("escolha o valor de C: "))
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("x1:")
        print(x1)
        print("x2:")
        print(x2)
    elif delta == 0:
        x = -b / (2*a)
        print(x)
    else: 
        print("não existe raiz real")

elif escolha == "2":
    a = float(input("escolha o valor de A: "))
    b = float(input("escolha o valor de B: "))
    c = float(input("escolha o valor de C: "))
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("x1:")
        print(x1)
        print("x2:")
        print(x2)
    elif delta == 0:
        x = -b / (2*a)
        print(x)
    else: 
        print("não existe raiz real")
    
elif escolha == "j":
    c = float(input("digite o valor de capital: "))
    i = float(input("digite o valor de i: "))
    t = float(input("digite o valor de t: "))
    juros = (c*i*t) /100
    print(juros)
    
elif escolha == "jc":
    c = float(input("digite o valor do capital: "))
    i = float(input("digite a taxa de juros: "))
    t = float(input("digite o tempo: "))
    n = int(input("digite o número de períodos por ano: "))
    
    montante = c * (1 + i/(100*n)) ** (n*t)
    print(montante)
    print(montante - c)
    
elif escolha == "s2":
    print("Sistema Linear 2x2:")
    print("a1*x + b1*y = c1")
    print("a2*x + b2*y = c2")
    print("-" * 25)
    
    a1 = float(input("a1: "))
    b1 = float(input("b1: "))
    c1 = float(input("c1: "))
    a2 = float(input("a2: "))
    b2 = float(input("b2: "))
    c2 = float(input("c2: "))
    
    det = a1*b2 - a2*b1
    
    if abs(det) < 1e-10:
        print("sem solução única!")
    else:
        x = (c1*b2 - c2*b1) / det
        y = (a1*c2 - a2*c1) / det
        
        print(f"  x = {x:.6f}")
        print(f"  y = {y:.6f}")
        
elif escolha == "s3":
    try:
        a1 = float(input("a1: "))
        b1 = float(input("b1: "))
        c1 = float(input("c1: "))
        d1 = float(input("d1: "))
        a2 = float(input("a2: "))
        b2 = float(input("b2: "))
        c2 = float(input("c2: "))
        d2 = float(input("d2: "))
        a3 = float(input("a3: "))
        b3 = float(input("b3: "))
        c3 = float(input("c3: "))
        d3 = float(input("d3:"))
        
        det = a1*(b2*c3-b3*c2) - b1*(a2*c3-a3*c2) + c1*(a2*b3-a3*b2)
        
        if abs(det) < 1e-10:
            print("sem solução!")
        else:
            x = (d1*(b2*c3-b3*c2) - b1*(d2*c3-d3*c2) + c1*(d2*b3-d3*b2)) / det
            y = (a1*(d2*c3-d3*c2) - d1*(a2*c3-a3*c2) + c1*(a2*d3-a3*d2)) / det
            z = (a1*(b2*d3-b3*d2) - b1*(a2*d3-a3*d2) + d1*(a2*b3-a3*b2)) / det
            
            print(f"\nx={x:.4f} y={y:.4f} z={z:.4f}")
            
    except ValueError:
        print("digite apenas números!")
    except:
        print("erro no cálculo!")
        
elif escolha == "log":
    print("Logaritmo log_b(x)")
    try:
        x = float(input("x (argumento): "))
        b = float(input("b (base): "))
        
        if x <= 0 or b <= 0 or b == 1:
            print("x > 0 e b > 0 ≠ 1!")
        else:
            resultado = math.log(x, b)
            print("resultado")
            print(resultado)
            
    except:
        print("numeros inválidos!")
        
elif escolha == "trig":
    print("1-Seno  2-Cosseno  3-Tangente")
    op = input("escolha: ")
    
    try:
        angulo = float(input("graus: "))
        rad = math.radians(angulo)
        
        if op == "1":
            print("sin(", angulo, "°) =", math.sin(rad))
        elif op == "2":
            print("cos(", angulo, "°) =", math.cos(rad))
        elif op == "3":
            print("tan(", angulo, "°) =", math.tan(rad))
        else:
            print("sin =", math.sin(rad))
            print("cos =", math.cos(rad))
            print("tan =", math.tan(rad))
            
    except:
        print("deu erro")
        
elif escolha == "a":
    print("1-Quadrado 2-Retângulo 3-Triângulo 4-Trapézio 5-Circulo 6-Losango")
    opp = input("escolha: ")
    
    if opp == "1":
        lado = float(input("qual o tamanho do lado do quadrado? "))
        resultado = print (lado**2)
        print(resultado)
        
    elif opp == "2":
        base = float(input("qual a base do retangulo? "))
        altura = float(input("qual a altura do retangulo? "))
        resultado = print(base * altura)
        print(resultado)
    
    elif opp == "3":
        base = float(input("qual a base do triangulo? "))
        altura = float(input("qual a altura do triangulo? "))
        resultado = (base * altura) / 2  
        print(resultado)

    elif opp == "4":
        base = float(input("qual a base maior do trapezio? "))
        altura = float(input("qual a altura do triapezio? "))
        base2 = float(input("qual a base menor do trapezio? "))
        resultado = ((base + base2) * altura) / 2
        print(resultado)
        
    elif opp == "5":
        raio = float(input("qual o raio do circulo? "))
        resultado = ((raio**2) * 3.14)
        print(resultado)
    
    elif opp == "6":
        diagmaior = float(input("qual a diagonal maior? "))
        diagmenor = float(input("qual a diagonal menor? "))
        resultado = (diagmaior * diagmenor) / 2
        print(resultado)
        
elif escolha == "v":
    print("1-cubo 2-paralelepipedo 3-cone 4-cilindro 5-esfera 6-piramide")
    opp = input("escolha a opção ")
    
    if opp == "1":
        aresta = float(input("qual a aresta do cubo? "))
        resultado = print(aresta**3)
        print(resultado)
        
    elif opp == "2":
        comprimento = float(input("qual o comprimendo? "))
        altura = float(input("qual a altura? "))
        largura = float(input("qual a largura? "))
        resultado = print(comprimento * altura * largura)
        print(resultado)
        
    elif opp == "4":
        altura = float(input("qual a altura? "))
        raio = float(input("qual o raio? "))
        resultado = print(((raio**2) * altura)*3.14)
        print(resultado)
        
    elif opp == "3":
        altura = float(input("qual a altura? "))
        raio = float(input("qual o raio? "))
        resultado = print((((raio**2) * altura)*3.14)/3)
        print(resultado)
        
    elif opp == "5":
        raio = float(input("qual o valor do raio? "))
        resultado = print((((raio**3)*3.14)*4)/3)
        
    elif opp =="6":
        escolha = print("1-base quadrada 2-base retangular 3-base triangular")
        bss = input("escolha: ")
        
        if bss == "1":
            base = float(input("qual o lado da base? "))
            altura = float(input("qual a altura? "))
            base1 = base**2
            resultado = print((base1 * altura)/3)
            print(resultado)
            
        elif bss == "2":
            largura = float(input("qual a largura da base? "))
            comprimento = float(input("qual o comprimento da base? "))
            altura = float(input("qual a altura? "))
            lc = largura*comprimento
            resultado = print((lc*altura)/3)
            print(resultado)
        
        elif bss == "3":
            altura = float(input("Qual a altura? "))
            base = float(input("Qual a base? "))
            
            base1 = (math.sqrt(3) * base**2) / 4
            volume = (base1 * altura) / 3
            print(volume)
#FEITO ATÉ 02/04/2026
        
        
        
        
        
        
        
