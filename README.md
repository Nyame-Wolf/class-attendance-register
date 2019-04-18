This is from the andela bootcamp projects pdf. 
the it contains two files. attendance_register.py which contains code representing the requirements below and test_attendance_register.py which represents the tests to ensure code from attendance register works.
Application Requirements:
1. Class Attendance Register
■The class attendance register is used to check-in students when they come into
class. To be able to do this, we need to have the following commands.
■check in <student_id> <class_id>​ - Checks in a student into a class
at the current time. A student once checked cannot be checked into
another class except the class he has been checked into has ended.
■check out <student_id> <class_id> <reason>​ - Force check out a
student from a class but a reason must be provided e.g Medical, Need to
go home etc.
■log start <class_id>​ - This creates a new time log for a particular
class
■log end <class_id>​ - This ends a time log for a class that has already
been started
■student add <student_details>​ - This command creates a new
student in the database and generate an id for the student
■student remove <student_id>​ - This command deletes a student
based on the student_id.
■class add <class_details>​ - This command creates a new class in the
database and generates an id for the class.
■class remove <class_id>​ - This command deletes a class based on the
class_id.
■class list​ - List all the classes with their status (Shows the status of the
class and the number of students in that class at the moment)
■student list​ - List all the students and if they’re currently in a class