# Importing Required libraries
import pandas as pd
import csv


# Storing all data in a list
temp_star_data = []
with open("star_data_with_gravity.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        row.pop(0)
        temp_star_data.append(row)

# print(star_data)


headers = temp_star_data[0]
star_data_rows = temp_star_data[1:]
# print(star_data_rows)


# Storing the star data which is under 100 light year distance
star_data_suitable_distance = []
for star_data in star_data_rows:
    try:
        distance = float(star_data[1])
        if(distance <= 100):
            star_data_suitable_distance.append(star_data)
    except:
        distance = float(star_data[1].split(",")[0])
        if(distance <= 100):
            star_data_suitable_distance.append(star_data)

print("No. of planets with distance under 100 light years is {}".format(len(star_data_suitable_distance)))


star_data_suitable_gravity = []

for star_data in star_data_suitable_distance:
    if(float(star_data[4]) > 150 and float(star_data[4]) < 350):
        star_data_suitable_gravity.append(star_data)

print("No. of planets whoose gravity is between 150 to 350 is {}".format(len(star_data_suitable_gravity)))

df = pd.DataFrame(star_data_suitable_gravity, columns = headers)
df.to_csv("final.csv")