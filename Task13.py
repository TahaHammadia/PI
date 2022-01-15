class school13:

    def __init__(self, studs):
        """
        studs is the list of lists of students. Each list contains the students who have ranked the school at the i^th position.
        """
        self.studs = studs

class student13:

    def __init__(self, group):
        self.group = group


def affect(n, schools):
    """
    n is the number of students which is supposed to be known
    """

    cpt = n # cpt counts the number of students who do not have a school yet
