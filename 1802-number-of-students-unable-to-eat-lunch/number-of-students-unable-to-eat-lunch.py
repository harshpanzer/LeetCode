class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length=len(students)
        count=0
        for i in range(length):
            for j in range(length):
                try:
                    if(students[0]==sandwiches[0]):
                        students.pop(0)
                        sandwiches.pop(0)
                    elif(students[0]!=sandwiches[0]):
                        a=students[0]
                        students.pop(0)
                        students.append(a)
                except:
                    return len(students)
        return len(students)