from tkinter import *
import openpyxl

def main_program():
    window = Tk()
    window.geometry("1920x1080")
    window.configure(background="#FFCC66")
    window.title("Grafico")

    answers1 = StringVar()
    answers2 = StringVar()
    answers3 = StringVar()

    question1 = Label(window, text="1 - Quanto tempo você passa utilizando dispositivos eletronicos (Computador, celular e tablet) por dia?", background="#FFCC66", foreground="#000", font=("Helvetica", 13))
    question1.pack()

    Alternatives1 = Radiobutton(window, text="a) 2 - 3 horas", background="#FFCC66", value="a", variable=answers1, font=("Helvetica", 13))
    Alternatives1.pack()

    Alternatives2 = Radiobutton(window, text="Mais de 3 horas", background="#FFCC66", value="b", variable=answers1, font=("Helvetica", 13))
    Alternatives2.pack()

    Alternatives3 = Radiobutton(window, text="c) Não utiliza", background="#FFCC66", value="c", variable=answers1, font=("Helvetica", 13))
    Alternatives3.pack()

    question2 = Label(window, text="2 - Quanto você fica nas redes sociais?", background="#FFCC66", foreground="#000", font=("Helvetica", 13))
    question2.pack()

    Alternatives4 = Radiobutton(window, text="a) 1 - 2 horas", background="#FFCC66", value="d", variable=answers2, font=("Helvetica", 13))
    Alternatives4.pack()

    Alternatives5 = Radiobutton(window, text="b) Mais de 3 horas", background="#FFCC66", value="e", variable=answers2, font=("Helvetica", 13))
    Alternatives5.pack()

    Alternatives6 = Radiobutton(window, text="c) Não utiliza", background="#FFCC66", value="f", variable=answers2, font=("Helvetica", 13))
    Alternatives6.pack()

    question3 = Label(window, text="3 - Quanto tempo você faz pausa?", background="#FFCC66", foreground="#000", font=("Helvetica", 13))
    question3.pack()

    Alternatives7 = Radiobutton(window, text="a) 30 - 60 minutos", background="#FFCC66", value="g", variable=answers3, font=("Helvetica", 13))
    Alternatives7.pack()

    Alternatives8 = Radiobutton(window, text="b) Raramente faz pausa", background="#FFCC66", value="", variable=answers3, font=("Helvetica", 13))
    Alternatives8.pack()

    Alternatives9 = Radiobutton(window, text="Não se aplica", background="#FFCC66", value="i", variable=answers3,font=("Helvetica", 13))
    Alternatives9.pack()

    Button(window, text="Enviar resposta").place(x=912, y=360, width=100, height=20)



    window.mainloop()


def exel():
    book = openpyxl.workbook()
    book.create_sheet("Grafico")
    graphic_page = book["Grafico"]



def third_program():
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
