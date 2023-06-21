#Topic: Vehicle Rental System
from data_type import Car, Bike

#use the sys module to call the exit() function
import sys
#use to print out current date time
import datetime
#use to increament the file name
import os

# use this library to delay , so that user have time to read the print statement before it go into another stage
import time
# class to manage the vehicle rental system
class VehicleRentalSystem:

    #this class use dictionary to store the information of the vehicles
    def __init__(self):
        self.vehicle_dict = {} #dictionary
        self.reservation_list = [] #list 

    #add the vehicle information, key as the unique_id and all the vehicle information store as value
    #the class bike or car is store as value
    def add_vehicle(self, vehicle,unique_id):
        self.vehicle_dict[unique_id] = vehicle
        #uncomment to test the code's functionality after adding it
        # print("Vehicle added successfully.")

    #print all the document store inside the dictionary create when calling function add_vehicle
    def show_list(self):
        clear_screen()
        print("1. Show List of All Vehicles")
        self.show_list_bike()
        self.show_list_car()
        input("Press any key to return to homepage: ")
        return
    
    #create one more function so that it is easier to display in the interface
    def show_list_car1(self):
        clear_screen()
        print("2. Show List of Cars")
        self.show_list_car()
        input("Press any key to return to homepage: ")
        return
    
    def show_list_bike1(self):
        clear_screen()
        print("3. Show List of Bikes")
        self.show_list_bike()
        input("Press any key to return to homepage: ")
        return
    
    #print all the car list
    def show_list_car(self):
        for unique_id, vehicle in self.vehicle_dict.items():
            if isinstance(vehicle, Car):
                vehicle.print_with_id(unique_id)


    #print all the bike list
    def show_list_bike(self):
        for unique_id, vehicle in self.vehicle_dict.items():
            if isinstance(vehicle, Bike):
                vehicle.print_with_id(unique_id)
        
    #store vechicle into separete dictionary based on its type
    def get_vehicle_list(self, type):
        #create a temporary dictionary first, so that later can return this list
        vehicle_list = {}
        for unique_id, vehicle in self.vehicle_dict.items():
            if isinstance(vehicle,type):
                vehicle_list[unique_id] = vehicle
        return vehicle_list

    def reserve_vehicle(self, id):
        #since id already been checked before it pass into this function, therefore the id inside this function of course is inside the dictionary
        vehicle = self.vehicle_dict[id]
        if vehicle.get_availability():
            #if vehicle is available then, reserve the vehicle
            vehicle.set_availability(False)
            current_time = self.current_time()

            #create a list to store infor
            reservation_detail = [id, vehicle, current_time]
            self.reservation_list.append(reservation_detail)
            print(f"Vehicle with unique ID '{id}' has been reserved in {current_time}.")
            print("Vehicle rented successfully !")
        else:
            print(f"Vehicle with unique ID '{id}' is not available for reservation.")
            print("Vehicle rented unsuccessfully !")

    #rent either bike or car
    def rent(self,type,name):
        clear_screen()
        v_list = self.get_vehicle_list(type)
        print(f"{name} List:")
        for id, vehicle in v_list.items():
            if vehicle.get_availability():
                vehicle.print_with_id(id)
        v_id = input("Enter the unique ID of the bike you want to rent (or 0 to go back): ")
        if v_id == "0":
            return
        elif v_id not in v_list:
            print("Invalid input. Please enter a valid unique ID.")
            time.sleep(2)
            self.rent(type,name)  # Prompt user to re-enter a valid input
        else:
            self.reserve_vehicle(v_id)
            time.sleep(2)
        
    def current_time(self):
        # Get the current date and time
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return current_date
    
    def rental_cost(self, start_time, vehicle,id):
        start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        return_time = self.current_time()
        return_time = datetime.datetime.strptime(return_time, "%Y-%m-%d %H:%M:%S")
        rental_duration = return_time-start_time
        rental_cost = rental_duration.total_seconds() / 60 *vehicle.rental_price # Convert duration to minutes and calculate cost
        
        # Save the output to a text file
        # Find the next available filename
        counter = 1
        while os.path.exists(f"rental{counter}_details.txt"):
            counter += 1
        output_filename = f"rental{counter}_details.txt"
        # Display the rental receipt
        receipt = '''
        [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
        |                                                                            |
        |           [RENTAL-RECEIPT]                                                 |
        |                                                                            |
        |       Current date and time: {}                           |
        |       Return date: {}                                     |
        |       Rental duration (minutes): {:.2f}                                      |
        |       Brand: {}                                                       |
        |       Model: {}                                                        |
        |       Rental cost: ${:.2f}                                                   |
        |                                                                            |
        [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
        '''.format(start_time, return_time, rental_duration.total_seconds() / 60, vehicle.brand,vehicle.model, rental_cost)
        with open(output_filename, "w") as file:
            file.write(receipt)

        print("Rental details saved to", output_filename)
        vehicle.set_availability(True)
        print(f"Vehicle with unique ID '{id}' successfully returned.")


    
    def return_vehicle(self):
        if self.reservation_list:
            for reservation_details in self.reservation_list:
                vehicle_id = reservation_details[0]
                vehicle = reservation_details[1]
                reservation_time = reservation_details[2]
                print(f"Reservation Time: {reservation_time}")
                vehicle.print_with_id(vehicle_id)
            while True:
                option = input("Enter the vehicle ID that you want to return ('B' to return to homepage): ")
                if option in [reservation_details[0] for reservation_details in self.reservation_list]:
                    self.rental_cost(reservation_details[2],reservation_details[1],reservation_details[0])
                    self.reservation_list.remove(reservation_details)
                    break
                elif option.lower() == 'b':  # Fix: Check both conditions separately
                    break
                else: 
                    print("Invalid vehicle ID. Please try again.")
        else:
            print("No vehicles available for return.\n")
            time.sleep(2)

    def interface_main(self):
        print_menu()
        option = input("\nEnter your choice: ")
        if option == "1":
            while True:
                show_option1_page()
                option1_choice = input("\nEnter your choice: ")
                if option1_choice == "4":
                    self.interface_main()
                elif option1_choice == "1":
                    self.show_list()
                    self.interface_main()
                elif option1_choice == "2":
                    self.show_list_car1()
                    self.interface_main()
                elif option1_choice == "3":
                    self.show_list_bike1()
                    self.interface_main()
                else:
                    print("Invalid input. Please try again.")
                    time.sleep(2) #delay for 3seconds, before it loop again
            
        elif option == "2":
            while True:
                show_option2_page()
                option2_choice = input("\nEnter your choice: ")
                if option2_choice == "3":
                    self.interface_main()
                elif option2_choice == "1":
                    self.rent(Car, "Car")
                elif option2_choice == "2":
                    self.rent(Bike, "Bike")
                else:
                    print("Invalid input. Please try again.")
                    time.sleep(2) #delay for 3seconds, before it loop again
        elif option == "3":
            show_option3_page()
            self.return_vehicle()
            time.sleep(2)
            self.interface_main()
                
        elif option == "4":
            # Quit the program
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)
            self.interface_main()        

