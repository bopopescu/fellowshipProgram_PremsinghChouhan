from datastructure.Utility import linked_list, Node

f = open('read', 'r')
text = f.read()

my_list = linked_list()
lst = []
lst = text.split(" ")
print(lst)
for loop in range(len(lst)):
    str1 = lst[loop]
    f1 = Node(str1)
    my_list.insert(f1)
my_list.print_list()
str2 = input("Enter a string to search: ")
obj2 = Node(str2)
x1 = my_list.search_item(obj2)
if x1 == 1:
    my_list.delete_position(obj2)
    my_list.print_list()
else:
    my_list.insert(obj2)
    my_list.print_list()