# write a program to demonstrate single ,multiple ,and multilevel inheritance
# class father():
#     def father_speak():
#         return "father class"
# class mother():
#     def mother_speak():
#         return "mother class"
# class kid(father,mother):
#     def kid_speak():
#         return  "im kid having propertiess of father and mother"
# obj=kid()       
# print(obj.kid_speak())


class Animal:
    def speak():
        return "speaking"
class Dog(Animal):
    def speak():
        return "dog is speaking"
class Puppy(Animal):
    def speak():
        return "puppy is speaking" 
obj1=Puppy
print(obj1.speak())       
 