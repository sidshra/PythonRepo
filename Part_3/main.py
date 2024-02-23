from fastapi import FastAPI, HTTPException, status
from typing import Dict, List

app = FastAPI()

# Sample below
# messages: Dict[str, str] = {
#     "message_1": "Hello, World!",
#     "message_2": "This is a saved message",
# }

messages: Dict[str, str] = {}


# Part 3.1. POST api (10 marks)
# ====================================================================================
# This intends to create a simple message
# Implement the POST /message API with a query parameter taking in str as message:
# - Save the message content (value) and message id (key) into dictionary `messages`
# - The key of the dict should be message_{index}, eg. `message_1`, `message_2`
# - Automatically increment the index value somehow
# - Ensure that you can avoid overwriting and existing key when calling this POST API
# - If the message is saved successfully, check to status code 200
@app.post("/message")
def create_message(message: str):
    # ========================================================================
    # @app.post("/message", status_code=200) -> to make sure the default status code is 200
    ct = 1
    msg_list = []

    # Splitting the key & incrementing the number
    for i in messages.keys():
        split_list = i.split("_")
        msg_list.append(int(split_list[1]))
        msg_list.sort()
    for i in range(len(msg_list)):
        if msg_list[i] == ct:
            ct += 1
        else:
            break
    # Assigning to the newly added value to the new key
    key_val = "message_" + str(ct)
    messages[key_val] = message
    return f"{message}: Saved successfully "
    # ========================================================================


# Part 3.2. GET all messages api (3 marks)
# ====================================================================================
# Return all saved messages, with code 200
# If there is no message, return code 404
@app.get("/")
def get_all_messages() -> dict:
    # ========================================================================
    sorted_messages: Dict[str, str] = {}
    msg_list = []
    for i in messages.keys():
        split_list = i.split("_")
        msg_list.append(int(split_list[1]))
    msg_list.sort()
    for i in range(len(msg_list)):
        key_val = "message_" + str(msg_list[i])
        sorted_messages[key_val] = messages[key_val]
    if sorted_messages == {}:
        raise HTTPException(status_code=404, detail="There is no message")
    else:
        return sorted_messages
    # ========================================================================


# Part 3.3. GET single messages api, given a message_key (5 marks)
# ====================================================================================
# Get a message content, given a message key, eg. GET /message/message_1
# If a key does not exist, return code 404
@app.get("/message/{message_key}")
def get_message(message_key: str) -> str:
    # ========================================================================
    if message_key in messages.keys():
        return messages[message_key]
    else:
        raise HTTPException(status_code=404, detail="Message not found")
    # ========================================================================


# Part 3.4. PATCH single messages api, give message_key and new_message (5 marks)
# ====================================================================================
# Update message content, given a message key,
# - eg. PATCH /message/message_1 and also provide query string variable `message`
# - If a message key does not exist, return code 404
# - If a message key indeed exist, override, and return the updated value
@app.patch("/message/{message_key}")
def update_message(message_key: str, new_message: str) -> str:
    # ========================================================================
    if message_key in messages.keys():
        messages[message_key] = new_message
        return messages[message_key]
    else:
        raise HTTPException(status_code=404, detail="Message not found")
    # ========================================================================


# Part 3.5. DELETE single message given message_key (3 marks)
# ====================================================================================
# Delete message key and value, given a message_key,
# - eg. DELETE /message/message_1
# - If a message key does not exist, return code 404
# - If a message key indeed exist, delete, and return the message value (similar to pop)
@app.delete("/message/{message_key}")
def delete_message(message_key: str) -> str:
    # ========================================================================
    if message_key in messages.keys():
        messages.pop(message_key)
        return f"{message_key}: Successfully deleted "
    else:
        raise HTTPException(status_code=404, detail="Message not found")
    # ========================================================================
