#reading dataset as numpy array using function genfromtext() by skiping the header part from the file and splitting at ","
dataset = np.genfromtxt("titanic_mod.csv",dtype="int",skip_header=1,delimiter=",")    
total_s_male_fare=0                 #variable for total fare of males survived
s_male_count=0                      #variable for total male survived
ns_male_count=0                     #variable for total non surviving males
total_ns_male_fare=0                #variable for total fare of non surviving males
for i in dataset:                   #loop to iterate through the dataset
    if i[1]==1 and i[3]==1:             #checking surviving males and increamenting the counter variables
        total_s_male_fare+=i[7]
        s_male_count+=1
    if i[1]==0 and i[3]==1:             #comparing non survival and males and increamenting the counter variables
        total_ns_male_fare+=i[7]
        ns_male_count+=1
mean_s_fare=total_s_male_fare/s_male_count              #mean of fares of surviving males
mean_ns_fare=total_ns_male_fare/ns_male_count           #mean of fares of non surviving males

#printing all the desired values according to the question
print(f"Mean of fare paid by male that survived is:- {'%.3f'%mean_s_fare}")
print(f"Mean of fare paid by male that did not survived is:- {'%.3f'%mean_ns_fare}")
print(f"Difference of fare between them is:- {'%.3f'%(mean_s_fare-mean_ns_fare)}")
