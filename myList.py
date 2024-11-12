def main ():
    #Create an empty list
    my_list = []

    #Append elements to the list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    #Insert the value 15 at the 2nd position (index 1)
    my_list.insert(1, 15)

    #Extend my_list with another list
    my_list.extend([50, 60, 70])

    #Remove the last element from my_list
    my_list.pop()

    #Sort my_list in asc. order
    my_list.sort()

    #Find and print the index pf the value 30
    index_of_30 = my_list.index(30)

    #Print final state of my_list and the index of 30
    print("Final list:", my_list)
    print("Index of value 30:", index_of_30)

if __name__ == "__main__":
    main()