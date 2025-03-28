from unittest.mock import Mock

m2 = Mock(autospec=True)

m2.get_data.side_effect = [50, True, "Olsztyn"]
print(m2.get_data())
print(m2.get_data())
print(m2.get_data())


def modify(*args):
    args = [arg * 2 for arg in args]
    return args


m2.get_data.side_effect = modify

print(m2.get_data(7, -8))

m2.get_data.side_effect = TypeError("Wrong type")

try:
    print(m2.get_data())
except TypeError as er:
    print(er)
