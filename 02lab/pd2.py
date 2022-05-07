# zad1
print("ZADANIE 1")
x15 = lambda x: x + 15
xy = lambda x, y: print(x * y)

print(x15(5))
xy(4, 5)


# zad2
print("\nZADANIE 2")
list_of_dicts = [
    {'make':'Nokia', 'model':216, 'color':'Black'},
    {'make':'Mi Max', 'model':2, 'color':'Gold'},
    {'make':'Samsung', 'model':7, 'color':'Blue'}
]
sort_by_make = lambda x: x['make']
print("Sorted by make:")
print(list_of_dicts_sorted_by_make := sorted(list_of_dicts, key=sort_by_make))

sort_by_model = lambda x: x['model']
print("Sorted by model:")
print(list_of_dicts_sorted_by_model := sorted(list_of_dicts, key=sort_by_model))

sort_by_color = lambda x: x['color']
print("Sorted by color:")
print(list_of_dicts_sorted_by_color := sorted(list_of_dicts, key=sort_by_color))


# zad3
print("\nZADANIE 3")
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sqr = list(map(lambda x: x**2, L))
cb = list(map(lambda x: x**3, L))

print("Squared: ", sqr)
print("Cubed: ", cb)


# zad4 w osobnym pliku