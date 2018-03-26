from flask import request

with app.test_request_context('/user', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/user'
    assert request.method == 'GET'
