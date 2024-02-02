# Continue


```python
for n in range(11):
    if n % 2 == 0:
        continue
    print(n)  # 1 3 5 7 9
```


# Break


```python
for n in range(11):
    if n == 6:
        break
    print(n)  # 0 1 2 3 4 5
```