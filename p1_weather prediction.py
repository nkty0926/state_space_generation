"""
Author : Tae Yong Namkoong
Title : p1_weather.py
"""
import pandas as panda
import os

column = ["DATE", "PRCP", "TMAX", "TMIN", "RAIN"]

#return the Manhattan distance between two dictionary data points from the data set.
def manhattan_distance(data_point1, data_point2):
    # use Manhattan distance function in 2D to compute distance
    distance = (abs(data_point1["PRCP"] - data_point2["PRCP"]) +
               abs(data_point1["TMAX"] - data_point2["TMAX"]) +
               abs(data_point1["TMIN"] - data_point2["TMIN"]))
    return distance

# return a list of data point dictionaries read from the specified file.
def read_dataset(filename):
    if not os.path.exists(filename): #check if file exists
        filename = os.path.join("..", filename) #concantenate path components
    file = open(filename,"r") #open file to read
    data = file.read() #get data from file
    datapoints = data.strip("\n").split("\n")  #remove leading/trailing spaces
    datapoints = [row.split(" ") for row in datapoints] #split each line by spaces to read data line by line
    dataframe = panda.DataFrame(datapoints, columns=column) #create pandas dataframe
    dataframe["TMAX"] = dataframe["TMAX"].astype(float)#convert to float
    dataframe["PRCP"] = dataframe["PRCP"].astype(float)
    dataframe["TMIN"] = dataframe["TMIN"].astype(float)
    datalist = dataframe.to_dict('records') #create list with one dictionary for each line

    return datalist

# return a prediction of whether it is raining or not based on a majority vote of the list of neighbors.
def majority_vote(nearest_neighbors):
    count = 0 #initialize count to 0
    for neighbor in nearest_neighbors: #for each neighbor in the list
        if neighbor["RAIN"] == "TRUE": #increment count if RAIN is true
            count += 1
    if count / len(nearest_neighbors) >= 0.5: #if a tie occurs, or greater than 50%, return TRUE
            return "TRUE"
    else:
        return "FALSE" #else return false

# using the above functions, return the majority vote prediction for whether it's raining or not on the provided test point.
def k_nearest_neighbors(filename, test_point, k, year_interval):
    data = read_dataset(filename) # return a list of data point dictionaries read from the specified file
    neighbors = list() #create new list
    year = int(test_point["DATE"][:4]) #slice first 4 chars of date
    for row in data: #for each row in list
        if row["DATE"][:4] == "" or row["DATE"][:4] == " ": # ignore missing data
            continue
        else:
            valid_year = int(row["DATE"][:4]) # gets year in int
            # filter out the invalid
            # data points that are interval or more years away from the input test point in terms of the year values
            if valid_year in range(year - year_interval + 1, year + year_interval):
                neighbors.append(row) #after filtering, append data to neighbors list

    neighbors.sort(key=lambda x:manhattan_distance(x,test_point)) #find closest k valid neighbors
    return majority_vote(neighbors[:k]) #return majority_vote on the filtered/sorted neighbors list

