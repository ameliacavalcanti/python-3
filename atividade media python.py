#Media Aluno Paulino

print("Entre com as notas do aluno Paulino: ")
n1=int(input("\033[1;30;107mEntre com a nota 1: \033[m"))
n2=int(input("\033[1;34;107mEntre com a nota 2: \033[m"))
n3=int(input("\033[1;35;107mEntre com a nota 3: \033[m"))
media=(float(n1+n2+n3)/3)

if media > 6:
    print(f"\033[4;32mAluno Aprovado. A média foi de {media:,.2f}\033[m")
else:
    print(f"\033[4;31mAluno reprovado. A média foi de {media:,.2f}\033[m")