def clear_screen():
    #os.system('cls') command for Windows and os.system('clear') command for Unix/Linux/Mac:
    #therefore this code can used for all operating system
    os.system('cls' if os.name == 'nt' else 'clear')

#example of the system
def print_menu():
    clear_screen()
    with open("welcome_page.txt", "r") as file:
        menu_content = file.read()
    print(menu_content)

def show_option1_page():
    clear_screen()
    art = '''
    ----------------------------------------------------
    ||||||||||||||||||||||||||||||||||||||||||||||||||||
    ----------------------------------------------------
                                        ,-~ |
        ________________          o==]___|
        |                |            \ \\
        |________________|            /\\ \\
    __  /  _,-----._      )           |  \\ \\.
    |_||/_-~         `.   /()          |  /|]|_|_____
    |//              \\ |              \\/ /_-~     ~-_
    //________________||              / //___________\\
    //__|______________| \____________/ //___/-\\ \\~-_
    ((_________________/_-o___________/_//___/  /\\,  \\
    |__/(  ((====)o===--~~                 (  ( (o/)  )
        \  ``==' /                         \  `--'  /
        `-.__,-'       Vespa P-200 E       `-.__,-'
    '''

    print(art)
    print("Option 1: Show List\n")
    print("1. Show List of All Vehicles")
    print("2. Show List of Cars")
    print("3. Show List of Bikes")
    print("4. Return to Welcome Page")

def show_option2_page():
    clear_screen()
    print("   -           __")
    print(" --          ~( @\   \\")
    print("---   _________]_[__/_>________")
    print("     /  ____ \ <>     |  ____  \\")
    print("    =\_/ __ \_\_______|_/ __ \__D")
    print("________(__)_____________(__)____")
    print("Option 2: Rent a Vehicle\n")
    print("1. Rent a Car")
    print("2. Rent a Bike")
    print("3. Return to Welcome Page")

