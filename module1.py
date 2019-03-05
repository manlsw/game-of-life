#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      shaowei.liu
#
# Created:     10/06/2018
# Copyright:   (c) shaowei.liu 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
   # def calc(numbers):

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def get_description(self):
        long_name=str(self.year) + " " + self.make + " " + self.model
        return long_name
    def read_odometer(self):
        print("this car has" + str(self.odometer)+ "miles on it")

    def update_odometer(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print("you can't roll back an odometer")

    def increment(self,miles):
        self.odometer+=miles


class Battery():
    def __init__(self,batter_size=70):
        self.batter_size=batter_size

    def describe_battery(self):
        print("this car has a "+" "+str(self.batter_size)+" "+ "-kWH battery.")

class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=Battery()


Tesla=Electric_car("Benz","S600",2018)

Tesla.battery_size.describe_battery()





