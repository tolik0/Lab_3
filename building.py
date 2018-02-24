from classroom import Classroom


class AcademicBuilding:
    """
    Class for classroom representation
    """

    def __init__(self, address, classrooms):
        """
         (AcademicBuilding, str, list) -> NoneType
        Create new building
        classrooms - list of Classroom
        """
        self.classrooms = classrooms[:]
        self.address = address

    def total_equipment(self):
        """
         (AcademicBuilding) -> list
        Return list of tuples where first element is name of equipment and
        second is amount of it in building
        """
        tot_equipment = dict()
        for i in self.classrooms:
            for equip in i.equipment:
                if equip in tot_equipment:
                    tot_equipment[equip] += 1
                else:
                    tot_equipment[equip] = 1
        return [(i, tot_equipment[i]) for i in tot_equipment]

    def __str__(self):
        """
         (AcademicBuilding) -> str
        Return string with information about building in comfortable for
        user way
        """
        return self.address + "\n" + "\n".join(
            [str(i) for i in (self.classrooms)])
