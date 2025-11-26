# av4_sist_gestao_pessoas

API REST para um pequeno sistema de gestão de tarefas de uma equipe.
Duas entidades principais: Projeto e Tarefa.
Cada Projeto pode possuir várias Tarefas (relacionamento 1:N)

Projeto: id, nome, descricao, data_criacao
Tarefa: id, titulo, status, prioridade, data_limite, projeto(FK)
