from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15, 1.80]
weight = [165.3, 38.4, 60]

bmi = give_bmi(height, weight)
bmi_limit = 26

print(bmi, type(bmi))
print(
    "bmi list: [%s]" % ', '.join(map(str, bmi)) + "\nlimit: " + str(bmi_limit)
)
print(apply_limit(bmi, bmi_limit))
