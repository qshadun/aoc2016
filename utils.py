def read_lines(input_file):
    ans = []
    for line in open(input_file):
        ans.append(line.rstrip('\n'))
    return ans