

def validateChessDict(board):
    validNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    validPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    pieceCounts = {}
    for k, v in board.items():
        if len(k) != 2 or k[0] not in validNumbers or k[1] not in validLetters:
            print('Invalid board space:', k)
            return False
        
        prefix = v[0]
        if prefix != 'w' and prefix != 'b':
            print('Invalid piece prefix:', v)
            return False
        
        piece = v[1:]
        if piece not in validPieces:
            print('Invalid piece:', v)
            return False
        
        pieceCounts[prefix] = pieceCounts.get(prefix, 0) + 1
        pieceCounts[v] = pieceCounts.get(v, 0) + 1

    if pieceCounts.get('wking', 0) != 1 or pieceCounts.get('bking', 0) != 1:
        print('Both sides need exactly 1 king')
        return False
    
    if pieceCounts.get('wpawn', 0) > 8 or pieceCounts.get('bpawn', 0) > 8:
        print('A side cannot have more than 8 pawns')
        return False
    
    if pieceCounts.get('w', 0) > 16 or pieceCounts.get('b', 0) > 16:
        print('A side cannot have more than 16 pieces')
        return False

    return True

sample = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '7d': 'wpawn'}
print(validateChessDict(sample))