from datetime import datetime, timedelta

def main():

    #Gets time of the country the user cants to convert
    #print ("You can choose from: ")
    user_input_country = input ("Are you in Mexico or in London? ")

    if user_input_country == "Mexico":

        user_time_input = input("Enter the time in Mexico (HH:MM): ")
    
        time_format = "%H:%M"
        mexico_time = datetime.strptime(user_time_input, time_format)
        
        time_in_london = mexico_time + timedelta(hours=7)
        print("Time in London is:", time_in_london.strftime(time_format))

    elif user_input_country == "London":
        user_time_input = input("Enter the time in London (HH:MM): ")
    
        time_format = "%H:%M"
        london_time = datetime.strptime(user_time_input, time_format)
        
        time_in_mexico = london_time + timedelta(hours=-7)
        print("Time in Mexico is:", time_in_mexico.strftime(time_format))
    

if __name__ == "__main__":
    main()