import hashlib

def generate_md5_password(password):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return md5_hash

# Contoh penggunaan
password = 'password123'
md5_password = generate_md5_password(password)
print("MD5 Hashed Password:", md5_password)

print (hashlib.md5(password.encode()).hexdigest())
