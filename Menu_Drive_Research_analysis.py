import math
import numpy as np

# driver code
# Answer to ques 6
def main():
    
    #reading dataset as numpy array using function genfromtext() by skiping the header part from the file and splitting at ","
    dataset = np.genfromtxt("titanic_mod.csv",skip_header=1,delimiter=",")
    print('''
        Main Menu
        
        1. Compute Correlation
        2. Ranked List of 20 Oldest Survivors by Passenger Cabin Class Number
        3. Ranked List of 20 Female Survivors by Highest Non-Self Family Member Onboard Count and then by Highest fare
        0. Exit
        ''')
    option=int(input("Enter your option:"))     #taking user's choice 
    if option==1:
        correlation(dataset)            #calling function to find correlation between two values
    elif option==2:
        oldest_survivor(dataset)        #calling function to find ranked list of 20 oldest survivor by their class
    elif option==3:
        female_survivor(dataset)        #calling function to find ranked list of 20 female passengers with highest number of family members and by highest fare
    elif option==0:
        exit()

#Answer to question 7
def correlation(dataset):               #function to compute correlation
    print("List of header names for performing correlation")
    print('''
            0. passenger_id
            1. survived
            2. p_class
            3. gender
            4. age
            5. sibsp
            6. parch
            7. fare ''')
    header_dict={0:"passenger_id",1:"survived",2:"p_class",3:"gender",4:"age",5:"sibsp",6:"parch",7:"fare"}
    first_quan=int(input("Enter the number for first quantity"))            #first quantity to compare
    second_quan=int(input("Enter the number for second quantity"))          #second quantity to compare
    first_quan_list=[]                  #list of first quantity
    second_quan_list=[]                 #list of second quantity 

    for i in dataset:
        first_quan_list.append(i[first_quan])           #adding first quantity to the list
        second_quan_list.append(i[second_quan])         #adding second quantity to the list
        numerator = 0                                   #numerator of correlation
        first_quan_list_mean= np.mean(first_quan_list)          #mean of first list of first quantity
        second_quan_list_mean = np.mean(second_quan_list)       #mean of first list of second quantity
        sigma_M1=0          #Σ(x-x(mean))
        sigma_M2 = 0        #Σ(y-y(mean))
        for i in range(0,len(first_quan_list)):
            M1 = (first_quan_list[i]-first_quan_list_mean)      # (x-x(mean))
            M2 = (second_quan_list[i]-second_quan_list_mean)    # (y-y(mean))
            product = M1*M2             #(x-x(mean))*(y-y(mean))
            numerator += product        #Σ(x-x(mean))*(y-y(mean))
            sigma_M1 += M1**2           #Σ(x-x(mean))^2
            sigma_M2 += M2**2           #Σ(y-y(mean))^2
            

    denominator = math.sqrt(sigma_M1*sigma_M2)      # √((Σ(x-x(mean))^2)-(Σ(x-x(mean))^2))

    correlation = numerator/denominator             #(Σ(x-x(mean))*(y-y(mean))) / √((Σ(x-x(mean))^2)-(Σ(x-x(mean))^2))
    
    print('The correlation between {} and {} is '.format(header_dict[first_quan],header_dict[second_quan]),'%.3f'%correlation)       #printing the value of correaltion(rounded off to 3 decimal places)


