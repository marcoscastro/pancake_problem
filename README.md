# Pancake Problem
Solution to the pancake problem.

I love pancakes and you?

The problem of pancakes aims to sort a stack of pancakes with varying sizes.

The ordering of the pancakes are made by a sequence of flips.

A flip consists of inserting a spatula between two pancakes and rotates all the pancakes that are above the spatula.

Each vertex (state) is a stack of pancakes.

![alt tag](https://raw.githubusercontent.com/marcoscastro/pancake_problem/master/images/algorithm.png)

The states that are within the dotted area are part of the fringe of the graph. The border is a priority queue that stores the states that are about to be expanded.

Each state has a total cost that is the sum of the weight of the edge with the cost of the predecessor state.

The code was done in the Python language. In the function "build_pancakes" (file main.py) is possible to pass the amount of pancakes and a difference of size between the pancakes to a better visualization. In the function "run" is possible to pass a time waiting to visualize more slowly.

Looks the animation: https://www.youtube.com/watch?v=kk-_DDgoXfk

A video that to explains  the pancake problem: https://www.youtube.com/watch?v=hq3GyBw4jfo

Execution to 4 pancakes and time_sleep of 1 second:

![alt tag](https://raw.githubusercontent.com/marcoscastro/pancake_problem/master/images/execution.png)
