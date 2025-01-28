Database = {"name": "last name"}
def AddToDatabase():
    name = input("please enter your name:")
    print(Database.update(name))
    last_name = input("please enter your last name:")
    print(Database.update(last_name))
    age = input("please enter your age:")
    print(Database.update(age))
    print(Database)