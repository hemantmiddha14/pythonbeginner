class student:
    def __init__(self, fname, lname, roll_no):
        self.fname = fname
        self.lname = lname
        self.roll_no = roll_no




class skills(student):
    def __init__(self, fname, lname, roll_no, skills):
        super().__init__(fname, lname, roll_no)
        self.skills = skills

"""To Print the ouptut as exact representation
    def __repr__(self):
        return "skills('{}', '{}', '{}')".format(self.fname + self.lname, self.roll_no, self.skills)"""

    
"""To Print the ouptut as string
    def __str__(self):
        return '{}, {}'.format(self.fname + self.lname, self.skills)"""

st1 = skills('Hemant', 'Middha', 69, 'Acting')

#print(st1)


print(st1.fname, st1.lname, ',', st1.roll_no, '-->', 'Passion:', st1.skills)




class interests(student):
    pass

