Total_Users= int(input("Total Users: "))
Staff_Users= int(input("Staff Users: "))
Non_TeachingStaffs=Staff_Users//3
Staff_Users = Staff_Users+Non_TeachingStaffs
Student_Users = Total_Users-Staff_Users
if(Total_Users <= 0):
    print("Invalid Input")
elif(Total_Users <= Staff_Users):
    print("Invalid Input" )
else:
    print("Student Users = ",Student_Users)
