from .schedule import Schedule
from .data import Data
class Population:
    def __init__(self, size):
        self._data=Data()
        self._size = size
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize())
    def get_schedules(self):
        return self._schedules