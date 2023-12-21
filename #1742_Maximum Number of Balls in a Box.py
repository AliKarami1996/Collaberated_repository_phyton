low_limit = eval(input("Enter the low limit: "))
high_limit = eval(input("Enter the high limit: "))
ball_number_index_sum = sum(int(index) for index in range(low_limit,high_limit+1))
n = high_limit - low_limit + 1
ball_count = [0] * n

for i in range(low_limit, high_limit + 1):
    box_index = sum(int(index) for index in str(i)) - low_limit
    ball_count[box_index] += 1

max_balls_in_box = max(ball_count)

print(ball_number_index_sum)
print(ball_count)
print(f"The number of balls in the box with the most balls is: {max_balls_in_box}")