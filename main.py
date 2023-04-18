# Request the number of tickets
num_tickets = int(input("Enter the number of tickets: "))
# Initialize variables
total_cost = 0
discount = 0
# Request age for each ticket and calculate the cost
for i in range(num_tickets):
    age = int(input("Enter the visitor's age: "))
    if age < 18:
        ticket_cost = 0
    elif age < 25:
        ticket_cost = 9.90
    else:
        ticket_cost = 13.90
    total_cost += ticket_cost
# Apply discount if three or more visitors registered
if num_tickets >= 3:
    discount = 0.1 * total_cost
    total_cost -= discount
# Display the total cost to pay
print(total_cost)
