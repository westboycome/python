import  traceback
assert 5>3
try:
    assert 3 < 4
except (AssertionError):
    traceback.print_exc()
print("after ...")
