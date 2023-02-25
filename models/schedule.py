import random as rnd
from .classInstance import Class
from .data import Data
class Schedule:
    def __init__(self):
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
        self._no_of_class_in_week=72

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        self._data = Data()
        courses = self._data.get_courses()
        sections = self._data.get_sections()
        days_of_week = ('sun', 'mon', 'tue', 'wed', 'thu', 'fri')

        for _ in range(self._no_of_class_in_week):  # 6 days a week
            rnd_section = sections[rnd.randrange(0, len(sections))]
            rnd_course = courses[rnd.randrange(0, len(courses))]
            newClass = Class(self._classNumb, rnd_section, rnd_course, days_of_week[rnd.randrange(0, 6)])
            self._classNumb += 1
            newClass.set_instructor(
                rnd_course.get_instructor_list()[rnd.randrange(0, len(rnd_course.get_instructor_list()))])
            newClass.set_timeslot(self._data.get_timeslots()[rnd.randrange(0, 5)])
            self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if ((classes[i].get_timeslot().get_timestamp()[0] >= classes[i].get_instructor().get_time_available()[0] and
                 classes[i].get_timeslot().get_timestamp()[1] <= classes[i].get_instructor().get_time_available()[
                     1]) == False):
                self._numbOfConflicts += 1  # teacher can teach class only within his available time
            for j in range(0, len(classes)):
                if (j > i):  # not sure if it should be >= or just >
                    if (classes[i].get_day() == classes[j].get_day()):
                        if (classes[i].get_section() == classes[j].get_section()):
                            if (classes[i].get_timeslot() == classes[
                                j].get_timeslot()):  # same day, same section ma eutei timeslot dui choti occur hunu vayena
                                self._numbOfConflicts += 1
                            if (classes[i].get_course() == classes[j].get_course()):
                                if (classes[i].get_instructor() == classes[
                                    j].get_instructor()):  # same day, same section, different timeslot ma same course xa vani, same instructor feri aauna payena, arko instructor aaunu payo. example: there might be two math classes in same day, but differnt teachers
                                    self._numbOfConflicts += 1
                        if (classes[i].get_timeslot() == classes[
                            j].get_timeslot()):  # cache could be used as it is already calculated.
                            if (classes[i].get_section() != classes[j].get_section()):
                                if (classes[i].get_instructor() == classes[
                                    j].get_instructor()):  # same day, same timeslot, different section ma same instructor huna payena
                                    self._numbOfConflicts += 1

        return 1 / ((1.0 * self._numbOfConflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in self._classes:
            returnValue += str(i) + " , "
        return returnValue

