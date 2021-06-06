from sqlalchemy import *
engine = create_engine('sqlite:///filmy.db')

metadata = MetaData()

Filmy = Table(
    'Filmy', metadata,
    Column('id', Integer, primary_key=True),
    Column('Nazwa', String),
    Column('Rezyser', String),
    Column('Aktory', String),
    Column('Vod', String)
)

metadata.create_all(engine)
conn = engine.connect()

class Film:
    def __init__(self, nazwa, rezyser, cast, vod):
        self.nazwa = nazwa
        self.rezyser = rezyser
        self.cast = cast
        self.vod = vod

    def dodawanie(self):
        s = Filmy.select().where(Filmy.c.Nazwa == self.nazwa)
        result = conn.execute(s)
        if result.fetchone() is None:
            ins = Filmy.insert().values(Nazwa = self.nazwa, Rezyser = self.rezyser, Aktory = ', '.join(self.cast), Vod = ', '.join(self.vod))
            conn.execute(ins)
        else:
            print('Taki film już jest w bazie')

    def update(self, nazwa):
        upd = Filmy.update().where(Filmy.c.Nazwa == nazwa).values(Nazwa = self.nazwa, Rezyser = self.rezyser, Aktory = ', '.join(self.cast), Vod = ', '.join(self.vod))
        conn.execute(upd)


def DodacFilm():
    cast = []
    vod = []
    nazwa = input("Nazwa: ")
    rezyser = input('Reżyser: ')
    print('Wprowadź aktorów, zakońć 0: ')
    while True:
        s = input('Aktor: ')
        if s != '0':
            cast.append(s)
        else: break
    print("Wprowadź VOD, zakońć 0: ")
    while True:
        s = input('Vod: ')
        if s != '0':
            vod.append(s)
        else: break
    film = Film(nazwa, rezyser,cast,vod)
    return film

def DeleteFilm():
    nazwa = input('Nazwa: ')
    delf = Filmy.delete().where(Filmy.c.Nazwa == nazwa)
    conn.execute(delf)

def UpdateFilm():
    nazwa = input('Podaj nazwę: ')
    print('Podaj nowe danny: ')
    DodacFilm().update(nazwa)
   
def SelectFilm():
    nazwa = input('Wprowadź nazwę: ')
    s = Filmy.select().where(Filmy.c.Nazwa == nazwa)
    result = conn.execute(s)
    if result.fetchone is None:
        print('Takiego filmu nie ma!')
    else:
        for row in result:
            print('Nazwa: ' + row[1])
            print('Reżyser ' + row[2])
            print('Aktory: ' + row[3])
            print('VOD: ' + row[4])
while True:
    print('Menu: ')
    print('1 - Dodać film')
    print('2 - Usunąć film')
    print('3 - Edytować film')
    print('4 - Znaleźć film')
    choise = int(input('Wybierz: '))
    if choise == 1:
        DodacFilm().dodawanie()
    elif choise == 2:
        DeleteFilm()
    elif choise == 3:
        UpdateFilm()
    elif choise == 4:
        SelectFilm()
    elif choise == 5:
        print('Dowidzenia')
        break
