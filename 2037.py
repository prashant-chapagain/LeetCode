class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        count = 0
        seats = sorted(seats)
        students = sorted(students)
        for i in range(len(seats)):
            count = count + abs(seats[i]-students[i])
        return count
        