from classroom import Classroom


class AcademicBuilding:
    def __init__(self, adress, classrooms):
        self.classrooms = classrooms[:]
        self.adress = adress

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
        return self.adress + "\n" + "\n".join(
            [str(i) for i in (self.classrooms)])