import csv
import pdb

updated_list=[]

def addCSV(newfile):
    with open(newfile, 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header row if it exists
        for row in csv_reader:
            # Process each row
            updated_list.append(row)
            # print(row)

addCSV('ArizonaSmokeShops.csv')
addCSV('ColoradoSmokeShops.csv')
addCSV('IdahoSmokeShops.csv')
addCSV('MontanaSmokeShops.csv')
addCSV('NewMexicoSmokeShops.csv')
addCSV('UtahSmokeShops.csv')
addCSV('WyomingSmokeShops.csv')


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

# # Business Name
# print(newList[0][0])

# # Phone Number
# print(newList[0][13])
# # City, State
# print(newList[0][4])
# #BusinessType
# print(newList[0][5])

final_list = []

for item in newList:
    # breakpoint()
    businessName = item[0]
    phoneNumber = item[13]
    cityStateZip = item[4]
    businessType = item[5]
    if (phoneNumber.strip() != "" and 
        ("tobacco" in businessType.lower() or "cannabis" in businessType.lower() or "smoke" in businessType.lower() or "vaporizer" in businessType.lower() or "cigar" in businessType.lower())):
        final_list.append({
            "BusinessName": businessName,
            "PhoneNumber": phoneNumber,
            "cityStateZip": cityStateZip,
            "Type": businessType
        })
    # final_list.append({"BusinessName": businessName, "PhoneNumber": phoneNumber, "cityStateZip": cityStateZip, "Type": businessType})



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