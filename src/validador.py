from pydantic import BaseModel, Field, field_validator
from typing import Optional


class SegmentacaoEnum(str):
    FULL = "Full"
    RMKT_ALL_90DIAS = "Rmkt_All_90dias"
    INTERESSES_FERRAMENTAS = "Interesses em Ferramentas e Tecnologias em Dados"
    LOOKALIKE_COMPRADORES_1 = "Lookalike_Compradores_1"
    INTERESSE_DADOS = "Interesse_Dados"
    CARGO_DADOS = "Cargo_Dados"

    @classmethod
    def values(cls):
        return {cls.FULL, cls.RMKT_ALL_90DIAS, cls.INTERESSES_FERRAMENTAS, cls.LOOKALIKE_COMPRADORES_1, cls.INTERESSE_DADOS, cls.CARGO_DADOS}

class User(BaseModel):
    Organizador: int = Field(..., ge=240, le=3532, description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês do registro")
    Dia_da_Semana: str = Field(..., description="Dia da semana correspondente à data")
    Tipo_Dia: str = Field(..., description="Classificação do dia: útil, feriado, etc.")
    Objetivo: str = Field(..., description="Objetivo da campanha ou ação")
    Date: str = Field(..., description="Data da entrada no formato YYYY-MM-DD")
    AdSet_name: Optional[str] = Field(None, description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(0.0, ge=0, le=600 , description="Valor gasto no anúncio")
    Link_clicks: Optional[int] = Field(None, ge=0, le=394, description="Número de cliques no link")
    Impressions: int = Field(0, ge=0, le=50782, description="Número de impressões do anúncio")
    Conversions: Optional[int] = Field(None, ge=1, le=361, description="Número de conversões registradas")
    Segmentacao: str = Field(..., description="Segmentação usada no anúncio")
    Tipo_de_Anuncio: str = Field(..., description="Tipo do anúncio")
    Fase: str = Field(..., description="Fase da campanha")

    @field_validator('Segmentacao')
    def validate_segmentacao(cls, value):
        if value not in SegmentacaoEnum.values():
            raise ValueError(f"Segmentação inválida: {value}. Valores permitidos: {SegmentacaoEnum.values()}")
        return value