import requests

from bs4 import BeautifulSoup

# Прекрасный супчик
class Soups:
    def __init__(self, URL, save_flag=None):
        self.URL = URL
        self.save_flag = save_flag
        self.cook_soup()

    # Варим супчик - получаем html
    def cook_soup(self):
        page = requests.get(self.URL, timeout=60)
        status = page.status_code

        if status:
            document = page.text
            self.soup = BeautifulSoup(document, "html.parser")

            if self.save_flag:
                self.taste_soup(document)

            # return self.soup
        else:
            return False

    # Пробуем супчик - сохраняем html в файл
    def taste_soup(self, document):
        URL = self.URL.replace("https://", "")
        URL = self.URL.replace("http://", "")
        URL = self.URL.replace("/", "")

        with open("%s.html" % URL, mode="w") as f:
            f.write(document)


# миска прекрасного супа
class Bowls(Soups):
    def __init__(self, URL, tag=None, tag_name=None):
        super().__init__(URL)
        self.tag = tag
        self.tag_name = tag_name
        self.warm_soup()

    # варим суп
    def warm_soup(self, tag=None, tag_name=None):
        self.bowl_of_soup = self.soup.findAll(self.tag, class_=self.tag_name)


def main():

    URL = "https://www.drom.ru/makers/"

    # приготовим супчик
    soup = Soups(URL, True)

    # нальем миску супа
    bowl = Bowls(URL, "a", "b-link")
    for i in bowl.bowl_of_soup:
        print(i)


if __name__ == "__main__":
    main()
