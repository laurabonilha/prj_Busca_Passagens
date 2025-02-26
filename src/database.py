import sqlite3

class DataBase:
    def __init__(self, arg_caminhoDB='data/fila.db'):
        self.arg_caminhoDB = arg_caminhoDB

    def cria_tabela(self):
        # Cria a tabela se ainda não existir
        var_dbConexao = sqlite3.connect(self.arg_caminhoDB)
        var_dbCursor = var_dbConexao.cursor()
        var_dbCursor.execute("""
            CREATE TABLE IF NOT EXISTS fila (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origem TEXT,
                destino TEXT,
                data_chegada TEXT,
                data_saida TEXT,
                status TEXT DEFAULT 'pendente'
            )
        """)
        var_dbConexao.commit()
        var_dbConexao.close()

    def adiciona_item_fila(self, arg_origem, arg_destino, arg_dataInicio, arg_dataFim):
        var_dbConexao = sqlite3.connect(self.arg_caminhoDB)
        var_dbCursor = var_dbConexao.cursor()
        var_dbCursor.execute("INSERT INTO fila_passagens (origem, destino, data_chegada, data_saida) VALUES (?, ?, ?, ?)", 
                       (arg_origem, arg_destino, arg_dataInicio, arg_dataFim))

    def captura_itens_pendentes(self):
        # Obtem os itens pendentes da fila
        var_dbConexao = sqlite3.connect(self.arg_caminhoDB)
        var_dbCursor = var_dbConexao.cursor()
        var_dbCursor.execute("SELECT * FROM fila_passagens WHERE status = 'pendente'")
        var_qtdItensPendentes = var_dbCursor.fetchall()
        var_dbConexao.close
        return var_qtdItensPendentes
    
    def atualiza_item_status(self, var_itemID, var_itemStatus):
        var_dbConexao = sqlite3.connect(self.arg_caminhoDB)
        var_dbCursor = var_dbConexao.cursor()
        var_dbCursor.execute("UPDATE fila_passagens SET status = ? WHERE id = ?", (var_itemStatus, var_itemID))
        var_dbConexao.commit()
        var_dbConexao.close()

    