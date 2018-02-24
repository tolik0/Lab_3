from classroom import Classroom


class AcademicBuilding:
    """
    Class for classroom representation
    """
    def __init__(self, address, classrooms):
        """
         (Classroom, str, int, list) -> NoneType
        Create new classroom
        """
        self.classrooms = classrooms[:]
        self.address = address

    def total_equipment(self):
        tot_equipment = dict()
        for i in self.classrooms:
            for equip in i.equipment:
                if equip in tot_equipment:
                    tot_equipment[equip] += 1
                else:
                    tot_equipment[equip] = 1
        return [(i, tot_equipment[i]) for i in tot_equipment]

    def __str__(self):
        return self.address + "\n" + "\n".join(
            [str(i) for i in (self.classrooms)])