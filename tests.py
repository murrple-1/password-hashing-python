import passwordhash

print 'Sample hash:'
sampleHash = passwordhash.createHash('test_password')
print sampleHash

print 'Test results:'

hashOfPassword = passwordhash.createHash('password')

if passwordhash.validatePassword('password', hashOfPassword):
    print 'pass'
else:
    print 'FAIL'

if passwordhash.validatePassword('wrong_password', hashOfPassword):
    print 'FAIL'
else:
    print 'pass'

try:
    passwordhash.validatePassword('password', algorithm='')
    print 'FAIL'
except TypeError as e:
    print 'pass'