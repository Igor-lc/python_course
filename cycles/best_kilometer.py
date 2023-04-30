# ver 1
f = list(map(int, open('run.txt', encoding='utf8')))
start, end, best_km = 0, 5, float('inf')

while end <= len(f):
    time = sum(f[start:end])
    if best_km > time:
        best_km = time
    start += 1
    end += 1

print(f"{best_km // 60:02}:{best_km % 60:02}")

# ver 2
run_file = open("run.txt")
times = run_file.readlines()
i = 0
while i < len(times):
    times[i] = int(times[i])
    i += 1
current_km_time = sum(times[:5])
best_km_time = current_km_time

i = 5
while i < len(times):
    current_time = times[i]

    # Вычисляем время, которое вышло за пределы текущего км.
    first_time = times[i - 5]
    # Вычисляем время текущего км.
    current_km_time = current_km_time - first_time + current_time

    # Если текущее время меньше лучшего километра, то обновляем лучшее время.
    if current_km_time < best_km_time:
        best_km_time = current_km_time
    i += 1

print("{:02}:{:02}".format(best_km_time // 60, best_km_time % 60))
