xor_values = [
    47, 103, 117, 15, 14, 2, 10, 66, 85, 4, 82, 18, 89, 82, 5, 21, 84, 7, 11, 68, 95,
    4, 82, 65, 91, 2, 82, 22, 95, 86, 81, 65, 8, 87, 4, 22, 92, 85, 87, 70, 13, 81,
    10, 69, 88, 80, 6, 77, 84, 87, 85, 23, 14, 2, 2, 65, 94, 82, 6, 21, 9, 6, 87, 66,
    88, 10, 11, 70, 17
]

key = "l33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33t"

key_values = [ord(c) for c in key]

flag_chars = []
for i, xor_val in enumerate(xor_values):
    key_idx = i % len(key_values)
    key_val = key_values[key_idx]
    original_char = xor_val ^ key_val
    flag_chars.append(chr(original_char))

flag = ''.join(flag_chars)
print(f"Recovered flag: {flag}")

flag=""
print("\nHex values for verification:")
for i, val in enumerate(xor_values):
    key_idx = i % len(key_values)
    key_val = key_values[key_idx]
    original = val ^ key_val
    print(f"{i:3d}: XOR={val:3d} (0x{val:02x}) ^ KEY[{key_idx}]={key_val:3d} ({chr(key_val)}) = {original:3d} (0x{original:02x}) = '{chr(original)}'")
    flag+=chr(original)
print(flag)
