import json
from flask import request,make_response
import json
from apihelpers import get_display_results,verify_endpoints_info


# specific client will return the client with the provided input id
def specific_client():
    invalid = verify_endpoints_info(request.args,['client_id'])
    if(invalid != None):
        return make_response(json.dumps(invalid,default=str),400)
    results = get_display_results('call specific_client(?)',[request.args.get('client_id')])
    results_json = make_response(json.dumps(results,default=str),200)
    return results_json

# add client will add the new client to the database and return the id of newly inserted client
def add_client():
    invalid = verify_endpoints_info(request.json,['username','first_name','last_name','email','image_url','password'])
    if(invalid != None):
        return make_response(json.dumps(invalid,default=str),400)
    results = get_display_results('call add_client(?,?,?,?,?,?)',
    [request.json.get('username'),request.json.get('first_name'),request.json.get('last_name'),request.json.get('email'),
    request.json.get('image_url'),request.json.get('password')])
    results_json = make_response(json.dumps(results,default=str),200)
    return results_json