class ArrayPriorityQueue:

    def __init__(self):
        self.__queue = []

    def insert(self, element: int, priority: int) -> None:
        self.__queue.append((priority, element))

    def extract_max(self) -> int | None:
        if len(self.__queue) == 0:
            return None

        max_index = 0
        for i in range(len(self.__queue)):
            if self.__queue[i][1] > self.__queue[max_index][1]:
                max_index = i

        _, item = self.__queue[max_index]
        return item

    def extract_min(self) -> int | None:
        if len(self.__queue) == 0:
            return None

        min_index = 0
        for i in range(len(self.__queue)):
            if self.__queue[i][1] < self.__queue[min_index][1]:
                min_index = i

        _, item = self.__queue[min_index]
        return item

    def peek(self) -> tuple | None:
        if len(self.__queue) == 0:
            return None

        max_index = 0
        min_index = 0
        for i in range(len(self.__queue)):
            if self.__queue[i][1] > self.__queue[max_index][1]:
                max_index = i

            if self.__queue[min_index][1] < self.__queue[min_index][1]:
                min_index = i

        return self.__queue[min_index][1], self.__queue[max_index][1]
            