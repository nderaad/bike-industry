
class Bike(object):
    def __init__(self,model,weight,cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    
class Store(object):
    def __init__(self,name,margin):
        self.name = name
        self.margin = margin
        print('You created {}, a bike shop with a {} margin'.format(self.name, self.margin))
    
    def inventory(self,name,bike,number):
        self.name = name
        self = [bike,number]
        if self[1] == 1:
            print('{} now has {} {} bike.'.format(name,self[1],self[0]))
        elif self[1] > 1:
            print('{} now has {} {} bike.'.format(name,self[1],self[0]))
        elif self[1] == 0:
            print('{} now has {} {} bikes.'.format(name,self[1],self[0]))
        else:
            print('Please enter a real whole number of {} bikes.'.format(self[0]))

class Customers(object):
    def __init__(self,name,fund,bought):
        self.name = name
        self.fund = fund
        self.bought = bought
        
Swingline = Bike("Swingline",20,150)
Zippy = Bike("Zippy",15,200)
Fasto = Bike("Fasto",10,250)
Hillmaster = Bike("Hillmaster",30,350)
Pacesetter = Bike("Pacesetter",25,175)
Roadrunner = Bike("Roadrunner",12,190)

Bikeapalooza = Store("Bikeapalooza",0.2)
# not sure how to get Bikeapalooza below as the first variable w/out typing it out
Bikeapalooza.inventory("Bikeapalooza",Swingline.model,3)
Bikeapalooza.inventory("Bikeapalooza",Zippy.model,2)
Bikeapalooza.inventory("Bikeapalooza",Fasto.model,6)
Bikeapalooza.inventory("Bikeapalooza",Hillmaster.model,1)
Bikeapalooza.inventory("Bikeapalooza",Pacesetter.model,0)
Bikeapalooza.inventory("Bikeapalooza",Roadrunner.model,.5)