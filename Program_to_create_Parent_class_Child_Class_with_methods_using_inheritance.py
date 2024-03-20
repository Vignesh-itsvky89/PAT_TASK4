# Create a Parent class with methods 
class TVClass():
    def __init__(self,price,inches , OnOFF_status,  brand="LG", channel =1 , volume_level=50):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches =inches
        self.OnOFF_status = OnOFF_status
        self.volume_level=volume_level
# Method 1
    def volume(self):
        if self.volume_level <=0 or self.volume_level>=100:
            print ("Invalid input !! Volume can't never be below 0 or above 100")
        else:
            print ("Volume level setted to:", self.volume_level)
# Method 2
    def set_Channel(self):
        if self.channel <=0 or self.channel >50:
            print ("Channel no not available in TV!! TV will stay at the current channel.")
        else:
            print ("Channel no setted to:", self.channel)
# Method 3
    def reset_TV(self):
        print ("**Reset TV Method is called, So TV is getting resetted** ")
        print ("Volume level resetted to ", self.volume_level)
        print ("Channel Number resetted to: ",self.channel)
# creating object of the class. This invokes constructor
p1= TVClass(10000,"55'Inches",channel=2, OnOFF_status="ON",volume_level=51)
p2= TVClass(10000,"55'Inches",OnOFF_status="ON")
p1.volume()
p1.set_Channel()
print("\n")
p2.reset_TV() 
print("\n"" The status of TV before resetting is: ", p1.__dict__)                      
print("\n"" The status of TV after resetting is: ", p2.__dict__)

# Create a Child class - 1
class LED(TVClass):
    def __init__(self,Refresh_rate ,screen_thickness= "3 Inches", energy_usage = "Low Energy" , Lifespan = "50 Years", ViewingAngle ="360 Degree" , Backlight = "On", DisplayDetails = "8k Resolution"):
        TVClass.__init__(self,price=100000,inches = "50 Inches" , OnOFF_status= "ON",  brand="LG", channel =50 , volume_level=50)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_rate= Refresh_rate
        self.viewingAngle = ViewingAngle
        self.Backlight = Backlight
        self.DisplayDetails=DisplayDetails
# creating object of the class. This invokes constructor
p1=LED("120Hz")
print("\n""Detailed features of LED TV: ", p1.__dict__)

# Create a Child class - 2
class PLASMA(TVClass):
    def __init__(self,Refresh_rate ,screen_thickness= "2 Inches", energy_usage = "Medium Energy" , Lifespan = "40 Years", ViewingAngle ="180 Degree" , Backlight = "On", DisplayDetails = "UHD"):
        TVClass.__init__(self,price=50000,inches = "50 Inches" , OnOFF_status= "ON",  brand="LG", channel =50 , volume_level=101)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_rate= Refresh_rate
        self.viewingAngle = ViewingAngle
        self.Backlight = Backlight
        self.DisplayDetails=DisplayDetails
# creating object of the class. This invokes constructor

p1=PLASMA("100Hz")
print("\n""Detailed features of PLASMA TV: ", p1.__dict__)


