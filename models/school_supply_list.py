class SchoolSupplyList:
    def __init__(
        self,
        school_name: str,
        grade: str,
        school_year: str,
        student_name: str = "",
        id: int | None = None
    ) -> None:
        self.school_name = school_name
        self.grade = grade
        self.school_year = school_year
        self.student_name = student_name
        self.id = id