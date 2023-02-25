from .section import Section
from .instructor import Instructor
from .course import Course
from .timeslot import  Timeslot
from datetime import time
class Data:
    data_section = [[302, 'Sec1'], [303, 'Sec2'], [304, 'Sec3'], [305, 'Sec4']]
    data_instructor = [[50, 'Dr.ram', [time(10, 0, 0), time(13, 0, 0)]],
                       [51, 'Prof.shyam', [time(10, 0, 0), time(16, 0, 0)]],
                       [52, 'Er.hari', [time(10, 0, 0), time(14, 0, 0)]],
                       [53, 'Er.bheem', [time(10, 0, 0), time(13, 0, 0)]],
                       [54, 'Dr.arjun', [time(10, 0, 0), time(16, 0, 0)]],
                       [52, 'Er.dhruv', [time(12, 0, 0), time(15, 0, 0)]],
                       [53, 'Dr.raju', [time(10, 0, 0), time(16, 0, 0)]],
                       [54, 'Dr.subash', [time(11, 0, 0), time(16, 0, 0)]]]
    data_timeslot = [[1, 'Time1', [time(10, 0, 0), time(11, 0, 0)]], [2, 'Time2', [time(11, 0, 0), time(12, 0, 0)]],
                     [3, 'Time3', [time(13, 0, 0), time(14, 0, 0)]], [4, 'Time4', [time(14, 0, 0), time(15, 0, 0)]],
                     [5, 'Time5', [time(15, 0, 0), time(16, 0, 0)]]]

    def __init__(self):
        self._sections = []
        self._instructors = []
        self._timeslots = []
        self._week_in_sem = 12
        for i in self.data_section:
            self._sections.append(Section(i[0], i[1]))
        for i in self.data_instructor:
            self._instructors.append(Instructor(i[0], i[1], i[2]))
        for i in self.data_timeslot:
            self._timeslots.append(Timeslot(i[0], i[1], i[2]))
        course1 = Course(1001, 'math', 50, [self._instructors[0], self._instructors[1], self._instructors[5]])
        course2 = Course(1002, 'phy', 50, [self._instructors[3], self._instructors[6]])
        course3 = Course(1003, 'che', 50, [self._instructors[2], self._instructors[4], self._instructors[7]])
        self._courses = [course1, course2, course3]
        self._numberofclasses = len(self._courses)
        # for i in range(len(self._courses)):
        #     self._numberofclasses+=1

    def get_numberofclasses(self):
        return self._numberofclasses

    def get_sections(self):
        return self._sections

    def get_instructors(self):
        return self._instructors

    def get_timeslots(self):
        return self._timeslots

    def get_courses(self):
        return self._courses
