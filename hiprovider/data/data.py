ingredients = [
        {"id":"1",
        "nome":"farina 00",
        "id_fornitore":"1",
        "id_prodotto":"1",
        "semilavorato": False
        },
        {"id":"2","nome":"uova",
        "id_fornitore":"2",
        "id_prodotto":"1",
        "semilavorato": False
        },
        {"id":"3",
        "nome":"farina 00",
        "id_fornitore":"3",
        "id_prodotto":"2",
        "semilavorato": False
        },
        {"id":"4",
        "nome":"zucchero",
        "id_fornitore":"3",
        "id_prodotto":"1",
        "semilavorato": False
        },
        {"id":"5",
        "nome":"uova",
        "id_fornitore":"4",
        "id_prodotto":"2",
        "semilavorato": False
        },
        {"id":"7",
        "nome":"farina 000",
        "id_fornitore":"5",
        "id_prodotto":"3"
        ,"semilavorato": False
        }
    ]

producers = [
    {"id":"1","nome":"Barilla","sito":"http:\/\/www.barilla.it","note":'null'},
    {"id":"4","nome":"Bistefani","sito":"http:\/\/www.bistefani.it","note":'null'},
    {"id":"5","nome":"Colussi","sito":"http:\/\/www.colussi.it","note":'null'}
    ]

articles= [
    {"id":"1","articolo":"Biscottone","id_produttore":"1"},
    {"id":"2","articolo":"Goloso","id_produttore":"4"},
    {"id":"3","articolo":"Carezze","id_produttore":"5"}
    ]


suppliers = [
    {"id":"1","nome":"Agraria Tornabene Srl","sito":"http:\/\/www.tornabene.it","e-mail": "pippo@tim.it","origine":"IT"},
    {"id":"2","nome":"Allevamento Galline Spa","sito":"http:\/\/www.algall.it","e-mail": "pippo@tim.it","origine":"IT"},
    {"id":"3","nome":"Az. Agricola Ladispoli","sito":"http:\/\/www.ladispoli.it","e-mail": "pippo@tim.it","origine":"IT"},
    {"id":"4","nome":"Uova&Uova","sito":"http:\/\/www.biuova.it","e-mail": "pippo@tim.it","origine":"IT"},
    {"id":"5","nome":"Zuccherificio Pasticcio","sito":"http:\/\/www.pasticcio.it","e-mail": "pippo@tim.it","origine":"IT"}
    ]


def get_ingredients():
    return ingredients

def get_articles():
    return articles

def get_producers():
    return producers

def get_suppliers():
    return suppliers