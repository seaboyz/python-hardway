formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a Peom",
    "Or a song about fear"
))
print(formatter.format(
   "本是后山人",
   "\n偶做前堂客",
   "\n醉舞经阁半卷书",
   "\n坐井说天阔"
))
