class Student:
    # Represents a student with enrollments and grades
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrollments = []
    
    def enroll(self, course):
        # Enroll the student in a course
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)
    
    def record_grade(self, course, grade):
        # Assign a grade to a course the student is enrolled in
        for enrollment in self.enrollments:
            if enrollment.course == course:
                enrollment.grade = grade
                return
        raise ValueError("Student not enrolled in this course")
    
    def calculate_gpa(self):
        # Compute the student's GPA based on enrolled courses
        total_points = 0
        count = 0
        for enrollment in self.enrollments:
            if enrollment.grade is not None:
                total_points += enrollment.grade
                count += 1
        return total_points / count if count > 0 else 0
    
    def display_info(self):
        # Display student information and enrolled courses with grades
        print(f"Student ID: {self.student_id}, Name: {self.name}")
        print("Enrollments:")
        for enrollment in self.enrollments:
            grade = enrollment.grade if enrollment.grade is not None else "Not graded"
            print(f"  {enrollment.course.course_code} - {enrollment.course.title}: {grade}")
        print(f"GPA: {self.calculate_gpa():.2f}\n")

class Course:
    # Represents a course with a course code and title
    def __init__(self, course_code, title):
        self.course_code = course_code
        self.title = title
        self.enrollments = []

class Enrollment:
    # Links a student to a course and stores the grade
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

# Testing the system
student1 = Student(101, "Alice")
student2 = Student(102, "Bob")

course1 = Course("CS101", "Introduction to Computer Science")
course2 = Course("MATH201", "Calculus I")

# Enroll students in courses
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

# Assign grades
student1.record_grade(course1, 3.7)
student1.record_grade(course2, 3.9)
student2.record_grade(course1, 3.5)

# Display student details and GPA
student1.display_info()
student2.display_info()