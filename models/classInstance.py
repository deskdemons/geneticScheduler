class Class:
    def __init__(self, id, section, course, day):
        self._id = id
        self._section = section
        self._course = course
        self._instructor = None
        self._timeslot = None
        self._day = day

    def get_id(self):
        return self._id

    def get_section(self):
        return self._section

    def get_course(self):
        return self._course

    def get_instructor(self):
        return self._instructor

    def get_timeslot(self):
        return self._timeslot

    def get_day(self):
        return self._day

    def set_instructor(self, instructor):
        self._instructor = instructor

    def set_timeslot(self, timeslot):
        self._timeslot = timeslot

    def __str__(self):
        return str(self._day) + "," + str(self._section.get_name()) + "," + str(self._course.get_name()) + "," + str(
            self._instructor.get_name()) + "," + str(self._timeslot.get_name())