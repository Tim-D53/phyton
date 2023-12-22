def round(cats):
    # 0 - have not hat
    # 1 - have hat
    cats_list = [0] * cats

    for i in range(1, cats + 1):
        for j in range(i, cats + 1, i):
            if cats_list[j - 1] == 0:
                cats_list[j - 1] = 1
            else:
                cats_list[j - 1] = 0

    total_list_cats_with_hat = []
    for i in range(100):
        if cats_list[i] == 1:
            total_list_cats_with_hat.append(i + 1)
    return total_list_cats_with_hat


cats = 100
print(round(cats))
