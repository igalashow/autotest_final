class BasePage():
    """ Класс базовой страницы """
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """ Открывает страницу в браузере """
        self.browser.get(self.url)
