"""-------------------------------------------
 Program Name: Student Course Registration System
 Author: Jonathan Canola
 Date: 04/05/1994
 -------------------------------------------
 Pseudocode: [See suggestions below]
 -------------------------------------------
 Program Inputs: username and password - admin user menu to add, remove, update and search for course - student user menu to add and drop courses
 Program Outputs: Login to either menu or error message if login failed - display searched course - list students registerd for specific course - list couses for a specific student - student id and passwords - List all courses
 -------------------------------------------
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Set


class User(ABC):
    """Abstract base class representing a system user.

    Attributes:
        user_id: Unique login ID for the user.
        password: Password used for authentication.
        name: Display name of the user.
    """

    def __init__(self, user_id: str, password: str, name: str) -> None:
        self._user_id = user_id
        self._password = password
        self._name = name

    @property
    def user_id(self) -> str:
        """Return the user's login ID."""
        return self._user_id

    @property
    def password(self) -> str:
        """Return the user's password."""
        return self._password

    @property
    def name(self) -> str:
        """Return the user's display name."""
        return self._name

    @abstractmethod
    def get_role(self) -> str:
        """Return the role name for the user."""
        raise NotImplementedError


class Student(User):
    """Represents a student user in the registration system."""

    def __init__(self, user_id: str, password: str, name: str) -> None:
        super().__init__(user_id, password, name)
        self._registered_courses: Set[str] = set()

    def get_role(self) -> str:
        """Return the role name for the student."""
        return "Student"

    @property
    def registered_courses(self) -> Set[str]:
        """Return the set of registered course IDs."""
        return self._registered_courses


class Administrator(User):
    """Represents an administrator user in the registration system."""

    def get_role(self) -> str:
        """Return the role name for the administrator."""
        return "Administrator"


