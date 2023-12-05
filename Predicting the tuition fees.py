year1 = 2023
tuition = 10000
rate = 1.05
total_cost = 0

while tuition <= 20000:

    year1 += 1
    tuition = tuition * rate

    print("Year", year1, tuition)


    for _ in range(4):
    total_cost += tuition
    year1 += 1
    tuition *= rate
    print("Year", year1, tuition)