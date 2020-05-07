import configparser
import hashlib
import getpass
import json

config = configparser.ConfigParser()

userTypes = ['doctor', 'nurse', 'lab_assistant', "pharmacist", "patient"]

# read config file
config.read('users.ini')
isLogged = False
loggedUserType = ''
privilege_level = ''


while(isLogged == False):
    # Get Input from user
    print("Login First! (username & password you enter are invisible)")
    username = getpass.getpass(prompt='Enter Username :')
    password = getpass.getpass(prompt='Enter Password :')
    pw = hashlib.md5(password.encode())
    passwordHashed = pw.hexdigest()


    users = config.sections()

    for key in config.sections():
        if(username == config.get(key, 'username') and (passwordHashed == config.get(key, "password"))):
            print("Welcome " + config.get(key, 'username') + "!" +
                  "    (Logged In as a " + config.get(key, 'user_type')+")")
            isLogged = True
            loggedUserName = config.get(key, 'username')
            loggedUserType = config.get(key, 'user_type')
            privilege_level = config.get(key, 'privilege_level')
            break

    if (isLogged == False):
        print("Invalid Login")

# create patient


def createPatient(username, password):
    newPassword = hashlib.md5(password.encode())
    config[username] = {
        "username": username,
        "password": newPassword.hexdigest(),
        "user_type": "patient",
        "privilege_level": "5"
    }
    with open('users.ini', 'w') as configfile:
        config.write(configfile)


# function to add personal details of the patient


def personal_details():
    name = input("Enter name of patient : ")
    username = input("Create a (unique) username for the patient : ")
    id = input("Create (unique) patient id : ")
    age = input("Enter age :")
    location = input("Enter location : ")
    password = input("Create password for the patient : ")
    createPatient(username, password)
    return {
        "name": name,
        "username": username,
        "id": id,
        "age": age,
        "location": location,
        "password": password
    }


# function to add sickness details of the patient


def sickness_details():
    date_of_sick = input("Enter date : ")
    type_of_sick = input("Enter type of sick : ")
    other_details = input("Enter other details : ")
    return {
        "date_of_sick": date_of_sick,
        "type_of_sick": type_of_sick,
        "other_details": other_details
    }

# function to add the drug prescriptions of the patient


def drug_prescriptions():
    drug_details = input("Enter drug details : ")
    period_for_drugs = input("Enter period for drugs : ")
    return {
        "drug_details": drug_details,
        "period_for_drugs": period_for_drugs,
        "status": "Not Given"
    }

# function to add the lab test prescriptions of the patient


def lab_test_prescriptions():
    lab_test_details = input("Enter lab test details : ")
    date_for_test = input("Enter date for the test : ")
    return {
        "lab_test_details": lab_test_details,
        "date_for_test": date_for_test,
        "status": "Not Done Yet"
    }


# function to encounter a patient by a doctor

