from database import DataBase
from excel import Excel
from web import Web
import pandas as pd

class AutomationManager:

    def __init__(self):
        self.var_clssExcel = Excel()
        self.var_clssDataBase = DataBase()
        self.var_classWeb = Web()

    def insere_item_fila(self, arg_caminhoPlanilha):
        var_itensInserirFila = self.var_clssExcel.excel_ler_planilha(arg_caminhoPlanilha)
        print(var_itensInserirFila.columns)
        for _, row in var_itensInserirFila.iterrows(): # Ignorando o índice
            var_strOrigem = str(row["Origem"]) if pd.notna(row["Origem"]) else ""
            var_strDestino = str(row["Destino"]) if pd.notna(row["Destino"]) else ""
    
            # Convertendo as datas para o formato ISO
            var_dtInicio = pd.to_datetime(row["Data início"], format="%d/%m/%Y").strftime("%d-%m-%Y") if pd.notna(row["Data início"]) else ""
            var_dtFinal = pd.to_datetime(row["Data final"], format="%d/%m/%Y").strftime("%d-%m-%Y") if pd.notna(row["Data final"]) else ""
    
            var_strTipoPassagem = str(row["Tipo passagem"]) if pd.notna(row["Tipo passagem"]) else ""

            self.var_clssDataBase.adiciona_item_fila(var_strOrigem, var_strDestino, var_dtInicio, var_dtFinal, var_strTipoPassagem)
    
    def process(self):
        var_itensProcess = self.var_clssDataBase.captura_itens_pendentes()
        var_resultadoItensProcess = []

        for item in var_resultadoItensProcess:
            pass
