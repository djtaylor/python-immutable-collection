# Immutable Collection
This is a very simplistic module for creating an immutable object, based off `namedtuple`, from an existing dictionary. This is used primary for runtime configuration and arguments that should not be changed.

### Installation
```
$ pip install immutable_collection
```

### Testing
Testing is done with `unittest` and `nose` for test collection.
```
$ python setup.py test
```

### Usage
```python
from immutable_collection import ImmutableCollection

# Create a new collection from a dictionary
my_dict = {'one': 'two', 'three': 'four'}
my_ic = ImmutableCollection(my_dict)
my_collection = my_ic.get()

# Accessing collection data
print(my_collection.one)

# Create a new collection from a dictionary and map additional data
my_ic = ImmutableCollection(my_dict)
my_ic.map({'five': 'six'})
my_collection.get()

# Accessing mapped data
print(my_collection.five)
```
