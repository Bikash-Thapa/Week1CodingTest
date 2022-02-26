import json
import re

with open('websiteData.txt', encoding="utf8") as websiteData:
    file_data = websiteData.read()

emails_list = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_data)
length = len(emails_list)

email_category = []
for i in range(length):
    split_email = emails_list[i].split('@')
    if split_email[0].count('.') == 1:
        email_category.insert(i, "Human")
    elif len(split_email[0]) < 8:
        email_category.insert(i, "Non-Human")
    else:
        email_category.insert(i, "Undefined")

email_count = []
for j in range (length):
    count = 1
    for k in range (length):
        if j == k:
            continue
        elif emails_list[j] == emails_list[k]:
            count += 1
    email_count.insert(j, count)

result_dictionary = {}

for i in range(length):
    result_dictionary[emails_list[i]]={'Occurance':email_count[i], 'EmailType':email_category[i]}

json_output = json.dumps(result_dictionary)
with open('result.json', 'w', encoding="utf8") as result:
    result_content = result.write(json_output)
