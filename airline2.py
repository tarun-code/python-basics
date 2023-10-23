import random
import string

class Airline:
   
    list=[]
    airline_name="INDIGO AIRLINES"
    def __init__(self,date,p_name):
        cities=["Raipur","Pune","Mumbai","Delhi","Kolkata","Jaipur","Hydrabad","Banglore","Chennai","Bhilai"]
        letters = string.ascii_uppercase
        self.departure_cities=random.choice(cities)
        self.pass_name=p_name
        self.on_date=date
        temp=random.choice(cities)
        while self.departure_cities==temp:
            temp=random.choice(cities)
            
        self.arrival_cities=temp
        self.flight_number= random.randrange(5, 10000)
        self.seat_assign=str(random.randrange(2, 10))+random.sample(letters, 1)[0]
        
    def get_departure(self):
      return self.departure_cities
    def get_seat(self):
      return self.seat_assign 
    
    def get_arrival(self):
      return self.arrival_cities
     
    def get_flight(self):
      return self.flight_number 
    
    def set_arrival(self,rcv_arri):
        
        self.arrival_cities=rcv_arri 
    def set_departure(self,rcv_depar):
        
        self.departure_cities=rcv_depar   
    
    def set_flight(self,rcv_flight_num):
        
        self.flight_number=rcv_flight_num
        
    def set_seat(self,rcv_seat):
        
        self.seat_assign=rcv_seat
    
    
    @staticmethod         
    def print_tickets():
         for i in  Airline.list:
            print("welcomes to the ",i.airline_name)
            print("You Travel on : ",i.on_date)
            print("Your Name is : ",i.pass_name)
            print("your destination is : ",i.get_arrival())
            print("you Departured from : ",i.get_departure())
            print("your Flight number : ",i.get_flight())
            print("your Seat number  : ",i.get_seat())
            print("************************ ")
            
             
         
       



def main():
    
  
    
    
   
    ticket=int(input("Enter How Many Tickets You want :")) 
    i=0
   
    while i<ticket:
        print("******Enter Your Details****** ")
        date=input("Enter Date :") 
     
        name=input("Enter Your name :") 
        obj=Airline(date,name)
        Airline.list.append(obj)
        i+=1
        
    Airline.print_tickets()




if __name__=="__main__":
    main()        
        