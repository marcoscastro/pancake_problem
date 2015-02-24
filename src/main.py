# encoding:utf-8

# Author: Marcos Castro
# This file implements the solution of pancake problem

'''

A brief explanation

In the pancake problem, we have a stack of pancakes.

You would like to get them in order where the biggest pancake is on the bottom and smallest pancake is on top.

The only way you can do this as you're cooking the pancakes is to insert your spatula at some point in the stack and do a flip.

The cost is the number of pancakes flipped. We have that minimize the number of flips.

Example of a initial state:

  --------
------------
   ------
    ----

Flip with cost 4:

    ----
   ------
------------
  --------

Goal:

    ----
   ------
  --------
------------

The solution uses the concept of fringe (the states on your fringe are the states that are about to expand). You take something off the fringe, you put its children from the successor function on the fringe, and those actions that generated the children have costs as well as result states.

'''

import random, time
from graph import *
from priority_queue import *


# returns a random list of the sizes of pancakes
def build_pancakes(amount_pancakes=4, size_difference=2):

    if(amount_pancakes < 2): # size must be greater or equal than 2
        print('Error: parameter \"amount_pancakes\" must be greater than 2.')
        return None
    elif(size_difference < 1): # size_difference must be greater or equal than 1
        print('Error: parameter \"size_difference\" must be greater than 1.')
        return None

    # this is necessary to make a good alignment on the function "show_pretty_pancakes"
    if((amount_pancakes + size_difference) % 2 != 0):
        size_difference += 1

    # pancake's size begins with 3
    init, limit, list_pancakes = 3, size_difference * amount_pancakes + 3, []

    for size_pancake in range(init, limit, size_difference):
        list_pancakes.append(size_pancake)

    # generates a random list of pancakes
    random_list_pancakes = []
    for i in range(amount_pancakes):
        # choose randomly a element
        pancake = random.choice(list_pancakes)
        # inserts in random_list_pancakes
        random_list_pancakes.append(pancake)
        # removes element chosen of list_pancakes
        list_pancakes.remove(pancake)
    return random_list_pancakes


# returns all the pancakes as a beautiful "string"
def show_pretty_pancakes(list_pancakes):
    # gets max_length_pancake to adjust alignment
    pretty_pancakes, max_length_pancake = '', max(list_pancakes)

    for pancake_lenght in list_pancakes:
        pancake, size_difference = '', (max_length_pancake - pancake_lenght)
        amount_spaces = size_difference / 2
        for i in range(amount_spaces):
            pancake += ' '
        for i in range(pancake_lenght):
            pancake += '-'
        for i in range(amount_spaces):
            pancake += ' '
        pretty_pancakes += pancake + '\n'
    return pretty_pancakes


# returns a list of tuples where each tuple is (state, cost_edge)
def get_states(state, dict_states_predecessors):
    len_state, states = len(state), []

    for i in range(len_state):
        sub_list = state[0:i+1] # gets sublist
        len_sub_list = len(sub_list) # gets lenght sublist
        # gets tail list
        tail_list = state[i+1:len_state]
        # realizes the flip
        # remove the top element (first element)
        top_element = sub_list.pop(0)
        # invert "sub_list"
        sub_list = sub_list[::-1]
        # inserts element of top on end of list
        sub_list.append(top_element)
        # concatenates the two lists
        list_state = sub_list + tail_list
        # inserts the "states" and the edge's cost if the state no exists in "dict_states_predecessors"
        if str(list_state) not in dict_states_predecessors:
            states.append((sub_list + tail_list, i+1))

    if len(states) > 0:
        states.pop(0) # removes first state that is the same "state"
    return states # return all states


# runs algorithm
def run(state, time_sleep=1):
   
    goal_state = state[:] # copy the goal state
    goal_state.sort() # ordering goal_state
    graph = Graph() # creates graph

    # fringe of the graph, fringe is an priority queue, priority is the smaller cost
    fringe = PriorityQueue()

    # append in priority queue, each item is a tuple (node, cumulative_cost)
    fringe.insert((Node(state), 0), 0)

    while not fringe.is_empty(): # while fringe not is empty

        node, cost_node = fringe.remove() # removes node of the fringe

        if node.getState() == goal_state: # verifies if reached the goal
            print(show_pretty_pancakes(node.getState())) # show the stack of pancakes
            return cost_node

        # expands the node (generates states), each neighbor is a tuple (state, cost_edge)
        neighbors = get_states(node.getState(), graph.getStatesPredecessors(node))

        if neighbors:
            print(show_pretty_pancakes(node.getState())) # show the stack of pancakes
            time.sleep(time_sleep) # sleeps some seconds

            for neighbor in neighbors:
                state_neighbor, cost_edge = neighbor # unpack tuple (state, cost_edge)
                neighbor_node = Node(state_neighbor) # creates neighbor node
                graph.setParent(node, neighbor_node, cost_edge) # set parent
                cumulative_cost = cost_node + cost_edge # calculates cumulative cost
                fringe.insert((neighbor_node, cumulative_cost), cumulative_cost) # adds neighbor node on the fringe


if __name__ == "__main__":
    initial_state = build_pancakes(amount_pancakes=4, size_difference=4)
    if(initial_state):
        init_time = time.time()
        total_cost = run(initial_state, time_sleep=1)
        end_time = time.time()
        difference_time = int(end_time - init_time)
        print('Total cost: %s\n' % total_cost)
        print('Time: %s seconds or %2.2f minutes' % (difference_time, (difference_time / 60.0)))