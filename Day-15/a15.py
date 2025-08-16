
class SmartDevice:
    def power_on(self):
        print("Turning on device...")

class Smartphone(SmartDevice):
    def power_on(self):
        print("Smartphone: Booting mobile OS...")

class Smartwatch(SmartDevice):
    def power_on(self):
        print("Smartwatch: Starting wearable system...")


devices=[SmartDevice(),Smartphone(),Smartwatch()]

for d in devices:
    d.power_on()


#stretch task
from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class CreditCard(PaymentMethod):
    def process_payment(self,amount):
        print(f"CreditCard: Processing payment of ₹{amount}")

class UPI(PaymentMethod):
    def process_payment(self,amount):
        print(f"UPI: Processing payment of ₹{amount}")

class Cash(PaymentMethod):
    def process_payment(self,amount ):
        print(f"Cash: Accepting payment of ₹{amount}")


payments=[CreditCard(),UPI(),Cash()]
amounts=[5000,1200,250]

for method,amt in zip(payments,amounts):
    method.process_payment(amt)


#challenge

class ContentCreator:
    def __init__(self,name,followers):
        self.name=name
        self.followers=followers

    def create_content(self):
        print("Creating some content...")


class YouTuber(ContentCreator):
    def create_content(self):
        print("Recording and editing videos...")


class Blogger(ContentCreator):
    def create_content(self):
        print("Writing and publishing articles...")

creator1=YouTuber("Ananya",50000)
creator2=Blogger("Vikram",10000)

creators=[creator1,creator2]

for c in creators:
    print(f"Creator: {c.name}")
    print(f"Role: {c.__class__.__name__}")
    print("Task: ",end="")
    c.create_content()
    print()
