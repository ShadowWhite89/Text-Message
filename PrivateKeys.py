 # Public Key Generator
 2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
 3.
 4. import random, sys, os, primeNum, cryptomath
 5.
 6.
 7. def main():
 8.     # Create a public/private keypair with 1024-bit keys:
 9.     print('Making key files...')
10.     makeKeyFiles('al_sweigart', 1024)
11.     print('Key files made.')
12.
13. def generateKey(keySize):
14.     # Creates public/private keys keySize bits in size.
15.     p = 0
16.     q = 0
17.     # Step 1: Create two prime numbers, p and q. Calculate n = p * q:
18.     print('Generating p prime...')
19.     while p == q:
20.         p = primeNum.generateLargePrime(keySize)
21.         q = primeNum.generateLargePrime(keySize)
22.     n = p * q
23.
24.     # Step 2: Create a number e that is relatively prime to (p-1)*(q-1):
25.     print('Generating e that is relatively prime to (p-1)*(q-1)...')
26.     while True:
27.         # Keep trying random numbers for e until one is valid:
28.         e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
29.         if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
30.             break
31.
32.     # Step 3: Calculate d, the mod inverse of e:
33.     print('Calculating d that is mod inverse of e...')
34.     d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
35.
36.     publicKey = (n, e)
37.     privateKey = (n, d)
38.
39.     print('Public key:', publicKey)
40.     print('Private key:', privateKey)
41.
42.     return (publicKey, privateKey)
43.
44.
45. def makeKeyFiles(name, keySize):
46.     # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
47.     # is the value in name) with the n,e and d,e integers written in
48.     # them, delimited by a comma.
49.
50.     # Our safety check will prevent us from overwriting our old key files:
51.     if os.path.exists('%s_pubkey.txt' % (name)) or
          os.path.exists('%s_privkey.txt' % (name)):
52.         sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt
              already exists! Use a different name or delete these files and
              rerun this program.' % (name, name))
53.
54.     publicKey, privateKey = generateKey(keySize)
55.
56.     print()
57.     print('The public key is a %s and a %s digit number.' %
          (len(str(publicKey[0])), len(str(publicKey[1]))))
58.     print('Writing public key to file %s_pubkey.txt...' % (name))
59.     fo = open('%s_pubkey.txt' % (name), 'w')
60.     fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
61.     fo.close()
62.
63.     print()
64.     print('The private key is a %s and a %s digit number.' %
          (len(str(privateKey[0])), len(str(privateKey[1]))))
65.     print('Writing private key to file %s_privkey.txt...' % (name))
66.     fo = open('%s_privkey.txt' % (name), 'w')
67.     fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
68.     fo.close()
69.
70.
71. # If makePublicPrivateKeys.py is run (instead of imported as a module),
72. # call the main() function:
73. if __name__ == '__main__':
74.     main()
