def read_lines(input_file):
    ans = []
    for line in open(input_file):
        ans.append(line.rstrip('\n'))
    return ans

left_turn = {
    (-1, 0): (0, -1),
    (1, 0): (0, 1),
    (0, -1): (1, 0),
    (0, 1): (-1, 0),
}

right_turn = {
    (-1, 0): (0, 1),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (0, 1): (1, 0),
}