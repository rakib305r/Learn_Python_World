                                #  CLASS AND OBJECT
# class Student:
#     name = "rakib"
# s1 = Student()
# print(s1.name)

                                # CONSTRUCTOR
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def information(self):
#         print("all information: ")
    
#     def get_price(self):
#         return self.price
        
# p1 = Product("laptop", 3000)

# print(p1.name, p1.price)
# p1.information()
# print(p1.get_price())

                                # EXAMPLE OF CONSTRUCTOR
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg marks is: ", sum/3)
            
s1 = Student("Rakib", [94, 89, 90])
s1.get_avg()
s1.name = "yamal"
s1.marks = [25, 85, 98]
s1.get_avg()