import sys
import time

# ver 1
seconds = int(sys.argv[1])  # 01:16:29
hours = seconds // 60 // 60
minutes = seconds // 60 % 60
sec = seconds - minutes * 60 - hours * 3600
if hours < 1 and minutes < 1:
    print(f'{sec:02d}')
elif hours < 1:
    print(f'{minutes:02d}:{sec:02d}')
else:
    print(f'{hours:02d}:{minutes:02d}:{sec:02d}')

# ver 2
seconds = int(sys.argv[1])
t = ""
h = int(seconds / 3600)

if h:
    if h <= 9:
        t += "0{}:".format(h)
    else:
        t += "{}:".format(h)
m = int((seconds - h * 3600) / 60)

if m or (not m and h):
    if m <= 9:
        t += "0{}:".format(m)
    else:
        t += "{}:".format(m)
s = (seconds - h * 3600 - m * 60)
if s <= 9:
    t += "0{}".format(s)
else:
    t += "{}".format(s)
print(t)


# ver 3
seconds = int(sys.argv[1])
t = ""
h = seconds // 3600
t += "{:02d}:".format(h) if h else ""
m = (seconds - h * 3600) // 60
t += "{:02d}:".format(m) if m or (not m and h) else ""
s = seconds - h * 3600 - m * 60
t += "{:02d}".format(s)
print(t)


# ver 4
seconds = int(sys.argv[1])
struct_time = time.gmtime(seconds)
format_time = time.strftime("%H:%M:%S", struct_time)
zero = format_time.startswith("00:")

while zero:
    format_time = format_time[3:]
    zero = format_time.startswith("00:")

print(format_time)


# ver 5
seconds = int(sys.argv[1])
struct_time = time.gmtime(seconds)

if seconds < 60:
    time_format = "%S"
elif seconds < 3600:
    time_format = "%M:%S"
else:
    time_format = "%H:%M:%S"

format_time = time.strftime(time_format, struct_time)

print(format_time)
