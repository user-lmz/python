class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    # def print_score(self):
    #     print('%s\n%d' % (self.name, self.score))
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('lisa', 99)
bart = Student('Bart', 59)
print(lisa._Student__name, lisa.get_grade())
print(bart._Student__name, bart.get_grade())
print(lisa._Student__score)
print(bart._Student__score)