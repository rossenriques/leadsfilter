import csv
import pdb
import os

updated_list=[]

def addCSV(newfile):
    with open(newfile, 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header row if it exists
        for row in csv_reader:
            # Process each row
            updated_list.append(row)
            # print(row)

print("Current working directory:", os.getcwd())

# Directory path
directory = r"C:\Users\Dell\Documents\Leads\Hvac"


# Iterate through each file in the directory
for file in os.listdir(directory):
    # Generate the full file path
    file_path = os.path.join(directory, file)
    
    # Check if the file is a CSV (optional, if you only want to handle CSV files)
    if file.endswith(".csv"):
        addCSV(file_path)

print(len(updated_list))

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

newList=sort_and_deduplicate(updated_list)

print(len(newList))

final_list = []
seen_entries = set()

for item in newList:
    # breakpoint()
    businessName = item[0].strip().lower()
    phoneNumber = item[13].strip()

    unique_key = (businessName, phoneNumber)

    cityStateZipBackup = item[4]
    cityStateZip = item[2]

    finalCityStateZip = cityStateZip if cityStateZip.strip() != "" else cityStateZipBackup
    businessType = item[5]
    excluded_types = ["department", "hotel", "auto", "advertising", "apartment", "architect", "audio", "store", "car", "business", "chevrolet", "chiropracter", "computer", "consultant", "crane", "dentist", "engine", "doctor", "gym", "supplier"]
    excluded_names = ["walmart", "the home depot", "sears", "lowes", "autozone", "daikin"]
    included_types = ["Air", "repair", "service", "contractor", "heat", "hvac"]

    if (phoneNumber.strip() and
        all(keyword not in businessType.lower() for keyword in excluded_types) and
        any(keyword in businessType.lower() for keyword in included_types) and
        all(keyword not in businessName.lower() for keyword in excluded_names) and
        unique_key not in seen_entries):
        seen_entries.add(unique_key)

        final_list.append({
            "BusinessName": businessName,
            "PhoneNumber": phoneNumber,
            "cityStateZip": finalCityStateZip,
            "Type": businessType
    }) 

print(final_list)
print(len(final_list))



def write_hashed_list_to_csv(data, filename="output.csv"):
    """
    Writes a list of dictionaries (where values might be hashed) to a CSV file.

    Args:
        data: A list of dictionaries.
        filename: The name of the CSV file to write to.
    """
    if not data:
        return  # Avoid writing empty file

    fieldnames = data[0].keys()

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_hashed_list_to_csv(final_list, "hashed_data.csv")  