from categoria import categorias
from mensagens import mensagens

# Função para exibir a solução do problema
def exibir_solucao(tarefa):
    for nome_array, lista in categorias.items():
        if tarefa in lista:
            print(f"A possível solução do problema é: {nome_array}")
            print(mensagens[nome_array])  # Chamando a mensagem correspondente
            return
    print("Tarefa não encontrada em nenhum array.")
