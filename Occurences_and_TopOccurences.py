import numpy as np                  #importing library numpy

#reading dataset as numpy array using function genfromtext() by skiping the header part from the file and splitting at ","
dataset = np.genfromtxt("titanic_mod.csv",dtype="int",skip_header=1,delimiter=",")
def passengerAge(column_index,passenger_age):               #user-defined function according to the question 
    
    age_count=0
    for i in dataset:                                       #loop to iterate through the dataset
        if passenger_age==i[column_index]:                  #if statement to find specific age in the dataset
            age_count+=1                                    #when found increasing the value of counter variable by 1
    return age_count                                        #returning the value of counter variable
ages = []               #blank list of name ages
for i in dataset:                                           #loop to iterate through dataset
    ages.append(i[4])                                       #appending to list of name ages
ages = set(ages)                                            #converting list into set                                       
occurences = []         #blank list of name occurances
for i in ages:                                              #loop to iterate through the list ages
    occurences.append([i,passengerAge(4,i)])                #appending to list of name occurences
occurences = np.array(occurences)                           #coverting list to numpy array
occurences = occurences[occurences[:,1].argsort()[::-1]]    #sorting the array using argsort()
# print(occurences)
for i in range(0,3):                    #loop for printing the three most frequent ages
    print(f"Passengers aged {occurences[i][0]} accounted for {((passengerAge(4,occurences[i][0])/1046)*100):.3f}% of the passenger population")
