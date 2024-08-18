import enum


class SemesterType(enum.Enum):
    fall = "fall"
    spring = "spring"
    summer = "summer"

class PaperSession(enum.Enum):
    mid1 = "mid1"
    mid2 = "mid2"
    final = "final"

class PaperType(enum.Enum):
    lab = "lab"
    theory = "theory"
