salary = 0.01
target = 10**7
days = 0
total_sum = 0

while total_sum < target:
    days += 1
    total_sum += salary
    salary *= 2

print(f"Det behövs {days} dagar tills man tjänat 10 miljoner kronor.")