def show_option3_page():
    clear_screen()
    art = '''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣁⠀⢀⣀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⢸⣁⡩⠟⠉⣠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣍⣀⣠⠴⡾⠙⠺⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡇⢹⡞⢁⡄⠈⠲⡱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠘⡌⠇⢸⠁⠀⠀⠁⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⣀⣀⣠⠚⠁⢀⡔⠙⢆⢸⠀⢀⡇⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠁⠀⠀⢀⣹⣀⡴⠋⠀⢀⡼⠋⠉⢸⠃⠀⠀⠀⠈⣧⠀⠀⠀⢀⣀⣀⣠⣤⡤⣤⣀⠀
    ⠀⠀⠀⠀⠀⣠⠖⠉⠀⠀⣠⣴⣞⣿⣿⣿⡞⣯⠟⠉⢀⡤⠖⠯⣤⣤⠤⠤⠀⠉⣷⡞⠉⠉⣁⣀⠀⠚⠁⣠⠼⠃
    ⠀⠀⠀⠀⢰⡇⣠⠔⠒⡆⠻⣿⣀⠽⣯⣀⣀⣈⣶⣾⣅⣒⣁⡴⠊⠁⠀⠀⠀⣠⠟⢉⣷⣿⣷⠌⣡⠴⢯⣥⡀⠀
    ⠀⠀⠀⠀⠘⢿⣥⣤⣶⣧⠤⠤⠽⠶⠉⠭⣿⣇⣀⠙⠢⣴⠉⠀⠠⣀⠤⣴⠾⠗⠒⢋⣿⣿⣿⣯⠅⠀⠀⠀⠉⠀
    ⠀⠀⠀⠀⢴⣖⣿⡛⢻⠿⣖⣦⣀⡀⢀⣠⠶⠿⢯⠉⠀⠘⢦⡀⠀⠘⢆⣸⣤⣴⣾⣿⣿⣿⠙⢆⠀⠀⠀⠀⠀
    ⠀⠀⣠⠖⠀⣀⡈⡿⠈⢹⡿⢿⣌⠉⠁⠀⠳⡀⠈⣤⣴⠖⡾⠙⣦⣤⠜⠻⣿⣿⣍⣴⠋⣹⢧⣤⣀⠙⢦⡀⠀⠀
    ⠀⣰⠁⢠⣾⣿⠃⠇⢠⡿⠁⡈⢏⢳⡀⠀⠀⠹⡾⢋⡤⢴⣃⢤⡇⣙⣦⠀⠈⠹⣟⣿⣿⣦⣤⣬⣯⠱⡄⢳⠀⠀
    ⢠⠇⠀⡿⣹⠁⠀⣷⣻⠃⡄⢱⢸⠀⢇⠀⠀⠀⢀⣼⡀⣸⠃⠠⢡⣽⣿⡇⠀⣰⣛⡛⠦⠽⠿⠟⢻⡇⢸⠈⡆⠀
    ⢸⡄⠀⣧⢻⡀⠀⠉⠁⢠⠇⡜⣼⣠⠃⠀⣀⡴⠋⠀⠻⣄⠀⠒⣂⠀⠸⢀⠜⠛⢿⠯⣉⣳⡒⢒⣼⠇⢸⢀⠇⠀
    ⠀⢳⡀⠹⣟⠙⠢⠤⠒⣁⠜⣽⣹⢁⣤⣾⣛⣁⣀⣀⣀⣈⣛⣋⣁⣙⣦⡘⣆⠀⠈⢣⡀⠈⣉⡿⠋⣠⢋⡜⠀⠀
    ⠀⠀⠑⢤⣀⠉⠑⢚⣉⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠳⣄⠀⠉⠛⠓⠒⢉⣡⠞⠀⠀⠀
    ⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠒
    '''
    print(art)
    print("Option 3: Return a Vehicle\n")
    print("############################################")
    # Add more options or instructions for returning a vehicle




def main():
    #call out system and store it as a object
    system = VehicleRentalSystem()
    from data_list import vehicle_list
    #for loop and a list of tuples, you can conveniently add multiple vehicles into VehicleRentalSystem 
    # without having to repeat the add_vehicle calls for each vehicle individually.
    for vehicle, unique_id in vehicle_list:
        system.add_vehicle(vehicle,unique_id)

    system.interface_main()
    
main()