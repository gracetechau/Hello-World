''' 
Grace Techau 
Computational Thinking 
Lab Activity #1 

''' 
######################################################
##################### PART 1 #########################
######################################################

income = float(input("Please enter your 2023 annual income (example: 25000): "))

mfj = (input("If you are married filing jointly type Yes. Otherwise, type No: "))
# mfj = married filing jointly

if mfj == "Yes":
    spouse_income = float(input("Please enter your partner's 2023 annual income (example 25000): "))
    income = income + spouse_income
else: 
    spouse_income = 0
    income = income + spouse_income

#######################################################
########## PART 2 - Calculating STATE TAX #############
#######################################################

#max tax brackets for married filing jointly for the state of Iowa 
max_tax_1_mjf = 528.00
max_tax_2_mfj = 2841.60
max_tax_3_mfj = 7971.60

#max tax brackets for singles for the state of Iowa 
max_tax_1_single = 264.00
max_tax_2_single = 1420.80
max_tax_3_single = 3985.80

if mfj == "Yes":
    if income <= 12000:
        state_tax = (income*0.044)
    elif (income > 12000) and (income <= 60000):
        state_tax = (max_tax_1_mjf +(income - 12000)*0.0482)
    elif (income > 60000) and (income <= 150000):
        state_tax = (max_tax_2_mfj + (income - 60000)*0.0570)
    else: #i.e, if income > 150000
        state_tax = (max_tax_3_mfj + (income - 150000)*0.0600)

else: 
    if income <= 6000:
        state_tax = (income*0.044)
    elif (income > 6000) and (income <= 30000):
        state_tax = (max_tax_1_single +(income-6000)*0.0482)
    elif (income > 30000) and (income <= 75000):
        state_tax = (max_tax_2_single + (income - 30000)*0.0570)
    else: #i.e if income > 75000
        state_tax = (max_tax_3_single + (income-75000)*0.0600) 

print("Your state tax owed for Iowa in 2023 was $",round(state_tax))

##########################################################
############ PART 3 - Calculating FEDERAL TAX ###########
#########################################################

# Federal max tax brackets for married filing jointly 
fed_max_tax_1_mfj = 2200
fed_max_tax_2_mfj = 10294
fed_max_tax_3_mfj = 32580
fed_max_tax_4_mfj = 74208
fed_max_tax_5_mfj = 105664
fed_max_tax_6_mfj = 186601.5

# Federal max tax brackets for single 
fed_max_tax_1_single = 1100
fed_max_tax_2_single = 5147
fed_max_tax_3_single = 16290
fed_max_tax_4_single = 37104
fed_max_tax_5_single = 52832
fed_max_tax_6_single = 174238.25

if mfj == "Yes":
    income -= 27700
    if income <= 22000:
        federal_tax = (income*0.01)
    elif (income > 22000) and (income <= 89450):
        federal_tax = (fed_max_tax_1_mfj +(income - 22000)*0.12)
    elif (income > 89450) and (income <= 190750):
        federal_tax = (fed_max_tax_2_mfj + (income - 89450)*0.22)
    elif (income > 190750) and (income <= 364200):
        federal_tax = (fed_max_tax_3_mfj + (income - 190750)*0.24)
    elif (income > 364200) and (income <= 462500):
        federal_tax = (fed_max_tax_4_mfj + (income - 364200)*0.32)
    elif (income > 462500) and (income <= 693750):
        federal_tax = (fed_max_tax_5_mfj + (income - 462500)*0.35)
    else: #i.e if income > 693750
        federal_tax = (fed_max_tax_6_mfj + (income - 693750)*0.37)

else: #filing taxes as a single 
    income -= 13850
    if income <= 11000:
        federal_tax = (income*0.01)
    elif (income > 11000) and (income <= 44725):
        federal_tax = (fed_max_tax_1_single + (income - 11000)*0.12)
    elif (income > 44725) and (income <= 95375):
        federal_tax = (fed_max_tax_2_single + (income - 44725)*0.22)
    elif (income > 95375) and (income <= 182100):
        federal_tax = (fed_max_tax_3_single + (income - 95375)*0.24)
    elif (income > 182100) and (income <= 231250):
        federal_tax = (fed_max_tax_4_single + (income - 182100)*0.32)
    elif (income > 231250) and (income <= 578125):
        federal_tax = (fed_max_tax_5_single + (income - 231250)*0.35)
    else: # if income > 578125
        federal_tax = (fed_max_tax_6_single + (income - 578125)*0.37)

print("Your federal tax owed for 2023 was $",round(federal_tax))


total_tax = state_tax + federal_tax

print("Your total tax owed for 2023 was $",round(total_tax))







