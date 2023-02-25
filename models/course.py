class Course:
    def __init__(self, id, name, credit_hrs, instructor_list):
        self._id = id
        self._name = name
        self._credit_hrs = credit_hrs
        self._instructor_list = instructor_list

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credit_hrs(self):
        return self._credit_hrs

    def get_instructor_list(self):
        return self._instructor_list