#answer to question 8
def oldest_survivor(dataset):           #function to display 20 oldest survivor of specific passenger cabin class
    passenger_cabin_class=int(input("Enter the passenger cabin class number (1 to 3): "))               #taking input of passenger cabin class
    np.set_printoptions(suppress=True)                                  #using set_printoptions() function to remove the extra zeros
    survivor=[]                                                         #blank list
    for i in dataset:                                   #loop to iterate through the dataset
        if 1==i[1] and passenger_cabin_class==i[2]:                 #checking the cabin class and passenger is alive 
            survivor.append(i)                                      #if above condition satisfy appending to the list

    sorted_list = sorted(survivor, key=lambda x:x[4],reverse=True)      #sorting the list on the basis of age
    sorted_list = np.array(sorted_list)                                 #converting the list into numpy array

    #printing the output in the desired format 
    print("List of 20 Oldest Survivors for Passenger Cabin Class Number ",passenger_cabin_class,"\n")
    print('passenger_id\tsurvived\tpclass\t\tgender\t\t age\t\t sibsp\t\t parch\t\t fare')
    for i in range(0,20):
        print('%.0f'%sorted_list[i][0],'\t\t','%.0f'%sorted_list[i][1],'\t\t','%.0f'%sorted_list[i][2],'\t\t','%.0f'%sorted_list[i][3],'\t\t','%.0f'%sorted_list[i][4],'\t\t','%.0f'%sorted_list[i][5],'\t\t','%.0f'%sorted_list[i][6],'\t\t',sorted_list[i][7])

#answer to question 9
def female_survivor(dataset):               #function to identify the female survivor with large number of family members on the ship
    newNump = lambda val1,val2: val1+val2               #lambda function (one liner function)
    new_column = []                                     #blank list
    for i in dataset:                            #loop to iterate through the dataset
        col = newNump(i[5],i[6])                
        new_column.append(col)                  #appending specific data to the list from dataset
    dataset = np.column_stack((dataset, new_column))        

    female_survivors = []                       #blank list 
    for i in dataset:                           #loop to iterate through the dataset
        if i[3] == 0 and i[1] == 1:             
            female_survivors.append(i)          #appending the specific data from the dataset to list 


    female_survivors = np.array(female_survivors)                                   #coverting the list into numpy array
    female_survivors = female_survivors[female_survivors[:,8].argsort()[::-1]]      #sorting numpy array using argsort according to non self family member

    top_female_survivors = []                               #blank list
    for i in range(0,20):                                   #loop to iterate through the dataset
        top_female_survivors.append(female_survivors[i])    #appending the top 20 female surviour

    #sorting on the basis of highest to lowest fares in case of clashes in family member count  
    top_6 = []                          #list of female survivors with 6 family members                     
    top_5 = []                          #list of female survivors with 5 family members
    top_4 = []                          #list of female survivors with 4 family members
    top_3 = []                          #list of female survivors with 3 family members
    #adding element to the desired list 
    for i in top_female_survivors:      
        if i[8]==6:
            top_6.append(i)
        elif i[8]==5:
            top_5.append(i)
        elif i[8]==4:
            top_4.append(i) 
        elif i[8]==3:
            top_3.append(i)  

    #converting the list to numpy array
    top_6 = np.array(top_6)
    top_5 = np.array(top_5)
    top_4 = np.array(top_4)
    top_3 = np.array(top_3)
    #sorting the numpy arrays on the basis of fares
    top_6 = top_6[top_6[:,7].argsort()[::-1]]
    top_5 = top_5[top_5[:,7].argsort()[::-1]]
    top_4 = top_4[top_4[:,7].argsort()[::-1]]
    top_3 = top_3[top_3[:,7].argsort()[::-1]]

    top_20 = np.vstack((top_6, top_5,top_4,top_3))      #conversion into stack array

    #printing in the desired output format
    print("List of 20 Female Survivors by Highest Non-self Family Member Onboard Count, then by Highest Fare, in descending order\n")
    print('passenger_id\tsurvived\tpclass\t\tgender\t\t age\t sibsp\t parch\t  fare\t\t sibsp_parch')
    for i in range(0,20):
        print('%.0f'%top_20[i][0],'\t\t','%.0f'%top_20[i][1],'\t\t','%.0f'%top_20[i][2],'\t\t','%.0f'%top_20[i][3],'\t\t','%.0f'%top_20[i][4],'\t','%.0f'%top_20[i][5],'\t','%.0f'%top_20[i][6],'\t',"{:6.2f}".format(top_20[i][7]),'\t','%.0f'%top_20[i][8])

if __name__ == "__main__":
    main()
