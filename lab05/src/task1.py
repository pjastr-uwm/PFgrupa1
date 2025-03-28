from unittest.mock import Mock

m1 = Mock(name="Test Mock")
print(m1)
m1.get_data.return_value = 567

result = m1.get_data('user')
print(result)

m1.get_data.assert_called_with('user')

print(m1.get_data.call_args)

result2 = m1.get_data(True)
print(result2)

print(m1.get_data.call_args)

print(m1.get_data.call_args_list)

result3 = m1.get_data()
print(result3)

print(m1.get_data.call_args_list)
