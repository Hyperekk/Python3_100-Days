# with open("weather_data.csv","r") as f:
#     data = f.readlines()
    
# import csv
# with open("weather_data.csv","r") as f:
#     data = csv.reader(f)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict() 
# print(data_dict)
temp_list = data["temp"].to_list()

# print(len(temp_list))
# print(data["temp"].mean())

#                 Max value
# print(data["temp"].max())

#Get data from rows----------------------------------
# monday = data[data.day == "Monday"]
# print(monday)
# print(data[data.temp == data["temp"].max()])

#DF from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("example.csv")
print(data)


