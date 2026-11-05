def parts_sums(ls):
    new_ls = ls[:]
    sum_ls = []
    for _ in ls:
        sum_ls.append(sum(new_ls))   # before pop
        new_ls.pop(0)
    sum_ls.append(sum(new_ls))       # extra, after the loop
    return sum_ls