import os
import secrets

size = 16

result = os.urandom(size)
print(result)
print([hex(b) for b in result])

moves = ["rock", "paper", "scissors"]
for i in range(len(moves)):
    secure_random_move = secrets.choice(moves)
    print(i, secure_random_move)

# secrets.token_bytes() - higher level wrapper for os.urandom()
result = secrets.token_bytes(size)
print(result)

# secrets.token_hex()
result = secrets.token_hex(size)
print(result)

# secrets.token_urlsafe()
result = secrets.token_urlsafe(size)
print(result)
