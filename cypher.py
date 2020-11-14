import argparse
import math
ap = argparse.ArgumentParser(
     formatter_class=argparse.RawDescriptionHelpFormatter,
     description='''
                                ============================================
                                                <<CYPHER>>
                                ============================================
                                BY:      _       __
                                        || \\\\   ||  \\\\  || // \\\\  //
                                        ||  ||  ||__//  ||//   \\\\//
                                        ||  ||  || \\\\   ||\\\\    ||
                                        ||_//   ||  \\\\  || \\\\   ||

                                ============================================
                                ============================================
         ''')

ap.add_argument("-v",
                "--verbose",
                required=False, 
                action='store_true',
                help='(NOT IMPLEMENT YET) You can see the cipher background as the matrix or the array used for the encodig')
ap.add_argument("-k",
                "--key",
                required=True, 
                help='Is the secret key for base encryption. Depending on the cipher algorithm you choose, you\'ll have to use a number or a word')
ap.add_argument("-d",
                "--data",
                required=True,
                help='Is the message to encrypt/decrypt')
ap.add_argument("-a",
                "--algorithm",
                required=True,
                help='specify the algorithm you want to use',
                choices=['TRANS','TRANS_KEY','CAESAR'])
ap.add_argument("-u","--uncipher",
                required=False,
                action='store_true',
                help='use this if you want to decrypt a message')

args = vars(ap.parse_args())

#====================================================
def checkKey(key, algorithm, message):
    if algorithm == 'TRANS' or algorithm == 'CAESAR':
        try:
            key = int(args.get('key'))
        except:
            print(message)
            exit()
    elif algorithm == 'TRANS_KEY':
        try:
            key = str(args.get('key'))
        except:
            print(message)
            exit()

    return key    
#====================================================
#Cipher algorithms
def transpositionCipher():
    key = checkKey(args.get('key'),args.get('algorithm'), 'You must specify a number for key while using Numeric Transposition Cipher')
    data = args.get('data')
    encoded = ''
    if args.get('uncipher') == True :
        row = key
        col = int(math.ceil(len(data)/key))
        matrix = [[0] * col for i in range(row)]

        i=0
        x=0
        while i < row :
            j=0
            while j < col :
                if x < len(data) :
                    matrix[i][j] = data[x]
                else :
                    matrix[i][j] = ' '
                x+=1
                j+=1
            i+=1
        
        i=0
        while i < col :
            j=0
            while j < row :
                encoded += matrix[j][i]
                j+=1
            i+=1

        if args.get('verbose') == True :
            print("")

            print('Data:     \t'+'\"'+ str(args.get('data'))+'\"')
            print('Key:      \t'+'\"'+ str(args.get('key'))+'\"')
            print('Algorithm:\tTransposition with numeric key')
            print('Uncipher: \t'+str(args.get('uncipher')))

            print("")
            print("MATRIX:")

            i=0
            while i < row :
                print("\t\t"+str(matrix[i]))
                i+=1
            
            print("")

        print("\""+str(encoded)+"\"")
    else:
        col = key
        row = int(math.ceil(len(data)/key))
        matrix = [[0] * col for i in range(row)]

        i=0
        x=0
        while i < row :
            j=0
            while j < col :
                if x < len(data) :
                    matrix[i][j] = data[x]
                else :
                    matrix[i][j] = ' '
                x+=1
                j+=1
            i+=1
        
        i=0
        while i < col :
            j=0
            while j < row :
                encoded += matrix[j][i]
                j+=1
            i+=1

        if args.get('verbose') == True :
            print("")

            print('Data:     \t'+'\"'+ str(args.get('data'))+'\"')
            print('Key:      \t'+'\"'+ str(args.get('key'))+'\"')
            print('Algorithm:\tTransposition with numeric key')
            print('Uncipher: \t'+str(args.get('uncipher')))

            print("")
            print("MATRIX:")

            i=0
            while i < row :
                print("\t\t"+str(matrix[i]))
                i+=1
            
            print("")
        
        print("\""+str(encoded)+"\"")

