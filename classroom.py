class Classroom:
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment[:]

    def is_larger(self, c):
        return True if self.capacity > c.capacity else False

    def equipment_differences(self, c):
        return [i for i in self.equipment if i not in c.equipment]

    def __str__(self):
        return "Classroom {} has a capacity of {} persons and has the \
following equipment: {}.".format(self.number, self.capacity, ", ".join(
            self.equipment))

    def __repr__(self):
        class_name = type(self).__name__
        return "{} ({},{},{})".format(class_name, self.number, self.capacity,
                                      self.equipment)