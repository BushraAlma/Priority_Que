# test_priority_queue.py

import unittest
from priority_queue import PriorityQueue, PriorityQueueItem


class TestPriorityQueueItem(unittest.TestCase):
    """Tests for the PriorityQueueItem class."""

    def test_priority_validation(self):
        """Test if the priority validation correctly handles valid and invalid inputs."""
        # Valid priority
        PriorityQueueItem(5, 'test_command', 0)

        # Invalid priorities
        with self.assertRaises(ValueError):
            PriorityQueueItem(11, 'test_command', 0)
        with self.assertRaises(ValueError):
            PriorityQueueItem(-1, 'test_command', 0)
        with self.assertRaises(ValueError):
            PriorityQueueItem('high', 'test_command', 0)


class TestPriorityQueue(unittest.TestCase):
    """Tests for the PriorityQueue class."""

    def setUp(self):
        """Set up a new PriorityQueue for each test."""
        self.pq = PriorityQueue()

    def test_push_and_pop(self):
        """Test adding and removing items from the queue."""
        self.pq.push({'command': 'Test unit test', 'priority': 2})
        self.pq.push({'command': 'printing hello', 'priority': 1})
        self.pq.push({'command': 'organizing folders', 'priority': 4})
        self.pq.push({'command': 'sorting list', 'priority': 7})
        self.assertTrue(not self.pq.is_empty())

        # Test the order of removal based on priority
        self.assertEqual(self.pq.pop(), 'printing hello')  # This item has higher priority (lower number)
        self.assertEqual(self.pq.pop(), 'Test unit test')  # This item has lower priority (higher number)
        self.assertEqual(self.pq.pop(), 'organizing folders')
        self.assertEqual(self.pq.pop(), 'sorting list')
        self.assertTrue(self.pq.is_empty())

    def test_pop_empty_queue(self):
        """Test popping from an empty queue raises an IndexError."""
        with self.assertRaises(IndexError):
            self.pq.pop()


# Run the tests
if __name__ == '__main__':
    unittest.main()
