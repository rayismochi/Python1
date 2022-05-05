## Dados 
nome = input("Qual seu nome?")                                                  ## Insere o dado Nome
anoN = int(input("Qual o seu ano de nascimento?"))                              ## Insere o dado Ano de Nascimento
val1 = int(input("Insira um valor:"))                                           ## Insere o dado Valor 1
val2 = int(input("Agora, insira um segundo valor:"))                            ## Insere o dado Valor 2


## Cálculos

anoSoma = (anoN + 2022)                                                         ## Calcula a soma do Ano de Nascimento + Ano Atual
idade = (2022 - anoN)                                                           ## Calcula a Idade
valsoma = (val1 + val2)                                                         ## Calcula a soma dos Valores solicitados
valmult = (val1 * val2)                                                         ## Calcula a multiplicação dos Valores solicitados
valdiv = (val1 / val2)                                                          ## Calcula a divisão dos Valores solicitados
complexosoma = 20 + 10 + 15
complexodivisao = complexosoma / 2


## Resultados
print("Olá, ", nome)                                                            ## Dá o resultado do nome
print("Sua idade é:", idade)                                                    ## Dá o resultado da idade
print("Seu ano de nascimento somado ao ano corrente é:", anoSoma)               ## Dá o resultado da soma do ano de nascimento e ano atual
print("A soma dos valores é:", valsoma)                                         ## Dá o resultado da soma dos valores
print("A multiplicação dos valores é:", valmult)                                ## Dá o resultado da multiplicação dos valores
print("A divisão dos valores é:", valdiv)                                       ## Dá o resultado da divisão dos valores

print("Maria foi á feira á pedido de sua mãe, com uma lista de compras em mãos. Na lista, haviam os seguintes pedidos: \n10 maçãs \n6 bananas \n10 limões.")
print("Sabendo disso, Maria foi ás lojas e fez as compras, \nas maçãs custaram R$20, \na banana R$10 e \nos limões R$15.")
print("Ao chegar em casa, a mãe de Maria pediu que ela realizasse a soma do valor total e também dividisse por dois para que seu pai pagasse metade.")
print("Então, Maria pegou o papel e fez a conta do valor total, sendo: 20 + 10 +15 \nque somados deram R$", complexosoma)
print("E a divisão ela fez pegando este resultado e dividindo por dois, sendo: 45/2 \nque divididos deram: \n=", complexodivisao)
                                                                                ## Dá o problema e a resolução
