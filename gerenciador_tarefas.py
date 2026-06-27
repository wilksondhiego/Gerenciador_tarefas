from datetime import datetime


class Tarefa:
    def __init__(self, id, titulo, descricao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = "pendente"
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")

    def mostrar(self):

        print("ID:", self.id)
        print("Titulo:", self.titulo)
        print("Descricao:", self.descricao)
        print("Status:", self.status)
        print("Criada em:", self.data_criacao)
  

class GerenciadorDeTarefas:
    def __init__(self):
        self.lista_de_tarefas = []
        self.proximo_id = 1

    def criar_tarefa(self, titulo, descricao):
        nova_tarefa = Tarefa(self.proximo_id, titulo, descricao)
        self.lista_de_tarefas.append(nova_tarefa)
        self.proximo_id += 1
        print("Tarefa criada com sucesso!")

    def listar_tarefas(self):
        if len(self.lista_de_tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\ Lista de Tarefas")
            for tarefa in self.lista_de_tarefas:
                tarefa.mostrar()

    def buscar_tarefa(self, id):
        for tarefa in self.lista_de_tarefas:
            if tarefa.id == id:
                return tarefa
        return None

    def atualizar_tarefa(self, id, novo_titulo, nova_descricao, novo_status):
        tarefa = self.buscar_tarefa(id)
        if tarefa == None:
            print("Tarefa nao encontrada.")
        else:
            if novo_titulo != "":
                tarefa.titulo = novo_titulo
            if nova_descricao != "":
                tarefa.descricao = nova_descricao
            if novo_status != "":
                tarefa.status = novo_status
            print("Tarefa atualizada com sucesso!")

    def excluir_tarefa(self, id):
        tarefa = self.buscar_tarefa(id)
        if tarefa == None:
            print("Tarefa nao encontrada.")
        else:
            self.lista_de_tarefas.remove(tarefa)
            print("Tarefa excluida com sucesso!")



gerenciador = GerenciadorDeTarefas()

while True:
    print("\n Menu ")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        titulo = input("Digite o titulo: ")
        descricao = input("Digite a descricao: ")
        gerenciador.criar_tarefa(titulo, descricao)

    elif opcao == "2":
        gerenciador.listar_tarefas()

    elif opcao == "3":
        id = int(input("Digite o ID da tarefa: "))
        novo_titulo = input("Novo titulo (deixe vazio para nao alterar): ")
        nova_descricao = input("Nova descricao (deixe vazio para nao alterar): ")
        novo_status = input("Novo status - pendente ou concluido (deixe vazio para nao alterar): ")
        gerenciador.atualizar_tarefa(id, novo_titulo, nova_descricao, novo_status)

    elif opcao == "4":
        id = int(input("Digite o ID da tarefa: "))
        gerenciador.excluir_tarefa(id)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida.")
