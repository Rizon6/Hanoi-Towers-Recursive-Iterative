def print_move(start, target):
    print(start, "->", target)

def hanoi(disks, start, target, auxiliary_poles):
    if disks == 1: # base case
        print_move(start, target)
    else:
        if len(auxiliary_poles) == 0:
            raise ValueError("Number of auxiliary poles must be at least 1.")
        
        # Choose the first auxiliary pole available
        aux_pole = auxiliary_poles[0]
        remaining_auxiliary_poles = auxiliary_poles[1:]
        
        # Move top n-1 disks from start to auxiliary pole(s)
        hanoi(disks-1, start, aux_pole, remaining_auxiliary_poles)
        
        # Move the largest disk from start to target
        print_move(start, target)
        
        # Move the n-1 disks from auxiliary pole(s) to target
        hanoi(disks-1, aux_pole, target, remaining_auxiliary_poles)

def iterative_hanoi(disks, start, target):
    aux = 6 - (start + target)  # Calculate the index of the auxiliary peg

    # If the number of disks is even, swap target and auxiliary pegs
    if disks % 2 == 0:
        target, aux = aux, target

    moves = []  # Initialize a list to store moves

    # Generate the sequence of moves
    for move_number in range(1, 2**disks):
        from_peg = (move_number & move_number - 1) % 3
        to_peg = ((move_number | move_number - 1) + 1) % 3
        if disks % 2 == 0:
            from_peg, to_peg = to_peg, from_peg
        move = (from_peg+1, to_peg+1)
        moves.append(move)

    # Print the moves
    for move in moves:
        print_move(move[0], move[1])


iterative_hanoi(3,1,3)
print()
num_disks = 3
num_pegs = 4
start_peg = 1
target_peg = 4
auxiliary_pegs = [i for i in range(1, num_pegs + 1) if i != start_peg and i != target_peg]

hanoi(num_disks, start_peg, target_peg, auxiliary_pegs)