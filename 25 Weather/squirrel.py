import pandas

#Reading the data
data = pandas.read_csv("Squirrels.csv")
furs = data["Primary Fur Color"]

#Getting the number of colors
gray = len(data[furs == "Gray"])
cinnamon = len(data[furs == "Cinnamon"])
black = len(data[furs == "Black"])

#Creating dictionary with count
data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray,cinnamon,black]
}

#Saving dictionary
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")