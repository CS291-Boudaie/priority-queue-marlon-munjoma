class MinHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if not self.data:
            return None
            priority, item = self.data[0]
        return (item, priority)
     

    def add(self, priority, item):
        self.data.append((priority, item))
        self._bubble_up(len(self.data)-1)
        
    def pop_min(self):
        if not self.data:
            return None

        self.data[0], self.data[-1]=self.data[-1], self.data[0]
        priority, item = self.data.pop()
        if self.data:
            self._bubble_down(0)
        return (item, priority)

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx-1)//2
            if self.data[idx][0]< self.data[parent][0]:
                self.data[idx], self.data[parent]= self.data[parent], self.data[idx]
                idx = parent
            else:
                break
    

    def _bubble_down(self, idx):
        n = len(self.data)
        while True:
            left = 2*idx+1
            right = 2*idx+2
            smallest=idx

            if left < n and self.data[left][0]< self.data[smallest][0]:
            smallest = left
            if right < n and self.data[right][0]< self.data[smallest][0]:
            smallest=right

            if smallest == idx:
                break
            self.data[idx], self.data[smallest]= self.data[smallest], self.data[idx]
            idx = smallest

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