<h4>Sanitize user's input</h4>
All functions return the data if all checks are ok.<br>
If there is any strange character that doesn't match, false is returned

<h5>Example 1:</h5>

```python
sanizite = Allow()
data = 'rocky_99'
username = sanitize.alphanumeric(data)

if username:
	print 'Username is ok'
	# Register user 

```


<h5>Example 1:</h5>
Check for string password

```python
sanizite = Allow()
data = 'p@as$wor!2'
password = sanitize.alphanumeric(data)

if password['ok']:
	print 'Password is strong'
	# Allow password for use
else:
	msg_str = ''
	for msg in results:
	    if results[msg]:
	        msg_str += msg + ', '
	print "Password must include: {0}".format(msg_str)) 

```