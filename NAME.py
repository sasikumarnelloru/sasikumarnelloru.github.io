letters = {
    'A': [' AAA ', 'A   A', 'AAAAA', 'A   A', 'A   A'],
    'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
    'C': [' CCCC', 'C    ', 'C    ', 'C    ', ' CCCC'],
    'D': ['DDDD ', 'D   D', 'D   D', 'D   D', 'DDDD '],
    'E': ['EEEEE', 'E    ', 'EEEEE', 'E    ', 'EEEEE'],
    'F': ['FFFFF', 'F    ', 'FFF  ', 'F    ', 'F    '],
    'G': [' GGGG', 'G    ', 'G  GG', 'G   G', ' GGGG'],
    'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
    'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
    'J': ['JJJJJ', '    J', '    J', 'J   J', ' JJJ '],
    'K': ['K   K', 'K  K ', 'KK   ', 'K  K ', 'K   K'],
    'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
    'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
    'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
    'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
    'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
    'Q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q  QQ', ' QQ Q'],
    'R': ['RRRR ', 'R   R', 'RRRR ', 'R  R ', 'R   R'],
    'S': [' SSSS', 'S    ', 'SSSS ', '    S', 'SSSS '],
    'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
    'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
    'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
    'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
    'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
    'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
    'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
    'a': [' aaa ', 'a   a', 'a   a', 'a  aa', ' aa a'],
    'b': ['b    ', 'b    ', 'bbbb ', 'b   b', 'bbbb '],
    'c': [' cccc', 'c    ', 'c    ', 'c    ', ' cccc'],
    'd': ['    d', '    d', ' dddd', 'd   d', ' dddd'],
    'e': [' eeee', 'e   e', 'e  ee', 'e    ', ' eeee'],
    'f': [' ffff', 'f    ', 'fff  ', 'f    ', 'f    '],
    'g': [' ggg ', 'g   g', ' ggg ', '    g', ' gggg'],
    'h': ['h    ', 'h    ', 'hhhh ', 'h   h', 'h   h'],
    'i': ['  i  ', '  i  ', '  i  ', '  i  ', '  i  '],
    'j': ['  j  ', '  j  ', '  j  ', '  j  ', 'jjj  '],
    'k': ['k   k', 'k  k ', 'kk   ', 'k  k ', 'k   k'],
    'l': ['  l  ', '  l  ', '  l  ', '  l  ', '  l  '],
    'm': [' m m ', 'm m m', 'm m m', 'm   m', 'm   m'],
    'n': [' nnn ', 'n   n', 'n   n', 'n   n', 'n   n'],
    'o': [' ooo ', 'o   o', 'o   o', 'o   o', ' ooo '],
    'p': ['pppp ', 'p   p', 'pppp ', 'p    ', 'p    '],
    'q': [' qqqq', 'q   q', ' qqqq', '    q', '    q'],
    'r': ['  r r', '  rr ', '  r  ', '  r  ', '  r  '],
    's': [' sss ', 's    ', ' sss ', '    s', ' sss '],
    't': ['  t  ', '  t  ', ' ttt ', '  t  ', '  ttt'],
    'u': ['u   u', 'u   u', 'u   u', 'u  uu', ' uu u'],
    'v': ['v   v', 'v   v', 'v   v', ' v v ', '  v  '],
    'w': ['w   w', 'w   w', 'w w w', 'w w w', ' w w '],
    'x': ['x   x', ' x x ', '  x  ', ' x x ', 'x   x'],
    'y': ['y   y', ' y y ', '  y  ', ' y   ', 'y    '],
    'z': ['zzzzz', '   z ', '  z  ', ' z   ', 'zzzzz'],
    ' ': ['     ', '     ', '     ', '     ', '     '],
    '.': ['     ', '     ', '     ', '     ', '  .  ']
}

#string='abcdefghijklmnopqrstuvwxyz'
#string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string=input()
for i in range(5):
    for word in range(len(string)):
        current_word = string[word]
        if word == len(string)-1 :
            print(letters[current_word][i])
        else :
            print(letters[current_word][i],end='  ')
