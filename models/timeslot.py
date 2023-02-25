class Timeslot:
    def __init__(self, id, name, timestamp):
        self._id = id
        self._name = name
        self._timestamp = timestamp  # timestamp example would be [10:15,12:05]

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_timestamp(self):
        return self._timestamp