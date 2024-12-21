# Coding Notebook


### List Comprehensions

Return a list of the first character from each string in the list:  
```[x[0] for x in ["Elie", "Tim", "Matt"]]```

Return a list of the intersection between two lists of integers:  
```[x for x in [1,2,3,4] if x in [3,4,5,6]]```

Return a lowercase and reversed list of strings given an initial list:  
```[x[::-1].lower() for x in ["Elie", "Tim", "Matt"]]```

Return a list of numbers in the list 1...100 inclusive that are divisible by 12:  
```[x for x in range(1,101) if x % 12 == 0]```

Return a list of characters not in the list of vowels:  
```[c for c in "amazing" if c not in ['a', 'e', 'i', 'o', 'u']]```

Return a nested list using nested list comprehensions:  
```[[i for i in range(3)] for x in range(3)]```  
```[[i for i in range(10)] for x in range(10)]```  


### Dictionaries

Return a dictionary using mapped elements from two lists:  
```answer = { k:v for (k,v) in zip(list1, list2) }```  

Return a dictionary from a nested list:  
```person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]```  
   ```answer = dict(person)```

Could also use dict comprehension:  
```answer = {k:v for k,v in person}```

Alternative dict comprehension referencing list elements:  
```answer = {thing[0]: thing[1] for thing in person}```  

Return a dictionary of vowels with 0 as value:  
```answer = dict.fromkeys("aeiou", 0)```

Return a dictionary of ASCII values and letters:  
```answer = {count: chr(count) for count in range(65, 91)}```


### Lambda Functions

Return the cube of a given integer n using a lamba function:  
```cubed = lambda n: n**3```

Return a list of integers excluding negatives using `filter()`:  
```
def remove_negatives(numbers):
    result = filter(lambda x: x >= 0, numbers)
    return list(result)
```  

### Generator Expression  
Return True if all elements in a list are `str` type:
```
    def is_all_strings(lst):
        return all(type(l) == str for l in lst)
```  

Technically, this should be a `yield` no?

### Zip
Return an interleaved string based on two input strings:
```
def interleave(a: str, b: str) -> str:
    interleaved_string = ''
    
    temp_string = zip(a, b)
    
    for s in temp_string:
        interleaved_string += ''.join(s)
    
    return interleaved_string
```  

### Decorators  

