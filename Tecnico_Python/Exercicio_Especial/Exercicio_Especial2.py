from tkinter import *

def main_program():
    choise = "s"
    quant = 0
    saud = 0
    nsaud = 0
    nuti = 0
    nulo = 0
    while choise == "s" or choise == "S":
        quant = quant + 1
        print("1 - Quanto tempo você passa utilizando dispositivos eletronicos (Computador, celular e tablet) por dia?")
        print("a) 2 - 3 horas\nb) Mais de quatro horas\nc) Não utiliza")
        res1 = input("Selecione a letra correspondente a sua resposta: ")
        while res1 != "a" or res1 != "A" and res1 != "b" or res1 != "B" and res1 != "c" or res1 != "C":
            if res1 == "a" or res1 == "A":
                saud = saud + 1
            elif res1 == "b" or res1 == "B":
                nsaud = nsaud + 1
            elif res1 == "c" or res1 == "C":
                nuti = nuti + 1
            else:
                print("Erro: Digite a letra correta.")
        print("2 - Quanto você fica nas redes sociais?")
        print("a) 1 - 2 horas\nb) Mais de 3 horas\nc) Não utiliza")
        res2 = input("Selecione a letra correspondente a sua resposta")
        while res2 != "a" or res2 != "A" and res2 != "b" or res2 != "B" and res2 != "c" or res2 != "C":
            if res2 == "a" or res2 == "A":
                saud = saud + 1
            elif res2 == "b" or res2 == "B":
                nsaud = nsaud + 1
            elif res2 == "c" or res2 == "C":
                nuti = nuti + 1
            else:
                print("Erro: Digite a letra correta.")
        print("3 - Quanto tempo você faz pausa?")
        print("a) 30 - 60 minutos\nb) Raramente faz pausa\nc) Não se aplica")
        res3 = input("Selecione a letra correspondente a sua resposta")
        while res3 != "a" or res3 != "A" and res3 != "b" or res3 != "B" and res3 != "c" or res3 != "C":
            if res3 == "a" or res3 == "A":
                saud = saud + 1
            elif res3 == "b" or res3 == "B":
                nsaud = nsaud + 1
            elif res3 == "c" or res3 == "C":
                nuti = nuti + 1
            else:
                print("Erro: Digite a letra correta.")
        if saud > nsaud and saud > nuti:
            print("Você utiliza de forma saudavel")
        elif nsaud > saud and nsaud > nuti:
            print("Você não utiliza de forma saudavel")
        elif nuti > saud and nuti > nsaud:
            print("Você é uma pessoa desinformada")
        else:
            nulo = nulo + 1
            print("Você utiliza de forna netra")
        choise = input("Deseja continuar? [S/N]: ")


window = Tk()
window.geometry("1920x1080")
window.configure(background="#503459")
window.title("Grafico")
question1 = Label(window, text="1 - Quanto tempo você passa utilizando dispositivos eletronicos (Computador, celular e tablet) por dia?", background="#503459", foreground="#Ffffff")
question1.pack()

answers1 = Radiobutton(window, text="a) 2 - 3 horas", background="#503459", foreground="#Ffffff", value="f")
answers1.pack()


window.mainloop()
