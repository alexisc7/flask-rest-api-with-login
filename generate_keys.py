import secrets

# Longitud en bytes; 32 bytes → 64 caracteres hexadecimales
SECRET_KEY = secrets.token_hex(32)
JWT_SECRET_KEY = secrets.token_hex(32)

print(f"SECRET_KEY={SECRET_KEY}")
print(f"JWT_SECRET_KEY={JWT_SECRET_KEY}")