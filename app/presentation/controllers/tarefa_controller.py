from fastapi import APIRouter, HTTPException, status

from app.persistence.tarefa_mongodb_repository import TarefaMongoDBRepository
from app.persistence.tarefa_repository import TarefaInMemoryRepository

from ..viewmodels import Tarefa

print('Tarefas Controller <>')
routes = APIRouter()
prefix = '/tarefas'

# Banco de Dados
# filme_repository = FilmeInMemoryRepository()
tarefa_repository = TarefaMongoDBRepository()


@routes.get('/')
def todas_tarefas(skip: int | None = 0, take: int | None = 0):
    return tarefa_repository.todos(skip, take)


@routes.get('/{tarefa_id}')
def obter_tarefa(tarefa_id: int | str):
    tarefa = tarefa_repository.obter_um(tarefa_id)

    # fail fast
    if not tarefa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Essa tarefa com esse ID não existe = {tarefa_id }')

    return tarefa


@routes.post('/', status_code=status.HTTP_201_CREATED)
def nova_tarefa(tarefa: Tarefa):
    return tarefa_repository.salvar(tarefa)


@routes.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_tarefa(tarefa_id: int | str):
    tarefa = tarefa_repository.obter_um(tarefa_id)

    if not tarefa:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Tarefa não encontrada!")

    tarefa_repository.remover(tarefa_id)


@routes.put('/{tarefa_id}')
def atualizar_tarefa(tarefa_id: int | str, tarefa: Tarefa):
    tarefa_encontrada = tarefa_repository.obter_um(tarefa_id)

    if not tarefa_encontrada:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Tarefa não encontrada!")

    return tarefa_repository.atualizar(tarefa_id, tarefa)
