import time
from pymongo import MongoClient
connection = MongoClient('10.19.132.51')

from g2algorithm.debug import *


def delete_data_from_collection( database, collection_name, cond, debug=0):

    collection = get_collection_from_mongo( database, collection_name )
    collection.remove( cond )
    print "data removed"

    return 0



def get_next_sequence_id(database, index, collection):

    db = connection[database]

    existed = db[collection].find_one({"_id": index})
    if existed:
        ret = db[collection].find_and_modify(
            query={"_id": index},
            update={"$inc": {"seq": 1}},
            new=True
        )

        return ret['seq']
    else:
        db[collection].save({
            "_id": index,
            "seq": 1,
        })

        return 1



def get_collection_from_mongo( database, collection  ):


    db = connection[database]

    if collection in db.collection_names():
        output = db[ collection ]
    else:
        print "create new collection %s in %s " % (collection, database)
        db.create_collection( collection )
        output = db[ collection ]



    return output


def update_data_of_collection(database, collection_name, cond, update_dict, debug=0 ):

    collection = get_collection_from_mongo(database,  collection_name )
    collection.update( cond, update_dict, multi=True)




def save_back_to_mongo( database, collection_name, data):

    collection = get_collection_from_mongo(database,  collection_name )
    collection.save( data )




def insert_to_mongo( data, database, collection_name ):

    collection = get_collection_from_mongo(database, collection_name )
    collection.insert( data )


def get_distinct_value_from_collection( database, collection, cond, key ):

    data = get_collection_from_mongo( database, collection )
    output = data.find(cond).distinct(key)
    return output



def get_data_from_collection_by_cond( database, collection, cond, debug=0 ):

    datas = get_collection_from_mongo( database, collection ) 
    temp = datas.find( cond  )
    #output = list( temp )
    output = []
    for x in temp:
        output.append( x )

    return output




if __name__ == "__main__":


    database = "lipu_test"
    #get_collection_from_mongo( database, "tasks"  )
    collection = "tasks"

    '''
    tasks = get_data_from_collection_by_cond(database, collection, {'idProject' : 264} )
    print tasks[0]
    insert_to_mongo(  tasks[0], database, collection )
    save_back_to_mongo( database, collection, tasks[0])
    '''

    '''
    # This will take 1 min to execute
    print get_data_from_collection_by_cond(database, collection, {'idToolchain' : {"$in" : [2, 5]}, 'idBenchmark' : 2000001 , 'set' : '', 'idTarget':13   } )
    '''

    exit()




