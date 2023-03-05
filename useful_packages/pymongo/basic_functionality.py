from pymongo import MongoClient
import pprint








# -------------------------------------------------------------#
"""initialize connection with the DB"""
# -------------------------------------------------------------#

client = MongoClient("mongodb://127.0.0.1:27017")  # connect to local DB

dbs = client.list_database_names()  # get a list of databases names i have
test_db = client.test  # get the "test" database, if there is no test database, create one
collections = test_db.list_collection_names()  # list of collections in the database



# -------------------------------------------------------------#
"""documents insertion"""
# -------------------------------------------------------------#
def insert_document(collection):
    """Insert a single document into a DB
    """
    test_document = {
        "name": "Or",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id  # a bson object id for the insertion of a document
    print(inserted_id)

test_collection = test_db.test  # get the "test" collection, if there is no "test" collection, create one
# insert_document(test_collection)  # call to insert_document function




def insert_many_documents(collection):
    """An example of insertion of many documents in a collection
    """
    first_names = ["Or1", "Or2", "Or3"]
    last_names = ["keren1", "keren2", "keren3"]
    ages = [20, 21, 22, 23]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first name": first_name, "last name": last_name, "age": age}  # single document
        docs.append(doc)
    
    collection.insert_many(docs)  # insert the list of documents into person_collection

production = client.production  # create new DB called "production"
person_collection = production.person_collection  # create new collection called "person_collection"
# insert_many_documents(person_collection)  # call to insert_many_documents function




# -------------------------------------------------------------#
"""parse documents"""
# -------------------------------------------------------------#
printer = pprint.PrettyPrinter()  # to print the documents prettier

def find_all_documents(collection):
    """find all of the documents in a collection and print them 
    """
    documents = collection.find()  # if you leave this function empty it will find all documents in the collection
    print(documents)  # be aware that "documents" is not a list but a pymongo.cursor object 

    for document in documents:  # run over every document in the collection
        printer.pprint(document)  # print the document with pprint (readable)

# find_all_documents(production.person_collection)  # call to find all documents and give it a collection 




def find_document(collection, key: str, value: str):
    """find the fist document in a specific collection that match the requested key-value input
    prints the parsed document
    Args:
        collection: a collection in a DB
        key: str key in a document to search from
        value: str value of the value of the key to parse the specific document
    return: none
    """
    document = collection.find_one({f"{key}": f"{value}"})
    printer.pprint(document)

# find_document(production.person_collection, "first name", "Or1")  # call to find_document function
# find_document(test_db.test, "name", "Or")  # call to find_document function




def count_all_documents(collection):
    """this function prints the amount of documents in a specific collection
    """
    count = collection.count_documents(filter={})
    print(f"Number of documents in \"{collection.name}\" is : {count}")

# count_all_documents(production.person_collection)




def get_document_by_id(collection, document_id: str):
    """get a document from a collection by it's ID
    prints the requested document

    Args:
        collection: the collection to search from
        document_id: the ID to find
    return: none
    """
    from bson.objectid import ObjectId  # necessary to manipulate IDs

    _id = ObjectId(document_id)  # convert from string into object ID which mongoDB can handle
    document = collection.find_one({"_id": _id})  # parse by ID
    printer.pprint(document)

# get_document_by_id(client.production.person_collection, "63fe6710e519a6267e2e3b6c")  # call get_document_by_id function




def get_age_range(min_age: int, max_age: int):
    """An example for specific query of documents
    that bring all of person documents within the age 20 to 21 in the person_collection
    
    Args:
        int min_age: the minimal age to parse
        int max_age: the max age to parse
    """
    query = {"$and": [
        {"age": {"$gte": min_age}},  # gte stands for greater than or equal to
        {"age": {"$lte": max_age}}  # lte stands for less than or equal to
    ]}
    people = person_collection.find(query).sort("age")  # find every document that has the query conditions and parse it by age
    for person in people:
        printer.pprint(person)  # print every person

# get_age_range(20, 21)  # call to get_age_range function




def projection_columns():
    """get documents but contain specific fields in them
    this specific function gets from person_collection every person and prints only its first and second name.
    it skips the document ID
    """
    columns = {"_id": 0, "first name": 1, "last name": 1}  # 0 if you dont wont to get the field, 1 if you do
    people = person_collection.find({}, columns)  # give the find function the columns to extract from the documents
    for person in people:
        printer.pprint(person)

# projection_columns()  # call projection_columns function




# -------------------------------------------------------------#
"""update documents"""
# -------------------------------------------------------------#

def update_person_by_id(person_id):
    """update a document with an update query
    """
    from bson.objectid import ObjectId  # necessary for working with IDs, the import needs to be in the top of the file :)

    _id = ObjectId(person_id)  # convert ID str into ID object 
    all_updates = {  # the update query
        "$set": {"new_field": True},  # if there is a "new_field" field in the document it replace the old one, else create new field
        "$inc": {"age": 1},  # increment the age field by 1
        "$rename": {"first name": "first", "last name": "last"}  # rename fields
    }
    person_collection.update_one({"_id": _id}, all_updates)  # update only one document with a specific id
    person_collection.update_one({"_id": _id}, {"$unset": {"age": ""}})  # delete a filed from a specific document

# update_person_by_id("63fe6710e519a6267e2e3b6d")  # call to update_person_by _id function




def replace_one(person_id):
    """this function useful if the user wants to update all fields
    in a document but to keep the same ID
    
    """
    from bson.objectid import ObjectId  # necessary for working with IDs, the import needs to be in the top of the file :)

    _id = ObjectId(person_id)  # convert ID str into ID object 
    new_doc = {  # the new document to replace with an old one
        "first name": "new first name",
        "last name": "new last name",
        "age": 100 
    }
    person_collection.replace_one({"_id": _id}, new_doc)

# replace_one("63fe6710e519a6267e2e3b6e")




def delete_doc_by_id(person_id):
    """delete a document by an ID
    
    """
    from bson.objectid import ObjectId  # necessary for working with IDs, the import needs to be in the top of the file :)
    _id = ObjectId(person_id)  # convert ID str into ID object 
    person_collection.delete_one({"_id": _id})  # delete the document

# delete_doc_by_id("63fe672df92f2aba36ec5ace")





# -------------------------------------------------------------#
"""relationships"""
# -------------------------------------------------------------#





address = {
    "_id": "63fe6710e519a6267e2e3b6d",
    "street": "Bay Street",
    "number": 2706,
    "city": "San Francisco",
    "country": "United State",
    "zip": "94107"
}

def add_address_embed(person_id, address):
    """add a sub dictionary as a list to existing document
    
    Args:   
        person_id: the id of a document to add the dictionary to
        address: the dictionary to add
    """
    from bson.objectid import ObjectId  # necessary for working with IDs, the import needs to be in the top of the file :)
    _id = ObjectId(person_id)  # convert ID str into ID object 
    person_collection.update_one({"_id": _id}, {"$addToSet": {"addresses": address}})  # add address to the document, if there is an address before it will append this one aside

# add_address_embed("63fe6710e519a6267e2e3b6d", address)  # call to add_address_embed function





def add_address_relationship(person_id, address):
    """add a address document into address collection with the ID of its owner
    
    in other word create a relation ship between the person and the address!
    """
    from bson.objectid import ObjectId  # necessary for working with IDs, the import needs to be in the top of the file :)
    _id = ObjectId(person_id)  # convert ID str into ID object 
    
    address = address.copy()  # because list is pass by reference
    address['owner_id'] = person_id  # the relation ship between the person ID to the address
    address_collection = production.address  # get the address collection, if there is no "address" collection, create one
    address_collection.insert_one(address)  # insert new document

add_address_relationship("63fe6710e519a6267e2e3b6d", address)  # call add_address_relationship


