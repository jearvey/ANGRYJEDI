#Just using to generate unique IDs for comms
#using uuid 4 so it doesn't compromise privacy of user UUID

import uuid
id = uuid.uuid4()
print ("The id generated using uuid4() : ",end="") 
print (id) 
