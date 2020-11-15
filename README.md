# Cypher
Python Cypher Tool

Support for:
  - Caesar cipher
  - Columns Transposition with numeric key
  - Columns Transposition with keyword

Options:
  * -h, --help
        Shows usage manual for Python Cypher Tool
  * -v, --verbose
        With this option you will be able to see the encoding metadata and details
  * -a, --algorithm   [ALGORITHM]
        You have to specify the algorith you want to use
          - TRANS       -> Columns Transposition with numeric key
          - TRANS_KEY   -> Columns Transposition with keyword
          - CAESAR      -> Caesar cipher
  * -k, --key         [NUMKEY | KEYWORD]
        You have to specify the key for the encryption depending on the algorithm
          - TRANS       -> Numeric
          - TRANS_KEY   -> Keyword
          - CAESAR      -> Numeric
  * -d, --data        [DATA]
        You have to specify the message to encrypt    
  * -u, --uncipher
 
