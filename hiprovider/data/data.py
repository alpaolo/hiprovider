commodities = [
    {"id":"1","name":"farina 00","supplier":"1","product":"1"},
    {"id":"2","name":"uova","supplier":"2","product":"1"},
    {"id":"3","name":"farina 00","supplier":"3","product":"2"},
    {"id":"4","name":"zucchero","supplier":"5","product":"1"},
    {"id":"5","name":"uova","supplier":"4","product":"2"},
    {"id":"7","name":"farina 000","supplier":"3","product":"3"}
    ]

producers = [
    {"id":"1","name":"Barilla","site":"http:\/\/www.barilla.it","note":'null'},
    {"id":"4","name":"Bistefani","site":"http:\/\/www.bistefani.it","note":'null'},
    {"id":"5","name":"Colussi","site":"http:\/\/www.colussi.it","note":'null'}
    ]

products = [
    {"id":"1","article":"Biscottone","producer":"1"},
    {"id":"2","article":"Goloso","producer":"4"},
    {"id":"3","article":"Carezze","producer":"5"}
    ]


suppliers = [
    {"id":"1","name":"Agraria Tornabene Srl","site":"http:\/\/www.tornabene.it","origin":"IT"},
    {"id":"2","name":"Allevamento Galline Spa","site":"http:\/\/www.algall.it","origin":"IT"},
    {"id":"3","name":"Az. Agricola Ladispoli","site":"http:\/\/www.ladispoli.it","origin":"IT"},
    {"id":"4","name":"Uova&Uova","site":"http:\/\/www.biuova.it","origin":"IT"},
    {"id":"5","name":"Zuccherificio Pasticcio","site":"http:\/\/www.pasticcio.it","origin":"IT"}
    ]


def get_commodities():
    return commodities

def get_products():
    return products

def get_producers():
    return producers

def get_suppliers():
    return suppliers