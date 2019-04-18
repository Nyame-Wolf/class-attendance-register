import unittest
from attendance_register import AttendanceRegister
from datetime import datetime


class TestAttendanceRegister(unittest.TestCase):

    def setUp(self):
        # ar = attendance_register.AttendanceRegister()

        # self.stud1 = ar.student_add('Flee')
        # self.stud2 = ar.student_add('Bug')
        # self.stud3 = ar.student_add('Tick')

        # self.klass1 = ar.class_add('Physics')
        # self.klass2 = ar.class_add('Chemistry')

        # self.klass1.check_in(stud3)
        pass

    def tearDown(self):
        pass

    def test_student_add(self):
        ar = AttendanceRegister()
        self.assertEqual(
            ar.student_add('Flee'),
            "Added student with id 1"
        )
        # self.assertEqual(student_add(self.stud2.id), 2)
        # self.assertEqual(student_add(self.stud1.name), 'Flee')
        # self.assertEqual(student_add(self.stud2.name), 'Bug'
        # self.assertEqual(student_add(self.stud1.id), 1)
        # self.assertEqual(student_add(self.stud2.id), 2)
        # self.assertEqual(student_add(self.stud1.name), 'Flee')
        # self.assertEqual(student_add(self.stud2.name), 'Bug')

    def test_student_remove(self):
        self.assertIn(student_remove(self.stud1.id), False)
        self.assertIn(student_remove(self.stud2.id), False)


    def test_class_add(self):
        self.assertEqual(class_add(self.klass1.id), 1)
        self.assertEqual(class_add(self.klass2.id), 2)
        self.assertEqual(class_add(self.klass1.name), 'Physics')
        self.assertEqual(class_add(self.klass2.name), 'Chemistry')

    def test_class_remove(self):
        self.assertEqual(class_remove(self.klass1.id),False)
        self.assertIn(class_remove(self.klass2.id),False)

    def test_class_checkin(self):
        self.assertEqual(check_in(self.stud1),True )
        self.assertEqual(check_in(self.stud1),True)

        with self.Raises(ValueError):
            check_in(stud3,False)


    def test_class_checkout(self):
        self.assertEqual(check_out(self.stud1),)
        '''
        with self.Raises(ValueError):
        '''

    def test_log_start(self):
        self.assertEqual(log_start(self.start_time),datetime.now())
        '''
        with self.Raises(ValueError):
        '''

    def test_log_end(self):
        pass
        '''
        with self.Raises(ValueError):
        '''

    def test_class_list(self):
        pass

    def test_student_list(self):
        pass

if __name__ == '__main__':
    unittest.main()
