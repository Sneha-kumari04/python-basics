"""
Problem: Print numbers starting from 1 and stop when 17 occurs.
Approach: Using a infinite-loop, print numbers sequentially
"""
i = 1
while True:
    if i == 17:
        break # Break statements are used to terminate the loop immediately when condition is met.
    print(i)
    i += 1
