from Prac_08.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100,1.23)
    my_taxi.drive(40)
    print(my_taxi)
    print(my_taxi.get_fare())
    taxi = Taxi("Prius 1", 100,1.23)
    taxi.drive(100)
    print(my_taxi.start_fare())
    print(taxi.get_fare())



main()