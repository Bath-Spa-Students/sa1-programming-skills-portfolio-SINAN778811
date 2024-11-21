dictionary  = { 'Name' : 'Sinan' , 'Roll No ' :  '2846' , 'Fathers name ': 'shamsudheen' } 
print(dictionary.items())
 # in out put small braces bcz they are tuples , key value pair is in tuple form ---- There is a list and in the list every value is in tuple form 
 #   ('Name ', 'Sinan ')  -this is a element   -to secure our data not to change 



 # To check keys in our dictionary 


dictionary  = {'Name' : 'Sinan' , 'Roll No ' :  '2846' , 'Fathers name ': 'shamsudheen'}
print(dictionary.keys())

# output - in list form we get keys in our dict


# Delete method 


dictionary  = { 'Name' : 'Sinan' , 'Roll No ' :  '2846' , 'Fathers name ': 'shamsudheen'}
del dictionary ["Roll No"]
print(dictionary.items())
