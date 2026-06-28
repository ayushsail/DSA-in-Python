# (1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

#   (a) What was the average temperature in first week of Jan

#   (b) What was the maximum temperature in first 10 days of Jan

#   Figure out data structure that is best for this problem
import csv

arr = []
with open("nyc_weather.csv","r") as f :
    line = csv.reader(f)
    next(line)
    for row in line :
        temp = int(row[1])
        arr.append(temp)

print(arr)
print("the average temp in first week of Jan is",(sum(arr[0:6])/len(arr[0:6])),"degree")
print("The maximum temp in first 10 days of Jan is",(max(arr)),"degree")

# The best data structure to use here was a list because all we wanted was access of temperature elements


# (2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

#   (a) What was the temperature on Jan 9?

#   (b) What was the temperature on Jan 4?

#   Figure out data structure that is best for this 


weather_dict = {}
with open("nyc_weather.csv","r") as f :
    line = csv.reader(f)
    next(line)
    for row in line :
        date = row[0]
        temp = int(row[1])
        weather_dict[date] = temp

print(weather_dict)

print(weather_dict["Jan 9"],"degree")
print(weather_dict["Jan 4"],"degree")

# The best data structure to use here was a dictionary (internally a hash table) because we wanted to know temperature for specific day, requiring key, value pair access where you can look up an element by day using O(1) complexity



# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
import string
word_dict = {}
with open("poem.txt", "r") as f :
    data = f.read()
    
# Remove all punctuation
data = data.translate(str.maketrans("", "", string.punctuation))
words = data.split()

# print(words)
count = 0
for word in words :
    for otherword in words :
        if word == otherword :
            count += 1
    word_dict[word] = count
    count = 0

print(word_dict)

# the best data for this problem is dictionary
    