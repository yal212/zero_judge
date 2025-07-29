def find_permutations(s):
    # Write code here
    if len(s) == 1:
        return [s]

    permutations = []
    for index, char in enumerate(s):
        others = s[:index] + s[index+1:]
        for permutation in find_permutations(others):
            permutations.append(char + permutation)

    return sorted(permutations)
