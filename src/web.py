from botcity.web import WebBot, Browser, By

class Web:
    def __init__(self):
        # Inicializa o BotCity WebBot
        self.bot = WebBot()
        self.bot.headless = False  # True - roda em modo invisível
        self.bot.browser = "chrome"
        self.bot.driver_path = r"C:\chrome_driver\chromedriver.exe"
        

    def busca_passagem_onibus(self, arg_origem, arg_destino, arg_dataInicio, arg_dataFim):
        self.bot.start_browser()
        var_strUrlOnibus = 'https://www.clickbus.com.br/'
        self.bot.navigate_to(var_strUrlOnibus)
        self.bot.maximize_window()
        var_elmBlocoPesquisa = self.bot.find_element(selector='//*[@id="__next"]/div[1]/div[2]/div/div', by=By.XPATH)

        # Aguarda o carregamento do bloco de pesquisa por até 10 segundos
        self.bot.wait_for_element_visibility(element=var_elmBlocoPesquisa, visible=True, waiting_time=10000)

        # Inserindo origem
        var_elmInputOrigem = self.bot.find_element(selector='origin', by=By.ID)
        var_elmInputOrigem.clear()
        var_elmInputOrigem.send_keys(arg_origem)
        # Verificando se há mais de uma correspondência de local
        try:
            var_elmCorrespondencia = self.bot.find_element(selector='//*[@id="place-input-ul"]/a', by=By.XPATH)
            print("O site retornou correspondência para o local de origem. Verificando se há mais de uma")
        except:
            print("Não retornou correspondências do local de origem")



        
        # Inserindo destino
        var_elmInputDestino = self.bot.find_element(selector='destination', by=By.ID)
        var_elmInputDestino.clear()
        var_elmInputDestino.send_keys(arg_destino)

