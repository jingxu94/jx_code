import multiprocessing
import requests
from bs4 import BeautifulSoup

class MyProcess(multiprocessing.Process):

    def __init__(self, i):
        multiprocessing.Process.__init__(self)
        self.i = i

    def run(self):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(self.i*25)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        lis = soup.find('ol', class_='grid_view').find_all('li')
        for li in lis:
            title = li.find('span', class_="title").text
            print(title)

if __name__ == '__main__':
    for i in range(10):
        p = MyProcess(i)
        p.start()

