def hanoi(disks, source, helper, destination):
    # Base Destination
    if disks == 1:
        print('Disk {} moves from {} tower to tower {}.'.format(disks, source, destination))
        return
    
    # Recursive calls in which function calls itself
    hanoi(disks -1, source, destination, helper)
    print('Disks {} moves from tower {} to tower {}.'.format(disks, source,destination))
    hanoi(disks -1, helper, source, destination)



'''
Tower Names passed as arguments:
SOurce : A
Helper : B
Destination : C
'''

#Actual Function Call
if __name__ == "__main__":
    disks = int(input("Enter the Number of disks to be displaced: "))
    hanoi(disks, 'A', 'B', 'C')
