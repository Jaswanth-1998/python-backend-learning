def str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        Value = bytes_or_str.decode('utf-8')
    else:
        Value = bytes_or_str
    return Value

print(repr(str('foo')))
print(repr(str("boo")))
