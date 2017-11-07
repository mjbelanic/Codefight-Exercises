# split each string to make an array, then select last item of each array
def sortStudents(students):
    students.sort(key= lambda student: student.split()[-1])
    return students