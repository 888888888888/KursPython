__author__ = 'Crejzer'
import datetime

class MenadzerZdarzen:

    data = []

    #metoda do zwracania obecnej daty
    def obecnaData(self):
        data = datetime.datetime.now()
        data = data.strftime('%y%m%d')
        return data

    #metoda zwracajaca dane
    def show(self):
        return self.data

    #metoda zwracajaca kategorie (czyli operacje jaka mamy wykonac) oraz person (czyli uzytkownika)
    def parse_text(self, text):
        # I just won alottery #update @all
        category = '#update'
        person = '@all'
        words = text.split(' ')
        for word in words:
            if word.startswith('#'):
                category = word
            elif word.startswith('@'):
                person = word
        return category, person

    #meotda do aktualizowania naszych danych, tekst na naszym przykladnie jest to "I just won alottery"
    def update(self, text, id):
        category, person = self.parse_text(text)
        temp = {'id': id, 'text': text,
                'category': category, 'person': person}
        i = 0
        find = False
        for event in self.data:
            if event['id'] == id:
                find = True
                break
            i += 1
        if find:
            temp['date'] = self.data[i]['date']
            self.data[i] = temp
        return find

    #metoda do wysietlania id
    def show_id(self, id):
        for event in self.data:
            if int(event['id']) == id:
                return event
        return None

    #metoda do dodawania nowych danych
    def add(self, text):
        category, person = self.parse_text(text)
        temp = {'id': self.lastId + 1, 'text': text,
                'category': category, 'person': person, 'date': self.obecnaData()}
        self.data.append(temp)
        return temp

    #metoda zwracajaca ostatne id pod ktorym dane zostaly dodane
    def lastId(self):
        last = 0
        for event in self.data:
            if int(event['id']) > last:
                last = int(event['id'])
        return last

    #metoda do usuwania danych
    def remove(self, id):
        i = 0
        find = False
        for event in self.data:
            if int(event['id']) == id:
                find = True
                break
            i += 1
        if find:
            self.data.pop(i)
        return find