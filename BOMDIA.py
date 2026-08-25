#Exercício 1
print("Henrique me da um pastel de queijo e um suco de laranja.")

nome: str = "Arthur"
print(f"Meu nome é {nome}.")

sobrenome: str = "Oliveira"
print(f"Meu sobrenome é {sobrenome}.")

Profissao: str = "Vendedor"
print(f"Minha profissão é {Profissao}.")

#Exercício 2
numero_a: float = float(input("Digite um número: "))
numero_b: float = float(input("Digite outro número: "))

soma: float = numero_a + numero_b
subtracao: float = numero_a - numero_b
multiplicacao: float = numero_a * numero_b

if numero_b == 0:
    divisao: str = "indefinida (não é possível dividir por zero)"
else:
    divisao: str = str(numero_a / numero_b)

print(
    f"\nResultados para {numero_a} e {numero_b}:\n"
    f"Soma: {soma}\n"
    f"Subtração: {subtracao}\n"
    f"Multiplicação: {multiplicacao}\n"
    f"Divisão: {divisao}"
)

#Exercício 3
def celsius_para_fahrenheit(temperatura: float) -> float:
    return temperatura * 9 / 5 + 32


temperatura_celsius: float = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit: float = celsius_para_fahrenheit(temperatura_celsius)

print(
    f"{temperatura_celsius:.2f} graus Celsius equivalem a "
    f"{temperatura_fahrenheit:.2f} graus Fahrenheit."
)

