class ScenarioBuilder:
    def __init__(self, title):
        self.title = title

    def description(self, description):
        self.description = description
        return self
    
    def initial_code(self, code):
        self.initial_code = code
        return self

    def function_name(self, name):
        self.function_name = name
        return self

    def test_cases(self, cases):
        if not self.test_cases:
            self.test_cases = []
        self.test_cases.append(cases)
        return self
    
    def test_setup_code(self, setup_code):
        self.test_setup_code = setup_code
        return self

    def build(self):
        return {
            "title": self.title,
            "description": self.description,
            "initial_code": self.initial_code,
            "function_name": self.function_name,
            "test_cases": self.test_cases,
            "test_setup_code": self.test_setup_code
        }
    
class ScenarioTestCase:
    def description(self, description):
        self.description = description
        return self
    def input_data(self, input_data):
        self.input_data = input_data
        return self
    def expected_output(self, expected_output):
        self.expected_output = expected_output
        return self

generated_scenarios = [
    {
        "title": "Redact Username Decorator",
        "difficulty": 3,
    "description": "Create a decorator that get a username as a parameter and reducts the username from **ALL** input arguments of the function it decorates by using '???'  \nFor example if the username is  \n```Thomas```  \nand the function is called with  \n```Thomas is tired```  \nit should replace the argument with  \n```??? is tired```",
    "initial_code": "def redact_username(username: str):\n    # Your code here\n    pass",
    "function_name": "test_function",
    "test_setup_code": "@redact_username('John')\ndef test_function(input_string: str, notes: str=\"none\"):\n    return input_string + ' Notes: ' + notes",
    "test_cases": [
        {
            "input": ("John is tired",),
            "expected_output": "??? is tired Notes: none",
            "description": "Redacting username 'John' should return '???'."
        },
        {
            "input": ("Alice and John are buying a house",),
            "expected_output": "Alice and ??? are buying a house Notes: none",
            "description": "Redacting username 'John' should return 'Alice and ??? are buying a house'."
        },
        {
            "input": ("Charlie doesn't know anybody",),
            "expected_output": "Charlie doesn't know anybody Notes: none",
            "description": "No redaction needed as 'Charlie' is not the username."
        },
        {
            "input": ("Bank is closing loan", "John is the manager"),
            "expected_output": "Bank is closing loan Notes: ??? is the manager",
            "description": "All parameters should be redacted if they contain the username."
        },
        {
            "input": {"input_string":"Bank is closing loan", "notes":"John is the manager"},
            "expected_output": "Bank is closing loan Notes: ??? is the manager",
            "description": "All parameters should be redacted if they contain the username."
        }
    ]
},
{
    "title": "Unpacking and Extended Iterable Unpacking",
    "difficulty": 1,
    "description": (
        "Create a function called `split_first_last` that takes a list of at least two elements and returns a tuple "
        "containing the first element, a list of all middle elements, and the last element. "
        "Demonstrate your understanding of iterable unpacking and the use of the * operator in function arguments.\n\n"
        "For example:\n"
        "```python\n"
        "split_first_last([1, 2, 3, 4])  # (1, [2, 3], 4)\n"
        "split_first_last(['a', 'b', 'c'])  # ('a', ['b'], 'c')\n"
        "```\n"
        "If the list has only two elements, the middle list should be empty."
    ),
    "initial_code": (
        "def split_first_last(lst):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "split_first_last",
    "test_cases": [
        {
            "input": ([1, 2, 3, 4],),
            "expected_output": (1, [2, 3], 4),
            "description": "Should return (1, [2, 3], 4) for [1, 2, 3, 4]."
        },
        {
            "input": (['a', 'b', 'c'],),
            "expected_output": ('a', ['b'], 'c'),
            "description": "Should return ('a', ['b'], 'c') for ['a', 'b', 'c']."
        },
        {
            "input": ([10, 20],),
            "expected_output": (10, [], 20),
            "description": "Should return (10, [], 20) for [10, 20]."
        },
        {
            "input": ([1, 2, 3, 4, 5, 6],),
            "expected_output": (1, [2, 3, 4, 5], 6),
            "description": "Should return (1, [2, 3, 4, 5], 6) for [1, 2, 3, 4, 5, 6]."
        }
    ]
},
    {
        "title": "Add two numbers",
        "difficulty": 1,
    "description": "Create a function that adds two numbers together and returns the result.",
    "initial_code": "def add_numbers(a: int, b: int) -> int:\n    # Your code here\n    pass",
    "function_name": "add_numbers",
    "test_cases": [
        {
            "input": (2, 3),
            "expected_output": 5,
            "description": "Adding 2 and 3 should return 5."
        },
        {
            "input": (-1, 1),
            "expected_output": 0,
            "description": "Adding -1 and 1 should return 0."
        },
        {
            "input": (0, 0),
            "expected_output": 0,
            "description": "Adding 0 and 0 should return 0."
        }
    ]
},
    {
        "title": "Reverse list",
        "difficulty": 1,
    "description": "Create a function that reverses a list and returns the reversed list.",
    "initial_code": "def reverse_list(lst: list) -> list:\n    # Your code here\n    pass",
    "function_name": "reverse_list",
    "optional_code_goal": {"max_lines": 1},
    "test_cases": [
        {
            "input": ([2, 3],),
            "expected_output": [3, 2],
            "description": "Reversing the list [2, 3] should return [3, 2]."
        },
        {
            "input": ([5, 4, 3, 2, 1],),
            "expected_output": [1, 2, 3, 4, 5],
            "description": "Reversing the list [5, 4, 3, 2, 1] should return [1, 2, 3, 4, 5]."
        },
        {
            "input": ([1],),
            "expected_output": [1],
            "description": "Reversing the list [1] should return [1]."
        },
        {
            "input": ([],),
            "expected_output": [],
            "description": "Reversing an empty list should return an empty list."
        }

    ]
},
    {
        "title": "Group by Remainder",
        "difficulty": 2,
    "description": "Given a list of integers, create a function that returns a dictionary  that groups the integers based on the remainder when divided  by a given divisor. The keys of the dictionary should be the remainders, and the values should be lists of integers that yield those remainders.",
    "initial_code": "def group_by_remainder(lst:list, divisor:int) -> int:\n    # Your code here\n    pass",
    "function_name": "group_by_remainder",
    "optional_code_goal": {"max_lines": 3},
    "test_cases": [
        {
            "input": ([10, 20, 30, 25, 15], 5),
            "expected_output": {0: [10, 20, 30, 25, 15],},
            "description": "Grouping by remainder when divided by 5."
        },
        {
            "input": ([1, 2, 3, 4, 5], 2),
            "expected_output": {0: [2, 4], 1: [1, 3, 5]},
            "description": "Grouping by remainder when divided by 2."
        },
        {
            "input": ([7, 14, 21], 7),
            "expected_output": {0: [7, 14, 21]},
            "description": "All numbers yield the same remainder when divided by 7."
        },
        {
            "input": ([8, -8, -16], 4),
            "expected_output": {0: [8, -8, -16]},
            "description": "All numbers yield the same remainder when divided by 4."
        }
    ]
    
},
{    "title": "Calculate Factorial",
        "difficulty": 2,
    "description": "Create a function that calculates the factorial of a given number and returns the result.",
    "initial_code": "def factorial(n: int) -> int:\n    # Your code here\n    pass",
    "function_name": "factorial",
    "test_cases": [
        {
            "input": (5,),
            "expected_output": 120,
            "description": "Factorial of 5 should return 120."
        },
        {
            "input": (0,),
            "expected_output": 1,
            "description": "Factorial of 0 should return 1."
        },
        {
            "input": (1,),
            "expected_output": 1,
            "description": "Factorial of 1 should return 1."
        },
        {
            "input": (3,),
            "expected_output": 6,
            "description": "Factorial of 3 should return 6."
        }
    ]
},
{
    "title": "Dictionary Comprehension with Conditional Logic",
    "difficulty": 1,
    "description": (
        "Create a function called `even_square_dict` that takes a list of integers and returns a dictionary where the keys "
        "are the even numbers from the list and the values are their squares. Suggestion: Use a dictionary comprehension with a condition.\n\n"
        "For example:\n"
        "```python\n"
        "even_square_dict([1, 2, 3, 4, 5])  # {2: 4, 4: 16}\n"
        "even_square_dict([10, 15, 20])  # {10: 100, 20: 400}\n"
        "even_square_dict([])  # {}\n"
        "```\n"
        "Demonstrate your understanding of dictionary comprehensions and conditional logic in Python."
    ),
    "initial_code": (
        "def even_square_dict(numbers):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "even_square_dict",
    "test_cases": [
        {
            "input": ([1, 2, 3, 4, 5],),
            "expected_output": {2: 4, 4: 16},
            "description": "Should return {2: 4, 4: 16} for [1, 2, 3, 4, 5]."
        },
        {
            "input": ([10, 15, 20],),
            "expected_output": {10: 100, 20: 400},
            "description": "Should return {10: 100, 20: 400} for [10, 15, 20]."
        },
        {
            "input": ([1, 3, 5],),
            "expected_output": {},
            "description": "Should return {} for [1, 3, 5] (no even numbers)."
        },
        {
            "input": ([],),
            "expected_output": {},
            "description": "Should return {} for an empty list."
        }
    ]
},
{
    "title": "Tuple Packing and Unpacking",
    "difficulty": 2,
    "description": (
        "Create a function called `swap_and_pack` that takes two arguments, swaps them, and returns them as a tuple. "
        "Then, demonstrate tuple unpacking by writing a test that unpacks the result into two variables. "
        "This exercise is to show your understanding of tuple packing and unpacking in Python.\n\n"
        "For example:\n"
        "```python\n"
        "result = swap_and_pack('hello', 42)  # (42, 'hello')\n"
        "a, b = swap_and_pack('hello', 42)\n"
        "# a == 42, b == 'hello'\n"
        "```\n"
        "If you pass two values, the function should return them swapped in a tuple."
    ),
    "initial_code": (
        "def swap_and_pack(a, b):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "swap_and_pack",
    "test_cases": [
        {
            "input": ("hello", 42),
            "expected_output": (42, "hello"),
            "description": "Should return (42, 'hello') for input ('hello', 42)."
        },
        {
            "input": (1, 2),
            "expected_output": (2, 1),
            "description": "Should return (2, 1) for input (1, 2)."
        },
        {
            "input": ([1, 2], {"a": 10}),
            "expected_output": ({"a": 10}, [1, 2]),
            "description": "Should return ({'a': 10}, [1, 2]) for input ([1, 2], {'a': 10})."
        }
    ]
},
{
    "title": "Class Decorator: Add Repr",
    "difficulty": 2,
    "description": (
        "Write a class decorator called `add_repr` that adds a custom `__repr__` method to any class it decorates. "
        "The `__repr__` method should return a string in the format `<ClassName({attribute_dict})>`, "
        "where `attribute_dict` is the dictionary of the instance's attributes.\n\n"
        "For example:\n"
        "```python\n"
        "@add_repr\n"
        "class Point:\n"
        "    def __init__(self, x, y):\n"
        "        self.x = x\n"
        "        self.y = y\n"
        "p = Point(1, 2)\n"
        "repr(p)  # <Point({'x': 1, 'y': 2})>\n"
        "```\n"
        "Demonstrate your understanding of class decorators and dynamic method addition."
    ),
    "initial_code": (
        "def add_repr(cls):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "test_point_repr",
    "test_setup_code": (
        "@add_repr\n"
        "class Point:\n"
        "    def __init__(self, x, y):\n"
        "        self.x = x\n"
        "        self.y = y\n"
        "def test_point_repr():\n"
        "    p = Point(3, 4)\n"
        "    return repr(p)\n"
    ),
    "test_cases": [
        {
            "input": (),
            "expected_output": "<Point({'x': 3, 'y': 4})>",
            "description": "Should return custom repr for Point(3, 4)."
        }
    ]
},
{
    "title": "Function Decorator: Double Result",
    "difficulty": 2,
    "description": (
        "Write a function decorator called `double_result` that, when applied to any function, "
        "will double the result returned by that function. The decorator should not take any arguments.\n\n"
        "For example:\n"
        "```python\n"
        "@double_result\n"
        "def add(a, b):\n"
        "    return a + b\n"
        "add(2, 3)  # 10\n"
        "```\n"
        "Demonstrate your understanding of function decorators in Python."
    ),
    "initial_code": (
        "def double_result(func):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "add",
    "test_setup_code": (
        "@double_result\n"
        "def add(a, b):\n"
        "    return a + b\n"
    ),
    "test_cases": [
        {
            "input": (1,3),
            "expected_output": 8,
            "description": "add(1, 3) should return 8 because the result is doubled."
        },
        {
            "input": (0, 0),
            "expected_output": 0,
            "description": "add(0, 0) should return 0 because the result is doubled."
        },
        {
            "input": (-1, 2),
            "expected_output": 2,
            "description": "add(-1, 2) should return 2 because the result is doubled."
        }
    ]
},
{"title": "Collect unique values from a list",
    "difficulty": 1,
    "description": (
        "Create a function called `collect_unique_values` that takes a list of integers and returns a set of unique values. "
        "This exercise is to demonstrate your understanding of sets in Python.\n\n"
        "For example:\n"
        "```python\n"
        "collect_unique_values([1, 2, 2, 3, 4, 4])  # {1, 2, 3, 4}\n"
        "collect_unique_values([5, 5, 5])  # {5}\n"
        "collect_unique_values([])  # set()\n"
        "```\n"
    ),
    "initial_code": (
        "def collect_unique_values(lst):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "collect_unique_values",
    "test_cases": [
        {
            "input": ([1, 2, 2, 3, 4, 4],),
            "expected_output": {1, 2, 3, 4},
            "description": "Should return {1, 2, 3, 4} for [1, 2, 2, 3, 4, 4]."
        },
        {
            "input": ([5, 5, 5],),
            "expected_output": {5},
            "description": "Should return {5} for [5, 5, 5]."
        },
        {
            "input": ([],),
            "expected_output": set(),
            "description": "Should return an empty set for an empty list."
        }
    ]
},
{
    "title": "Handle expections",
    "difficulty": 1,
    "description": (
        "Create a function that gets a string and tries to convert it to a number. "
        "If the conversion fails, it should return 'Invalid input'. "
        "This exercise is to demonstrate your understanding of exception handling in Python.\n\n"
        "For example:\n"
        "```python\n"
        "to_number(\"10\")  # 10.0\n"
        "to_number(\"abc\")  # 'Invalid input'\n"
        "```\n"
    ),
    "initial_code": (
        "def to_number(s):\n"
        "    # Your code here\n"
        "    pass"
    ),
    "function_name": "to_number",
    "test_cases": [
        {
            "input": ("10",),
            "expected_output": 10.0,
            "description": "Should return 10.0 for input '10'."
        },
        {
            "input": ("abc",),
            "expected_output": "Invalid input",
            "description": "Should return 'Invalid input' for input 'abc'."
        },
        {
            "input": ("3.14",),
            "expected_output": 3.14,
            "description": "Should return 3.14 for input '3.14'."
        },
        {
            "input": ("-5",),
            "expected_output": -5.0,
            "description": "Should return -5.0 for input '-5'."
        }
    ]
},  
{
    "title": "Create a cm class that supports addition and subtraction",
    "difficulty": 2,
    "description": (
        "Create a class called `Centimeter` that represents a length in centimeters.\n  "
        "The class should support\n  "
        "- addition of other 'Centimeter' instances\n  "
        "- addition of an integer or float\n  "
        "- subtraction of other 'Centimeter' instances\n  "
        "- subtraction of an integer or float\n  "
        "- equality comparison with other 'Centimeter' instances\n\n  "
        "For example:\n"
        "```python\n"
        "cm1 = Centimeter(10)\n"
        "cm2 = Centimeter(5)\n"
        "result_add = cm1 + cm2  # Centimeter(15)\n"
        "result_sub = cm1 - cm2  # Centimeter(5)\n"
        "result_add_with_number = cm1 + 5  # Centimeter(15)\n"
        "```\n"
    ),
    "initial_code": (
        "class Centimeter:\n"
        "    # Your code here\n"
    ),
    "test_setup_code": (
        "def test_centimeter_operations(n1, n2):\n"
        "    cm1 = Centimeter(n1)\n"
        "    cm2 = Centimeter(n2)\n"
        "    assert (cm1 + cm2) == Centimeter(n1 + n2)\n"
        "    assert (cm1 + n2) == Centimeter(n1 + n2)\n"
        "    assert (cm1 - cm2) == Centimeter(n1 - n2)\n"
        "    assert (cm1 - n2) == Centimeter(n1 - n2)\n"
        "    assert (cm1 + Centimeter(0)) == cm1\n"
        "    assert (cm1 - Centimeter(0)) == cm1\n"
    ),
    "function_name": "test_centimeter_operations",
    "test_cases": [
        {
            "input": (10, 5),
            "expected_output": None,
            "description": "Adding Centimeter(10) and Centimeter(5) should return Centimeter(15)."
        },
        {
            "input": (20, 10),
            "expected_output": None,
            "description": "Subtracting Centimeter(10) from Centimeter(20) should return Centimeter(10)."
        },
        {
            "input": (0, 0),
            "expected_output": None,
            "description": "Adding two zero lengths should return Centimeter(0)."
        }
    ]
}
]
