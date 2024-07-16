# Time Complexity: O(V+E)
# Space Complexity: O(V+E)
from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    # Create the graph as an adjacency list and initialize the indegree array
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    # Build the graph and fill the indegree array
    for course, prereq in prerequisites:
        graph[prereq].append(course)  # Add an edge from prereq to course
        indegree[course] += 1         # Increment indegree of the course
    
    # Initialize the queue with all courses that have no prerequisites (indegree 0)
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    
    # Count of courses that have been processed
    count = 0
    
    while queue:
        current = queue.popleft()  # Get one course from the queue
        count += 1                 # Increment the processed course count
        
        # For each course dependent on the current course
        for neighbor in graph[current]:
            indegree[neighbor] -= 1  # Decrement the indegree of the dependent course
            if indegree[neighbor] == 0:  # If the dependent course has no more prerequisites
                queue.append(neighbor)   # Add it to the queue
    
    # If all courses have been processed, return True. Otherwise, return False.
    return count == numCourses

# Example usage
numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))  # Output: True
