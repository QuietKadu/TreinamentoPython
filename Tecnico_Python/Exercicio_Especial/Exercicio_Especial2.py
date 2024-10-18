from tkinter import *
from tkinter import messagebox
import openpyxl

saud = 0
nsaud = 0
nuti = 0
nulo = 0

def main_program():
    def get_answers():
        global saud, nsaud, nuti, nulo
        try:
            result = int(answers1.get()) + int(answers2.get()) + int(answers3.get())
        except ValueError:
            result = 0

        if 100 <= result <= 150:
            saud += 1
        elif -30 <= result <= 70:
            nsaud += 1
        elif -150 <= result <= -90:
            nuti += 1
        else:
            nulo += 1

        messagebox.showinfo("Resultado", f"Categoria: {'saudável' if saud > 0 else 'não saudável' if nsaud > 0 else 'meio-termo' if nuti > 0 else 'nulo'}\nResultado: {result}")
        update_excel()

    window = Tk()
    window.geometry("1920x1080")
    window.configure(background="#FFCC66")
    window.title("Grafico")

    answers1 = IntVar()
    answers2 = IntVar()
    answers3 = IntVar()

    question1 = Label(window, text="1 - Quanto tempo você passa utilizando dispositivos eletrônicos (Computador, celular e tablet) por dia?", background="#FFCC66", foreground="#000", font=("Helvetica", 13))
    question1.pack()

    Alternatives1 = Radiobutton(window, text="a) 2 - 3 horas", background="#FFCC66", value=50, variable=answers1, font=("Helvetica", 13))
    Alternatives1.pack()

    Alternatives2 = Radiobutton(window, text="b) Mais de 3 horas", background="#FFCC66", value=10, variable=answers1, font=("Helvetica", 13))
    Alternatives2.pack()

    Alternatives3 = Radiobutton(window, text="c) Não utiliza", background="#FFCC66", value=-50, variable=answers1, font=("Helvetica", 13))
    Alternatives3.pack()

    question2 = Label(window, text="2 - Quanto você fica nas redes sociais?", background="#FFCC66", foreground="#000", font=("Helvetica", 13))
    question2.pack()

    Alternatives4 = Radiobutton(window, text="a) 1 - 2 horas", background="#FFCC66", value=50, variable=answers2, font=("Helvetica", 13))
    Alternatives4.pack()

    Alternatives5 = Radiobutton(window, text="b) Mais de 3 horas", background="#FFCC66", value=10, variable=answers2, font=("Helvetica", 13))
    Alternatives5.pack()

    Alternatives6 = Radiobutton(window, text="c) Não utiliza", background="#FFCC66", value=-50, variable=answers2, font=("Helvetica", 13))
    Alternatives6.pack()

    question3 = Label(window, text="3 - Quanto tempo você faz pausa?", background="#FFCC66", foreground="#000", font=("Helvetica", 13))
    question3.pack()

    Alternatives7 = Radiobutton(window, text="a) 30 - 60 minutos", background="#FFCC66", value=50, variable=answers3, font=("Helvetica", 13))
    Alternatives7.pack()

    Alternatives8 = Radiobutton(window, text="b) Raramente faz pausa", background="#FFCC66", value=10, variable=answers3, font=("Helvetica", 13))
    Alternatives8.pack()

    Alternatives9 = Radiobutton(window, text="c) Não se aplica", background="#FFCC66", value=-50, variable=answers3, font=("Helvetica", 13))
    Alternatives9.pack()

    submit_button = Button(window, text="Enviar resposta", command=get_answers)
    submit_button.place(x=912, y=360, width=100, height=20)

    window.mainloop()

def update_excel():
    global saud, nsaud, nuti, nulo

    try:
        book = openpyxl.load_workbook("Planilha_do_Grafico.xlsx")
        graphic_page = book["Grafico"]
    except FileNotFoundError:
        book = openpyxl.Workbook()
        graphic_page = book.create_sheet("Grafico", 0)
        graphic_page.append(["Saudável", "Não está saudável", "Desinformado", "Meio termo"])

    graphic_page.append([saud, nsaud, nuti, nulo])
    book.save("Planilha_do_Grafico.xlsx")

main_program()
