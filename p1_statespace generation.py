"""
Author : Tae Yong Namkoong
Title : p1_statespace.py
"""
#returns a copy of state which fills the jug corresponding to the index in which (0 or 1) to its maximum capacity. Do not modify state.
def fill(state, max, which):
    jug = [i for i in state] # create new list for a copy of state
    jug[which] = max[which] # fill jug to index in which to max capacity
    return jug

#returns a copy of state which empties the jug corresponding to the index in which (0 or 1). Do not modify state.
def empty(state,max,which):
    jug = [i for i in state] # create new list for a copy of state
    jug[which] = 0 # empty jug to index in which to max capacity
    return jug

#function to transfer from given jug to given jug
def xfer(state,max,source,dest):
    jug = [i for i in state] # create new list for transfer
    while jug[source] > 0 and jug[dest] < max[dest]: #pour at index source until source is empty or dest is full
        jug[dest] += 1 # increment dest after transfer
        jug[source] -= 1  # decrement source after transfer
    return jug

#function to return list of unique successors states of given state
def succ(state,max):
    succ = set() # declare new set
    # 1. generating fill operation on current state
    if state not in fill(state,max,0):
        succ.add(tuple(fill(state,max,0)))
    if state not in fill(state,max,1):
        succ.add(tuple(fill(state,max,1)))

    # 2. generating empty operation on current state
    succ.add(tuple(empty(state,max,0)))
    succ.add(tuple(empty(state,max,1)))

    # 3. generating xfer operation on current state
    if state not in xfer(state,max,0,1):
        succ.add(tuple(xfer(state, max, 0,1)))
    if state not in xfer(state,max,1,0):
        succ.add(tuple(xfer(state, max, 1,0)))

    for f in list(succ): #prints the list of unique successor states of the current state in any order
        print(list(f))

