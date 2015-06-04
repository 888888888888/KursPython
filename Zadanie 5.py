__author__ = 'Crejzer'
"""Zadanie 5"""

import json
import falcon

#przekladowy server zgodny ze standardem WSGI
from wsgiref import simple_server

#import klasy z metodami potrzebnymi do stworzenia naszego servera
from MenadzerZdarzen import MenadzerZdarzen

zdarzenie = MenadzerZdarzen();

#dane do naszego zadania
PERSON = {'john', 'all', 'all-friends'}
CATEGORY = {'warn', 'update', 'poll'}

#glowne wejscie do aplikacji
app = falcon.API();

class Zasoby:

    #standardowa metoda HTML ktora umozliwia pobranie (wziescie) elementow do naszego serwera
    #req i resp sa to dwa stadardowe elementy HTML (req = request resp = respond)
    #id unikalny klucz dla naszych danych
    def on_get(self, req, resp, id):
        try:
            id_ = int(id)
        except:
            resp.status = falcon.HTTP_400
        else:
            resp.body = json.dumps(zdarzenie.show_id(id_))
            resp.status = falcon.HTTP_200

    #nasluchiwanie postow HTML (jesli JSON bedzie cos zawieral przeslemy go z kod stanu html 201, jesli blad wroci z kodem 400)
    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except:
            resp.status = falcon.HTTP_400
        else:
            result_json = json.loads(raw_json, encoding='utf-8')
            zdarzenie.add(text=result_json['event'])
            resp.body = json.dumps(result_json, encoding='utf-8')
            resp.status = falcon.HTTP_201

    #metoda do umieszczania nowych danych na naszym serwerze
    def on_put(self, req, resp, id):
        try:
            raw_json = req.stream.read()
            id = int(id)
        except:
            resp.status = falcon.HTTP_400
        else:
            result_json = json.loads(raw_json.decode('utf-8'))
            up = zdarzenie.update(text=result_json['event'], id=id)
            if up:
                resp.status = falcon.HTTP_200
            else:
                resp.status = falcon.HTTP_400

    #metoda do usuwania danych
    def on_delete(self, req, resp, id):
        try:
            id = int(id)
        except:
            resp.status = falcon.HTTP_400
        else:
            usun = zdarzenie.remove(id)
            if usun:
                resp.status = falcon.HTTP_200
            else:
                resp.status = falcon.HTTP_400

#pakowanie wszystkiego do naszej aplikacji i umieszczanie pod dana sciezka
app = falcon.API()
zasoby = Zasoby()
app.add_route('/', zasoby)
app.add_route('/{id}/', zasoby)

class ZasobyDodane:

    #wyswietlanie wszystkich zasobow
    def on_get(self, req, resp):
        try:
            temp = zasoby.show()
        except:
            resp.status = falcon.HTTP_400
        else:
            resp.body = json.dumps(temp)
            resp.status = falcon.HTTP_200

last_event = ZasobyDodane()
app.add_route('/last', last_event)

if __name__ == "__main__":

    #stawiam prosty server do spradzenia poprawnosci kodu
    host = "127.0.0.1"
    port = 8000
    httpd = simple_server.make_server(host, port, app)
    print "Serving on %s:%s" % (host, port)
    httpd.serve_forever()