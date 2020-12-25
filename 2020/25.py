# cLx 2020 day 25

# The handshake used by the card and the door involves an operation
# that transforms a subject number.

def transform(subjectNumber, loopSize):
	# To transform a subject number, start with the value 1
	value = 1

	# Then, a number of times called the loop size, perform
	# the following steps:

	for i in range(loopSize):
		# Set the value to itself multiplied by the subject number
		value*=subjectNumber

		# Set the value to the remainder after dividing the value by 20201227
		value = value % 20201227
	return value

def handshake(cardSecretLoopSize, doorSecretLoopSize):
	# The card always uses a specific, secret loop size when it
	# transforms a subject number. The door always uses a different,
	# secret loop size.

	# The card transforms the subject number of 7 according to the
	# card's secret loop size. The result is called the card's public key.
	cardPublicKey = transform(7, cardSecretLoopSize)

	# The card transforms the subject number of 7 according to the
	# card's secret loop size. The result is called the card's public key.
	doorPublicKey = transform(7, doorSecretLoopSize)

	# The card and door use the wireless RFID signal to transmit the
	# two public keys (your puzzle input) to the other device. Now, the
	# card has the door's public key, and the door has the card's public
	# key. Because you can eavesdrop on the signal, you have both public
	# keys, but neither device's loop size.

	# The card transforms the subject number of the door's public key
	# according to the card's loop size. The result is the encryption key.
	cardEncryptionKey = transform(doorPublicKey, cardSecretLoopSize)

	# The door transforms the subject number of the card's public key
	# according to the door's loop size. The result is the same
	# encryption key as the card calculated.
	doorEncryptionKey = transform(cardPublicKey, doorSecretLoopSize)
	assert cardEncryptionKey == doorEncryptionKey
	return cardEncryptionKey

# If you can use the two public keys to determine each device's loop
# size, you will have enough information to calculate the secret
# encryption key that the card and door use to communicate; this would
# let you send the unlock command directly to the door!

def searchSecretLoopSize(publicKey):
	i = 0
	value = 1
	while True:
		value*= 7
		value%= 20201227
		i+=1
		if value == publicKey:
			return i

def solve(filename):
	print("***", filename, "***")
	cardPublicKey, doorPublicKey = map(int, open(filename).read().split())
	print("cardPublicKey:", cardPublicKey)
	cardSecretLoopSize = searchSecretLoopSize(cardPublicKey)
	print("cardSecretLoopSize:", cardSecretLoopSize)

	print("doorPublicKey:", doorPublicKey)
	doorSecretLoopSize = searchSecretLoopSize(doorPublicKey)
	print("doorSecretLoopSize:", doorSecretLoopSize)

	key = transform(doorPublicKey, cardSecretLoopSize)
	print(key)
	return key

assert solve("input/25.input.test") == 14897079
assert solve("input/25.input")      == 16933668
