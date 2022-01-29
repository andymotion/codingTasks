import requests

#TODO
# Attempting a POST, PUT. and DELETE request on these endpoints will return a HTTP 404
# Tasks
# 1. Using a frame work of your choice, write a test suite of automated tests to test these endpoints
# 2. Include a ReadMe within the project with instructuins on how to run these tests
# 3. Upload your project to GitHUB and share the link

# PUT = update
# POST = create
# Delete = delete

# # #Returns a list of articles
# sky_endpoint_one = 'https://5f99522350d84900163b8737.mockapi.io/tech-test/articles'
# #
# # #Returns a single article
# sky_endpoint_two = 'https://5f99522350d84900163b8737.mockapi.io/tech-test/articles/2'
# #


def post(x):
    response = requests.post(url = x)
    post_code = response.status_code
    if post_code !=404:
        raise ValueError(f"Endpoint Post is not 404. Returned value of {post_code}")
    # print(post_code)
    return post_code


def put(x):
    response = requests.put(url=f"{x} /{put}", data = {"sky": "test"})
    put_code = response.status_code
    if put_code !=404:
        raise ValueError(f"Endpoint Put is not 404. Returned value of {put_code}")
    # print(put_code)
    return put_code

def delete(x):
    response = requests.delete(url = x)
    delete_code = response.status_code
    if delete_code !=404:
        raise ValueError(f"Endpoint Delete is not 404. Returned value of {delete_code}")
    # print(delete_code)
    return delete_code



# sky_one_post = post(sky_endpoint_one) #404
# sky_two_post = post(sky_endpoint_two) #400

# sky_one_put = put(sky_endpoint_one) #404
# sky_two_put = put(sky_endpoint_two) #400

# sky_one_delete = delete((sky_endpoint_one)) #400
# sky_two_delete = delete(sky_endpoint_two) #404



# 400 Bad Request
# The server could not understand the request due to invalid syntax.




