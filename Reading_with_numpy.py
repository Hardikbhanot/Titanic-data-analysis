import numpy as np          #importing library numpy

#reading dataset as numpy array using function genfromtext() by skiping the header part from the file and splitting at ","
data_set = np.genfromtxt('titanic_mod.csv',skip_header=1,delimiter=",",filling_values=None)      
np.set_printoptions(suppress=True)          #using set_printoptions() function to remove the extra zeros
print("2-D Array of Titain Details")
print(data_set)                             #printing the numpy array
print("\nThe size of the array is ",data_set.size)  #printing the size of array
print("The shape of the array is ",data_set.shape)  #printing the shape of array
