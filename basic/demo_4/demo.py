def remove_char(message: str, edge: int) -> str:
    return message[edge::]


message = 'pynative'
print(remove_char(message, 4))
print(remove_char(message, 2))