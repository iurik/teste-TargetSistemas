str = input("Digite alguma palavra: ")

l_str = list(str)
length = len(l_str)

fim = length -1
for i in range(int(length/2)):
    aux = l_str[i]
    l_str[i] = l_str[fim]
    l_str[fim] = aux
    fim -= 1

reverse = ''.join(l_str)
print("Palavra invertida: " , reverse)