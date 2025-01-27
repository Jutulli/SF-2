Year = input()

def is_distinct(string: str):
    for i in string:
        if string.count(i) != 1:
            return False
    return True

while not is_distinct(Year):
    Year = str(int(Year) + 1)

print(int(Year))