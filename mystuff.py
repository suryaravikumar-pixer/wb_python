class MyStuff:

    def __init__(self):
        self.continent_food = " Spaghetti Bologanese is a Italian dish !!"

    def apple(self):
        print("I love apples!")
     
    def orange(self):
        print("The orange is rich in 'C' vitamin and many other vitamins")


#inheritance
class vender(MyStuff):
    def __init__(self, name, vender_id):
        self.name = name
        self.vender_id = vender_id
        print(f'vender is {name} and is vender licence id {vender_id}') 

    def selling(self):
        print('selling banana')

