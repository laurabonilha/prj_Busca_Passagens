import pandas as pd
class Excel:
    def __init__(self):
        pass
        
    def excel_ler_planilha(self, arg_caminhoPlanilha):
        # Lê uma planilha de Excel e retorna um DataFrame
        self.var_strCaminhoPlanilha = arg_caminhoPlanilha
        var_strLeituraPlanilha = pd.read_excel(self.var_strCaminhoPlanilha)
        return var_strLeituraPlanilha
    
    def excel_escreve_planilha(self, arg_dataFrame):
        # Escreve os dados de um DataFrame em uma planilha de excel
        var_dfResultadosPassagens = arg_dataFrame
        var_dfResultadosPassagens.to_excel("data/passagens_output.xlsx", index=False)

