class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        
        last=0
        
        while len(students)>0 and last<len(students):
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                last=0
            else:
                students.append(students.pop(0))
                last+=1
        
        
        return len(students)
            