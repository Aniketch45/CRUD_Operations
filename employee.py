class Employee:
    def __init__(self, id, name, sal, dept):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = dept
    
    def toTuple(self):
        return (self.id, self.name, self.sal, self.dept)

if(__name__ == '__main__'):
    e = Employee('202', 'Amit', 60000, 'Android Developer')
    print(e.toTuple())