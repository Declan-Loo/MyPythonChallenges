"""
A265	150	
TOWER OF HANOI	

Use recursion to move all the disks to another tower (3 towers):
- One disk can be moved at any given time
- Only the "top" disk can be removed
- No large disk can sit over a small disk	
"""

#Recursive Function
def tower_of_hanoi(n, source, middle, target):
    #Base case
    if n == 1:
        #Move nth disk from source to target
        print("Move disk 1 from", source, "to", target)
        return
    #Move n-1 disks to middle via using target as temporary store.
    tower_of_hanoi(n - 1, source, target, middle)
    print("Move disk", n, "from", source, "to", target)
    #Finally move n-1 disks from middle to target.
    tower_of_hanoi(n - 1, middle, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')
