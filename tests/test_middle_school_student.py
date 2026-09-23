from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    # Assert
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
<<<<<<< HEAD
    assert ellis.gets_transportation == False 
=======
    assert ellis.gets_transportation == False
>>>>>>> d2f37ef157b27f8d31632129f23cfbda982556fb


def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ella"
    grade = "grade 6"
    classes = []

    # Act
    ella = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    summary = ella.summary()

    # Assert
    assert summary == "Ella is a grade 6 enrolled in 0 classes: \nElla has transportation."

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    
    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)
    summary = ellis.summary()
    
    # Assert
    assert "Ellis doesn't have transportation." in summary
    
