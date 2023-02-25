class Instructor:
    def __init__(self, id, name, time_available):
        self._id = id
        self._name = name
        self._time_available = time_available

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_time_available(self):
        return self._time_available