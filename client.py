from tasks import add

result = add.delay(4, 4)
print(result.ready())
result.get()
result.get(timeout=1)
result.get(propagate=False)