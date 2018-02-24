import unittest
from classroom import Classroom


class academicbuilding_test(unittest.TestCase):

    def test_is_larger(self):
        classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        classroom_007 = Classroom('007', 12, ['TV'])
        self.assertEqual(classroom_007.is_larger(classroom_016), False)

    def test_equipment_differences(self):
        classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        classroom_007 = Classroom('007', 12, ['TV', 'mic'])
        self.assertEqual(classroom_007.equipment_differences(classroom_016),
                         ['TV'])

    def test_str(self):
        classroom_007 = Classroom('007', 12, ['TV'])
        self.assertEqual(classroom_007.__str__(),
                         "Classroom 007 has a capacity of 12 persons and has "
                         "the following equipment: TV.")

    def test_repr(self):
        classroom_007 = Classroom('007', 12, ['TV'])
        self.assertEqual(classroom_007.__repr__(), "Classroom (007,12,['TV'])")


if __name__ == '__main__':
    unittest.main()
