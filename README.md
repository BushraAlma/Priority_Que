## Contents

- `interview_questions`: A collection of interview questions that do not require programming solutions.
- `priority_queue_task`: This folder contains the implementation of a priority queue in Python, along with its unit tests.


## PriorityQueue Implementation in Python

## Overview
This repository contains a simple yet efficient implementation of a priority queue in Python. The priority queue is implemented using a min-heap and can handle elements with a defined priority. It's designed to process elements with a higher priority (lower numerical value) before those with a lower priority (higher numerical values)

## Features
Customizable priority for each element
Elements with the same priority are processed in the order of arrival
Efficient insertion and removal operations

## Installation
Clone the repository to your local machine:
```
git clone https://github.com/BushraAlma/ILM.git
cd ILM
```

## Usage
#### PriorityQueue Class
The PriorityQueue class is the main class that implements the priority queue. To use it, simply import and instantiate the class, then use its methods to interact with the queue.

#### Example

```
from priority_queue import PriorityQueue

# Create a priority queue instance
pq = PriorityQueue()

# Add items to the queue
pq.push({'command': 'Command1', 'priority': 2})
pq.push({'command': 'Command2', 'priority': 1})

# Pop an item from the queue
command = pq.pop()
print(command)  # Outputs: Command2 (as it has a higher priority)
```

To run the tests for the priority queue, execute the following command:
```
python test_priority_queue.py
```

## Contributing
Contributions to this project are welcome! Please follow these steps to contribute:

Fork the repository
```
Create a new branch for your feature or bug fix.
Commit your changes and push them to your fork.
Submit a pull request with a clear description of your changes.
```

## License
This project is open source and available under the MIT License.

