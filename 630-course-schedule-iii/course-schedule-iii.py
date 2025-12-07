class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
    
        current_day = 0
        heap = []  # max-heap (store negative for max)
        
        for duration, deadline in courses:
            # Try to take this course
            if current_day + duration <= deadline:
                # Can take it!
                current_day += duration
                heapq.heappush(heap, -duration)  # negative for max-heap
            
            # Can't fit, but maybe swap with longest?
            elif heap and -heap[0] > duration:
                # Remove longest course
                longest = -heapq.heappop(heap)
                current_day -= longest
                
                # Add this shorter course
                current_day += duration
                heapq.heappush(heap, -duration)
        
        return len(heap)
            