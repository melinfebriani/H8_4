myList = [1, 'dua', 3, 4.0, 5, True]

student = {
    'name': 'Raka',
    'age': 18
}

people = ('Raka', ('kode', 'random'))

a = 0
while a < 10:
    print(a, end=' ')
    a = a + 1

for word in ['raka', 'billy', 'kode']:
    print(word, end='\n')

if 1:
    print('true')

if not 1:
    print('true')
else:
    print('false')

age = 21
if age * 365 > 20000:
    print('Time to retire!')
elif age * 365 > 10000:
    print('Lots of time left!')
else:
    print('Time to get started!')

def add(a, b):
    return a + b

add(5,4)