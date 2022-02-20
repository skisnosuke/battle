passed = 0
failed = 0

print("1+1=2になるように")
result = 1 + 1
if(result == 2):
  print("Passed")
  passed += 1
else:
  print("Error result: %d" % result)
  failed += 1

print("Passed: %d, Failed: %d" % (passed, failed))