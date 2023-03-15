from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractmethod
    def saludar(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso
    
    def saludar(self):
        return f"Buenos días, soy {self.nombre} y soy estudiante del curso {self.curso}."

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
    
    def saludar(self):
        return f"Buenos dias, soy {self.nombre} y soy Licenciada de {self.asignatura}."

class Administrativo(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.cargo = cargo
    
    def saludar(self):
        return f"Buenos dias, soy {self.nombre} y soy {self.cargo} en la universidad."

personas = [Estudiante("Petrolina", 20, "Programación"),
            Profesor("Maria del Carmen", 35, "Lenguaje"),
            Administrativo("Chepe", 45, "Secretario")]

for persona in personas:
    print(persona.saludar())