class Course:
    """Represents a course in the registration system.

    Attributes:
        course_id: Unique course identifier.
        title: Course title.
        description: Brief course description.
        credits: Number of course credits.
        capacity: Maximum number of students allowed.
    """

    def __init__(
        self,
        course_id: str,
        title: str,
        description: str,
        credits: int,
        capacity: int,
    ) -> None:
        self._course_id = course_id
        self._title = title
        self._description = description
        self._credits = credits
        self._capacity = capacity
        self._registered_students: Set[str] = set()

    @property
    def course_id(self) -> str:
        """Return the course ID."""
        return self._course_id

    @property
    def title(self) -> str:
        """Return the course title."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Set the course title."""
        self._title = value

    @property
    def description(self) -> str:
        """Return the course description."""
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Set the course description."""
        self._description = value

    @property
    def credits(self) -> int:
        """Return the number of credits."""
        return self._credits

    @credits.setter
    def credits(self, value: int) -> None:
        """Set the number of credits."""
        self._credits = value

    @property
    def capacity(self) -> int:
        """Return the maximum course capacity."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        """Set the maximum course capacity."""
        self._capacity = value

    @property
    def registered_students(self) -> Set[str]:
        """Return the set of registered student IDs."""
        return self._registered_students

    def is_full(self) -> bool:
        """Return True if the course has reached capacity."""
        return len(self._registered_students) >= self._capacity

    def seats_remaining(self) -> int:
        """Return the number of remaining seats."""
        return self._capacity - len(self._registered_students)

    def add_student(self, student_id: str) -> None:
        """Register a student in the course.

        Raises:
            ValueError: If the course is full or the student is already enrolled.
        """
        if student_id in self._registered_students:
            raise ValueError("Student is already registered for this course.")
        if self.is_full():
            raise ValueError("Course is full.")
        self._registered_students.add(student_id)

    def remove_student(self, student_id: str) -> None:
        """Drop a student from the course.

        Raises:
            ValueError: If the student is not enrolled in the course.
        """
        if student_id not in self._registered_students:
            raise ValueError("Student is not registered for this course.")
        self._registered_students.remove(student_id)

    def __str__(self) -> str:
        """Return a formatted string describing the course."""
        full_status = "FULL" if self.is_full() else f"Open ({self.seats_remaining()} seats left)"
        return (
            f"{self.course_id} | {self.title} | Credits: {self.credits} | "
            f"Capacity: {len(self.registered_students)}/{self.capacity} | {full_status}\n"
            f"Description: {self.description}"
        )


class RegistrationSystem:
    """Main application class that manages users, courses, and registrations."""

    def __init__(self) -> None:
        self._students: Dict[str, Student] = {}
        self._courses: Dict[str, Course] = {}
        self._admin = Administrator("admin", "password", "System Administrator")
        self._seed_data()

    def _seed_data(self) -> None:
        """Populate the system with sample students and courses."""
        self._students = {
            "s1001": Student("s1001", "pass1001", "Alice Johnson"),
            "s1002": Student("s1002", "pass1002", "Brian Smith"),
            "s1003": Student("s1003", "pass1003", "Carla Davis"),
        }

        self._courses = {
            "CS101": Course("CS101", "Intro to Python", "Learn Python basics and problem solving.", 3, 3),
            "CS201": Course("CS201", "Data Structures", "Study lists, stacks, queues, trees, and graphs.", 4, 2),
            "MATH110": Course("MATH110", "College Algebra", "Review algebraic expressions, functions, and equations.", 3, 4),
        }

    def authenticate_user(self, user_id: str, password: str) -> Optional[User]:
        """Authenticate a user by login ID and password.

        Args:
            user_id: The entered login ID.
            password: The entered password.

        Returns:
            The matching User object if authentication succeeds, otherwise None.
        """
        if user_id == self._admin.user_id and password == self._admin.password:
            return self._admin

        student = self._students.get(user_id)
        if student and student.password == password:
            return student
        return None

    def add_course(self, course: Course) -> None:
        """Add a new course to the system.

        Raises:
            ValueError: If the course ID already exists.
        """
        if course.course_id in self._courses:
            raise ValueError("A course with that ID already exists.")
        self._courses[course.course_id] = course

    def remove_course(self, course_id: str) -> None:
        """Remove a course from the system.

        Raises:
            ValueError: If the course ID does not exist.
        """
        course = self._courses.get(course_id)
        if not course:
            raise ValueError("Course not found.")

        for student_id in list(course.registered_students):
            self._students[student_id].registered_courses.discard(course_id)

        del self._courses[course_id]

    def update_course(
        self,
        course_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        credits: Optional[int] = None,
        capacity: Optional[int] = None,
    ) -> None:
        """Update selected course attributes.

        Raises:
            ValueError: If the course is missing or the new capacity is invalid.
        """
        course = self._courses.get(course_id)
        if not course:
            raise ValueError("Course not found.")

        if capacity is not None and capacity < len(course.registered_students):
            raise ValueError("Capacity cannot be smaller than current enrollment.")

        if title is not None:
            course.title = title
        if description is not None:
            course.description = description
        if credits is not None:
            course.credits = credits
        if capacity is not None:
            course.capacity = capacity

    def search_courses(self, query: str) -> List[Course]:
        """Search courses by course ID or title.

        Args:
            query: Search text entered by the user.

        Returns:
            A list of matching Course objects.
        """
        query = query.strip().lower()
        return [
            course
            for course in self._courses.values()
            if query in course.course_id.lower() or query in course.title.lower()
        ]

    def register_student_for_course(self, student_id: str, course_id: str) -> None:
        """Register a student for a course.

        Raises:
            ValueError: If the student or course is missing, or registration fails.
        """
        student = self._students.get(student_id)
        course = self._courses.get(course_id)

        if not student:
            raise ValueError("Student not found.")
        if not course:
            raise ValueError("Course not found.")

        course.add_student(student_id)
        student.registered_courses.add(course_id)

    def drop_student_from_course(self, student_id: str, course_id: str) -> None:
        """Drop a student from a course.

        Raises:
            ValueError: If the student or course is missing, or drop fails.
        """
        student = self._students.get(student_id)
        course = self._courses.get(course_id)

        if not student:
            raise ValueError("Student not found.")
        if not course:
            raise ValueError("Course not found.")

        course.remove_student(student_id)
        student.registered_courses.discard(course_id)

    def list_all_courses(self) -> List[Course]:
        """Return all courses sorted by course ID."""
        return sorted(self._courses.values(), key=lambda course: course.course_id)

    def get_student_courses(self, student_id: str) -> List[Course]:
        """Return all courses registered by a specific student.

        Raises:
            ValueError: If the student does not exist.
        """
        student = self._students.get(student_id)
        if not student:
            raise ValueError("Student not found.")
        return sorted((self._courses[course_id] for course_id in student.registered_courses), key=lambda course: course.course_id)

    def get_course_students(self, course_id: str) -> List[Student]:
        """Return all students registered in a specific course.

        Raises:
            ValueError: If the course does not exist.
        """
        course = self._courses.get(course_id)
        if not course:
            raise ValueError("Course not found.")
        return sorted((self._students[student_id] for student_id in course.registered_students), key=lambda student: student.user_id)

    def list_student_credentials(self) -> List[Student]:
        """Return all students sorted by ID."""
        return sorted(self._students.values(), key=lambda student: student.user_id)


def get_non_empty_input(prompt: str) -> str:
    """Prompt until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_int(prompt: str) -> int:
    """Prompt until the user enters a positive integer."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid number. Please enter a valid integer.")


def pause() -> None:
    """Pause until the user presses Enter."""
    input("\nPress Enter to continue...")


def display_courses(courses: List[Course]) -> None:
    """Display a list of courses in a readable format."""
    if not courses:
        print("No courses found.")
        return

    print("\n--- Course List ---")
    for course in courses:
        print(course)
        print("-" * 70)


def admin_menu(system: RegistrationSystem) -> None:
    """Display and process the administrator menu."""
    while True:
        print(
            "\n=== Administrator Menu ===\n"
            "1. Add new course\n"
            "2. Remove course\n"
            "3. Update course details\n"
            "4. Search for course\n"
            "5. List students in a course\n"
            "6. List courses for a student\n"
            "7. List all student IDs and passwords\n"
            "8. List all courses\n"
            "9. Logout"
        )

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                course_id = get_non_empty_input("Course ID: ").upper()
                title = get_non_empty_input("Title: ")
                description = get_non_empty_input("Description: ")
                credits = get_positive_int("Credits: ")
                capacity = get_positive_int("Capacity: ")
                system.add_course(Course(course_id, title, description, credits, capacity))
                print("Course added successfully.")

            elif choice == "2":
                course_id = get_non_empty_input("Enter course ID to remove: ").upper()
                system.remove_course(course_id)
                print("Course removed successfully.")

            elif choice == "3":
                course_id = get_non_empty_input("Enter course ID to update: ").upper()
                print("Leave a field blank if you do not want to change it.")
                title = input("New title: ").strip()
                description = input("New description: ").strip()
                credits_text = input("New credits: ").strip()
                capacity_text = input("New capacity: ").strip()

                credits = int(credits_text) if credits_text else None
                capacity = int(capacity_text) if capacity_text else None

                system.update_course(
                    course_id,
                    title=title or None,
                    description=description or None,
                    credits=credits,
                    capacity=capacity,
                )
                print("Course updated successfully.")

            elif choice == "4":
                query = get_non_empty_input("Enter course title or ID to search: ")
                display_courses(system.search_courses(query))

            elif choice == "5":
                course_id = get_non_empty_input("Enter course ID: ").upper()
                students = system.get_course_students(course_id)
                print(f"\nStudents registered for {course_id}:")
                if not students:
                    print("No students are registered for this course.")
                else:
                    for student in students:
                        print(f"- {student.user_id}: {student.name}")

            elif choice == "6":
                student_id = get_non_empty_input("Enter student ID: ").lower()
                courses = system.get_student_courses(student_id)
                print(f"\nCourses registered by {student_id}:")
                display_courses(courses)

            elif choice == "7":
                print("\nStudent IDs and Passwords:")
                for student in system.list_student_credentials():
                    print(f"- ID: {student.user_id} | Password: {student.password}")

            elif choice == "8":
                display_courses(system.list_all_courses())

            elif choice == "9":
                print("Logging out of administrator account.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")

        pause()


def student_menu(system: RegistrationSystem, student: Student) -> None:
    """Display and process the student menu."""
    while True:
        print(
            f"\n=== Student Menu ({student.name}) ===\n"
            "1. Register for course\n"
            "2. Drop course\n"
            "3. List my courses\n"
            "4. List all courses\n"
            "5. Logout"
        )

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                display_courses(system.list_all_courses())
                course_id = get_non_empty_input("Enter course ID to register: ").upper()
                system.register_student_for_course(student.user_id, course_id)
                print("Successfully registered for the course.")

            elif choice == "2":
                course_id = get_non_empty_input("Enter course ID to drop: ").upper()
                system.drop_student_from_course(student.user_id, course_id)
                print("Successfully dropped the course.")

            elif choice == "3":
                courses = system.get_student_courses(student.user_id)
                print("\nYour registered courses:")
                display_courses(courses)

            elif choice == "4":
                display_courses(system.list_all_courses())

            elif choice == "5":
                print("Logging out of student account.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")

        pause()


def main() -> None:
    """Run the course registration system application."""
    system = RegistrationSystem()

    while True:
        print(
            "\n=== Student Course Registration System ===\n"
            "1. Login\n"
            "2. Exit"
        )

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_id = get_non_empty_input("User ID: ")
            password = get_non_empty_input("Password: ")
            user = system.authenticate_user(user_id, password)

            if user is None:
                print("Invalid username or password.")
                pause()
                continue

            print(f"Welcome, {user.name}! You are logged in as {user.get_role()}.")

            if isinstance(user, Administrator):
                admin_menu(system)
            elif isinstance(user, Student):
                student_menu(system, user)

        elif choice == "2":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
