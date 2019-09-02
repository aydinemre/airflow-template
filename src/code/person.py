# -*- coding: utf-8 -*-

# Created by emre.aydin (eaydin@boynergrup.com) at 2019-09-02
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name : {} Age : {}".format(self.name, self.age)


def main(name='default_name', age=17):
    person = Person(name, age)
    print(person)


if __name__ == '__main__':
    main("Emre", 24)
