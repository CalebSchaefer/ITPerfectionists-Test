#import module for working with json
import json

# class definitions
class Contacts:
 def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    
class Leads:
   def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    
class Registrants:
   def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    
# function to convert json data to dictionary - store as registrants class object
# Returns: registrant class object
def jsonToRegistrant(jsonString):
    jsonString = json.dumps(jsonString)
    jsonDict = json.loads(jsonString)
    registrantDict = jsonDict['registrant']
    registrant = Registrants(registrantDict['name'], registrantDict['email'], registrantDict['phone'])
    return registrant

# function to check LeadsList against ContactsList.
# if user exists in LeadsList, update contactsList with any new info
# Returns: Boolean value indicating whether or not the user already exists in the system
def checkLeads(registrant, UserExists):
    empty = "None"
    i = 0
    while i < len(LeadsList):
        if((registrant.email == LeadsList[i].email and registrant.email != empty)):
            if (LeadsList[i].name == empty and registrant.name != empty):
                LeadsList[i].name = registrant.name
            if((LeadsList[i].phone == empty) and registrant.phone != empty):
                LeadsList[i].phone = registrant.phone
            ContactsList.append(LeadsList[i])
            LeadsList.remove(LeadsList[i])
            UserExists = True
            break
        elif(registrant.phone == LeadsList[i].phone and registrant.phone != empty):
            if (LeadsList[i].name == empty and registrant.name != empty):
                LeadsList[i].name = registrant.name
            if(LeadsList[i].email == empty and registrant.phone != empty):
                LeadsList[i].phone = registrant.phone
            LeadsList[i].name = registrant.name
            ContactsList.append(LeadsList[i])
            LeadsList.remove(LeadsList[i])
            UserExists = True
            break
        i += 1
    return UserExists
    
# this function checks to see if the registrant is already in the contacts list.
# If exists, updates information if empty. 
# Returns: Boolean value indicating whether or not the user already exists in the system
def checkUpdate(registrant, UserExists):
    i = 0
    empty = "None"
    while i < len(ContactsList):
        if ((registrant.email == ContactsList[i].email) and (registrant.email != empty)):
                UserExists = True
                if(ContactsList[i].name == empty):
                    ContactsList[i].name = registrant.name
                if(ContactsList[i].phone == empty):
                    ContactsList[i].phone = registrant.phone
                break
        elif ((registrant.phone == ContactsList[i].phone) and (registrant.phone != empty)):
                UserExists = True
                if(ContactsList[i].name == empty):
                    ContactsList[i].name = registrant.name
                if(ContactsList[i].email == empty):
                    ContactsList[i].email = registrant.email
                break  
        i += 1
    return UserExists
    
# this function takes in ContactsList and formats/prints contents    
def printContacts(ContactsList):
    print("CONTACTS LIST:\n")
    for i in range(len(ContactsList)):
        print(ContactsList[i].name)
        print(ContactsList[i].email)
        print(ContactsList[i].phone + "\n")
        
# this function takes in LeadsList and formats/prints contents         
def printLeads(LeadsList):
    print("\n\n LEADS LIST:\n")
    for i in range(len(LeadsList)):
        print(LeadsList[i].name)
        print(LeadsList[i].email)
        print(LeadsList[i].phone + "\n")
        
# begin main program

# given contacts data - store in Contacts class objects
ContactsList = []
ContactsList.append(Contacts("Alice Brown", "None", "1231112223"))
ContactsList.append(Contacts("Bob Crown", "bob@crowns.com", "None"))
ContactsList.append(Contacts("Carlos Drew", "carl@drewess.com", "3453334445"))
ContactsList.append(Contacts("Doug Emerty", "None", "4564445556"))
ContactsList.append(Contacts("Egan Fair", "eg@fairness.com", "5675556667"))

# given leads data - store in Leads class objects
LeadsList = []
LeadsList.append(Leads("None", "kevin@keith.com", "None"))
LeadsList.append(Leads("Lucy", "lucy@liu.com", "3210001112"))
LeadsList.append(Leads("Mary Middle", "mary@middle.com", "3331112223"))
LeadsList.append(Leads("None", "None", "4442223334"))
LeadsList.append(Leads("None", "ole@olson.com", "None"))

# given registrants data - parse Json and store in Registrants class objects
JsonRegistrants = []
JsonRegistrants.append({
  "registrant": 
     { 
        "name": "Lucy Liu", 
        "email": "lucy@liu.com",
        "phone": "None",
     }
})
JsonRegistrants.append({
  "registrant": 
     { 
        "name": "Doug", 
        "email": "doug@emmy.com",
        "phone": "4564445556",
     }
})
JsonRegistrants.append({
  "registrant": 
     { 
        "name": "Uma Thurman", 
        "email": "uma@thurs.com",
        "phone": "None",
     }
})

# parse registrant data and store in contacts if appropriate
empty = "None"
for i in range(len(JsonRegistrants)):
    UserExists = False
    registrant = jsonToRegistrant(JsonRegistrants[i])
    # check to see if users exist in contacts/leads and if so, update and set flag to true.
    # Otherwise continue until end of structure. Add to contacts list if not found anywhere else
    if(checkUpdate(registrant, UserExists) == False):
        if(checkLeads(registrant, UserExists) == False):
                ContactsList.append(registrant) 
# print results of contacts/leads to screen
printContacts(ContactsList)
printLeads(LeadsList)


    

