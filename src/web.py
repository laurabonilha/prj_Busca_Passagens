from botcity.web import WebBot, Browser, By

class Web:
    def __init__(self):
        # Inicializa o BotCity WebBot
        self.bot = WebBot()
        self.bot.headless = False  # True - roda em modo invisível
        self.bot.browser = "chrome"
        

    def busca_passagem_onibus(self, arg_origem, arg_destino, arg_dataInicio, arg_dataFim):
        self.bot.start_browser()
        var_strUrlOnibus = 'https://www.clickbus.com.br/'
        self.bot.navigate_to(var_strUrlOnibus)
        self.bot.maximize_window()
        var_elmBlocoPesquisa = self.bot.find_element(selector='//*[@id="__next"]/div[1]/div[2]/div/div', by=By.XPATH)

        # Aguarda o carregamento do bloco de pesquisa por até 10 segundos
        self.bot.wait_for_element_visibility(element=var_elmBlocoPesquisa, visible=True, waiting_time=10000)

        self.bot.find_element(element='origin', by=By.ID).type(arg_origem)

        self.bot.find_element(element='destination', by=By.ID).type(arg_destino)

