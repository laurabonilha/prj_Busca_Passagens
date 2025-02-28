from database import DataBase
from excel import Excel
from web import Web

class AutomationManager:

    def __init__(self):
        self.var_clssExcel = Excel()
        self.var_clssDataBase = DataBase()
        self.var_classWeb = Web()

    def insere_item_fila(self, arg_caminhoPlanilha):
        self.var_clssExcel.excel_ler_planilha(arg_caminhoPlanilha)



manager = AutomationManager()
manager.insere_item_fila(arg_caminhoPlanilha='data\templates\template_excel_input.XLSX')