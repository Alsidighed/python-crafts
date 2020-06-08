class PupilAppraisals:
    def __init__(self, fullName, informatics, maths, physics):
        self.fullName = fullName
        self.informatics = informatics
        self.maths = maths
        self.physics = physics
    def outputInformatics(self):
        print("Оценка", self.fullName, "по информатике:", self.informatics)
    def outputAll(self):
        print("Оценки", self.fullName, ":", " ".join([str(e) for e in (self.informatics, self.maths, self.physics)]))
class PupilAppraisalsPlusTeacher(PupilAppraisals):
    def __init__(self, teacherFullName, exp, degree, pupilFullName, informatics, maths, physics):
        self.teacherFullName = teacherFullName
        self.exp = exp
        self.degree = degree
        super().__init__(pupilFullName, informatics, maths, physics)
    def outputTeacher(self):
        print("Учитель ", self.teacherFullName, ", стаж ", self.exp, " лет, ", self.degree, sep = "")
class PupilAppraisalsPlusTeacherPlusTutor(PupilAppraisalsPlusTeacher):
    def __init__(self, tutorFullName, startDate, endDate, teacherFullName, exp, degree, pupilFullName, informatics, maths, physics):
        self.tutorFullName = tutorFullName
        self.startDate = startDate
        self.endDate = endDate
        super().__init__(teacherFullName, exp, degree, pupilFullName, informatics, maths, physics)
    def outputTutor(self):
        print("Репетитор ", self.tutorFullName, ", поступление ", self.startDate, ", выпуск ", self.endDate, sep = "")
class Shape:
    def __init__(self, type, height, width):
        self.type = type
        self.height = height
        self.width = width
    def __str__(self):
        return f"{self.type} высотой {self.height} см ({self.height / 100} м) и шириной {self.width} см ({self.width / 100} м)"
class Square(Shape):
    def __init__(self, height, width):
        super().__init__("Квадрат", height, width)
class Triangle(Shape):
    def __init__(self, height, width):
        super().__init__("Треугольник", height, width)
p = PupilAppraisalsPlusTeacherPlusTutor("Юсупов М. А.", "14 апреля 2019 года", "3 июня 2019 года", "Русакова Н. В.", 34, "Заслуженный учитель Российской Федерации", "Лушникова Я. В.", 5, 5, 4)
p.outputInformatics()
p.outputAll()
p.outputTeacher()
p.outputTutor()
print(Square(10, 5))
print(Triangle(20, 75))
