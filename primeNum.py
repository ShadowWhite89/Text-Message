 def makeKeyFiles(name, keySize):
     # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
     # is the value in name) with the n,e and d,e integers written in
     # them, delimited by a comma.
     # Our safety check will prevent us from overwriting our old key files:
     if os.path.exists('%s_pubkey.txt' % (name)) or
          os.path.exists('%s_privkey.txt' % (name)):
      sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt
            already exists! Use a different name or delete these files and
            rerun this program.' % (name, name)
     print()
     print('The public key is a %s and a %s digit number.' %
          (len(str(publicKey[0])), len(str(publicKey[1]))))
     print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
     fo.close()
   print()
    print('The private key is a %s and a %s digit number.' %
          (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
     fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
  fo.close()
   # If makePublicPrivateKeys.py is run (instead of imported as a module),
   # call the main() function:
  if __name__ == '__main__':
    main()
