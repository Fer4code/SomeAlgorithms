def three_sum(r):
    if r is None:
        return 0
    else:
        left = three_sum(r.left)
        right = three_sum(r.right)
        return r.val + r.left + r.right


def are_symetric(r1, r2):
    if r1 is None and r2 is None:
        return True
    elif ((r1 is None) != (r2 is None)) or r1.val != r2.val:
        return False
    else:
        return are_symetric(r1.left, r2.right) and are_symetric(r1.right, r2.left)
            
            

def is_symmetric(r):
    if r is None:
        return True
    return are_symetric(r.left, r.right)
