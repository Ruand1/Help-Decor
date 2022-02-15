# ----- Importando bibliotecas
from HelpDecor import*

arq = 'cadastrocliente.txt'
arq2 = 'cadastrofestas.txt'
arq3 = 'cadastropecas.txt'

# ----- Programa principal
# --- Tela Carregamento
carregamento('HELP DECOR')

# --- Inicio da AI(Ambrósio)
#inteligencia1('HELP DECOR') ------------------------------------------------------------------ INCLUIR PÓS TESTES

# --- Loop Menu
while True:
    menu(['Cadastro de Clientes', 'Cadastro Festas', 'Cadastro Peças de Decoração', 'Sair'])

    num = validaint(4, 'Escolha uma opção:')  # <-------- num recebe função de validação da opção escolhida

    #inteligencia2(num, menu, 'HELP DECOR') ----------------------------------------------------INCLUIR PÓS TESTES

# --- Cadastro Clientes
    if num == 1:
        while True:
            cliente = cadastrocliente()  #<----- função para cadastro e ver clientes
            if cliente == 1:
                if not arquivoExiste(arq):
                    criararquivo(arq)
                nomecliente=str(input('Nome do cliente:')).strip().capitalize()
                sleep(0.5)
                telefone=int(input('Telefone do cliente:'))
                sleep(0.5)
                endereco=str(input('Endereço do cliente:')).strip().capitalize()
                cadastrar(arq, nomecliente, telefone, endereco)
            elif cliente == 2:
                try:
                    sleep(0.5)
                    linhasepara('HELP DECOR')
                    vercliente(arq)
                except IndexError:
                    print(colored('Ops... Ainda não temos clientes cadastradas(os)...', 'magenta'))
                    linhasepara('Help Decor')
            elif cliente == 3:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    pesquisacliente(arq)
                except IndexError:
                    print(colored('Ops... Ainda não temos clientes cadastradas(os)...', 'magenta'))
                    linhasepara('Help Decor')
            else:
                print(colored('Voltando....', 'magenta'))
                linhasepara('Help Decor')
                break
# --- Cadastro Festas
    if num == 2:
        while True:
            festas = cadastrofestas()  #<----- função para cadastro e ver festas
            if festas == 1:
                if not arquivoExiste(arq2):
                    criararquivo(arq2)
                nomecliente=str(input('Nome do cliente:')).strip().capitalize()
                sleep(0.5)
                tema = str(input('Tema da festa:')).strip().capitalize()
                sleep(0.5)
                data = str(input('Data da festa:')).strip()
                sleep(0.5)
                cadastrarfesta(arq2, nomecliente, tema, data)
            elif festas == 2:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    verfestas(arq2)
                except IndexError:
                    print(colored('Ops... Ainda não temos festas cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif festas == 3:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    pesquisafestas(arq2)
                except IndexError:
                    print(colored('Ops... Ainda não temos festas cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            else:
                print(colored('Voltando....', 'magenta'))
                linhasepara('Help Decor')
                break
# --- Cadastro Peças Decoração
    if num == 3:
        while True:
            pecas = cadastropecas()  #<----- função para cadastro e ver peças
            if pecas == 1:
                if not arquivoExiste(arq3):
                    criararquivo(arq3)
                tipo = str(input('Tipo de peça:')).strip().capitalize()
                sleep(0.5)
                cor = str(input('Cor da peça:')).strip().capitalize()
                sleep(0.5)
                tamanho = str(input('Tamanho da peça:')).strip().capitalize()
                sleep(0.5)
                composicao = str(input('Material da peça:')).strip().capitalize()
                sleep(0.5)
                quantidade = int(input('Quantidade de peças:'))
                sleep(0.5)
                id = validaint(200, 'ID da Decor:')
                cadastrarpeca(arq3, tipo, cor, tamanho, composicao, quantidade, id)
            elif pecas == 2:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    verpecas(arq3)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif pecas == 3:  #<--- V1.0.1 - Incluído módulo de pesquisa - funcionando ok
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    pesquisapecas(arq3)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif pecas == 4:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    editarpecas(arq3)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif pecas == 5:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    excluirpecas(arq3)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
            else:
                print(colored('Voltando...', 'magenta'))
                linhasepara('Help Decor')
                break
# --- Sair
    if num == 4:
        print(colored('Volte sempre que precisar...', 'magenta'))
        break





# --------------- Incluir módulo de locação
# --------------- transformar feminimo em masculino .replace('','')
# --------------- fazer validação int para quantidade de peça2