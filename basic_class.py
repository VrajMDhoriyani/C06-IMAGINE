class Student:
    school_name = "IMAGIINE-VrajMD"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def average(self):
        """
        Return the average of marks.
        """
        sum = 0
        for i in self.marks:
            sum += i
        return sum/len(self.marks)


    def grade(self):
        """
        Return grade based on average:
        90+  -> A
        75-89 -> B
        50-74 -> C
        Below 50 -> D
        """
        if self.average() > 90:
            return "A"
        elif self.average() < 90 and self.average()>75:
            return "B"
        elif self.average() <75 and self.average()>50:
            return "C"
        else:
            return "D"
        

    def __str__(self):
        """
        Return formatted student details when printed.
        """
        return f'''Name:{self.name}
                   Average:{self.average()}
                   Grade:{self.grade()}
                   School Name:{self.school_name}
        '''

        


# ------------------------
# Test your class below
# ------------------------

if __name__ == "__main__":
    s1 = Student("Alice", [85, 90, 88])
    s2 = Student("Bob", [60, 70, 65])

    print(s1) 
    print(s2)