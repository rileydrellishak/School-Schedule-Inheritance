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
    name = "Adrian"
    grade = "7th"
    classes = ["Computer"]

    adrian = MiddleSchoolStudent(name, grade, classes)

    assert adrian.name == "Adrian"
    assert adrian.grade == "7th"
    assert adrian.classes == ["Computer"]
    assert not adrian.gets_transportation

def test_middle_school_student_summary_with_transportation():
    name = "Adrian"
    grade = "7th grader"
    classes = ["Computer"]

    adrian = MiddleSchoolStudent(name, grade, classes, True)

    assert adrian.summary() == "Adrian is a 7th grader enrolled in 1 classes: Computer\nAdrian has transportation"

def test_middle_school_student_summary_without_transportation():
    name = "Adrian"
    grade = "7th grader"
    classes = ["Computer"]

    adrian = MiddleSchoolStudent(name, grade, classes)

    assert adrian.summary() == "Adrian is a 7th grader enrolled in 1 classes: Computer\nAdrian doesn't have transportation"
