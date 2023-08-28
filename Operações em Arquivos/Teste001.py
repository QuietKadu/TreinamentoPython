nome = "Teste.txt"
f = open("C:/Python/Aulas/Aula46/" + nome, "at")
#r - read - Leitura
#a - append - Anexar
#w - write - Escrita
#x - create - Criar
#t - texto
#b - binário

txt = input("Digite um texto: ")
f.write(txt + "\n")




f.close()
