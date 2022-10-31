
print("Welcome to the tip calculator my bro\n ")
total = float(input("What was the total bill $?\n "))
percentage_chosen = int(input("What percentage tip would you like to give? 10, 12, or 15?\n "))
people_who_ate = int(input("How many people to split the bill? \n"))
tip_to_give_per_person = (float(total) / 100) * float(percentage_chosen) / int(people_who_ate)
total_sin_propina = float(total) / int(people_who_ate)
total_con_propina = percentage_chosen / 100 * total + total
bill_per_person = total_con_propina / people_who_ate
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount} ")
print("No seas laji y siempre se educado con la persona que te atiende")