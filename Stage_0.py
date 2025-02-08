
#make a dictionary with all my data
group_members_data = {'Member 1': {
    "Name": "Juan Lobo",
    "Email": "lobojuancamilo1@gmail.com",
    "Slack username" : "juanlobo_11",
    "Hobby" : "videogames",
    "Country": "Colombia",
    "Discipline": "Bioinformatics",
    "Programming Language" : "Python"}}

#print in a understandable way

print(f'''
Member 1:
Name: {group_members_data["Member 1"]["Name"]}
Email: {group_members_data["Member 1"]["Email"]}
Slack username: {group_members_data["Member 1"]["Slack username"]}
Hobby: {group_members_data["Member 1"]["Hobby"]}
Country: {group_members_data["Member 1"]["Country"]}
Discipline: {group_members_data["Member 1"]["Discipline"]}
Programming Language: {group_members_data["Member 1"]["Programming Language"]}''')
