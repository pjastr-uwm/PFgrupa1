from unittest.mock import Mock

m3 = Mock()

m3.some_method(4,5,6)
m3.some_method()
m3.some_method("a", name="Test")
m3.some_method(a=99.2, b=-4.5)
m3.some_method(78, True, x="abc")

print(m3.some_method.called)
print(m3.some_method.call_count)
print(m3.some_method.call_args)
print(m3.some_method.call_args[0])  # argumenty pozyjne
print(m3.some_method.call_args[1])  # argumenty keyword (nazwane)

print(m3.some_method.call_args_list)
for i,call in enumerate(m3.some_method.call_args_list):
    print("number", i)
    print("positional args", call[0])
    print("keyword args", call[1])
