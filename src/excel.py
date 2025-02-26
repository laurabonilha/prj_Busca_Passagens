import pandas as pd
class Excel:
    def __init__(self, arg_filePath):
        self.arg_filePath = arg_filePath

    def excel_ler_planilha(self):
        # Lê uma planilha de Excel e retorna um DataFrame
        return pd.read_excel(self.arg_filePath)
    
    def excel_escreve_planilha(self, arg_dataFrame):
        # Escreve os dados de um DataFrame em uma planilha de excel
        arg_dataFrame.to_excel("data/passagens_output.xlsx", index=False)