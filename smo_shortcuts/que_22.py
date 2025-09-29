count = 0
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if (i + j + k + l) <= 12:
                    count += 1

print(count)
