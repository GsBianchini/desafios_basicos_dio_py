#Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
#A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.
#Imprima o nome do animal correspondente à entrada fornecida.

a = input() 
b = input() 
c = input() 

if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro":
            animal = "aguia"
        elif c == "onivoro":
            animal = "pomba"
    elif b == "mamifero":
        if c == "onivoro":
            animal = "homem"
        elif c == "herbivoro":
            animal = "vaca"
elif a == "invertebrado":
    if b == "inseto":
        if c == "hematofago":
            animal = "pulga"
        elif c == "herbivoro":
            animal = "lagarta"
    elif b == "anelideo":
        if c == "hematofago":
            animal = "sanguessuga"
        elif c == "onivoro":
            animal = "minhoca"


print(animal)

#este desafio também pode ser feito em forma de dicionário, porém, entreguei desta forma.