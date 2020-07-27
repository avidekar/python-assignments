import json

def sort_by_price_ascending(json_string):

    # convert json object to python object
    python_obj = json.loads(json_string)

    # sort the python object with the given criteria
    # order items by price in ascending order, if price is same, then order by
    # alphabetical order
    sorted_python_obj = sorted(python_obj, key=lambda index: (index['price'], index['name']))
    # convert python object back to json object
    ret_json_obj = json.dumps(sorted_python_obj)

    return ret_json_obj

sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')