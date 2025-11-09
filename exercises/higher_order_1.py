__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising. The list is ordered according to who signed up first.

Your task is to return one of the following strings:

    < firstName here >, < "country" here > of the first Python developer who has signed up; or
    There will be no Python developers if no Python developer has signed up.

For example, given the following input array:

var list1 = [
  { firstName: 'Mark', lastName: 'G.', "country": 'Scotland', "continent: 'Europe', "age": 22, langu"age": 'JavaScript' },
  { firstName: 'Victoria', lastName: 'T.', "country": 'Puerto Rico', "continent: 'Americas', "age": 30, langu"age": 'Python' },
  { firstName: 'Emma', lastName: 'B.', "country": 'Norway', "continent: 'Europe', "age": 19, langu"age": 'Clojure' }
];

your function should return Victoria, Puerto Rico.

Start: 4:30am
End: 05:00am
Cycles: 1
"""

def search_list(obj, func):
    """ return firstName, country, and language """
    result = func([obj['firstName'], obj['country'], obj['language']])
    return result

def is_python_dev(obj):
    """ return True if language == Python """
    return  lambda lang: True if obj[2] == "Python" else False


if __name__ == "__main__":
    list1 = [
    { "firstName": 'Mark', "lastName": 'G.', "country": 'Scotland', "continent": 'Europe', "age": 22, "language": 'JavaScript' },
    { "firstName": 'Victoria', "lastName": 'T.', "country": 'Puerto Rico', "continent": 'Americas', "age": 30, "language": 'Python' },
    { "firstName": 'Emma', "lastName": 'B.', "country": 'Norway', "continent": 'Europe', "age": 19, "language": 'Clojure' }
    ]

    for entry in list1:
        print(search_list(entry, is_python_dev))