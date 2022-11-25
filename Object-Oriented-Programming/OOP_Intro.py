class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.health = 0
        self.experience = 0
        self.description = ""
    def print_basics(self):
        print("Name:        ",self.name)
        print("Attack:      ",self.attack)
        print("Defence:     ",self.defence)
        print("Health:      ",self.health)
        print("Experience:  ",self.experience)
        print("Description: ",self.description)
    def print_me(self):
        self.print_basics()
    def print_intro(self):
        print("This is an exciting story?")

class wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = 0
    def print_me(self):
        self.print_basics()
        print("Magic:       ", self.magic)

class knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = 0
    def print_me(self):
        self.print_basics()
        print("Armour:      ", self.armour)

#Example of object (James)
print("James = Character()")
James = Character()
James.name = "James Abela"
James.attack = "N/A"
James.defence = "N/A"
James.health = "N/A"
James.experience = "N/A"
James.description = "Teacher that teaches Object-Oriented Programming for a living."

James.print_basics()
James.print_intro()
print("")

#Creates a wizard character
print("Merlin = wizard()")
Merlin = wizard()
Merlin.magic = 9999
Merlin.name = "Merlin"
Merlin.attack = 50
Merlin.defence = 10
Merlin.health = 1000
Merlin.experience = 72999
Merlin.description = "Old wise wizard who does everything to help people"

Merlin.print_me()
print("")

#Creates a knight character
print("Arthur = knight()")
Arthur = knight()
Arthur.armour = 200
Arthur.name = "Arthur"
Arthur.attack = 150
Arthur.defence = 60
Arthur.health = 50
Arthur.experience = 20
Arthur.description = "Knight turned king who pulled a sword from a stone."
Arthur.print_me()
