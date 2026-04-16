from Crypto.Cipher import AES

tag=bytes.fromhex("8861f4b44208b79a8a11041fc02911a9")
key=bytes.fromhex("ea5143c3c93e8e8a359eeedf9da0b130")
nonce=bytes.fromhex("7d7e3beb5f79bb18700f462f3aa91576") # iv

with open("tractor.png", "rb") as f:
    png_data = f.read()

# Try to find and decrypt the hidden data using a rolling window of 69 bytes
window_size = 69
found_data = False

# Try rolling windows through the file
for i in range(len(png_data) - window_size + 1):
    window_data = png_data[i:i+window_size]
    try:
        # Try to decrypt this window data using the cipher and tag
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(window_data, tag)

        # If we get here, decryption was successful
        print("Successfully decrypted data at offset {}!".format(i))
        print(window_data)
        print("Decrypted data: {}".format(decrypted_data))
        
        # Try to decode as text if possible
        try:
            decoded_text = decrypted_data.decode('utf-8')
            print("Decoded text: {}".format(decoded_text))
        except UnicodeDecodeError:
            print("Could not decode as UTF-8 text.")
        
        found_data = True
        break
    
    except (ValueError, KeyError) as e:
        # This window failed to decrypt, continue to the next one
        continue