def toCelcius(F):
    return round((F-32) * (5/9), 2)

data = open('Assignment3\data.txt', "r")
temp_dict = {}

lstData = data.readlines()
for i in range(5,16):
    elements = lstData[i]
    elements = elements.replace("\n", "")
    elements = elements.split("\t")

    year = int(elements[0])
    farenheight_lst = elements[1].split("    ")

    cel_list = []
    for c in farenheight_lst:
        cel_list.append(toCelcius(float(c)))

    temp_dict[year] = cel_list

#---------------------------------------------------------------------------------

def topThreeYears(temp: dict):
    avg_dict = temp.copy()
    averages = []
    top_values = []
    year_lst = []
    
    #Calculates average for all keys
    for key in avg_dict.keys():
        avg = round(sum(avg_dict[key])/len(avg_dict[key]), 2)
        avg_dict[key] = avg
        averages.append(avg)

    #Finds the top 3
    for i in range(3):
        avg = max(averages)
        top_values.append(avg)
        averages.remove(avg)

        for key in avg_dict.keys():
            if avg_dict[key] == avg:
                year_lst.append(key)

    return year_lst

#---------------------------------------------------------------------------------

month_dict = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12
}

def avgTempMonth(temp: dict, month: str):
    month_number = month_dict[month]

    values = []
    for year in temp.keys():
        values.append(temp[year][month_number])
    return round(sum(values)/len(values), 2)

#---------------------------------------------------------------------------------

def belowFreezing(temp: dict):
    freezing_months = set()
    for year in temp.keys():
        for index, value in enumerate(temp[year]):
            if value <= 0:
                freezing_months.add(list(month_dict.keys())[index])

    return freezing_months

print(belowFreezing(temp_dict))

#---------------------------------------------------------------------------------

data_celsius = open('Assignment3\data_celsius.txt', 'w')

for i in range(4):
    data_celsius.write(lstData[i]) 

for key in temp_dict.keys():
    line = str(key) + "\t"
    for value in temp_dict[key]:
        line += str(value) + " " * (4 + 4 - len(str(value)))
    line += "\n"

    data_celsius.write(line)
