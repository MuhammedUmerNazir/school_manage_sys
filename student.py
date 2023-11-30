from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, first, last, dob, phone, address, international = False):
        super().__init__(self, first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    def add_enrolled(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError("Invalid Enroll...")
        
        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False
    
    def isPartTime(self):
        return len(self.enrolled) <= 3



        