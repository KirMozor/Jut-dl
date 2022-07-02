import requests
from bs4 import BeautifulSoup
import wget

def parsUrlToPage(quotes):
    for title in quotes:
            s = title.text.strip(), title.get('href')
            b = "https://jut.su" + s[1]
            #b = b.split()
            f = open("url", "a")
            f.write("{};{};".format(s[0], b))
            f.close()
def parsVideoToPage(quotes):
    for title in quotes:
        s = title.text.strip(), title.get('src')
        return(s)
def main(quality, url):
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')

    f = open("url", "w")
    f.close()

    quotes = soup.find_all('a', class_='short-btn black video the_hildi')
    parsUrlToPage(quotes)
    quotes = soup.find_all('a', class_='short-btn green video the_hildi')
    parsUrlToPage(quotes)
    download(header, quality)

def download(header, quality):
    f = open("url", "r")
    s = f.read()
    f.close()
    j = s.split(";")

    while True:
        if len(j) == 0 or len(j) == 1:
            print("\nСкачивание успешно завершенно... Приятного просмотра!")
        else:
            url = j[1]

            response = requests.get(url, headers=header)
            soup = BeautifulSoup(response.text, 'lxml')

            quotes = soup.find_all('source', label=quality)
            s = parsVideoToPage(quotes)
            print("\nИмя: {}, ссылка: {}, ссылка на видео: {}".format(j[0], j[1], s[1]))
            print("Начинаю скачивание видео...")

            f = open(j[0] + ".mp4", "wb")
            download = requests.get(s[1], headers=header)
            f.write(download.content)
            f.close()
            print("Закончил скачивать")

            j.pop(0)
            j.pop(0)

print("Здравствуйте, я скачиваю аниме с сайта Jut.su\n")
print("Я могу просто спарсить url до нужной анимешки, потом вы подправите файл с ссылками и я скачаю все серри аниме из этого файла\nИли у вас уже есть файл, скажите если есть\n1. Скачай аниме из файла 2. Спарси url и скачай сразу 3. Просто спарси url")
parsOrNo = int(input())

if parsOrNo == 1:
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    print("\nОкей, буду скачивать аниме из файла")
    print("В каком качестве скачивать?\n1. 360 2. 480 3. 720 4. 1080")
    quality = int(input())
    print("")

    if quality == 1:
        quality = "360p"
        download(header, quality)
    if quality == 2:
        quality = "480p"
        download(header, quality)
    if quality == 3:
        quality = "720p"
        download(header, quality)
    if quality == 4:
        quality = "1080p"
        download(header, quality)
    else:
        print("Вы написали что-то не то. Надо писать от 1 до 4. Запустите меня заново =)")

if parsOrNo == 2:
    print("\nУкажите ссылку на аниме, и начну его скачивать!")
    url = str(input())
    print("В каком качестве скачивать?\n1. 360 2. 480 3. 720 4. 1080")
    quality = int(input())

    if quality == 1:
        quality = "360p"
        main(quality, url)
    if quality == 2:
        quality = "480p"
        main(quality, url)
    if quality == 3:
        quality = "720p"
        main(quality, url)
    if quality == 4:
        quality = "1080p"
        main(quality, url)
    else:
        print("Вы написали что-то не то. Надо писать от 1 до 4. Запустите меня заново =)")

if parsOrNo == 3:
    print("\nУкажите ссылку на аниме, и начну его скачивать!")
    url = str(input())
    print("Начинаю парсить url в файл")

    f = open("url", "w")
    f.close()

    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='short-btn black video the_hildi')
    parsUrlToPage(quotes)
    quotes = soup.find_all('a', class_='short-btn green video the_hildi')
    parsUrlToPage(quotes)
    print("Готово, заверщаю работу")