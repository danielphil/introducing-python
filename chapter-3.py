def years():
    years_list = list(range(1982, 1988))
    print("3rd birthday on {}!".format(years_list[3]))
    print("Oldest on {}.".format(years_list[-1]))

def things():
    l = ["mozzarella", "cinderella", "salmonella"]
    # effectively does nothing as it capitalizes a copy of the string
    l[1].capitalize()
    print(l)

    l[0] = l[0].upper()
    print(l)

    del l[2]
    print(l)

def surprise():
    l = ['Groucho', 'Chico', 'Harpo']
    print(l[-1].lower()[::-1].capitalize())

def english2french():
    e2f = {
        'dog': 'chien',
        'cat': 'chat',
        'walrus': 'morse'
    }
    print(e2f['walrus'])

    f2e = {french: english for english, french in e2f.items()}
    print(f2e['chien'])
    print(set(e2f.keys()))

def life():
    cats = ['Henri', 'Grumpy', 'Lucy']

    life = {
        'animals': {
            'cats': cats,
            'octopi': {},
            'emus': {}
        },
        'plants': {},
        'other': {}
    }

    print(life.keys())
    print(life['animals'].keys())
    print(life['animals']['cats'])

if __name__ == "__main__":
    years()
    things()
    surprise()
    english2french()
    life()