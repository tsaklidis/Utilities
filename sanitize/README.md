<h4>Sanitize user's input</h4>
All functions return the data if all checks are ok.<br>
If there is any strange character that doesn't match, False is returned

<h5>Example 1:</h5>

```python
sanitize = Allow()
data = 'rocky_99'
username = sanitize.alphanumeric(data)

if username:
    print 'Username is ok'
    # Register user 

```


<h5>Example 2:</h5>
Check for password strength. If password is strength (check function comments),<br>
the same password is returned. Otherwise a dict with info is returned


```python
strength = Allow()
data = 'p@as$wor!2'
password = strength.password_check(data)
msg_str = ''

if password == data:
    msg_str = 'Password is strong'
    # Allow password for use
else:
    for msg in password:
        if password[msg]: # Password should be like True keys
            msg_str += msg + ', '
    print "Password must include: {0}".format(msg_str)

```