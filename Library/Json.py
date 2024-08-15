import json

# 1. Load JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# 2. Access and print JSON data
print("Company Name:", data['company']['name'])
print("First Employee Name:", data['employees'][0]['name'])

#  # 3. Modify JSON data
# data['company']['location'] = 'San Francisco'
# data['employees'][1]['skills'].append('social media')

# # 4. Add a new employee
# new_employee = {
#     "id": 3,
#     "name": "Alice Johnson",
#     "age": 28,
#     "department": "HR",
#     "skills": ["recruitment", "employee relations"]
# }
# data['employees'].append(new_employee)

# 5. Serialize Python object to JSON and save to a file
# with open('updated_data1.json', 'w') as file:
#     json.dump(data, file, indent=4)

# # 6. Pretty-print JSON data
# pretty_json = json.dumps(data, indent=4)
# print("Pretty JSON:\n", pretty_json)

# 7. Load JSON data from a string
# json_string = '''
# {
#     "product": "Laptop",
#     "brand": "XYZ",
#     "price": 1200,
#     "features": {
#         "processor": "Intel i7",
#         "ram": "16GB",
#         "storage": "512GB SSD"
#     }
# }
# '''
# product_data = json.loads(json_string)
# print("Product Name:", product_data['product'])

# 8. Serialize Python object to JSON string
# python_object = {
#     "name": "Sample",
#     "numbers": [1, 2, 3, 4, 5]
# }
# json_string = json.dumps(python_object)
# print("Serialized JSON String:", json_string)