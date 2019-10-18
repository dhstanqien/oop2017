# OOP - Object-Oriented Programming
# event-driven model

# encapsulation
# - grouping of data and methods within a class entity
# - (principle of data/information hiding) private data
#   only accessible via public methods

# inheritance
# - subclass / child class adopt data and methods from super
#   class / parent class
# - subclass can define its own data and methods

# polymorphism


# super class

class Person(object):

    # constructor
    def __init__(self, pid, pname, pweight, pheight):
        self.id = pid
        self.name = pname
        self.weight = pweight
        self.height = pheight

    # assessors
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height    

    # modifiers / mutators
    def set_name(self, pname):
        self.name = pname

    def set_weight(self, pweight):
        self.weight = pweight

    def set_height(self, pheight):
        self.height = pheight        

    # helper / support
    def display(self):
        print(self.id)
        print(self.name)
        print(self.weight)
        print(self.height)

        
# subclasses

class Student(Person):

    # constructor
    def __init__(self, pid, pname, pweight, pheight, pclassid): 
        super().__init__(pid, pname, pweight, pheight)
        self.classid = pclassid

    # assessor
    def get_classid(self):
        return self.classid    

    # modifiers / mutators
    def set_classid(self, pclassid):
        self.classid = pclassid
    
    # helper / support
    def display(self):
        super().display()
        print(self.classid)


class Staff(Person):

    # constructor
    def __init__(self, pid, pname, pweight, pheight, pdept): 
        super().__init__(pid, pname, pweight, pheight)
        self.dept = pdept

    # assessor
    def get_dept(self):
        return self.dept    

    # modifiers / mutators
    def set_dept(self, pdept):
        self.dept = pdept
    
    # helper / support
    def display(self):
        super().display()
        print(self.dept)

# main
#p1 = Person(1, "Tom", 80, 1.45)
student1 = Student(1, "Tom", 80, 1.45, "17Y5C33")
#p2 = Person(2, "Mary", 50, 1.60)     
staff1 = Staff(1, "Mr Pang", 65, 1.63, "Math")
