import heapq
import itertools
from typing import Any, Dict

__all__ = ['PriorityQueue', 'PriorityQueueItem']


class PriorityQueueItem:
    """
    Represents an item in the priority queue with a priority, command, and a counter.

    Attributes:
        priority (int): Priority of the item, must be in the range [0, 10].
        command (Any): The command associated with the item.
        count (int): Counter to maintain the order of items with same priority.
    """

    def __init__(self, priority: int, command: Any, count: int):
        self.validate_priority(priority)
        self.priority = priority
        self.command = command
        self.count = count

    def __lt__(self, other):
        """
        Less than comparison for sorting in the priority queue.
        Items are compared based on priority, and then by count.

        Complexity:
            Time: O(1)
        """
        if self.priority == other.priority:
            return self.count < other.count
        return self.priority < other.priority

    @staticmethod
    def validate_priority(priority):
        """
        Validate that the priority is an integer and within the range [0, 10].

        Args:
            priority (int): The priority to be validated.

        Raises:
            ValueError: If the priority is not an integer or not in the range [0, 10].

        Complexity:
            Time: O(1)
        """
        if not isinstance(priority, int):
            raise ValueError("Priority must be an integer")
        if not (0 <= priority <= 10):
            raise ValueError("Priority must be between 0 and 10")


class PriorityQueue:
    """
    A simple priority queue implementation using a min-heap.

    Attributes:
        heap (List[PriorityQueueItem]): The heap that stores the queue items.
        counter (itertools.count): A counter for assigning a unique count to each item.
    """

    def __init__(self):
        self.heap = []
        self.counter = itertools.count()  # Counter to maintain order of insertion

    def push(self, item: Dict):
        """
        Add an item to the priority queue.

        Args:
            item (Dict): A dictionary containing 'command' and 'priority'.

        Complexity:
            Time: O(log n) due to heap insertion
            Space: O(n) as the heap grows with each item
        """
        count = next(self.counter)
        wrapped_item = PriorityQueueItem(item['priority'], item['command'], count)
        heapq.heappush(self.heap, wrapped_item)

    def pop(self):
        """
        Remove and return the highest priority item from the queue.

        Returns:
            Any: The command of the highest priority item.

        Raises:
            IndexError: If the queue is empty.

        Complexity:
            Time: O(log n) due to heap removal
        """
        if self.heap:
            return heapq.heappop(self.heap).command
        raise IndexError("pop from empty priority queue")

    def is_empty(self):
        """
        Check if the priority queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.

        Complexity:
            Time: O(1)
        """
        return len(self.heap) == 0


# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    # Assuming that the lowest numerical priority is the highest priority
    pq.push({'command': 'print("Hello, World!")', 'priority': 2})
    pq.push({'command': 'print("Run other modules")', 'priority': 1})
    pq.push({'command': 'print("Sorting folders by name")', 'priority': 2})
    pq.push({'command': 'print("Restart Computer")', 'priority': 1})
    pq.push({'command': 'print("Look for a file in DB")', 'priority': 5})

    while not pq.is_empty():
        command = pq.pop()
        exec(command)
