import itertools

tasks = ['a1', 'a2', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'd1', 'd2']

def main():
    perms = itertools.permutations(tasks)
    perms = filter(is_in_order, perms)
    permList = list(perms)
    valid_order = len(permList)
    print("Ordered permutations: ", valid_order)
    print(permList[0]) 
    permList = list(filter(is_valid, permList))
    print(permList[0]) 
    valid_constraint = len(permList)
    print("Valid permutations: ", valid_constraint)

    print(valid_constraint / valid_order)

def is_in_order(perm: list[str]) -> bool:
    if perm.index('a1') > perm.index('a2'):
        return False
    if perm.index('b1') > perm.index('b2') or perm.index('b2') > perm.index('b3'):
        return False
    if perm.index('c1') > perm.index('c2') or perm.index('c2') > perm.index('c3'):
        return False
    if perm.index('d1') > perm.index('d2'):
        return False
    return True

def is_valid(perm: list[str]) -> bool:
    if perm.index('a1') > perm.index('b3'):
        return False
    if perm.index('c2') > perm.index('a2'):
        return False
    if perm.index('d1') > perm.index('b2'):
        return False
    return True

if __name__ == '__main__':
    main()