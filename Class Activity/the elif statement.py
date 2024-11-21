#trying the flowchart
#Asking the person to put their score
marks = int(input("enter your marks :"))
#prints A if the mark is more than or equal to 90
if marks >= 90:
    print("Your grade is A.")
#prints B if the mark is more than or equal to 80
elif marks >= 80:
    print("Your grade is B.")
#prints C if the mark is more than or equal to 70
elif marks >=70:
    print("Your grade is C.")
#prints D if the mark is more than or equal to 60
elif marks >=60:
    print("Your garde is D.")
#prints F if the mark is less than 60
else:
    print("Your grade is F.")
