from bson.objectid import ObjectId
from pydantic import BaseModel


class Tarefa(BaseModel):
    id: int | None | str
    descricao: str
    responsavel: str | None
    nivel: int
    prioridade: int
    situacao: str 


    class Config:
        orm_mode = True

    @classmethod
    def fromDict(cls, tarefa):
        tarefa_ = Tarefa(id=str(tarefa['_id']),
                       descricao=tarefa['descricao'],
                       responsavel=tarefa['responsavel'],
                       nivel=tarefa['nivel'],
                       prioridade=tarefa['prioridade'],
                       situacao=tarefa['situacao'])
        return tarefa_

    def toDict(self):
        return {
            "descricao": self.descricao,
            "responsavel": self.responsavel,
            "nivel": self.nivel,
            "prioridade": self.prioridade,
            "situacao" : self.situacao
        }


class User(BaseModel):
    id: int | None
    nome: str
    email: str
    senha: str
