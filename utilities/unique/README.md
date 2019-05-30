Create random unique string<br>

<h4>get_random_string</h4>
Returns a random unique string. Uniquines is based on timestamp. Default length is 8.<br>
Argumentrs: length, prefix, suffix, invalid_chars

<h5>Example 1:</h5>
If you need to get a random unique string of 16 chars with prefix 'user'


```python
get_random_string(16, 'user')
```

<h5>Example 2:</h5>
If you need to get a random unique string of 6 chars but don't use the chars 'ofdA'

```python
avoid_chars = 'ofdAre'
get_random_string(6, invalid_chars=avoid_chars)
```
