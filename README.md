# Sending data:
* Write into the bus file with this format (no space): "request",conversion_type, original_unit, target_unit, original_val,"pending"
* The microservice will split(",") the string into list items in order to process the instruction.
* Conversion type currently supports currency and time. Check the codes to see the scope. Conversion table is hardcoded. It is not exhaustive yet.
* The microservice will only activate if it finds "request" AND "pending". Make sure to send correct string.

# Receiving data:
* Microservice writes into the bus file with this format: "response",new_value,"complete"
* I recommend your program to scan for "response" AND "complete" as a confirmation that the middle value can be retrieved.
* Use splint(",") to make it easier to receive data and turn it into function list. 
