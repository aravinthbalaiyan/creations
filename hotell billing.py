class hotel:
    def __init__(self,food_list):
        self.food_list=food_list
    def show(self):
        for key,value in self.food_list.items():
            print(f"{key}\t{value}")
    def total_bill(self):
        total=0
        print("-------------------------------------------------")
        print("FOOD\t\tQUANTITY\t\tPRICE")
        print("-------------------------------------------------")
        for key, value in order.items():
            if key in self.food_list:
                price=self.food_list[key]
                total+=price*value
                print(f"{key}\t\t{value}\t\t\t{price*value}")
            else:
                break
        print("-------------------------------------------------")
        print(f"                           Total bill : {total}")
        print("-------------------------------------------------")
    def set_order(self, order):
        self.order = order

class customer:
    def get_order(self):
        order={}
        while True:
            print("Enter a food name or type 'done'  to finish")
            key=input("Enter a food name : ")
            if key.lower()=='done':
                break
            value=int(input("Enter a food quantity : "))
            order[key]=value
        return order

food_list={'dosa':30,'idly':10,'vadai':10,'poori':30}
aravinth=hotel(food_list)
arun=customer()

while True:
    print('1.show the menu_list\n2.enter a order\n3.total_bill\n0.exit')
    option=int(input('enter your option : '))
    if option==1:
        print("------------------------------------------")
        print("FOOD\tPRICE")
        print("------------------------------------------")
        aravinth.show()
        print("------------------------------------------")
    if option==2:
        print("------------------------------------------")
        print("FOOD\tPRICE")
        print("------------------------------------------")
        aravinth.show()
        print("------------------------------------------")
        order=arun.get_order()
        aravinth.set_order(order)
    if option==3:
        aravinth.total_bill()
    if option==0:
        break