#Importando a classe Usuario do módulo usuario.py
from usuario import Usuario

#Classe UsuarioService
#Lida com a lógica de negócios relacionada aos usuários

class UsuarioService:
    def __init__(self):
        self.usuarios = []
    
#Cria um novo usuário
    def criar_usuario(self, nome, email, idade):
        usuario = Usuario(nome.lower(), email.lower(), idade)
        self.usuarios.append(usuario)
        

#Mostra todos os usuários cadastrados
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome}, Email: {usuario.email}, Idade: {usuario.idade}")

#Busca um usuário pelo nome
    def buscar_usuario_por_nome(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                print(f"Usuário encontrado: Nome: {usuario.nome}, Email: {usuario.email}, Idade: {usuario.idade}")
                return usuario
        print("Usuário não encontrado.")
        return None