print("Bem-vindo ao jogo do NIM! Escolha:")

def main():
    print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato")
    tipo_jogo=int(input(""))
    if (tipo_jogo==1):
        print("Voce escolheu uma parida isolada!")
        partida(1,0)
    if (tipo_jogo==2):
        print("Voce escolheu um campeonato!")
        partida(1,1)
    else:
        print("Opção inválida!")
        main()

def partida(q,i):
    print("**** Rodada",q,"****")
    n=int(input("Quantas peças?"))
    m=int(input("Limite de peças por jogada?"))
    if n%(m+1)==0:
        print("Você começa jogando!")
        usuario_escolhe_jogada(n,m,q,i)
    else:
        print("O computador começa!")
        computador_escolhe_jogada(n,m,q,i)

def usuario_escolhe_jogada(n,m,q,i):
    x=int(input("Quantas peças você tira?"))
    if x>m:
        print("ops! jogada invalida! jogue novamente")
        usuario_escolhe_jogada(n,m,q,i)
    else:
        n=n-x
        print("Agora restam",n, "peça(s) no tabuleiro.")
        computador_escolhe_jogada(n,m,q,i)

def computador_escolhe_jogada(n,m,q,i):
    w=n
    while w%(m+1)!=0:
        w=w-1
    jog_comp=n-w
    n=n-jog_comp
    print("O computador tirou",jog_comp,"peça(s)\nResta(m)", n, "peça(s).")
    if n <= 0:
        n = n + n
        print("Fim do jogo! O computador ganhou!")
        if i==0:
            main()
        q=q+1
        if q>3:
            print("** ** Final do campeonato! ** **\nPlacar: Você 0 x 3 Computador")
            main()
        partida(q,i)
        main()
    usuario_escolhe_jogada(n,m,q,i)

main()