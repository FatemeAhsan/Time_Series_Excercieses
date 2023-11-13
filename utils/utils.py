import doctest

def print_doctest(func):
    lines = doctest.script_from_examples(func.__doc__).splitlines()
    ex_indx = lines.index('#         Example::')
    print('\n'.join(lines[ex_indx + 2:]))

def print_test_rs(verbose=True):
    doctest.testmod(verbose=verbose)

def print_locals(name, locals_):
    for k, v in locals_.items():
        try:
            print(name, '-', k, '=', v, '-', v.shape)
        except:
            print(name, '-', k, '=', v)
