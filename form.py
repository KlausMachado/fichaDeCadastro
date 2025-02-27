class Register:
    def __init__(self, code, name, age, gender):
        self.code = code
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Codigo: {self.code}\nNome: {self.name}\nIdade: {self.age}\nGenero: {self.gender}'