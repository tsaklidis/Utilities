# Info
Python utilities in order to make your <i>coding</i> life easier<br>
Some of the functions, are unable to run as a single python code so you have to create <a href='https://www.djangoproject.com/start/'>Django</a> project. <br>

Also use python3

<hr>

<h3>Sanitize user's input</h3>
All functions return the data if all checks are ok.<br>
If there is any strange character that doesn't match, a custom Exception is raised

<h5>Example 1:</h5>

```python
import sanitize
data = 'rocky_99'
try:
	sanitize.alphanumeric(data)
    # Register user 
except sanitize.SanitizationException as e:
	print(e)

```


<h5>Example 2:</h5>
Check for password strength. If password is strength (check function comments),<br>
the same password is returned. Otherwise Exception is raised


```python
import sanitize
data = 'p@as$wor!2'

try:
	sanitize.password_check(data)
	# Do what you need
except sanitize.SanitizationException as e:
	# Something is wrong, print the errors
	print(e)

```


<hr>

<h3>Create random unique string</h3>

<h4>unique.get</h4>
Returns a random unique string. Uniquines is based on timestamp. Default length is 8.<br>
Argumentrs: length, prefix, suffix, invalid_chars

<h5>Example 1:</h5>
If you need to get a random unique string of 16 chars with prefix 'user'


```python
get(16, 'user')
```

<h5>Example 2:</h5>
If you need to get a random unique string of 6 chars but don't use the chars 'ofdA'

```python
avoid_chars = 'ofdAre'
get(6, invalid_chars=avoid_chars)
```


<hr>
<h3>Time calculator</h3>

First of all you need to import datetime

<h4>Days from today</h4>
Returns the date after given days. If true is passed, hence will be calculated backwords

<h5>Example 1:</h5>
If you need to get the date after one week

```python
days_hence(7)
```

<h5>Example 2:</h5>
If you need to get the date before 5 days

```python
calculate_back = True
days_hence(5, calculate_back)
```

<h4>Ensure age of at least 18 years old.</h4>h4>
<h5>Example 1:</h5>
Find if the given birthdate is adult. Default adult years are 18.

```python
sample_date = datetime.date(1987, 8, 13)
is_adult(sample_date)
```

If the given date is over 18 years old, returns True else False
<h5>Example 2:</h5>

```python
sample_date = datetime.date(1987, 8, 13)
adult_years = 21
is_adult(sample_date, adult_years)
```

In some countries adultd age differs, so pass the years you need