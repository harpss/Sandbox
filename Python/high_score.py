highest_score = 0
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    if float(score) > highest_score:
        highest_score = float(score)
        highest_scorer = name
result_f.close()
print("The highest score was: ")
print(highest_score)
print(" , scored by ")
print(name)
