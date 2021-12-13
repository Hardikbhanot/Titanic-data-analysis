#reading dataset as numpy array using function genfromtext() by skiping the header part from the file and splitting at ","
dataset = np.genfromtxt("titanic_mod.csv",dtype="int",skip_header=1,delimiter=",")
max_sibling=0                           #variable for highest number of sibling
cheapest_fare=300                       #variable for lowest fare 
total_parch=0                           #varibale for total parents and children
total_passenger=0                       #variable for total passengers
fares=[]                                #List to store the fares
for i in dataset:                       #loop to iterate through the dataset
    total_parch+=i[6]                   #increasing the value of counter variable according to data set
    total_passenger+=1                  #increasing the value of counter variable according to data set
    fares.append(i[7])                  #appending the fares to the list
    mean_parch=total_parch/total_passenger  #Mean of total parent and children
    if i[7]<cheapest_fare and i[7]>0:       #checking if cheapest fare earlier is less than this value and is greater than 1
        cheapest_fare=i[7]                  #updating cheapest fare value
    if max_sibling<=i[5]:                   #comparing max sibling value
        max_sibling=i[5]
fares.sort()                    #sorting fares 
fare_percentile=np.percentile(fares,50)         #50th percentile of fares

#printing all the desired values according to the question
print(f"Highest value of number of siblings and/or spouses onboard are {max_sibling}")        
print(f"50th percentile value of fare paid is {fare_percentile}")
print(f"Cheapest non-zero fare paid are {cheapest_fare}")
print(f"Mean value of parents and/or children onboard is {'%.2f'%mean_parch}")
