#PYTHON NOTES
print('hello independent study')

#variables are containers that store data
name = 'Kaylee'
age = 16
favorite_book = 'Magnolia Parks'
height = 5.17

#printing strings
print(name,age)
print(f'{name} is: {age}')
f_string = f'My favorite book is {favorite_book}'
print(f_string)

#Math operations
print(32*5)
print(height*12)
print(height/5)
print(5+5)
print((5+5)*2)
print(5+5*2)

#Lists are ordered collections (e.g. playlist)
books = ['Magnolia Parks', 'Scarlet Letter', 'Wuthering Heights']
print(books)
#Use a loop to look at each item
for item in books:
    print(item)

#number of items
books_length = len(books)
print(books_length)
#example of nesting/chaining function; len first then print
print(len(books))