def test_range():
    guess_me = 7
    start = 1

    while True:
        if start < guess_me:
            print('too low')
        elif start == guess_me:
            print('found it!')
            break
        elif start > guess_me:
            print('oops')
            break
        
        start += 1

def test(value):
    if value < 7:
        print('too low')
    elif value > 7:
        print('too high')
    else:
        print('just right')

def for_loop():
    for value in [3, 2, 1, 0]:
        print(value)

def even_list():
    print([even for even in range(10) if even % 2 == 0])

def squares():
    print({value: value ** 2 for value in range(10)})

def odd():
    print({value for value in range(10) if value % 2 == 1})

def generator_comprehension():
    for string in ('Got {}'.format(value) for value in range(10)):
        print(string)

def good():
    return ['Harry', 'Ron', 'Hermione']

def get_odds():
    for value in range(10):
        if value % 2 == 1:
            yield value

def get_third_odd():
    odds = get_odds()
    for _, odd_value in zip(range(3), get_odds()):
        pass

    print(odd_value)

def test(func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper

@test
def try_test():
    print('hello from try_test!')

class OopsException(Exception):
    pass

def test_oops():
    try:
        raise OopsException()
    except OopsException:
        print('Caught an oops')

def zip_test():
    titles = ['Creature of Habit', 'Crewel Fate']
    plots = ['A nun turns into a monster', 'A haunted yarn shop']
    movies = dict(zip(titles, plots))
    print(movies)

if __name__ == '__main__':
    test(5)
    test(7)
    test_range()
    for_loop()
    even_list()
    squares()
    odd()
    generator_comprehension()
    print(good())
    get_third_odd()
    try_test()
    test_oops()
    zip_test()