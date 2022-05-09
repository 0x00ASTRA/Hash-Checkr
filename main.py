from hashlib import sha256, sha512, md5
import fancytxt as ft

print('')
file_path = input('Enter the file path: ').strip("'")
print('')
inp_hash = input('Enter the checksum: ')
print('')
hash_type_list = ['sha256', 'sha512', 'md5']
    
def get_hash_type():
    htl_l = len(hash_type_list)

    for i in range(htl_l):

        hash_type = hash_type_list[i]
        txt = f'Option {i} ' + hash_type

        print(txt)
        print

    print(ft.eq_line(len(txt)))

    opts = f'0 - {htl_l}'
    sel_str = f'Select your option [{opts}]: '

    ht = int(input(sel_str))

    print(ft.eq_line(len(sel_str) + 1))

    return ht

def calculate_hash():

    ht = get_hash_type()
    func_list = [sha256(), sha512(), md5()]
    func_type = func_list[ht]

    hash = func_type
    calc_str = 'Calculating hash...'
    csln = ft.eq_line(len(calc_str))

    print(csln)
    print('')
    print(calc_str)
    print('')
    print(csln)

    with open(file_path, 'rb') as f:

        b = 0
        while b != b'':

            b = f.read(1024)
            hash.update(b)
        
    return hash.hexdigest()


def verify():

    file_hash = calculate_hash()
    valid = False

    print('')
    print(file_hash)
    print('')

    hl = []
    fhl = []

    for i in range(len(inp_hash)):

        hl.append(str(i))
    
    for i in range(len(file_hash)):

        fhl.append(str(i))

    if hl == fhl:
        vstr = 'The file hash is a MATCH'
        valid = True
        ln = ft.eq_line(len(vstr))
        print(ln)
        print('')
        print(vstr)
        print('')
        print(ln)
    else:
        print(' *!* The file hash is NOT A MATCH *!*')

    return valid

if __name__ == '__main__':
    verify()