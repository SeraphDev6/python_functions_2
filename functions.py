x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update_values():
    global x
    global students
    global sports_directory
    global z
    x[1][0]=15
    students[0]["last_name"]="Bryant"
    sports_directory["soccer"][0]="Andres"
    z[0]["y"]=30
update_values()

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(some_list):
    for entry in some_list:
        output=""
        for key in entry:
            output+=f"{key} - {entry[key]}, "
        print(output[:-2])
iterate_dictionary(students)

def iterate_dictionary2(key_name, some_list):
    if key_name not in some_list[0]:
        return False
    for entry in some_list:
        print(entry[key_name])
iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for i in some_dict[key]:
            print(i)
        print()
print_info(dojo)