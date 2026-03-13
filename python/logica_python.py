# Criando variáveis

nome = 'Esther'
sobrenome = 'Soares'
idade = 20
altura = 1.66
adulto = True 

# Escrevendo no console.
print(nome)
print(idade)
print(altura)
print(adulto)

# Concatenando informações.
print('Meu nome é', nome)
print('Meu sobrenome é ' + sobrenome)
print('Meu nome completo é',nome,sobrenome)

# Maneira moderna de concatenar.
print(f'Meu nome é {nome} e tenho {idade} de idade')

# Verificando o tipo da variável.
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))

# Expressões númericas.

numero = 10
numero2 = 5

soma = numero + numero2
sub = numero - numero2
mult = numero * numero2
div = numero / numero2

print(f'A soma é {soma}')
print(f'A sub é {sub}')
print(f'A mult é {mult}')
print(f'A div é {div}')

expressao = numero + (numero2 * numero2) - numero
print(expressao)

# Outras operações.
potencia = numero**2
print(potencia)