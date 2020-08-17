#code
def shortest_path(path):
    path_names = []

    if path[0] == '/':
        path_names.append('/')

    for item in path.split('/'):
        if item == '..':
            path_names.pop()
        elif item not in ['.', '']:
            path_names.append(item)

    if path_names[0] == '/':
        result = '/' + '/'.join(path_names[1:])
    else:
        result = '/'.join(path_names)

    return result

#tests 
import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(shortest_path("/usr/lib/../bin/gcc"), "/usr/bin/gcc")
        self.assertEqual(shortest_path("//./../scripts/awkscripts/././"), "scripts/awkscripts")

unittest.main()