<<<<<<< HEAD
import requests


facade_service = "http://localhost:5000/facade_service"

message = {"message": "Test message"}
post_response = requests.post(facade_service, data=message)
print(post_response.content.decode(), post_response.status_code)

get_response = requests.get(facade_service)
print(get_response.content.decode())

=======
import requests


facade_service = "http://localhost:5000/facade_service"

message = {"message": "Test message"}
post_response = requests.post(facade_service, data=message)
print(post_response.content.decode(), post_response.status_code)

get_response = requests.get(facade_service)
print(get_response.content.decode())

>>>>>>> master
