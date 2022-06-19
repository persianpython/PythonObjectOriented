from random import choice


class Student:
    educational_platform = "youtube PersianPython"

    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def greet(self):
        greetings = [
            "salam, man {} hastam va dore Object Oriented ra tamasha kardam",
            "chetori man {} hastam",
        ]

        greeting = choice(greetings)

        return greeting.format(self.name)


def class_create(student_names):
    return [Student(name) for name in student_names]


if __name__ == "__main__":
    names = ["mohammad", "ali", "reza", "mostafa"]

    for student in class_create(names):
        print(student.greet())