def encounterPatient():
    record = {
        "personal_details": personal_details(),
        "sickness_details": sickness_details(),
        "drug_prescriptions": drug_prescriptions(),
        "lab_test_prescriptions": lab_test_prescriptions(),
    }
    print("Patient Details Added.")

    def write_json(data, filename='data.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    with open('data.json') as json_file:
        data = json.load(json_file)
        temp = data['records']
        temp.append(record)

    write_json(data)


def getMyDetails():
    username = loggedUserName
    with open('data.json') as f:
        data = json.load(f)
        for record in data['records']:
            if(record['personal_details']['username'] == username):
                print(record)


# function to get all records of all patients


def getAllDetailsOfAllPatients():
    with open('data.json') as f:
        data = json.load(f)
        print(data)


# function to get details of particulat patient

def getDetailsOfPatient(id):
    isAvailable = False
    with open('data.json') as f:
        data = json.load(f)
        for record in data['records']:
            if(id == record['personal_details']['id']):
                print(record)
                isAvailable = True
                break
    if(isAvailable == False):
        print("Wrong Id")


# function to get patientIds


def getpatientIds():
    print("Patient Id's of all patients are below")
    with open('data.json') as f:
        data = json.load(f)
        for record in data['records']:
            print(record['personal_details']['id'])


# function to get personal detsils of the patient


def getPatientPersonalDetails(id):
    with open('data.json') as f:
        data = json.load(f)
        for record in data['records']:
            if(id == record['personal_details']['id']):
                print(record['personal_details'])
                break


# function to get sick details of the patient


def getSickDetails(id):
    with open('data.json') as f:
        data = json.load(f)
        for record in data['records']:
            if(id == record['personal_details']['id']):
                print(record['sickness_details'])
                break

# function to get drug details of the patient


def getPatientDrugDetails(id, update=False):
    with open('data.json') as f:
        data = json.load(f)
        for record in data['records']:
            if(id == record['personal_details']['id']):
                if(update == True):
                    record['drug_prescriptions']['status'] = "Given"
                    with open('data.json', 'w') as file:
                        json.dump(data, file, indent=2)
                    print("Drugs Given")
                print(record['drug_prescriptions'])
                break


# function to get lab prescription details of the patient


def getLabTestPrescriptions(id, update=False):
    with open('data.json') as f:
        data = json.load(f)
        for record in data['records']:
            if(id == record['personal_details']['id']):
                if(update == True):
                    record['lab_test_prescriptions']['status'] = "Lab test done"
                    with open('data.json', 'w') as file:
                        json.dump(data, file, indent=2)
                    print("Lab Test Done")
                print(record['lab_test_prescriptions'])
                break

# funcions to doctor


def doctorAccess():
    loop = True
    while(loop):
        print("Press 1 to encounter patient")
        print("Press 2 to access all details of all patient")
        print("Press 3 to access details of particular patient")
        print("Press 4 to access drug details of particular patient")
        print("Press 5 to access lab details of particular patient")
        print("Press 6 to exit")
        choise = input("Enter number : ")
        if(choise == "1"):
            encounterPatient()
        elif(choise == "2"):
            getAllDetailsOfAllPatients()
        elif(choise == "3"):
            getpatientIds()
            id = input("Enter patient id to get details : ")
            getDetailsOfPatient(id)
        elif(choise == "4"):
            getpatientIds()
            id = input("Enter patient id to get drug details : ")
            getPatientDrugDetails(id)
        elif(choise == "5"):
            getpatientIds()
            id = input("Enter patient id to get lab details : ")
            getLabTestPrescriptions(id)
        elif(choise == "6"):
            print("Thank You!")
            loop = False
        else:
            print("Invalid number!!! Try again")


# Access for the nurse


def nurseAccess():
    loop = True
    while(loop):
        print("Press 1 to access sickness details of particular patient")
        print("Press 2 to access drug details of particular patient")
        print("Press 3 to access lab details of particular patient")
        print("Press 4 to exit")
        choise = input("Enter number : ")
        if(choise == "1"):
            getpatientIds()
            id = input("Enter patient id to get details : ")
            getSickDetails(id)
        elif(choise == "2"):
            getpatientIds()
            id = input("Enter patient id to get drug details : ")
            getPatientDrugDetails(id)
        elif(choise == "3"):
            getpatientIds()
            id = input("Enter patient id to get lab details : ")
            getLabTestPrescriptions(id)
        elif(choise == "4"):
            print("Thank You!")
            loop = False
        else:
            print("Invalid Number!!! Try again.")

# Access for the pharmacist


def pharmacistAccess():
    loop = True
    while(loop):
        print("Press 1 to access drug details of particular patient")
        print("Press 2 to exit")
        choise = input("Enter number : ")
        if(choise == "1"):
            getpatientIds()
            id = input("Enter patient id to get drug details : ")
            getPatientDrugDetails(id, update=True)
        elif(choise == "2"):
            print("Thank You!")
            loop = False
        else:
            print("Invalid number!!! Try again.")

# Access for the lab assistant


def labAssistantAccess():
    loop = True
    while(loop):
        print("Press 1 to access lab details of particular patient")
        print("Press 2 to exit")
        choise = input("Enter number : ")
        if(choise == "1"):
            getpatientIds()
            id = input("Enter patient id to get lab details : ")
            getLabTestPrescriptions(id, update=True)
        elif(choise == "2"):
            print("Thank You!")
            loop = False
        else:
            print("Invalid number!!! Try again")


# Access for the patient

def patientAccess():
    loop = True
    while(loop):
        print("Press 1 to get your details")
        print("Press 2 to exit")
        choise = input("Enter number : ")
        if(choise == "1"):
            getMyDetails()
        elif(choise == "2"):
            print("Thank You!")
            loop = False
        else:
            print("Invalid number!!! Try again")


if(privilege_level == "1"):
    doctorAccess()
elif(privilege_level == "2"):
    nurseAccess()
elif(privilege_level == "3"):
    pharmacistAccess()
elif(privilege_level == "4"):
    labAssistantAccess()
elif(privilege_level == "5"):
    patientAccess()
