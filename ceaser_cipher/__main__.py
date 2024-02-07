import art

def cipher_dict(shift_amount):
	n = shift_amount % len(alphabet)
	shift_part = alphabet[0:n]
	shifted_part = alphabet[n:]
	shifted_alphabet = shifted_part + shift_part
	# makes a dictionary of the alphabet to it's respective shifted letter i.e shift = implies {'a': 'b',...}
	return {alphabet[i]: shifted_alphabet[i] for i in range(len(alphabet))}

def ceaser(plain_text, shift_amount, direction):
	encryption_dict = cipher_dict(shift_amount)


	if direction == "encode":
		# create an empty string
		encrypted_text = ""
		# translate text from alphabet to the shifted alphabet via cipher dict
		for l in list(plain_text):
			if l in alphabet:
				encrypted_text += encryption_dict[l]
			else:
				
				encrypted_text += l
		print(f"The encoded text is \n {encrypted_text}")
		
	elif direction == "decode":
		decrypted_text = ""
		for l in list(plain_text):
			if l in alphabet:
				decrypted_text += list(encryption_dict.keys())[list(encryption_dict.values()).index(l)]
				
			else:
				decrypted_text += l
		print(f"The decoded text is \n {decrypted_text}")

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep_going ="yes"
while keep_going.lower() == "yes":
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	ceaser(plain_text=text, shift_amount=shift, direction=direction)
	keep_going = input("Would you like to keep going?(yes/no)")

