senh = "l"
confirm = "m"
menu = int
opc = "S"
print("=" * 35)
print("MONITORAMENTO DE QUALIDADE DO AR")
print("=" * 35)
print("Ola seja bem vindo!!\n")
while confirm != senh:
    senh = input("Digite sua senha: ")
    confirm = input("Confirme sua senha: ")
    if confirm != senh:
        print("\nSenha incorreta, insira novamente\n")
print("\nSenha correta!\n")
while menu != 1 and menu != 2 and menu != 3:
    print("1 - Calcular\n2 - Sobre\n3 - Sair")
    menu = int(input("Digite a opção que você deseja: "))
    if menu != 1 and menu != 2 and menu != 3:
        print("\nOpção incorreta, digite novamente\n")
if menu == 1:
    while opc == "S" or opc == "s":
        Is = float(input("\nDigite o ISup(valor critico superior do indice): "))
        In = float(input("Digite o IInf(valor critico inferior do indice): "))
        Cs = float(input("Digite o concentracao do poluente que corresponde ao CInf(a concentracao do poluente que corresponde ao ISup): "))
        Ci = float(input("Digite a concentracao do poluente que corresponde ao Cc(a concentracao do poluente que corresponde ao IInf): "))
        Cc = float(input("Digite a concentracao medida para o poluente em questao: "))
        iqar = (Is - In) / (Cs - Ci) * (Cc - Ci) + In
        if iqar <= 50:
            print("\nA qualidade do ar está no nivel [BOA]")
            print("Descricao: Nao ha praticamente risco a saude.")
        elif iqar >= 51 and iqar <= 100:
            print("\nA qualidade do ar está no nivel [REGULAR]")
            print("Descricao: Pessoas de grupos sensiveis (criancas, idosos e pessoas com doencas respiratorias e cardiacas), podem apresentar sintomas como tosse seca cansaco. A populacao, em geral, nao e afetada.")
        elif iqar >= 101 and iqar <= 199:
            print("\nA qualidade do ar está no nivel [INADEQUADA]")
            print("[ALERTA!!! RISCO ALTO]")
            print("Descricao: Toda a populacao pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensiveis (criancas, idosos e pessoas com doencas respiratorias e cardiacas), podem apresentar efeitos mais serios na saude.")
        elif iqar >= 200 and iqar <= 299:
            print("\nA qualidade do ar está no nivel [MA]")
            print("[ALERTA!!! RISCO ALTO]")
            print("Descricao: Toda a populacao pode apresentar agravamento dos sintomas como tosse seca, cansaco, ardor nos olhos, nariz e garganta e ainda apresentar falta de ar e respiracao ofegante. Efeitos ainda mais graves a saude de grupos sensiveis (criancas, idosos e pessoas com problemas cardiovasculares).")
        elif iqar >= 300 and iqar <= 399:
            print("\nA qualidade do ar está no nivel [PESSIMO]")
            print("[ALERTA EMERGENCIAL!!! RISCO MUITO ALTO]")
            print("Descricao: Toda a populacao pode apresentar serios riscos de manifestacoes de doencas respiratorias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensiveis.")
        else:
            print("\nA qualidade do ar está no nivel [CRITICA]")
            print("[ALERTA EMERGENCIAL!!! RISCO MUITO ALTO]")
            print("Descricao: Toda a populacao pode apresentar serios riscos de manifestacoes de doencas respiratorias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensiveis.")
        opc = str(input("\nDeseja continuar? [S/N]: "))
elif menu == 2:
    print("\nO indice de qualidade do ar nos permite entender os niveis de poluicao atmosferica concentrada em ambientes internos e  externos e as propriedades que tornam o ar improprio e ofensivo a saude e ao meio ambiente. Nosso projeto concente em   criar um programa que calcule a qualidade do ar em todos os lugares.")
else:
    print("\nPrograma finalizando......")
print("\nPrograma Finalizado.")
