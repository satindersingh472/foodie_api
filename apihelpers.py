
# import single function from dbhelpers to connect
# execute and close the connection
from dbhelpers import conn_exe_close
# import request, make_response,jsonify from flask
from flask import make_response
import json

# single function to handle database interactions
# and based on results will send errors
def get_display_results(statement,args_list):
    return conn_exe_close(statement,args_list)
    
# will verifiy end points arguments for presence
# if necessary arguments not sent then remind the user to send
def verify_endpoints_info(sent_data,required_args):
    for data in required_args:
        if(sent_data.get(data) == None):
            return f'The {data} argument is required'
