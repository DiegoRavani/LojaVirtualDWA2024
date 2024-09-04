from pydantic import BaseModel, field_validator

from util.validators import *


class AlterarProdutoDTO(BaseModel):
    nome: str
    preco: float
    descricao: str
    estoque: int

    @field_validator("id")
    def validar_id(cls, v):
        msg = is_greater_than(v, "id", 0)
        if msg: raise ValueError(msg)
        return v

    @field_validator("preco")
    def validar_preco(cls, v):
        msg = is_in_range(v, "Preço", 0.0, 100000.0)
        if msg:
            raise ValueError(msg)
        return v

    @field_validator("descricao")
    def validar_descricao(cls, v):
        msg = is_not_empty(v, "Descricao")
        if not msg:
            msg = is_not_empty(v, "Descricao", 16)
        if msg:
            raise ValueError(msg)
        return v

    @field_validator("estoque")
    def validar_estoque(cls, v):
        msg = is_in_range(v, "Estoque", 0, 1000)
        if msg:
            raise ValueError(msg)
        return v