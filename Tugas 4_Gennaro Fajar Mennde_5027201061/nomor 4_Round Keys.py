from operator import xor

def bytes2matrix(text):
    # Converts a 16-byte array into a 4x4 matrix.
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    # Converts a 4x4 matrix into a 16-byte array
    return [print(chr(j), end="") for sub in matrix for j in sub]

def add_round_key(source, key): #state (xor) round_key
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(source)):
        for j in range(len(source)):
            result[i][j] = xor(source[i][j], key[i][j])
            
    return result

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

addKey = add_round_key(state, round_key)
matrix2bytes(addKey)