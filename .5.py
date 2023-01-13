class Car :
    model = "17'"
    year ="2006"
    manufacturer = "China"
    engine_capacity="3"
    car_color="red"
    price="1848849"

    def __init__(self, model, year, manufacturer, engine_capacity, car_color, price ):
        self.model=model
        self.year=year
        self.manufacturer=manufacturer
        self.engine_capacity=engine_capacity
        self.car_color=car_color
        self.price=price
    def print(self):
        print(self.price)
        print(self.model)
        print(self.year)
        print(self.manufacturer)
        print(self.engine_capacity)


class Book:
    name = "'Twilight'"
    year = "2006"
    publisher="'FASHION_HOUSE'"
    genre="romantic"
    author="Stephanie Mayer"
    price='5846'

    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher=publisher
        self.genre=genre
        self.author =author
        self.price = price

    def print(self):
        print(self.publisher)
        print(self.name)
        print(self.year)
        print(self.author)
        print(self.price)


class Stadion:
    name = "'Kairat'"
    data= "29.09.2006"
    country = "'Kazakhstan'"
    city = "Semey"
    vmestimost="32"

    def __init__(self, name, data, country, city, vmestimost):
        self.name = name
        self.data =data
        self.country=country
        self.city=city
        self.vmestimost = vmestimost

    def print(self):
        print(self.name)
        print(self.data)
        print(self.country)
        print(self.city)



