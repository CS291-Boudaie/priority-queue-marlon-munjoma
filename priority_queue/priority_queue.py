class MinHeap:
    def __init__(self):
        # We'll store elements as tuples: (priority, item)
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if not self.data:
            return None
        return self.data[0]
        # TODO: Return (priority, item) but do NOT remove
        # If empty, return None (or raise an error)
        

    def add(self, priority, item):
        self.data.append((priority, item))
        self._bubble_up(len(self.data)-1)
        # TODO: Add (priority, item) to end of list
        # Then bubble it UP into correct position
        

    def pop_min(self):
        if not self.data:
            return None

        self.data[0], self.data[-1]=self.data[-1], self.data[0]
        min_item = self.data.pop()
        if self.data:
            self._bubble_down(0)
        return min_item
        # TODO: Remove and return the smallest element (priority, item)
        # Steps:
        # 1) swap root with last element
        # 2) pop last element (former root)
        # 3) bubble DOWN new root
    

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx-1)//2
            if self.data[idx][0]< self[parent][0]:
                self.data[idx], self.data[parent]= self.data[parent], self.data[idx]
                idx = parent
            else:
                break
        # TODO: Implement
        # Keep swapping this node with its parent while it has a smaller priority.
        # parent index = (idx - 1) // 2
        # Stop when you reach the root OR parent already has <= priority.
    

    def _bubble_down(self, idx):
        n = len(self.data)
        while True:
            left = 2*idx+1
            right = 2*idx+2
            smallest=idx

            if left<n and self.data[left][0], self.data[smallest][0]:
            smallest = left
            if right < n and self.data[right][0], self.data[smallest][0]:
            smallest=right

            if smallest == idx:
                break
            self.data[idx], self.data[smallest]= self.data[smallest], self.data[idx]
            idx = smallest
            
        # Keep swapping this node downward until the heap property is restored.
        # left child = 2*idx + 1, right child = 2*idx + 2
        # Find the smaller child, then swap if current priority is bigger.
        # Stop when no children exist OR current is <= both children.
        


# Once you have a min heap, the priority queue is pretty straightforward. 
# Make sure you understand what it is doing

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def is_empty(self):
        return self.heap.is_empty()

    def add(self, priority, item):
        self.heap.add(priority, item)

    def pop(self):
        return self.heap.pop_min()

    def peek(self):
        return self.heap.peek()

    def __len__(self):
        return len(self.heap)