from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent
from school_schedule.middle_school_student import MiddleSchoolStudent
# first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")

# second instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                has_parking_privileges=True,
                clubs=["Algorithms Club"]
            )


# third instance
john = MiddleSchoolStudent(
    "john", '8th grader',[
        "Algebra", 
                        "Writing", 
                        "Contemporary Issues", 
                        "Gym", 
                        "Earth Science", 
                        "Painting"

    ],
    gets_transportation=True
)
# fourt instance
ellis = MiddleSchoolStudent(
    "ellis", "junior",["Painting"], gets_transportation=True
)
students = [quinn, claire, john, ellis]
for student in students:
    print(student.summary())