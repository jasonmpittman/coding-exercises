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