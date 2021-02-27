from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui


class WhatsappBot:
    def __init__(self):
        options = ChromeOptions()
        options.headless = True
        options.add_argument('lang=pt-br')
        self.driver = Chrome(
            executable_path='./driver/chromedriver')
        self.driver.maximize_window()
        self.driver.get('https://web.whatsapp.com/')
        sleep(30)

    def selecionar_elemento(self, usuario):
        pesquisa = By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]'
        anexo = By.XPATH, '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span'
        imagem = By.XPATH, '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span'

        self.driver.find_element(*pesquisa).send_keys(usuario)
        sleep(2)
        self.driver.find_element_by_xpath(
            f"//span[@title='{usuario}']").click()
        sleep(3)
        self.driver.find_element(*anexo).click()
        sleep(5)
        self.driver.find_element(*imagem).click()
        sleep(2)
        pyautogui.click(753, 960)
        sleep(2)
        pyautogui.click(403, 445)
        sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        sleep(2)
        pyautogui.click(1520, 206)
        sleep(3)

    def enviar_fotos(self):
        fotos = By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div'
        self.driver.find_element(*fotos).click()
        sleep(5)


if __name__ == '__main__':
    usuario = ['Amor', 'Rosane', 'Deivisin Verdadeiro',
               'Zebuteco', 'Zebuteca Elenice']
    bot = WhatsappBot()
    for usuarios in usuario:
        bot.selecionar_elemento(usuarios)
        bot.enviar_fotos()
