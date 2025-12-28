class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        
        room_end = [0] * n
        count = [0] * n
        
        for start, end in meetings:
            free_room = -1
            earliest_room = 0
            
            for i in range(n):
                if room_end[i] <= start:
                    free_room = i
                    break
                if room_end[i] < room_end[earliest_room]:
                    earliest_room = i
            
            if free_room != -1:
                room_end[free_room] = end
                count[free_room] += 1
            else:
                duration = end - start
                room_end[earliest_room] += duration
                count[earliest_room] += 1
        best = 0
        for i in range(1, n):
            if count[i] > count[best]:
                best = i
        
        return best
