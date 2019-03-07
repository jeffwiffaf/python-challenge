
# coding: utf-8

# In[65]:


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# Need  to import budget_data.csv
# date profit/losses


import os 
import csv 

csvpath = os.path.join('.', 'PyBank_Resources_Budget_Data.csv')
#print(csvpath)


total_months = 0
total_net = 0
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 9999999999]


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print("Header",csv_header)
    #print("Data:")
    
    first_row = next(csvreader)
    #print("First Row",first_row)
    total_months += 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1]) #867884

    
    for row in csvreader:
        #print(row)
        total_months += 1
        total_net = total_net +int(row[1])
        net_change = int(row[1]) - previous_net #984655-867884 #322013-984655 #-69417-32013 
        previous_net = int(row[1]) #984655 #322013
        net_change_list.append(net_change)
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease [1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        
        
            
            
        
    print("Financial Analysis")
    print("-" * 50)
    print("Total Months:", total_months) #86 months
    print("Total Net:", total_net)
    print("Average Change: ",sum(net_change_list)/len(net_change_list))
    print("Greatest Increase in Profits", greatest_increase[0], greatest_increase[1])
    print("Greatest Decrease in Profits", greatest_decrease[0], greatest_decrease[1])

