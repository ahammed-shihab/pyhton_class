
class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print("Error: Student is already enrolled.")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Error: Student is not enrolled.")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully.")

    def view_student_info(self):
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Department:", self.__department)

        if self.__is_enrolled:
            print("Enrollment Status: Enrolled")
        else:
            print("Enrollment Status: Not Enrolled")

        print("------------------------")

    def get_student_id(self):
        return self.__student_id


# Creating some student objects manually
student1 = Student("101", "Rahim Ahmed", "CSE", True)
student2 = Student("102", "Karim Hasan", "EEE", False)
student3 = Student("103", "Nusrat Jahan", "CSE", True)


while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(StudentDatabase.student_list) == 0:
            print("No students found.")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "2":
        student_id = input("Enter student ID to enroll: ")

        found = False

        for student in StudentDatabase.student_list:
            if student.get_student_id() == student_id:
                student.enroll_student()
                found = True
                break

        if not found:
            print("Error: Invalid student ID.")

    elif choice == "3":
        student_id = input("Enter student ID to drop: ")

        found = False

        for student in StudentDatabase.student_list:
            if student.get_student_id() == student_id:
                student.drop_student()
                found = True
                break

        if not found:
            print("Error: Invalid student ID.")

    elif choice == "4":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
