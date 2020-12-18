
"""                 Structured-English

This program will display the total number of grades, average grade among those grades, 
and percentage of grades that fall above the average based on a file with grades. 
The program will first open the grades file called final.txt
Next, the program will read grades in file and make a list. Once the file is read into memory is will be closed. 

Based of the list, the program will then display the total number of grades in the list depending on how many 
grades there are, which should be 24.
Next, we will calculate the avergae grade of the grades in list and the program will display the percentage, which
should be 83.25%.
Then we will calculate the percentage of grades from the list above the average grade and the program will display 
the percentage of grades above the average.  


"""

"""                 Pseudocode
main()
    file = final name 
    calculate_percent_abov_avg

calculate_percent_abov_avg
    read file final.txt
    create list = each grade in list
    close file
    length = total of grades in list
    print("total number of grades: ", length)
    totalsum = sum of all grades in list
    average = total sum of grades / total of grades in list
    print("Average grade: ", average)

    for grade in list:
        if grade > average
            add grade to count
    percent above avergage = total count / length
    print("percent of grades above avergage: ", percent above average ")

main()
         
"""