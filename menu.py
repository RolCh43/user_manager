#Importando a classe UsuarioService do módulo usuario_service.py.
from usuario_service import UsuarioService


#Inicializando a classe UsuarioService.
class Menu :
    def __init__(self):
        # Importando a classe UsuarioService.
        self.usuario_service = UsuarioService()
        # Definindo o estado de execução do menu, através de um atributo que controla o loop.
        self.running = True
        # Definindo um dicionário de opções, onde cada chave é um número e o valor é o método correspondente.
        self.opcoes = {
            1: ("Criar usuário", self.opcao_criar_usuario),
            2: ("Mostrar usuários", self.opcao_mostrar_usuarios),
            3: ("Buscar usuário por nome", self.opcao_buscar_usuario_por_nome),
            4: ("Sair", self.opcao_sair)
        }

#   Método que exibe o menu de opções.
#   Ele itera sobre o dicionário de opções e imprime cada uma delas.
#   O método é chamado no loop do menu para mostrar as opções disponíveis ao usuário.
 
    def exibir_menu(self):
        print("\nMenu:")
        for key, (descricao, funcao) in self.opcoes.items():
            print(f"{key}. {descricao}")

#   Método que inicia o loop do menu.
#   Ele exibe o menu e aguarda a entrada do usuário.
    def iniciar(self):
        while self.running:
            self.exibir_menu()
            try:
                op = int(input("Escolha uma opção: "))
                self.executar_opcao(op)
            except ValueError:
                print("Caractere inválido. Por favor, insira um número.")
                continue

    #Métodos que correspondem às opções do menu.
    # Cada método chama um método correspondente na classe UsuarioService.
    # Cria um novo usuário- solicitando ao usuário nome, email e idade- chamando o método correspondente na classe UsuarioService.
    def opcao_criar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        self.usuario_service.criar_usuario(nome, email, idade)
        print(f"Usuário {nome} criado com sucesso!")
    
    #Mostra todos os usuários cadastrados, chamando o método correspondente na classe UsuarioService.
    def opcao_mostrar_usuarios(self):
        self.usuario_service.mostrar_usuarios()
        
    
    #Busca um usuário pelo nome, chamando o método correspondente na classe UsuarioService.
    def opcao_buscar_usuario_por_nome(self):
        nome = input("Digite o nome do usuário a buscar: ")
        self.usuario_service.buscar_usuario_por_nome(nome)

    #Método que encerra o loop do menu e exibe uma mensagem de despedida.
    # Ele altera o estado de execução do menu para False, fazendo com que o loop termine.
    def opcao_sair(self):
        print("Nos vemos em breve!")
        self.running = False
        
    # Método que executa a opção escolhida pelo usuário.
    # Ele verifica se a opção é válida no dicionário e chama o método correspondente.
    # Se a opção não for válida, exibe uma mensagem de erro.
    def executar_opcao(self, op):
        opcao = self.opcoes.get(op)
        if opcao:
            descricao, funcao = opcao
            funcao()
           
        else:
            print("Opção inválida. Tente novamente.")     