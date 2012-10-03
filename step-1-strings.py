message = 'Welcome to the quick introduction to Python talk at the Python North East User Group.'
message
'Python' in message
'PHP' in message
'Ruby' not in message

for letter in message:
    print(letter)

real_message = " We've got pizza!"
full_message = message + real_message + " And, we've got drinks!"
full_message
real_message * 5

len(message)
message[6]
message[-11]

message[56:73]
message[56:-12]
message[-29:-12]

message[56:]
message[-29:]
message[:48]
message[0:48]

message[56:73:1]
message[56:73:3]
message[::4]

message[0:7:0]

message[7:0:-1]
message[6::-1]
message[0::-1]
message[::-1]

message.lower()
message.upper()
message.title()
message.capitalize()

message.startswith('Welcome')
message.endswith('bye!')

message.split()
message.split('to')
