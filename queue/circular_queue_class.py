class CircularQueueOneSlotEmpty:
    def __init__(self, capacity):
        self.capacity = capacity
        self.N = self.capacity + 1
        self.array = [None] * self.N
        self.front = 0
        self.rear = 0 

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.N

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        self.rear = (self.rear + 1) % self.N
        self.array[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.front = (self.front + 1) % self.N
        item = self.array[self.front]
        self.array[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.array[(self.front + 1) % self.N]

    def size(self):
        return (self.rear - self.front + self.N) % self.N

    def display(self, msg="CircularQueueOneSlotEmpty"):
        print(f"{msg}: front={self.front}, rear={self.rear}, size={self.size()}/{self.capacity}")

        # 논리 순서로 아이템 출력
        items = [] 
        idx = (self.front + 1) % self.N
        for _ in range(self.size()):
            items.append(self.array[idx])
            idx = (idx + 1) % self.N
        print("items =", items)

        # 슬롯 시각화
        print("slots=[", end="")
        for i in range(self.N):
            if self.front < self.rear:
                occupied = (self.front < i <= self.rear)
            else:
                occupied = (i > self.front) or (i <= self.rear)

            if occupied and not self.is_empty():
                val = self.array[i]
            else:
                val = None
            print(val, end="   ")
        print("]")

def quiz_2():
    print("===========Quiz_2=========")
    q = CircularQueueOneSlotEmpty(capacity=8)

    # front = rear = 6
    q.front = 6
    q.rear = 6

    q.enqueue(10)
    q.display("10 삽입 결과")
    q.enqueue(11)
    q.display("11 삽입 결과")
    q.enqueue(12)
    q.display("12 삽입 결과")
    q.enqueue(13)
    q.display("13 삽입 결과")
    q.dequeue()
    q.display("첫 번째 삭제 결과")
    q.dequeue()
    q.display("두 번째 삭제 결과")
    print(f"최종 상태: front={q.front}, rear={q.rear}")
