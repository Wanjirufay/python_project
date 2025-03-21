my_list = []
# print (type (my_list))

my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)
# print(my_list) #[10, 20, 30, 40]

my_list.insert (1,15)
# print(my_list) #[10, 15, 20, 30, 40]

List2 = [50,60,70]

my_list.extend(List2)
# print (my_list) # [10, 15, 20, 30, 40, 50, 60, 70]

my_list.pop()

my_list.sort()

for index, value in enumerate(my_list): 
    if value == 30:
        print(index)

