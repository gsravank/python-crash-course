from name_function import get_formatted_name


print("Enter 'q' to quit at any time")
while 1:
    first = input("\nPlease give me first name: ")
    if first == 'q':
        break
    
    last = input("Please give me last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
