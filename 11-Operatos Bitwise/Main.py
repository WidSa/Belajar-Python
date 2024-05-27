# Operator Bitwise
# operator binary

a = 5
b = 3

# Bitwise OR(|)
c = a | b 
print('='*7, 'OR', '='*7)
print('Nilai a:', a, ', Binary: ', format(a, '08b'))
print('Nilai b:', b, ', Binary: ', format(b, '08b'))
print('='*10, '(|)')
print('Nilai c:', c, ', Binary: ', format(c, '08b'))

# Bitwise AND (&)
c = a & b 
print('='*7, 'AND', '='*7)
print('Nilai a:', a, ', Binary: ', format(a, '08b'))
print('Nilai b:', b, ', Binary: ', format(b, '08b'))
print('='*10, '(&)')
print('Nilai c:', c, ', Binary: ', format(c, '08b'))

# Bitwise XOR (^)
c = a ^ b 
print('='*7, 'XOR', '='*7)
print('Nilai a:', a, ', Binary: ', format(a, '08b'))
print('Nilai b:', b, ', Binary: ', format(b, '08b'))
print('='*10, '(^)')
print('Nilai c:', c, ', Binary: ', format(c, '08b'))

# Bitwise NOT (~)
c = ~a 
print('='*7, 'OR', '='*7)
print('Nilai a:', a, ', Binary: ', format(a, '08b'))
print('='*10, '(~)')
print('Nilai c:', c, ', Binary: ', format(c, '08b'))


# Shiffting 
# Shift Rigth (>>)
c = a >> 1
print('='*7, '>>', '='*7)
print('Nilai a:', a, ', Binary: ', format(a, '08b'))
print('='*10, '(>>)')
print('Nilai c:', c, ', Binary: ', format(c, '08b'))

# Shift Left (<<)
c = a << 1
print('='*7, '<<', '='*7)
print('Nilai a:', a, ', Binary: ', format(a, '08b'))
print('='*10, '(<<)')
print('Nilai c:', c, ', Binary: ', format(c, '08b'))

