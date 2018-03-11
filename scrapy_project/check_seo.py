class Check(object):
    errors_title = {}
    errors_keywords = []
    errors_descriptions = {}
    erros_h1 = {}
    error_h2 = {}

    def chech_title(self,title,url):
        if len(title) > 52:
            return 'Длинный тайтл'
            #self.errors_title[url]='Длинный Title'
        elif len(title) == 0:
            return 'Отсутствует'
            # self.errors_title[url] = 'Title отсутствует'
        if '!' in title or ',' in title or '.' in title:
            return 'Стоп символы'
            # self.errors_title[url] = 'В Title имеются стоп символы'


    def check_description(self,description,url):
        if len(description) > 250:
            return 'Слишком длинный Description'
        elif description == 0:
            return 'Description отсутствует'
        else:
            pass

    def check_keywords(self,keywords,url):
        if len(keywords) == 0:
            return 'Отсутствует Keywords'
        if len(keywords) > 250:
            return 'Слишком много символов в Keywords'
    def check_h1_and_h2(self,h1,h2,url):
        if len(h1) > 0:
            return 'Отсутствует h1'
        if len(h2) > 0:
            return 'Отсутствует h2'
        else:
            pass




