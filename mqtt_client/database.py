mqtt_info = {}
device_info = {}
sub_topic = {}

class Observer(object):
    """观察者核心：mqtt payload"""
    def __init__(self):
        self._data = None
        self._department = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        for obj in self._department:
            obj.change(value)

    def attach(self, department):
        self._department.append(department)

    def detach(self, department):
        self._department.remove(department)