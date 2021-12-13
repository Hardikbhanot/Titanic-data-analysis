freader = open("titanic_mod.csv","rb")      #opeing file in read mode
data = freader.readlines()                  #reading line by line using readline function
headers = data[0].decode()                  #decoding the bytes to string 
headers = headers.split(",")                #spliting to list
headers[0] = headers[0][1:20]               #slicing out the special characters
headers[7] = headers[7][0:4]                #slicing out the special characters
data[0] = data[0].decode()                  #decoding the bytes to string
print("Printing headers of data in List : ")
print(headers)                              #printing the list of header name (i) part
print("\nPrinting 5 headers with 5 rows :") 
print(f"{headers[0]}\t{headers[1]}\t{headers[2]}\t\t{headers[3]}\t\t{headers[4]}")      #Printing the first 5 column header names, followed by the first 5 rows (ii) part
for i in range(1,6):                        #loop to iterate through the data from 1st to 5th row
    data[i] = data[i].decode()
    data[i] = data[i].split(',')
    print(f"{data[i][0]}\t\t {data[i][1]}\t\t{data[i][2]}\t\t{data[i][3]}\t\t{data[i][4]}")

freader.close()                             #closing the file
