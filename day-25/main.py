# # with open("weather_data.csv", mode="r") as weather_data:
# #     data = weather_data.readlines()
# #
# # for index in range(len(data)):
# #     data[index] = data[index].strip()
# # print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(type(data))
#
# data_dict =data.to_dict()
#
# #print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # print(sum(temp_list)/len(temp_list))
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print(monday_temp[0])
#
# data_dic

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(data.shape)
#print(data.dtypes)

color_series = data["Primary Fur Color"]
print(color_series.value_counts())

#print(data["Primary Fur Color"].nunique())

fur_data = data["Primary Fur Color"].value_counts()

fur_data.to_csv("fur_data.csv")

gray_data = len(data[data["Primary Fur Color"] == "Gray"])
red_data = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_data = len(data[data["Primary Fur Color"] == "Black"])

dic_color = { "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
              "Counts": [gray_data, red_data, black_data]}

pd_color = pd.DataFrame(dic_color)

pd_color.to_csv("fur_data_2.csv")