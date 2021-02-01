import requests
from bs4 import BeautifulSoup


class MercadoLivreImg:
    def __init__(self, url):
        self.url = url
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, 'html.parser')


class DownloadImagens(MercadoLivreImg):

    def efetuar_download(self):
        self.buscar_imagem = self.soup.find_all(
            'div', {'class': 'slick-slide slick-active'})
        self.cont = 0
        try:
            for self.buscar_imagens in self.buscar_imagem:
                self.cont += 1
                img = self.buscar_imagens.find('img')
                imagens = img['data-src']

                with open(f'Imagens_salvas/imagem{self.cont}.jpg', 'wb') as self.minhas_imagens:
                    self.resposta = requests.get(f'{imagens}', stream=True)
                    self.minhas_imagens.write(self.resposta.content)
            if self.minhas_imagens:
                print('downloads efetuados com sucesso!!!')
        except:
            print('Não foi possivel efetuar os downloads')


url = 'https://lista.mercadolivre.com.br/notebook#D[A:notebook]'

mercado_livre = MercadoLivreImg(url)
baixar_imagens = DownloadImagens(url)
baixar_imagens.efetuar_download()
