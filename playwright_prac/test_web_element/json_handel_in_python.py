import json

def return_test_data():
    actual_course = []
    with open("test_json_data.json", "r") as json_file:
        json_data = json.load(json_file)
        print(json_data)

    for k,v in json_data.items():
        if k == 'instructor':
            actual_instructor = v
        if k == 'courses':
            for i in v:
                actual_course.append(i)
    return actual_instructor,actual_course
print(return_test_data())


