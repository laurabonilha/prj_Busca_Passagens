from botcity.web import WebBot, Browser, By

class Web:
    def __init__(self):
        # Inicializa o BotCity WebBot
        self.bot = WebBot()
        self.bot.headless = False  # True - roda em modo invisível
        self.bot.browser = "chrome"
        self.bot.start_browser()