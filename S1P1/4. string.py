bio_data = "Name: sayem, Age: 24, Country: BD, Student of: CSE, IIUC"

# Split the string into a list of information using the comma as the separator
info_list = bio_data.split(', ')

# Print each piece of information separately
for info in info_list:
    print(info.replace(', ', ': '))





bio_data = {
    "Name": "sayem",
    "Age": 24,
    "Country": "BD",
    "Student of": "CSE",
    "University": "IIUC"
}

# Create a formatted string using dictionary values
formatted_bio_data = f"Name: {bio_data['Name']}, Age: {bio_data['Age']}, Country: {bio_data['Country']}, Student of: {bio_data['Student of']}, University: {bio_data['University']}"

# Print the formatted string
print(formatted_bio_data)



def count_characters(string):
    return {char: string.count(char) for char in string}

# Test the function
test_string = "hello world"
char_counts = count_characters(test_string)
print(char_counts)



import re
text = "This is a #great day to learn #regex in #Python!"
hashtags = re.findall(r"#(\w+)", text)
print("Hashtags:", hashtags)

pattern = r'(\+?(88)?(01[0-9])[-\s]?\d{8})|(\+?(8801)[0-9][-?\s]?\d{6})|(\+?(880)1\d{1}[-?\s]?\d{6})'
phone_numbers = [
    "+8801712345678", "01712345678", "8801712345678", "+880 1712-345678",
    "01912345678", "8801912345678", "+880 191-2345678", "0191-2345678",
    "+880 18-12345678", "+8801812345678", "+880 1812-345678", "01812345678",
    "88018-12345678", "0181-2345678", "+880 17 1234 5678", "017 1234 5678",
    "880 17 1234 5678", "+88 01712345678", "+88 0191 234 5678", "+88 01812-345678"
]

for phone_number in phone_numbers:
    match = re.match(pattern, phone_number)
    if match:
        print(f"Matched: {phone_number}")

 


