class Classroom:
    """
    Class for classroom representation
    """

    def __init__(self, number, capacity, equipment):
        """
         (Classroom, str, int, list) -> NoneType
        Create new classroom
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment[:]

    def is_larger(self, c):
        """
        (Classroom, Classroom) -> boolean
        Show in what classroom there is larger capacity
        Return True if first classroom is larger
        """
        return True if self.capacity > c.capacity else False

    def equipment_differences(self, c):
        """
        (Classroom, Classroom) -> list
        Show equipment from first classroom that is not in second
        Return list of it
        """
        return [i for i in self.equipment if i not in c.equipment]

    def __str__(self):
        """
        (Classroom) -> str
        Return information about classroom in comfortable way for user
        """
        return "Classroom {} has a capacity of {} persons and has the \
following equipment: {}.".format(self.number, self.capacity, ", ".join(
            self.equipment))

    def __repr__(self):
        """
        (Classroom) -> str
        Return information about classroom in comfortable way for developer
        """
        class_name = type(self).__name__
        return "{} ({},{},{})".format(class_name, self.number, self.capacity,
                                      self.equipment)
