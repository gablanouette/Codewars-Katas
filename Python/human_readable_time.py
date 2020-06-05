
'''
Human Readable Time
5kyu

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''


# first variation
# def make_readable(seconds):
#     hr, min, sec = 0, 0, 0
#     hr = seconds//3600
#     seconds = seconds % 3600
#     min = seconds//60
#     seconds = seconds % 60
#     sec = seconds

#     return '{:02d}'.format(hr) + ':' + '{:02d}'.format(min) + ':' + '{:02d}'.format(sec)

# second variation; best practice
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

