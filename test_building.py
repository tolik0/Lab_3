import unittest
from building import AcademicBuilding, Classroom


class academicbuilding_test(unittest.TestCase):

    def test_total_equipment(self):
        classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        classroom_007 = Classroom('007', 12, ['TV'])
        classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        classrooms = [classroom_016, classroom_007, classroom_008]
        building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        self.assertEqual(building.total_equipment(),
                         [('PC', 2), ('projector', 2), ('mic', 1), ('TV', 1)])

    def test_str(self):
        classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        classroom_007 = Classroom('007', 12, ['TV'])
        classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        classrooms = [classroom_016, classroom_007, classroom_008]
        building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        self.assertEqual(building.__str__(), """Kozelnytska st. 2a
Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.""")


if __name__ == '__main__':
    unittest.main()
