for i in range(1, 101):

    if i == 1:
        continue

    count = 0

    for j in range(2, (i // 2) + 1):

        if i % j == 0:
            count += 1

        if count > 1:
            break

    if count == 0:
        print(i, end=" ")
