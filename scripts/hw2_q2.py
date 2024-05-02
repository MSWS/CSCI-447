import itertools
instructions = []

def main():
    for thread in range(3):
        for i in range(1, 4):
            instructions.append(chr(65 + thread)+"_"+str(i))

    perms = itertools.permutations(instructions)
    perms = filter(filter_valid, list(perms))

    ls = list(perms)
    print(ls)
    print(len(ls))

def filter_valid(s: list[str]) -> bool:
    for thread in range(3):
        for i in range(2, 4):
            t = chr(65 + thread)
            if s.index(t + "_" +str(i)) < s.index(t +"_" + str(i - 1)):
                return False
    return True

if __name__ == "__main__":
    main()