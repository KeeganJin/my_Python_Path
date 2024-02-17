## Function

### Function as arguments

```python
def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x,y):
    return x+y

test_func(compute)
```



### Lambda anonymous function

* lambda is a small anonymous function
* 
* use for one-time functions 

```python
def test_func(compute):
    result = compute(1,2)
    print(result)
#lambda arguments : funciton body (one line code)
test_func(lambda x,y :x + y)
```

## Exception

