import csv
import sys

# array of list_of_kwhs used from CSV
list_of_kwh = []

# Murfreesboro Electric Rates
customer_charge = 11.76
cost_of_kwh_per_month = 0.07478
fuel_cost_kwh_per_month = 0.01967

# initialize total to base charge of $11.76
total = customer_charge

def readFile(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        count = 0

        #Get number of lines because extra blank row is read in
        totalLines = sum(1 for row in reader)

        # go back to beginning
        f.seek(0)

        for row in reader:
            # used to ignore the first lines
            if (count >= 15) and (count < totalLines-1):
                list_of_kwh.append(row[1])
            count += 1

def calculate():
    t = total
    for k in list_of_kwh:
        t = t + ((float(k) * cost_of_kwh_per_month) + (float(k) * fuel_cost_kwh_per_month))
    return t

readFile(sys.argv[1])
print(calculate())
    





