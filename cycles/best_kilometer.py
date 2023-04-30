# ver 1
with open('run.txt', encoding='utf8') as f:
    f = list(map(int, f))

start, end, best_time = 0, 5, float('inf')

while end <= len(f):
    time = sum(f[start:end])
    if best_time > time:
        best_time = time
    start += 1
    end += 1

print(f"{best_time // 60:02}:{best_time % 60:02}")

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


'''318. BEST KILOMETER
Difficulty: 6 out of 10
The file run.txt, which is located next to the program, contains information about the running workout. Each line of this file is responsible for the time (in seconds) that the athlete spent to overcome the distance of 200 meters.

Consider an example of such a file:

70
70
67
68
68
65
65
60
61
62
60
63
65
66
67
70
67
68
71
It has 19 entries, which means the athlete ran 19 x 200m = 3800 meters. Since there were ups and downs during the run as well as other factors, the speed on different segments was different.

Write a program that analyses the data and outputs the best time a runner has completed per kilometer. Note that the best kilometer can be anywhere along the course. In this case, the best kilometer is a sequence of 60, 61, 62, 60, 63 or 306 seconds (5 minutes, 6 seconds). This kilometer was between 1800 and 2800 meters.

Data should be output in MM:SS format.

Usage example (for a file from a task):
> python program.py
> 05:06'''
