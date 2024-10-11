newphase = "rainstorm"
           #012345678
           #123456789 -- college board version
#create a new variable called shortphrase and assign it a value by slicing the newphase variable by removing the first three characters
#the first 3 characters are "rai"
#the last 3 characters are "orm"
#substring(string, start, end)

shortphase = newphase[3:len(newphase)-3]

#college board version[4:len(newphase)-6]
print(shortphase)
#explain len(newphase)-3 = 9-3 =6