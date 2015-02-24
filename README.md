# Pancake Problem
Solution to the pancake problem.

I love pancakes and you? Bill Gates too likes pancakes:

![alt tag](http://1.bp.blogspot.com/-ZnmgPPJ5upw/VOuGuwa8H0I/AAAAAAAAESg/gA5BrHV_zeM/s1600/image.png)

The problem of pancakes aims to sort a stack of pancakes with varying sizes.

The ordering of the pancakes are made by a sequence of flips.

A flip consists of inserting a spatula between two pancakes and rotates all the pancakes that are above the spatula.

Each vertex (state) is a stack of pancakes.

![alt tag](http://1.bp.blogspot.com/--4J5R_yFAKw/VOuHxdz1FNI/AAAAAAAAESo/j1akIvSt_qM/s1600/algorithm.png)

The states that are within the dotted area are part of the fringe of the graph. The border is a priority queue that stores the states that are about to be expanded.

Each state has a total cost that is the sum of the weight of the edge with the cost of the predecessor state.

![alt tag](http://2.bp.blogspot.com/-u0-RNtoPM-Q/VOuIsUGNxRI/AAAAAAAAESw/er-seftftq0/s1600/image.png)

The code was done in the Python language. In the function "build_pancakes" (file main.py) is possible to pass the amount of pancakes and a difference of size between the pancakes to a better visualization. In the function "run" is possible to pass a time waiting to visualize more slowly.

Looks the animation: https://www.youtube.com/watch?v=kk-_DDgoXfk

A video that to explains  the pancake problem: https://www.youtube.com/watch?v=hq3GyBw4jfo

Execution to 4 pancakes and time_sleep of 1 second:

![alt tag](http://4.bp.blogspot.com/-kiwBznv1iGc/VOx7XhlK_2I/AAAAAAAAETA/6w1TeH2vk6Y/s1600/execution.png)
