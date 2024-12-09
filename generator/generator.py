import random
from faker import Faker
from data.data import Person
fake_en = Faker('En')


def generated_file():
    path = rf'C:\Users\Iryna.Sarokina\SeleniumTask\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path

def generated_person():
    yield Person(
        firstname=fake_en.first_name(),
        lastname=fake_en.last_name(),
        comment=fake_en.text(),
        email=fake_en.email(),
        incorrect_email=fake_en.first_name()
    )