import doctest
import os
import shutil
import zipfile

def print_test_rs(verbose=True):
    doctest.testmod(verbose=verbose)

def print_doctest(func):
    lines = doctest.script_from_examples(func.__doc__).splitlines()
    ex_indx = lines.index('#         Example::')
    print('\n'.join(lines[ex_indx + 2:]))

def print_locals(name, locals_):
    for k, v in locals_.items():
        try:
            print(name, '-', k, '=', v, '-', v.shape)
        except:
            print(name, '-', k, '=', v)

def set_kaggle_api():
    os.makedirs('~/.kaggle', exist_ok=True)
    shutil.copy('kaggle.json', ' ~/.kaggle/') 
    os.chmod('~/.kaggle/kaggle.json', 600)  

def download_kaggle_competition(name):
    os.system('kaggle competitions download -c {name}')
    

def unzip(name):
    with zipfile.ZipFile(name, 'r') as zip_ref:
        zip_ref.extractall('.')

def read_csv_labels(fname):
    """Read `fname` to return a filename to label dictionary."""
    with open(fname, 'r') as f:
        # Skip the file header line (column name)
        lines = f.readlines()[1:]
    tokens = [l.rstrip().split(',') for l in lines]
    return dict(((name, label) for name, label in tokens))