def transpositionKeyCipher():
    key = checkKey(args.get('key'),args.get('algorithm'), 'You must specify a number for key while using Caesar Cipher')
    data = args.get('data')
    encoded = ''
    #Deleting repeated chars
    order = list(dict.fromkeys(key))
    sort = list(dict.fromkeys(key))

    if args.get('uncipher') == False :
    #Definig zero-matrix size
        row = len(order)
        col = int(math.ceil(len(data)/row))
        matrix = [[0] * col for i in range(row)]
    #Creating matrix
        i=0
        x=0
        while i < row :
            j=0
            while j < col :
                if x < len(data) :
                    matrix[i][j] = data[x]
                else :
                    matrix[i][j] = ' '
                x+=1
                j+=1
            i+=1
    #Creating relation table
        for i in range(len(order)) :
            sort[i] = [order[i],matrix[i]]
    #Sorting matrix by key
        sort.sort()
    #Encryption cycle
        i=0
        while i < col :
            j=0
            while j < row :
                encoded += sort[j][1][i]
                j+=1
            i+=1
    #Result
        if args.get('verbose') == True :
            print("")

            print('Data:     \t'+'\"'+ str(args.get('data'))+'\"')
            print('Key:      \t'+'\"'+ str(args.get('key'))+'\"')
            print('Algorithm:\tTransposition with keyword')
            print('Uncipher: \t'+str(args.get('uncipher')))

            print("")
            print('KEY:\t\t'+ str(order))
            print("MATRIX:")

            for i, x in enumerate(sort,start=0) :
                print("\t\t"+str(x[0])+":\t"+str(x[1]))

        print("")
        print("\""+str(encoded)+"\"")
  #=====================================================        
    else :
    #Definig zero-matrix size
        col = len(order)
        row = int(math.ceil(len(data)/col))
        matrix = [[0] * col for i in range(row)]
    #Creating matrix
        i=0
        x=0
        while i < row :
            j=0
            while j < col :
                if x < len(data) :
                    matrix[i][j] = data[x]
                else :
                    matrix[i][j] = ' '
                x+=1
                j+=1
            i+=1
        #Getting the ordered key    
        order.sort()
        #Defining matrix with ordered key
        tmp= []
        tmpMatrix = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                tmp+=matrix[j][i]
            tmpMatrix+=[[order[i],tmp]]
            tmp=[]
        #Decoding message comparing original key with tmp matrix (with ordered key)
        for i in range(len(sort)):
            for j in range(len(sort)):
                if sort[i] == tmpMatrix[j][0]:
                    for x in tmpMatrix[j][1]:
                        encoded+=x

        if args.get('verbose') == True :
            print("")

            print('Data:     \t'+'\"'+ str(args.get('data'))+'\"')
            print('Key:      \t'+'\"'+ str(args.get('key'))+'\"')
            print('Algorithm:\tTransposition with keyword')
            print('Uncipher: \t'+str(args.get('uncipher')))

            print("")
            print('KEY:\t\t'+ str(sort))
            print("MATRIX:")

            for i in range(len(sort)):
                for j in range(len(sort)):
                    if sort[i] == tmpMatrix[j][0]:
                        print("\t\t"+str(tmpMatrix[j][0]),end=":\t")
                        print(tmpMatrix[j][1])
            print("")    

        print("\""+str(encoded)+"\"")
            
def caesarCipher():
    key = checkKey(args.get('key'),args.get('algorithm'), 'You must specify a number for key while using Caesar Cipher')
    data = args.get('data')
    encoded = ''
    if args.get('uncipher') == True:
        for i in data:
            MAYUS = False
            MINUS = False
            v = ord(i) - key

            if i == " ":
                encoded+= " "
                continue
            if v > 64 and v < 91 :
                MAYUS=True
            if v > 96 and v < 123 :
                MINUS= True
            
            if MINUS==False and MAYUS==False :
                v+=26

            encoded+= chr(v)
        
        if args.get('verbose') == True :
            print("")

            print('Data:     \t'+'\"'+ str(args.get('data'))+'\"')
            print('Key:      \t'+'\"'+ str(args.get('key'))+'\"')
            print('Algorithm:\tCaesar Cipher')
            print('Uncipher: \t'+str(args.get('uncipher')))
            
            print("\nARRAY:")
            for i,x in enumerate(encoded):
                print("\t\t["+str(data[i])+"] -> ["+str(x)+"]" )
            
            print("") 

        print("\""+str(encoded)+"\"")
    else:
        for i in data:
            MAYUS = False
            MINUS = False
            v = ord(i) + key

            if i == " ":
                encoded+= " "
                continue
            if v > 64 and v < 91 :
                MAYUS=True
            if v > 96 and v < 123 :
                MINUS= True
            
            if MINUS==False and MAYUS==False :
                v-=26

            encoded+= chr(v)
        
        if args.get('verbose') == True :
            print("")

            print('Data:     \t'+'\"'+ str(args.get('data'))+'\"')
            print('Key:      \t'+'\"'+ str(args.get('key'))+'\"')
            print('Algorithm:\tCaesar Cipher')
            print('Uncipher: \t'+str(args.get('uncipher')))
            
            print("\nARRAY:")
            for i,x in enumerate(encoded):
                print("\t\t["+str(data[i])+"] -> ["+str(x)+"]" )
            
            print("")

        print("\""+str(encoded)+"\"")

methods = {'TRANS':transpositionCipher, 'TRANS_KEY': transpositionKeyCipher, 'CAESAR':caesarCipher}

#====================================================

if args.get('algorithm') in methods:
    methods[args.get('algorithm')]()


