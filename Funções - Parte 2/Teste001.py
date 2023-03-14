
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: Não Vota'
    elif 16 <= idade < 18 or idade > 65 :
        return f'Com {idade} anos: Voto Opicional'
    else:
        return f'Com {idade} anos: Voto Obrigatorio'


ano = int(input('Digite o ano que você nasceu: '))
print(voto(ano))
