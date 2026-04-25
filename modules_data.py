from levels_data import LEVELS_DATA

MODULES = [
    {
        'id': 1,
        'title': 'Arrays & Lists',
        'icon': '📋',
        'description': 'Master the most fundamental data structure — Python lists.',
        'difficulty': 'Beginner',
        'estimated_time': '45 min',
        'color': '#4f46e5',
        'content': """
<h2>What is an Array?</h2>
<p>An <strong>array</strong> is a collection of items stored at contiguous memory locations. In Python, we use <strong>lists</strong> — which are dynamic arrays that can grow and shrink.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Think of a list like a row of lockers. Each locker has a number (index) starting from 0, and you can instantly access any locker if you know its number.</p>
</div>

<h3>Creating Lists</h3>
<pre><code class="language-python">
# Empty list
empty = []

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Mixed types
mixed = [1, "hello", 3.14, True]

# List of strings
fruits = ["apple", "banana", "cherry"]
</code></pre>

<h3>Indexing — Accessing Elements</h3>
<p>Python uses <strong>zero-based indexing</strong> — the first element is at index 0.</p>
<pre><code class="language-python">
fruits = ["apple", "banana", "cherry"]
#          index 0   index 1   index 2

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry  (negative index counts from end)
print(fruits[-2])  # banana
</code></pre>

<h3>Slicing — Getting a Sub-list</h3>
<pre><code class="language-python">
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:5])   # [2, 3, 4]   (from index 2 up to but NOT including 5)
print(nums[:4])    # [0, 1, 2, 3]  (from start to index 4)
print(nums[6:])    # [6, 7, 8, 9]  (from index 6 to end)
print(nums[::2])   # [0, 2, 4, 6, 8]  (every 2nd element)
print(nums[::-1])  # [9, 8, 7, ..., 0]  (reversed!)
</code></pre>

<h3>Common List Operations</h3>
<pre><code class="language-python">
fruits = ["apple", "banana"]

# Adding elements
fruits.append("cherry")        # Add to end: ["apple", "banana", "cherry"]
fruits.insert(1, "blueberry")  # Insert at index: ["apple", "blueberry", "banana", "cherry"]

# Removing elements
fruits.pop()        # Remove & return last item
fruits.pop(0)       # Remove & return item at index 0
fruits.remove("banana")  # Remove first occurrence of "banana"

# Useful info
print(len(fruits))       # Number of elements
print("apple" in fruits) # Check if element exists (True/False)
print(fruits.index("cherry"))  # Find index of element

# Sorting
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()           # Sort in place: [1, 1, 2, 3, 4, 5, 9]
sorted_nums = sorted(nums)  # Returns new sorted list
</code></pre>

<h3>List Comprehensions</h3>
<p>A powerful Python shortcut to create lists:</p>
<pre><code class="language-python">
# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension (same result, one line!)
squares = [i ** 2 for i in range(10)]

# With condition
evens = [i for i in range(20) if i % 2 == 0]
</code></pre>

<h3>Time Complexity</h3>
<table class="complexity-table">
  <tr><th>Operation</th><th>Time</th><th>Why</th></tr>
  <tr><td>Access by index</td><td>O(1)</td><td>Direct memory jump</td></tr>
  <tr><td>Append</td><td>O(1)</td><td>Add to end</td></tr>
  <tr><td>Insert at index</td><td>O(n)</td><td>Must shift elements</td></tr>
  <tr><td>Search (linear)</td><td>O(n)</td><td>Check each element</td></tr>
  <tr><td>len()</td><td>O(1)</td><td>Stored internally</td></tr>
</table>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Find Max & Min Without Built-ins',
                'description': 'Write two functions: <code>find_max(arr)</code> and <code>find_min(arr)</code> that return the largest and smallest numbers in a list. <strong>Do not use Python\'s built-in max() or min() functions!</strong>',
                'starter_code': '''def find_max(arr):
    """Return the largest number in arr."""
    # Hint: Start with the first element as your "best so far"
    # then loop through the rest comparing each one
    pass

def find_min(arr):
    """Return the smallest number in arr."""
    pass

# Test your functions
print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))  # Expected: 9
print(find_min([3, 1, 4, 1, 5, 9, 2, 6]))  # Expected: 1
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}: got {got}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

print("Testing find_max:")
_test("find_max([3,1,4,1,5,9,2,6])", find_max([3,1,4,1,5,9,2,6]), 9)
_test("find_max([1])", find_max([1]), 1)
_test("find_max([-5,-1,-9])", find_max([-5,-1,-9]), -1)
_test("find_max([100,200,150])", find_max([100,200,150]), 200)

print("\\nTesting find_min:")
_test("find_min([3,1,4,1,5,9,2,6])", find_min([3,1,4,1,5,9,2,6]), 1)
_test("find_min([1])", find_min([1]), 1)
_test("find_min([-5,-1,-9])", find_min([-5,-1,-9]), -9)
_test("find_min([100,200,150])", find_min([100,200,150]), 100)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 Excellent! All tests passed!")
else:
    print("Keep trying! Check your logic.")
''',
                'hints': [
                    'Start by assuming the first element is the max/min.',
                    'Loop through the rest of the list starting at index 1.',
                    'Use an if statement to update your current best if you find something better.',
                ]
            },
            {
                'id': 2,
                'title': 'Check if a List is a Palindrome',
                'description': 'Write a function <code>is_palindrome(arr)</code> that returns <code>True</code> if a list reads the same forwards and backwards, <code>False</code> otherwise. Try to solve it in O(n) time using the two-pointer technique.',
                'starter_code': '''def is_palindrome(arr):
    """Return True if arr is a palindrome, False otherwise."""
    # Approach 1 (easy): arr == arr[::-1]
    # Approach 2 (two-pointer): use left and right pointers
    pass

# Test your function
print(is_palindrome([1, 2, 3, 2, 1]))  # True
print(is_palindrome([1, 2, 3, 4, 5]))  # False
print(is_palindrome([7]))              # True (single element)
print(is_palindrome([1, 1]))           # True
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

print("Testing is_palindrome:")
_test("[1,2,3,2,1] -> True",  is_palindrome([1,2,3,2,1]), True)
_test("[1,2,3,4,5] -> False", is_palindrome([1,2,3,4,5]), False)
_test("[7] -> True",          is_palindrome([7]),          True)
_test("[1,1] -> True",        is_palindrome([1,1]),        True)
_test("[1,2,1] -> True",      is_palindrome([1,2,1]),      True)
_test("[1,2,2] -> False",     is_palindrome([1,2,2]),      False)
_test("[] -> True",           is_palindrome([]),           True)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 Excellent! All tests passed!")
''',
                'hints': [
                    'The simplest solution: compare arr to arr[::-1].',
                    'For two-pointer: use left=0 and right=len(arr)-1, move them toward each other.',
                    'If arr[left] != arr[right] at any point, return False.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What is the index of the LAST element in a Python list of length 10?',
                'options': ['10', '9', '-10', '11'],
                'answer': 1,
                'explanation': 'Lists use 0-based indexing, so a list of 10 items has indices 0 through 9. The last element is at index 9 (or -1).'
            },
            {
                'question': 'What does nums[2:5] return for nums = [10, 20, 30, 40, 50, 60]?',
                'options': ['[20, 30, 40]', '[30, 40, 50]', '[30, 40, 50, 60]', '[20, 30, 40, 50]'],
                'answer': 1,
                'explanation': 'Slicing [2:5] returns elements at indices 2, 3, and 4 — which are 30, 40, 50. The end index (5) is NOT included.'
            },
            {
                'question': 'What is the time complexity of accessing an element by index in a list?',
                'options': ['O(n)', 'O(log n)', 'O(1)', 'O(n²)'],
                'answer': 2,
                'explanation': 'Accessing by index is O(1) — constant time — because Python can jump directly to the memory address without scanning the list.'
            },
            {
                'question': 'Which method adds an element to the END of a list?',
                'options': ['insert()', 'add()', 'append()', 'push()'],
                'answer': 2,
                'explanation': 'append() adds an element to the end of the list. insert(i, x) adds at a specific index. Python lists don\'t have add() or push().'
            },
            {
                'question': 'What does [x**2 for x in range(4)] produce?',
                'options': ['[1, 4, 9, 16]', '[0, 1, 4, 9]', '[0, 1, 2, 3]', '[1, 2, 3, 4]'],
                'answer': 1,
                'explanation': 'range(4) produces 0, 1, 2, 3. Squaring each: 0²=0, 1²=1, 2²=4, 3²=9. Result: [0, 1, 4, 9].'
            },
        ]
    },
    {
        'id': 2,
        'title': 'Strings',
        'icon': '🔤',
        'description': 'Explore strings — sequences of characters with powerful built-in methods.',
        'difficulty': 'Beginner',
        'estimated_time': '40 min',
        'color': '#0891b2',
        'content': """
<h2>What is a String?</h2>
<p>A <strong>string</strong> is a sequence of characters enclosed in quotes. In Python, strings are <strong>immutable</strong> — once created, they cannot be changed in place.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Strings behave like read-only lists of characters. You can access individual characters, slice them, and iterate over them — but you can't change a character in place.</p>
</div>

<h3>Creating Strings</h3>
<pre><code class="language-python">
s1 = 'Hello'         # Single quotes
s2 = "World"         # Double quotes
s3 = '''Multi
line'''              # Triple quotes (multi-line)

# Strings are sequences of characters
name = "Python"
print(name[0])   # P
print(name[-1])  # n
print(name[1:4]) # yth  (slicing works!)
</code></pre>

<h3>String Immutability</h3>
<pre><code class="language-python">
s = "hello"
# s[0] = "H"   ← This FAILS! TypeError: 'str' object does not support item assignment

# Instead, create a new string:
s = "H" + s[1:]   # "Hello"
# or
s = s.replace("h", "H")  # "Hello"
</code></pre>

<h3>Essential String Methods</h3>
<pre><code class="language-python">
s = "  Hello, World!  "

# Case methods
s.upper()       # "  HELLO, WORLD!  "
s.lower()       # "  hello, world!  "
s.title()       # "  Hello, World!  "

# Stripping whitespace
s.strip()       # "Hello, World!"  (removes leading/trailing spaces)
s.lstrip()      # "Hello, World!  "  (left only)
s.rstrip()      # "  Hello, World!"  (right only)

# Finding & replacing
s = "banana"
s.count("a")        # 3  (count occurrences)
s.find("na")        # 2  (first index, or -1 if not found)
s.replace("a", "o") # "bonono"

# Splitting & joining
"a,b,c".split(",")     # ["a", "b", "c"]
",".join(["a","b","c"]) # "a,b,c"

# Checking content
"hello123".isalpha()   # False (has digits)
"hello".isalpha()      # True
"123".isdigit()        # True
"hello".startswith("he")  # True
"world".endswith("ld")    # True
</code></pre>

<h3>String Formatting</h3>
<pre><code class="language-python">
name = "Alice"
score = 95.5

# f-strings (modern, recommended)
print(f"Hello, {name}! Your score is {score:.1f}")
# Output: Hello, Alice! Your score is 95.5

# format() method
print("Hello, {}! Score: {}".format(name, score))
</code></pre>

<h3>Iterating Over Strings</h3>
<pre><code class="language-python">
for char in "Python":
    print(char)   # P, y, t, h, o, n (one per line)

# Count vowels
vowels = 0
for ch in "Hello World":
    if ch.lower() in "aeiou":
        vowels += 1
print(vowels)  # 3
</code></pre>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Count Character Frequency',
                'description': 'Write a function <code>char_frequency(s)</code> that returns a dictionary where keys are characters and values are how many times each character appears in the string. Ignore spaces and be case-insensitive.',
                'starter_code': '''def char_frequency(s):
    """
    Return a dict of character frequencies.
    Ignore spaces. Treat upper/lower as same.
    Example: char_frequency("Hello") -> {"h": 1, "e": 1, "l": 2, "o": 1}
    """
    pass

# Test it
result = char_frequency("Hello World")
print(result)
# Expected (ignoring spaces, lowercase): {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}:")
        print(f"    Expected: {expected}")
        print(f"    Got:      {got}")
        _fail += 1

print("Testing char_frequency:")
_test(
    "char_frequency('hello')",
    char_frequency("hello"),
    {"h": 1, "e": 1, "l": 2, "o": 1}
)
_test(
    "char_frequency('aaa')",
    char_frequency("aaa"),
    {"a": 3}
)
_test(
    "char_frequency('A a')",
    char_frequency("A a"),
    {"a": 2}
)
_test(
    "char_frequency('')",
    char_frequency(""),
    {}
)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Convert the string to lowercase first using s.lower().',
                    'Use a dictionary: freq = {} then loop through each character.',
                    'For each char, do freq[char] = freq.get(char, 0) + 1',
                    'Skip spaces with: if char == " ": continue',
                ]
            },
            {
                'id': 2,
                'title': 'Check if Two Strings are Anagrams',
                'description': 'Write a function <code>are_anagrams(s1, s2)</code> that returns <code>True</code> if the two strings are anagrams of each other. Two strings are anagrams if they contain the same characters with the same frequencies (ignoring spaces and case).',
                'starter_code': '''def are_anagrams(s1, s2):
    """
    Return True if s1 and s2 are anagrams.
    Ignore case and spaces.
    "listen" and "silent" are anagrams!
    """
    pass

print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("hello", "world"))     # False
print(are_anagrams("Astronomer", "Moon starer"))  # True
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

print("Testing are_anagrams:")
_test("listen / silent -> True",  are_anagrams("listen", "silent"), True)
_test("hello / world -> False",   are_anagrams("hello", "world"), False)
_test("Astronomer / Moon starer -> True", are_anagrams("Astronomer", "Moon starer"), True)
_test("abc / cab -> True",        are_anagrams("abc", "cab"), True)
_test("rat / car -> False",       are_anagrams("rat", "car"), False)
_test("aab / baa -> True",        are_anagrams("aab", "baa"), True)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Clean both strings: lowercase and remove spaces.',
                    'Approach 1: Sort both strings and compare — sorted(s1) == sorted(s2)',
                    'Approach 2: Build frequency dicts for both and compare them.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'Which of the following will FAIL because strings are immutable?',
                'options': ['s = "hello"; s = s.upper()', 's = "hello"; s[0] = "H"', 's = "hello"; s = s + " world"', 's = "hello"; s = s.replace("h","H")'],
                'answer': 1,
                'explanation': 'Strings are immutable — you cannot assign to an index. s[0] = "H" raises a TypeError. The other options create NEW strings.'
            },
            {
                'question': 'What does "hello world".split() return?',
                'options': ['"hello", "world"', '["hello", "world"]', '["h","e","l","l","o"," ","w","o","r","l","d"]', 'Error'],
                'answer': 1,
                'explanation': 'split() without arguments splits on whitespace, returning a list of words: ["hello", "world"].'
            },
            {
                'question': 'What is the output of "banana".count("an")?',
                'options': ['1', '2', '3', '4'],
                'answer': 1,
                'explanation': '"banana" contains "an" at positions 1 and 3: b[an][an]a. Count = 2.'
            },
            {
                'question': 'Which method removes whitespace from BOTH ends of a string?',
                'options': ['strip()', 'trim()', 'clean()', 'remove()'],
                'answer': 0,
                'explanation': 'strip() removes whitespace (spaces, tabs, newlines) from both the beginning and end. lstrip() and rstrip() do one side each.'
            },
            {
                'question': 'What does f"Value: {2 + 3}" evaluate to?',
                'options': ['"Value: {2 + 3}"', '"Value: 5"', 'Error', '"Value: 2 + 3"'],
                'answer': 1,
                'explanation': 'f-strings evaluate the expression inside {}. 2 + 3 = 5, so the result is "Value: 5".'
            },
        ]
    },
    {
        'id': 3,
        'title': 'Linked Lists',
        'icon': '🔗',
        'description': 'Build your first custom data structure — nodes connected by pointers.',
        'difficulty': 'Beginner',
        'estimated_time': '55 min',
        'color': '#7c3aed',
        'content': """
<h2>What is a Linked List?</h2>
<p>A <strong>linked list</strong> is a chain of <strong>nodes</strong>. Each node stores a value AND a reference (pointer) to the next node in the chain.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Unlike arrays (contiguous memory), linked list nodes can be anywhere in memory. Each node "points" to the next one, like a treasure hunt where each clue tells you where to find the next.</p>
</div>

<div class="visual-box">
  <p><strong>Visual representation:</strong></p>
  <code>[10 | •]──▶[20 | •]──▶[30 | •]──▶[40 | None]</code>
  <br><small>value | next_pointer</small>
</div>

<h3>The Node Class</h3>
<pre><code class="language-python">
class Node:
    def __init__(self, data):
        self.data = data    # The value stored
        self.next = None    # Pointer to next node (starts as None)

# Create individual nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link them together
node1.next = node2
node2.next = node3

# Now we have: 10 → 20 → 30 → None
</code></pre>

<h3>The LinkedList Class</h3>
<pre><code class="language-python">
class LinkedList:
    def __init__(self):
        self.head = None   # Points to the first node

    def append(self, data):
        '''Add a new node at the end.'''
        new_node = Node(data)

        if self.head is None:       # List is empty
            self.head = new_node
            return

        # Walk to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node     # Link last node to new node

    def display(self):
        '''Print all values in the list.'''
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" → ".join(elements) + " → None")

# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # 10 → 20 → 30 → None
</code></pre>

<h3>Prepend (Add to Front)</h3>
<pre><code class="language-python">
def prepend(self, data):
    '''Add a new node at the beginning - O(1)!'''
    new_node = Node(data)
    new_node.next = self.head   # New node points to current head
    self.head = new_node        # Head now points to new node
</code></pre>

<h3>Delete a Node</h3>
<pre><code class="language-python">
def delete(self, data):
    '''Remove the first node with the given data.'''
    if self.head is None:
        return

    # Special case: delete the head
    if self.head.data == data:
        self.head = self.head.next
        return

    # Find the node BEFORE the one to delete
    current = self.head
    while current.next is not None:
        if current.next.data == data:
            current.next = current.next.next  # Skip over the deleted node
            return
        current = current.next
</code></pre>

<h3>Array vs Linked List</h3>
<table class="complexity-table">
  <tr><th>Operation</th><th>Array</th><th>Linked List</th></tr>
  <tr><td>Access by index</td><td>O(1) ✅</td><td>O(n) ❌</td></tr>
  <tr><td>Insert at front</td><td>O(n) ❌</td><td>O(1) ✅</td></tr>
  <tr><td>Insert at end</td><td>O(1) ✅</td><td>O(n)*</td></tr>
  <tr><td>Delete from front</td><td>O(n) ❌</td><td>O(1) ✅</td></tr>
  <tr><td>Memory</td><td>Contiguous</td><td>Scattered</td></tr>
</table>
<p><small>*O(1) if you keep a tail pointer</small></p>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Build a Linked List',
                'description': 'Implement a <code>Node</code> class and a <code>LinkedList</code> class with <code>append()</code>, <code>prepend()</code>, and <code>display()</code> methods. The display method should return a Python list of values (not print).',
                'starter_code': '''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add node at the end."""
        pass

    def prepend(self, data):
        """Add node at the beginning."""
        pass

    def to_list(self):
        """Return all values as a Python list."""
        # e.g., if list is 10 -> 20 -> 30, return [10, 20, 30]
        pass

# Test
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.to_list())   # [10, 20, 30]

ll.prepend(5)
print(ll.to_list())   # [5, 10, 20, 30]
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

ll = LinkedList()
_test("Empty list", ll.to_list(), [])

ll.append(10)
_test("After append(10)", ll.to_list(), [10])

ll.append(20)
ll.append(30)
_test("After append 20, 30", ll.to_list(), [10, 20, 30])

ll.prepend(5)
_test("After prepend(5)", ll.to_list(), [5, 10, 20, 30])

ll.prepend(1)
_test("After prepend(1)", ll.to_list(), [1, 5, 10, 20, 30])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'For append: if head is None, set head to new node. Otherwise, traverse until current.next is None.',
                    'For prepend: set new_node.next = self.head, then self.head = new_node.',
                    'For to_list: create an empty list, traverse nodes, append each data value.',
                ]
            },
            {
                'id': 2,
                'title': 'Search & Count in a Linked List',
                'description': 'Add <code>search(data)</code> (returns True/False) and <code>length()</code> (returns count of nodes) methods to the LinkedList class.',
                'starter_code': '''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, data):
        """Return True if data exists in list, False otherwise."""
        pass

    def length(self):
        """Return the number of nodes in the list."""
        pass

# Test
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.append(val)

print(ll.search(30))   # True
print(ll.search(99))   # False
print(ll.length())     # 5
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

ll = LinkedList()
_test("length of empty list", ll.length(), 0)
_test("search in empty list", ll.search(10), False)

for val in [10, 20, 30, 40, 50]:
    ll.append(val)

_test("length after 5 appends", ll.length(), 5)
_test("search(30) -> True",  ll.search(30), True)
_test("search(10) -> True",  ll.search(10), True)
_test("search(50) -> True",  ll.search(50), True)
_test("search(99) -> False", ll.search(99), False)
_test("search(0) -> False",  ll.search(0),  False)

ll.append(60)
_test("length after 6th append", ll.length(), 6)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'For search: traverse the list. If current.data == data, return True. If you reach None, return False.',
                    'For length: use a counter variable. Traverse and increment counter each step.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'In a singly linked list, each node contains:',
                'options': ['Only the data value', 'The data and a pointer to the next node', 'The data and pointers to both next and previous nodes', 'Only a pointer to the next node'],
                'answer': 1,
                'explanation': 'In a singly linked list, each node has two parts: the data (value) and a "next" pointer to the following node. Doubly linked lists also have a "prev" pointer.'
            },
            {
                'question': 'What is the time complexity of inserting at the FRONT of a linked list?',
                'options': ['O(n)', 'O(log n)', 'O(1)', 'O(n²)'],
                'answer': 2,
                'explanation': 'Inserting at the front (prepend) is O(1) — just create a new node, point it to the current head, and update head. No traversal needed!'
            },
            {
                'question': 'To traverse a linked list, you start at:',
                'options': ['The tail', 'The middle', 'Any node', 'The head'],
                'answer': 3,
                'explanation': 'You always start traversal at the head node. The head is the entry point to the list — without it, you\'d have no way to access the chain.'
            },
            {
                'question': 'What value does the LAST node\'s "next" pointer hold?',
                'options': ['0', '-1', 'None', 'A reference to the head'],
                'answer': 2,
                'explanation': 'The last node\'s next pointer is None, which signals the end of the list. This is how traversal loops know to stop.'
            },
            {
                'question': 'Compared to arrays, linked lists are BETTER for:',
                'options': ['Random access by index', 'Frequent insertions at the front', 'Binary search', 'Cache performance'],
                'answer': 1,
                'explanation': 'Linked lists excel at insertions/deletions at the front (O(1)). Arrays are better for random access (O(1) vs O(n)), binary search, and cache locality.'
            },
        ]
    },
    {
        'id': 4,
        'title': 'Stacks & Queues',
        'icon': '📚',
        'description': 'Learn two essential data structures with opposite ordering principles.',
        'difficulty': 'Beginner',
        'estimated_time': '50 min',
        'color': '#b45309',
        'content': """
<h2>Stacks — Last In, First Out (LIFO)</h2>
<p>A <strong>stack</strong> is like a stack of plates. You can only add to the top and remove from the top. The last plate placed is the first one removed.</p>

<div class="concept-box">
  <h4>🔑 Real World Examples</h4>
  <ul>
    <li>Browser back button (history of pages)</li>
    <li>Undo/Redo in text editors</li>
    <li>Function call stack in programs</li>
    <li>Checking balanced brackets: ( [ { } ] )</li>
  </ul>
</div>

<h3>Stack Operations</h3>
<pre><code class="language-python">
# Using Python list as a stack
stack = []

# Push — add to top: O(1)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  # [10, 20, 30]  — top is on the right

# Peek — look at top without removing: O(1)
top = stack[-1]
print(top)    # 30

# Pop — remove from top: O(1)
item = stack.pop()
print(item)   # 30
print(stack)  # [10, 20]

# Check if empty
if not stack:
    print("Stack is empty")
</code></pre>

<h3>Stack Class Implementation</h3>
<pre><code class="language-python">
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
</code></pre>

<h3>Classic Stack Application: Bracket Matching</h3>
<pre><code class="language-python">
def is_balanced(s):
    '''Check if brackets in s are balanced.'''
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)        # Push opening bracket
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return False          # No matching opener
            stack.pop()               # Pop the matching opener

    return len(stack) == 0            # Stack should be empty at end

print(is_balanced("()[]{}"))  # True
print(is_balanced("([{}])"))  # True
print(is_balanced("([)]"))    # False
</code></pre>

<h2>Queues — First In, First Out (FIFO)</h2>
<p>A <strong>queue</strong> is like a line at a store. The first person in line is the first to be served.</p>

<div class="concept-box">
  <h4>🔑 Real World Examples</h4>
  <ul>
    <li>Print queue (documents printed in order received)</li>
    <li>Customer service lines</li>
    <li>BFS (Breadth-First Search) in graphs</li>
    <li>Task scheduling in operating systems</li>
  </ul>
</div>

<h3>Queue Implementation</h3>
<pre><code class="language-python">
from collections import deque  # Efficient double-ended queue

queue = deque()

# Enqueue — add to back: O(1)
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")
print(queue)  # deque(['Alice', 'Bob', 'Charlie'])

# Dequeue — remove from front: O(1)
first = queue.popleft()
print(first)  # "Alice"
print(queue)  # deque(['Bob', 'Charlie'])

# Peek at front
front = queue[0]
</code></pre>

<div class="warning-box">
  <h4>⚠️ Don't use list as a queue!</h4>
  <p>list.pop(0) is O(n) because it shifts all elements. Always use <code>collections.deque</code> for queues — its popleft() is O(1).</p>
</div>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Implement a Stack & Check Balanced Brackets',
                'description': 'First, implement a <code>Stack</code> class with <code>push()</code>, <code>pop()</code>, <code>peek()</code>, <code>is_empty()</code>, and <code>size()</code>. Then use it to implement <code>is_balanced(s)</code> that checks if brackets in a string are properly balanced.',
                'starter_code': '''class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass


def is_balanced(s):
    """
    Return True if all brackets in s are balanced.
    Brackets: (), [], {}
    Other characters are ignored.
    """
    pass

# Test
print(is_balanced("()[]{}"))  # True
print(is_balanced("([{}])"))  # True
print(is_balanced("([)]"))    # False
print(is_balanced("{[}"))     # False
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

print("Testing Stack:")
s = Stack()
_test("is_empty() on new stack", s.is_empty(), True)
s.push(1); s.push(2); s.push(3)
_test("size() after 3 pushes", s.size(), 3)
_test("peek() == 3", s.peek(), 3)
_test("pop() == 3", s.pop(), 3)
_test("pop() == 2", s.pop(), 2)
_test("size() after 2 pops", s.size(), 1)
_test("is_empty() when 1 item left", s.is_empty(), False)
s.pop()
_test("is_empty() after all pops", s.is_empty(), True)

print("\\nTesting is_balanced:")
_test("() -> True",       is_balanced("()"), True)
_test("()[]{} -> True",   is_balanced("()[]{}"), True)
_test("([{}]) -> True",   is_balanced("([{}])"), True)
_test("(] -> False",      is_balanced("(]"), False)
_test("([)] -> False",    is_balanced("([)]"), False)
_test("{[} -> False",     is_balanced("{[}"), False)
_test("abc(def) -> True", is_balanced("abc(def)"), True)
_test("empty -> True",    is_balanced(""), True)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Stack.push: use self._data.append(item)',
                    'Stack.pop: check is_empty first, then return self._data.pop()',
                    'For is_balanced: push opening brackets, when you see a closing bracket check if top of stack matches.',
                    'Use a dict: matching = {")" : "(", "]": "[", "}": "{"}',
                ]
            },
            {
                'id': 2,
                'title': 'Implement a Queue',
                'description': 'Implement a <code>Queue</code> class using Python\'s <code>collections.deque</code> with <code>enqueue()</code>, <code>dequeue()</code>, <code>front()</code>, <code>is_empty()</code>, and <code>size()</code> methods.',
                'starter_code': '''from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Add item to the back of the queue."""
        pass

    def dequeue(self):
        """Remove and return item from the front."""
        pass

    def front(self):
        """Return the front item without removing it."""
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

# Test
q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")
print(q.front())     # Alice
print(q.dequeue())   # Alice
print(q.front())     # Bob
print(q.size())      # 2
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

q = Queue()
_test("is_empty() on new queue", q.is_empty(), True)
_test("size() on new queue", q.size(), 0)

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
_test("size() after 3 enqueues", q.size(), 3)
_test("front() == A", q.front(), "A")
_test("is_empty() with items", q.is_empty(), False)
_test("dequeue() == A (FIFO!)", q.dequeue(), "A")
_test("dequeue() == B", q.dequeue(), "B")
_test("front() == C", q.front(), "C")
_test("size() after 2 dequeues", q.size(), 1)
_test("dequeue() == C", q.dequeue(), "C")
_test("is_empty() after all dequeued", q.is_empty(), True)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'enqueue: use self._data.append(item) to add to the back.',
                    'dequeue: use self._data.popleft() to remove from the front.',
                    'front: return self._data[0] (peek without removing).',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'A stack follows which principle?',
                'options': ['First In, First Out (FIFO)', 'Last In, First Out (LIFO)', 'Random access', 'Priority ordering'],
                'answer': 1,
                'explanation': 'A stack is LIFO — Last In, First Out. Think of a stack of plates: the last plate placed is the first one removed.'
            },
            {
                'question': 'Which real-world scenario is best modeled by a QUEUE?',
                'options': ['Browser history (back button)', 'Undo/Redo functionality', 'Customers waiting in line at a bank', 'Function call stack'],
                'answer': 2,
                'explanation': 'A queue (FIFO) models a waiting line perfectly — the first customer to arrive is the first to be served. Undo/Redo and browser history are stacks (LIFO).'
            },
            {
                'question': 'What does "peek" mean in a stack?',
                'options': ['Remove the top element', 'Add an element to the top', 'View the top element without removing it', 'Check if the stack is empty'],
                'answer': 2,
                'explanation': 'Peek lets you see the top element without removing it — like glancing at the top plate without taking it off the stack.'
            },
            {
                'question': 'Why should you use collections.deque instead of a list for a queue?',
                'options': ['deque uses less memory', 'deque.popleft() is O(1), while list.pop(0) is O(n)', 'lists cannot store strings', 'deque is faster for push operations'],
                'answer': 1,
                'explanation': 'list.pop(0) must shift every remaining element one position left, taking O(n) time. deque.popleft() removes from the front in O(1).'
            },
            {
                'question': 'For the string "([{", is_balanced() should return:',
                'options': ['True', 'False', 'None', 'Error'],
                'answer': 1,
                'explanation': 'Three opening brackets with no closing brackets — the stack will have 3 items left at the end. A balanced string requires an empty stack when done, so this returns False.'
            },
        ]
    },
    {
        'id': 5,
        'title': 'Binary Trees',
        'icon': '🌳',
        'description': 'Explore tree-shaped data structures and recursive traversal.',
        'difficulty': 'Intermediate',
        'estimated_time': '60 min',
        'color': '#16a34a',
        'content': """
<h2>What is a Binary Tree?</h2>
<p>A <strong>binary tree</strong> is a hierarchical data structure where each node has at most <strong>two children</strong> — called the left child and the right child.</p>

<div class="concept-box">
  <h4>🔑 Key Terminology</h4>
  <ul>
    <li><strong>Root</strong>: The topmost node (has no parent)</li>
    <li><strong>Leaf</strong>: A node with no children</li>
    <li><strong>Height</strong>: Number of nodes on the longest path from root to a leaf (a root-only tree has height 1; an empty tree has height 0)</li>
    <li><strong>Parent/Child</strong>: Nodes directly connected above/below</li>
  </ul>
</div>

<div class="visual-box">
<pre>
        10          ← Root
       /  \\
      5    15       ← Level 1
     / \\     \\
    3   7     20   ← Level 2 (3, 7, 20 are leaves)
</pre>
</div>

<h3>TreeNode Class</h3>
<pre><code class="language-python">
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None    # Left child
        self.right = None   # Right child

# Build the tree above manually:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)
</code></pre>

<h3>Binary Search Tree (BST)</h3>
<p>A BST has a special property: for every node, <strong>all values in its left subtree are smaller</strong>, and <strong>all values in its right subtree are larger</strong>.</p>

<pre><code class="language-python">
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        '''Insert a value maintaining BST property.'''
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def search(self, val):
        '''Return True if val is in the BST.'''
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)
</code></pre>

<h3>Tree Traversals</h3>
<p>There are three common ways to visit every node in a binary tree:</p>

<pre><code class="language-python">
def inorder(node):
    '''Left -> Root -> Right (gives sorted order for BST!)'''
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def preorder(node):
    '''Root -> Left -> Right (good for copying a tree)'''
    if node is None:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

def postorder(node):
    '''Left -> Right -> Root (good for deleting a tree)'''
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]

# For our example tree (10, 5, 15, 3, 7, 20):
# Inorder:   [3, 5, 7, 10, 15, 20]  ← sorted!
# Preorder:  [10, 5, 3, 7, 15, 20]
# Postorder: [3, 7, 5, 20, 15, 10]
</code></pre>

<h3>BST Search Complexity</h3>
<table class="complexity-table">
  <tr><th>Operation</th><th>Average</th><th>Worst (unbalanced)</th></tr>
  <tr><td>Search</td><td>O(log n)</td><td>O(n)</td></tr>
  <tr><td>Insert</td><td>O(log n)</td><td>O(n)</td></tr>
  <tr><td>Delete</td><td>O(log n)</td><td>O(n)</td></tr>
</table>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Build a Binary Search Tree',
                'description': 'Implement a <code>BST</code> class with <code>insert(val)</code> and <code>search(val)</code> methods. Then add <code>inorder()</code> that returns all values in sorted order.',
                'starter_code': '''class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert val into the BST."""
        pass

    def search(self, val):
        """Return True if val is in the BST."""
        pass

    def inorder(self):
        """Return list of all values in sorted (ascending) order."""
        pass

# Test
bst = BST()
for val in [10, 5, 15, 3, 7, 20, 1]:
    bst.insert(val)

print(bst.inorder())     # [1, 3, 5, 7, 10, 15, 20]
print(bst.search(7))     # True
print(bst.search(99))    # False
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

bst = BST()
for val in [10, 5, 15, 3, 7, 20, 1]:
    bst.insert(val)

_test("inorder gives sorted list", bst.inorder(), [1, 3, 5, 7, 10, 15, 20])
_test("search(7) -> True",  bst.search(7),  True)
_test("search(10) -> True", bst.search(10), True)
_test("search(1) -> True",  bst.search(1),  True)
_test("search(99) -> False", bst.search(99), False)
_test("search(0) -> False",  bst.search(0),  False)

bst2 = BST()
bst2.insert(5)
_test("single node inorder", bst2.inorder(), [5])
_test("single node search hit",  bst2.search(5), True)
_test("single node search miss", bst2.search(3), False)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Use recursion! A helper method _insert(node, val) makes it cleaner.',
                    'For insert: if val < node.val, go left; otherwise go right.',
                    'For inorder: result = inorder(left) + [current] + inorder(right)',
                    'Base case for recursion: if node is None, return [] (for inorder) or False (for search).',
                ]
            },
            {
                'id': 2,
                'title': 'Tree Height & Count Nodes',
                'description': 'Add two methods to a BST: <code>height()</code> returns the height of the tree (number of levels), and <code>count()</code> returns the total number of nodes.',
                'starter_code': '''class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return
        self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None: node.left = TreeNode(val)
            else: self._insert(node.left, val)
        else:
            if node.right is None: node.right = TreeNode(val)
            else: self._insert(node.right, val)

    def height(self):
        """Return the height of the tree (0 if empty, 1 if only root)."""
        pass

    def count(self):
        """Return the total number of nodes."""
        pass

# Test
bst = BST()
print(bst.height())  # 0 (empty)
bst.insert(10)
print(bst.height())  # 1 (just root)
for val in [5, 15, 3, 7]:
    bst.insert(val)
print(bst.height())  # 3
print(bst.count())   # 5
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

bst = BST()
_test("height of empty tree", bst.height(), 0)
_test("count of empty tree",  bst.count(), 0)

bst.insert(10)
_test("height with root only", bst.height(), 1)
_test("count with root only",  bst.count(), 1)

for val in [5, 15, 3, 7]:
    bst.insert(val)
_test("height of 3-level tree", bst.height(), 3)
_test("count of 5-node tree",   bst.count(), 5)

bst.insert(1)
_test("height after inserting deeper node", bst.height(), 4)
_test("count after 6th insert", bst.count(), 6)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Use recursion. height(node) = 1 + max(height(left), height(right))',
                    'Base case: if node is None, return 0.',
                    'count(node) = 1 + count(left) + count(right)',
                    'Create private helper methods _height(node) and _count(node).',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'In a Binary Search Tree, where are values smaller than the root stored?',
                'options': ['In the right subtree', 'In the left subtree', 'At the root', 'In a separate list'],
                'answer': 1,
                'explanation': 'BST property: values smaller than a node go to its LEFT subtree, and values larger go to the RIGHT subtree. This is what makes BST search efficient.'
            },
            {
                'question': 'Which traversal of a BST produces values in sorted (ascending) order?',
                'options': ['Preorder (Root→Left→Right)', 'Postorder (Left→Right→Root)', 'Inorder (Left→Root→Right)', 'Level-order'],
                'answer': 2,
                'explanation': 'Inorder traversal (Left → Root → Right) of a BST always produces values in ascending sorted order. This is one of the BST\'s key properties.'
            },
            {
                'question': 'What is the height of a tree with only a root node?',
                'options': ['0', '1', '2', '-1'],
                'answer': 1,
                'explanation': 'A tree with only the root has height 1 (one level). An empty tree has height 0. Definitions can vary, but this is the most common convention.'
            },
            {
                'question': 'What is the average time complexity of searching in a balanced BST?',
                'options': ['O(1)', 'O(n)', 'O(n log n)', 'O(log n)'],
                'answer': 3,
                'explanation': 'In a balanced BST, each comparison eliminates half the remaining nodes (like binary search). This gives O(log n) time — e.g., finding among 1 million nodes takes ~20 comparisons.'
            },
            {
                'question': 'A leaf node in a tree is one that:',
                'options': ['Has two children', 'Has no parent', 'Has no children', 'Has exactly one child'],
                'answer': 2,
                'explanation': 'A leaf node has no children — both its left and right pointers are None. It\'s at the "edge" of the tree.'
            },
        ]
    },
    {
        'id': 6,
        'title': 'Searching Algorithms',
        'icon': '🔍',
        'description': 'Compare linear search and binary search — and understand Big-O notation.',
        'difficulty': 'Beginner',
        'estimated_time': '45 min',
        'color': '#0e7490',
        'content': """
<h2>What is Searching?</h2>
<p>Searching means finding whether an item exists in a collection, and if so, where it is. Two fundamental algorithms are <strong>linear search</strong> and <strong>binary search</strong>.</p>

<h2>Linear Search — O(n)</h2>
<p>Check <strong>every element one by one</strong> until you find the target or exhaust the list.</p>

<div class="concept-box">
  <h4>🔑 Key Points</h4>
  <ul>
    <li>Works on ANY list (sorted or unsorted)</li>
    <li>O(n) time — checks up to n elements in worst case</li>
    <li>Simple to understand and implement</li>
  </ul>
</div>

<pre><code class="language-python">
def linear_search(arr, target):
    '''
    Search for target in arr.
    Returns the index if found, -1 if not found.
    '''
    for i in range(len(arr)):
        if arr[i] == target:
            return i       # Found! Return index
    return -1              # Not found

arr = [64, 25, 12, 22, 11]
print(linear_search(arr, 22))   # 3
print(linear_search(arr, 99))   # -1
</code></pre>

<p><strong>How many comparisons?</strong></p>
<ul>
  <li><strong>Best case</strong>: Target is first element → 1 comparison → O(1)</li>
  <li><strong>Worst case</strong>: Target is last or not there → n comparisons → O(n)</li>
  <li><strong>Average case</strong>: n/2 comparisons → O(n)</li>
</ul>

<h2>Binary Search — O(log n)</h2>
<p>Works ONLY on a <strong>sorted list</strong>. Repeatedly cut the search space in half.</p>

<div class="concept-box">
  <h4>🔑 How it works</h4>
  <p>Like guessing a number 1-100: guess 50 first. Too high? Guess 25. Too low? Guess 37. Each guess eliminates HALF the remaining possibilities!</p>
</div>

<pre><code class="language-python">
def binary_search(arr, target):
    '''
    Binary search on a SORTED array.
    Returns index if found, -1 otherwise.
    '''
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2     # Middle index

        if arr[mid] == target:
            return mid                 # Found!
        elif arr[mid] < target:
            left = mid + 1             # Target is in right half
        else:
            right = mid - 1            # Target is in left half

    return -1                          # Not found

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search(arr, 7))    # 3
print(binary_search(arr, 13))   # 6
print(binary_search(arr, 4))    # -1
</code></pre>

<h3>Step-by-step example</h3>
<div class="visual-box">
<pre>
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17], target = 7

Step 1: left=0, right=8, mid=4, arr[4]=9  > 7  → right=3
Step 2: left=0, right=3, mid=1, arr[1]=3  < 7  → left=2
Step 3: left=2, right=3, mid=2, arr[2]=5  < 7  → left=3
Step 4: left=3, right=3, mid=3, arr[3]=7 == 7  → Found at index 3!
</pre>
</div>

<h3>Why is Binary Search O(log n)?</h3>
<table class="complexity-table">
  <tr><th>List Size</th><th>Linear Search (max)</th><th>Binary Search (max)</th></tr>
  <tr><td>10</td><td>10 steps</td><td>4 steps</td></tr>
  <tr><td>100</td><td>100 steps</td><td>7 steps</td></tr>
  <tr><td>1,000</td><td>1,000 steps</td><td>10 steps</td></tr>
  <tr><td>1,000,000</td><td>1,000,000 steps</td><td>20 steps</td></tr>
</table>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Implement Linear Search',
                'description': 'Implement <code>linear_search(arr, target)</code> returning the index if found, -1 if not. Then implement <code>linear_search_all(arr, target)</code> that returns a list of ALL indices where target appears.',
                'starter_code': '''def linear_search(arr, target):
    """Return the first index of target in arr, or -1 if not found."""
    pass

def linear_search_all(arr, target):
    """Return a list of ALL indices where target appears."""
    pass

# Test
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(linear_search(arr, 5))          # 4 (first occurrence)
print(linear_search(arr, 99))         # -1
print(linear_search_all(arr, 5))      # [4, 8, 10]
print(linear_search_all(arr, 1))      # [1, 3]
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print("Testing linear_search:")
_test("find 5 (first at index 4)",  linear_search(arr, 5), 4)
_test("find 3 (first at index 0)",  linear_search(arr, 3), 0)
_test("find 9 at index 5",          linear_search(arr, 9), 5)
_test("find 99 not present -> -1",  linear_search(arr, 99), -1)
_test("empty list",                 linear_search([], 5), -1)

print("\\nTesting linear_search_all:")
_test("all 5s -> [4,8,10]",  linear_search_all(arr, 5), [4, 8, 10])
_test("all 1s -> [1,3]",     linear_search_all(arr, 1), [1, 3])
_test("all 3s -> [0,9]",     linear_search_all(arr, 3), [0, 9])
_test("99 not found -> []",  linear_search_all(arr, 99), [])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'For linear_search: use a for loop with range(len(arr)), return i when arr[i] == target.',
                    'For linear_search_all: create an empty results list, append every matching index.',
                ]
            },
            {
                'id': 2,
                'title': 'Implement Binary Search',
                'description': 'Implement <code>binary_search(arr, target)</code> on a sorted array. Return the index if found, -1 if not. Then implement a recursive version <code>binary_search_recursive(arr, target, left, right)</code>.',
                'starter_code': '''def binary_search(arr, target):
    """Iterative binary search on sorted arr. Return index or -1."""
    left = 0
    right = len(arr) - 1
    # Your code here
    pass

def binary_search_recursive(arr, target, left=None, right=None):
    """Recursive binary search. Return index or -1."""
    if left is None: left = 0
    if right is None: right = len(arr) - 1
    # Base case: search space is empty
    # Recursive case: check mid and recurse left or right
    pass

# Test (array MUST be sorted!)
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(arr, 7))            # 3
print(binary_search(arr, 19))           # 9
print(binary_search(arr, 4))            # -1
print(binary_search_recursive(arr, 13)) # 6
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print("Testing binary_search (iterative):")
_test("find 7 -> index 3",    binary_search(arr, 7),  3)
_test("find 1 -> index 0",    binary_search(arr, 1),  0)
_test("find 19 -> index 9",   binary_search(arr, 19), 9)
_test("find 11 -> index 5",   binary_search(arr, 11), 5)
_test("find 4 -> -1",         binary_search(arr, 4),  -1)
_test("find 20 -> -1",        binary_search(arr, 20), -1)
_test("empty list -> -1",     binary_search([], 5),   -1)

print("\\nTesting binary_search_recursive:")
_test("find 13 -> index 6",   binary_search_recursive(arr, 13), 6)
_test("find 1 -> index 0",    binary_search_recursive(arr, 1),  0)
_test("find 19 -> index 9",   binary_search_recursive(arr, 19), 9)
_test("find 4 -> -1",         binary_search_recursive(arr, 4),  -1)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Keep track of left and right boundaries.',
                    'mid = (left + right) // 2 — always use integer division.',
                    'If arr[mid] < target: search right half (left = mid + 1)',
                    'If arr[mid] > target: search left half (right = mid - 1)',
                    'For recursive: base case is left > right, return -1.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'Which algorithm requires the list to be SORTED before searching?',
                'options': ['Linear Search', 'Binary Search', 'Both', 'Neither'],
                'answer': 1,
                'explanation': 'Binary search REQUIRES a sorted array — it works by eliminating half the search space based on whether target is greater or lesser than the middle. Linear search works on any list.'
            },
            {
                'question': 'How many comparisons does binary search need for a list of 1,024 elements (worst case)?',
                'options': ['1,024', '512', '10', '100'],
                'answer': 2,
                'explanation': 'Binary search is O(log₂ n). log₂(1024) = 10. Each step halves the search space: 1024 → 512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1. That\'s 10 steps.'
            },
            {
                'question': 'Linear search has what time complexity in the worst case?',
                'options': ['O(1)', 'O(log n)', 'O(n)', 'O(n²)'],
                'answer': 2,
                'explanation': 'In the worst case (target not in list), linear search checks every element — O(n) time, proportional to the list size.'
            },
            {
                'question': 'In binary search, after comparing with the middle element and finding target > arr[mid], what do you do?',
                'options': ['Search the left half', 'Search the right half', 'Start over from the beginning', 'Return -1'],
                'answer': 1,
                'explanation': 'Since the array is sorted, if target > arr[mid], the target must be in the RIGHT half. Update left = mid + 1 and continue.'
            },
            {
                'question': 'Python\'s "in" operator (e.g., 5 in [1,2,5]) uses which search algorithm?',
                'options': ['Binary Search', 'Hash lookup', 'Linear Search', 'Tree search'],
                'answer': 2,
                'explanation': 'Python\'s "in" operator on a list uses linear search — O(n). For fast lookup, use a set or dictionary (hash-based, O(1) average).'
            },
        ]
    },
    {
        'id': 7,
        'title': 'Sorting Algorithms',
        'icon': '🔢',
        'description': 'Implement three fundamental sorting algorithms and understand their trade-offs.',
        'difficulty': 'Beginner',
        'estimated_time': '60 min',
        'color': '#9333ea',
        'content': """
<h2>Why Learn Sorting?</h2>
<p>Sorting is one of the most studied problems in computer science. Understanding sorting teaches you algorithm design, comparison, and optimization. It's also essential for enabling fast binary search!</p>

<h2>Bubble Sort — O(n²)</h2>
<p>Repeatedly <strong>compare adjacent elements</strong> and swap them if they're in the wrong order. Larger elements "bubble up" to the end.</p>

<pre><code class="language-python">
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # After each pass, the (i+1) largest elements are in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap!
    return arr

# Trace through [5, 3, 8, 1]:
# Pass 1: [3,5,8,1] → [3,5,8,1] → [3,5,1,8]  (8 bubbles to end)
# Pass 2: [3,5,1,8] → [3,1,5,8]              (5 is in place)
# Pass 3: [1,3,5,8]                           (done!)
</code></pre>

<h2>Selection Sort — O(n²)</h2>
<p>Find the <strong>minimum element</strong> in the unsorted portion and place it at the beginning.</p>

<pre><code class="language-python">
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum in the unsorted portion arr[i:]
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap minimum to position i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Trace through [5, 3, 8, 1]:
# i=0: min is 1 at idx 3 → swap → [1, 3, 8, 5]
# i=1: min is 3 at idx 1 → swap → [1, 3, 8, 5]
# i=2: min is 5 at idx 3 → swap → [1, 3, 5, 8]
# Done!
</code></pre>

<h2>Insertion Sort — O(n²), but great for small/nearly-sorted lists</h2>
<p>Build the sorted array one element at a time by <strong>inserting each element into its correct position</strong>.</p>

<pre><code class="language-python">
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # The element to insert
        j = i - 1
        # Shift larger elements one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key     # Insert key in correct position
    return arr

# Trace through [5, 3, 8, 1]:
# i=1: key=3, shift 5 right → [5,5,8,1] → insert 3 → [3,5,8,1]
# i=2: key=8, 5<8 so no shift needed → [3,5,8,1]
# i=3: key=1, shift 8,5,3 right → insert 1 → [1,3,5,8]
</code></pre>

<h3>Comparison</h3>
<table class="complexity-table">
  <tr><th>Algorithm</th><th>Best</th><th>Average</th><th>Worst</th><th>Stable?</th></tr>
  <tr><td>Bubble Sort</td><td>O(n)*</td><td>O(n²)</td><td>O(n²)</td><td>Yes ✅</td></tr>
  <tr><td>Selection Sort</td><td>O(n²)</td><td>O(n²)</td><td>O(n²)</td><td>No ❌</td></tr>
  <tr><td>Insertion Sort</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>Yes ✅</td></tr>
  <tr><td>Python's sort()</td><td>O(n)</td><td>O(n log n)</td><td>O(n log n)</td><td>Yes ✅</td></tr>
</table>
<p><small>Stable = equal elements maintain their original order.<br>
* Bubble sort achieves O(n) best-case <em>only</em> with an early-exit <code>swapped</code> flag — without it, every pass always runs and the best-case is also O(n²).</small></p>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Implement Bubble Sort',
                'description': 'Implement <code>bubble_sort(arr)</code> that sorts the list in ascending order. <strong>Important:</strong> work on a copy of the list so you don\'t modify the original. Return the sorted list.',
                'starter_code': '''def bubble_sort(arr):
    """Sort arr in ascending order using bubble sort. Return sorted list."""
    arr = arr.copy()  # Work on a copy
    n = len(arr)
    # Outer loop: n passes total
    # Inner loop: compare adjacent elements and swap if needed
    # Tip: use a 'swapped' flag to exit early when no swaps occurred —
    #      this gives O(n) best-case on an already-sorted input.
    pass

# Test
print(bubble_sort([5, 3, 8, 1, 9, 2]))   # [1, 2, 3, 5, 8, 9]
print(bubble_sort([1]))                   # [1]
print(bubble_sort([]))                    # []
print(bubble_sort([5, 5, 3, 3, 1]))      # [1, 3, 3, 5, 5]
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

print("Testing bubble_sort:")
_test("[5,3,8,1,9,2]", bubble_sort([5,3,8,1,9,2]), [1,2,3,5,8,9])
_test("[1]",           bubble_sort([1]),            [1])
_test("[]",            bubble_sort([]),             [])
_test("[5,5,3,1]",     bubble_sort([5,5,3,1]),      [1,3,5,5])
_test("already sorted", bubble_sort([1,2,3,4,5]),   [1,2,3,4,5])
_test("reverse sorted", bubble_sort([5,4,3,2,1]),   [1,2,3,4,5])
_test("negatives",      bubble_sort([-3,-1,-5,0]),  [-5,-3,-1,0])

# Verify original not modified
original = [5, 3, 1]
_ = bubble_sort(original)
_test("original not modified", original, [5, 3, 1])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Outer loop: for i in range(n)',
                    'Inner loop: for j in range(0, n - i - 1) — we don\'t need to check elements already bubbled to the end.',
                    'Swap: arr[j], arr[j+1] = arr[j+1], arr[j]',
                    "Don't forget: arr = arr.copy() to avoid modifying the original.",
                ]
            },
            {
                'id': 2,
                'title': 'Implement Insertion Sort',
                'description': 'Implement <code>insertion_sort(arr)</code>. For each element, find its correct position in the already-sorted portion and insert it there.',
                'starter_code': '''def insertion_sort(arr):
    """Sort arr in ascending order using insertion sort. Return sorted list."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]   # Element to place correctly
        j = i - 1
        # Shift elements greater than key one position to the right
        # Then place key in the correct position
        pass
    return arr

print(insertion_sort([5, 3, 8, 1, 9, 2]))  # [1, 2, 3, 5, 8, 9]
print(insertion_sort([2, 1]))               # [1, 2]
print(insertion_sort([1, 2, 3]))            # [1, 2, 3] (already sorted)
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

print("Testing insertion_sort:")
_test("[5,3,8,1,9,2]",  insertion_sort([5,3,8,1,9,2]), [1,2,3,5,8,9])
_test("[2,1]",           insertion_sort([2,1]),          [1,2])
_test("[1,2,3]",         insertion_sort([1,2,3]),        [1,2,3])
_test("[]",              insertion_sort([]),             [])
_test("[1]",             insertion_sort([1]),            [1])
_test("[5,4,3,2,1]",    insertion_sort([5,4,3,2,1]),    [1,2,3,4,5])
_test("with duplicates", insertion_sort([3,1,2,1,3]),   [1,1,2,3,3])

original = [3, 1, 2]
_ = insertion_sort(original)
_test("original not modified", original, [3, 1, 2])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'key = arr[i] saves the element you\'re currently placing.',
                    'while j >= 0 and arr[j] > key: — shift arr[j] to arr[j+1]',
                    'After the while loop: arr[j+1] = key places the element.',
                    "Don't forget to decrement j: j -= 1 inside the while loop.",
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What is the worst-case time complexity of Bubble Sort?',
                'options': ['O(n)', 'O(n log n)', 'O(n²)', 'O(log n)'],
                'answer': 2,
                'explanation': 'Bubble Sort has two nested loops, each running up to n times, giving O(n²). The inner loop runs n-1, n-2, ... 1 times — total ≈ n²/2 comparisons.'
            },
            {
                'question': 'Insertion Sort is most efficient when the input is:',
                'options': ['Completely random', 'Reverse sorted', 'Already nearly sorted', 'Contains many duplicates'],
                'answer': 2,
                'explanation': 'When the list is already (nearly) sorted, Insertion Sort approaches O(n) — each element is already near its correct position, requiring little shifting.'
            },
            {
                'question': 'Which sorting algorithm finds the minimum element in the unsorted portion on each pass?',
                'options': ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort'],
                'answer': 1,
                'explanation': 'Selection Sort scans the unsorted portion to find the minimum element and swaps it to the correct position. This is the defining characteristic of Selection Sort.'
            },
            {
                'question': 'In Python, arr[i], arr[j] = arr[j], arr[i] does what?',
                'options': ['Copies arr[i] to arr[j]', 'Swaps the values at indices i and j', 'Deletes both elements', 'Raises an error'],
                'answer': 1,
                'explanation': 'Python\'s tuple unpacking allows elegant simultaneous assignment: both sides are evaluated before assignment, achieving a clean swap in one line without a temp variable.'
            },
            {
                'question': 'Why do real applications use Python\'s built-in sort() instead of Bubble Sort?',
                'options': ['Bubble Sort has bugs', 'Built-in sort is O(n log n) vs O(n²)', 'Built-in sort uses less memory', 'Bubble Sort only works on numbers'],
                'answer': 1,
                'explanation': 'Python\'s built-in sort (Timsort) runs in O(n log n) worst case — dramatically faster than O(n²) for large datasets. For 1 million items: ~20M ops vs ~1 trillion ops!'
            },
        ]
    },
    {
        'id': 8,
        'title': 'Hash Tables',
        'icon': '🗂️',
        'description': 'Master dictionaries — Python\'s blazing-fast key-value lookup structure.',
        'difficulty': 'Beginner',
        'estimated_time': '50 min',
        'color': '#dc2626',
        'content': """
<h2>What is a Hash Table?</h2>
<p>A <strong>hash table</strong> maps <strong>keys to values</strong> using a <strong>hash function</strong> that converts keys into array indices. Python's <code>dict</code> is a built-in hash table.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Imagine a library with 1000 shelves. Instead of searching shelf by shelf, the librarian applies a formula to your book's title to instantly tell you which shelf it's on. That formula is a <em>hash function</em>.</p>
</div>

<h3>How a Hash Function Works</h3>
<pre><code class="language-python">
# Python's hash() converts a key to an integer
print(hash("apple"))   # e.g., -1234567890 (varies by run)
print(hash(42))        # 42 (integers hash to themselves)
print(hash("banana"))  # different number

# Hash table stores at index: hash(key) % table_size
# So "apple" might end up at index 7 in a 10-slot table
</code></pre>

<h3>Python Dictionaries</h3>
<pre><code class="language-python">
# Create
d = {}                          # Empty dict
d = {"name": "Alice", "age": 30}

# Insert / Update
d["city"] = "New York"         # Insert new key
d["age"] = 31                  # Update existing key

# Access
print(d["name"])               # "Alice"
print(d.get("phone", "N/A"))   # "N/A" (safe — no KeyError!)

# Delete
del d["city"]

# Check existence
if "name" in d:
    print("Name exists!")

# Iterate
for key in d:                  # Over keys
    print(key, d[key])

for key, value in d.items():   # Over key-value pairs
    print(f"{key}: {value}")

for value in d.values():       # Over values only
    print(value)
</code></pre>

<h3>Common Hash Table Patterns</h3>
<pre><code class="language-python">
# Pattern 1: Frequency counting
def count_words(text):
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

print(count_words("the cat sat on the mat"))
# {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

# Pattern 2: Grouping
def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

# Pattern 3: Memoization (cache function results)
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result
</code></pre>

<h3>Time Complexity</h3>
<table class="complexity-table">
  <tr><th>Operation</th><th>Average</th><th>Worst (rare)</th></tr>
  <tr><td>Insert / Update</td><td>O(1) ✅</td><td>O(n)</td></tr>
  <tr><td>Lookup (key in dict)</td><td>O(1) ✅</td><td>O(n)</td></tr>
  <tr><td>Delete</td><td>O(1) ✅</td><td>O(n)</td></tr>
  <tr><td>Iterate all keys</td><td>O(n)</td><td>O(n)</td></tr>
</table>
<p>The worst case happens with <strong>hash collisions</strong> — multiple keys mapping to the same slot. Python's implementation handles this well in practice.</p>
""",
        'labs': [
            {
                'id': 1,
                'title': 'Two Sum — Hash Map Solution',
                'description': 'Classic interview problem! Given a list <code>nums</code> and a <code>target</code>, find two numbers that add up to target. Return their indices. Use a hash map for O(n) solution instead of O(n²) brute force.',
                'starter_code': '''def two_sum(nums, target):
    """
    Find two indices i, j such that nums[i] + nums[j] == target.
    Return [i, j]. Assume exactly one solution exists.

    Hint: For each number, the "complement" needed is target - number.
    If that complement is already in your hash map, you found the pair!
    """
    seen = {}  # Maps {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        # Check if complement was seen before
        # If yes, return [index of complement, current index i]
        # If no, add current num to seen
        pass

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]  (2+7=9)
print(two_sum([3, 2, 4], 6))        # [1, 2]  (2+4=6)
print(two_sum([3, 3], 6))           # [0, 1]  (3+3=6)
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    # Accept either order [i,j] or [j,i]
    if got == expected or got == list(reversed(expected)):
        print(f"  ✓ {name}: {got}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected} or {list(reversed(expected))}, got {got}")
        _fail += 1

print("Testing two_sum:")
_test("[2,7,11,15], target=9",   two_sum([2,7,11,15], 9),  [0,1])
_test("[3,2,4], target=6",       two_sum([3,2,4], 6),      [1,2])
_test("[3,3], target=6",         two_sum([3,3], 6),         [0,1])
_test("[1,5,3,7], target=8",     two_sum([1,5,3,7], 8),    [1,3])
_test("[0,4,3,0], target=0",     two_sum([0,4,3,0], 0),    [0,3])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed! This is a classic interview solution!")
''',
                'hints': [
                    'The key insight: for each number x, you need (target - x) to complete the pair.',
                    'seen = {} stores {number: index} for numbers you\'ve already visited.',
                    'If (target - num) is already in seen, you found your pair!',
                    'Return [seen[complement], i] when you find a match.',
                ]
            },
            {
                'id': 2,
                'title': 'Find First Non-Repeating Character',
                'description': 'Write <code>first_unique_char(s)</code> that returns the index of the first character in a string that appears only once. Return -1 if all characters repeat.',
                'starter_code': '''def first_unique_char(s):
    """
    Return the index of the first non-repeating character.
    Return -1 if none exists.

    Example: "leetcode" -> 0  (l appears once, and it's first)
    Example: "loveleetcode" -> 2  (v is first unique char)
    """
    # Step 1: Count frequency of each character (use a dict!)
    # Step 2: Find the first character with frequency == 1
    pass

print(first_unique_char("leetcode"))      # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))          # -1
''',
                'test_code': '''
_pass = 0
_fail = 0

def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  ✓ {name}")
        _pass += 1
    else:
        print(f"  ✗ {name}: expected {expected}, got {got}")
        _fail += 1

print("Testing first_unique_char:")
_test('"leetcode" -> 0',       first_unique_char("leetcode"),      0)
_test('"loveleetcode" -> 2',   first_unique_char("loveleetcode"),  2)
_test('"aabb" -> -1',          first_unique_char("aabb"),          -1)
_test('"z" -> 0',              first_unique_char("z"),             0)
_test('"aab" -> 2',            first_unique_char("aab"),           2)
_test('"abcabc" -> -1',        first_unique_char("abcabc"),        -1)
_test('"dddccdbba" -> 8',      first_unique_char("dddccdbba"),     8)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Build a frequency dict: freq = {} then loop through the string.',
                    'freq[char] = freq.get(char, 0) + 1 for each character.',
                    'Then loop through the string a SECOND time with enumerate().',
                    'Return the index of the first character where freq[char] == 1.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What is the average time complexity of looking up a key in a Python dictionary?',
                'options': ['O(n)', 'O(log n)', 'O(1)', 'O(n²)'],
                'answer': 2,
                'explanation': 'Hash table lookups are O(1) on average — the hash function directly computes the storage location. This is why dicts are so powerful for lookups.'
            },
            {
                'question': 'What does dict.get("key", "default") return if "key" doesn\'t exist?',
                'options': ['None', 'KeyError', '"default"', '0'],
                'answer': 2,
                'explanation': 'dict.get(key, default) safely returns the default value when the key is absent, avoiding a KeyError. The default is optional (returns None if omitted).'
            },
            {
                'question': 'Which of these is NOT a valid dictionary key in Python?',
                'options': ['42', '"hello"', '(1, 2)', '[1, 2]'],
                'answer': 3,
                'explanation': 'Dictionary keys must be HASHABLE (immutable). Lists are mutable, so they cannot be dictionary keys. Integers, strings, and tuples are all hashable and valid keys.'
            },
            {
                'question': 'What is a "hash collision"?',
                'options': ['A bug in the hash function', 'Two different keys producing the same hash', 'An overfull dictionary', 'A deleted dictionary entry'],
                'answer': 1,
                'explanation': 'A hash collision occurs when two different keys produce the same hash value (same array index). Python handles this internally using techniques like open addressing.'
            },
            {
                'question': 'For the Two Sum problem, why is the hash map solution O(n) while brute force is O(n²)?',
                'options': ['Hash map stores more data', 'We only iterate through the list once, with O(1) lookups', 'Brute force makes too many comparisons', 'Both B and C'],
                'answer': 3,
                'explanation': 'Brute force checks every pair: O(n²). Hash map approach: one pass (O(n)) with O(1) lookup per element. We check if the complement exists in our map instead of looping again.'
            },
        ]
    },
    {
        'id': 9,
        'title': 'Graphs',
        'icon': '🕸️',
        'description': 'Explore graphs — the most versatile data structure for modeling connections and relationships.',
        'difficulty': 'Intermediate',
        'estimated_time': '60 min',
        'color': '#059669',
        'content': """
<h2>What is a Graph?</h2>
<p>A <strong>graph</strong> is a collection of <strong>nodes</strong> (vertices) connected by <strong>edges</strong>. Graphs model real-world relationships: roads, social networks, web pages, dependencies.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Unlike trees (which are a special kind of graph), general graphs can have cycles and nodes with many connections in any direction.</p>
</div>

<h3>Graph Terminology</h3>
<ul>
  <li><strong>Vertex / Node</strong> — a point in the graph (e.g., a city)</li>
  <li><strong>Edge</strong> — a connection between two nodes (e.g., a road)</li>
  <li><strong>Directed graph</strong> — edges have direction (A → B but not B → A)</li>
  <li><strong>Undirected graph</strong> — edges go both ways (A ↔ B)</li>
  <li><strong>Weighted graph</strong> — edges have a cost or distance</li>
  <li><strong>Adjacency</strong> — two nodes are adjacent if directly connected</li>
</ul>

<h3>Representing Graphs: Adjacency List</h3>
<p>The most common representation in Python is an <strong>adjacency list</strong> — a dictionary mapping each node to its neighbors.</p>
<pre><code class="language-python">
# Undirected graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

# Directed graph (one-way edges)
directed = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': [],
}
</code></pre>

<h3>Breadth-First Search (BFS)</h3>
<p>BFS explores the graph <strong>level by level</strong> — all neighbors before going deeper. Uses a <strong>queue</strong>.</p>
<pre><code class="language-python">
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()      # dequeue front
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

graph = {'A': ['B','C'], 'B': ['D','E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
</code></pre>

<h3>Depth-First Search (DFS)</h3>
<p>DFS explores as <strong>deep as possible</strong> before backtracking. Uses a <strong>stack</strong> (or recursion).</p>
<pre><code class="language-python">
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order += dfs(graph, neighbor, visited)

    return order

print(dfs(graph, 'A'))  # ['A', 'B', 'D', 'E', 'F', 'C']  (one possible order)
</code></pre>

<h3>BFS vs DFS</h3>
<table class="complexity-table">
  <tr><th>Property</th><th>BFS</th><th>DFS</th></tr>
  <tr><td>Data structure</td><td>Queue</td><td>Stack / Recursion</td></tr>
  <tr><td>Finds shortest path?</td><td>✅ Yes (unweighted)</td><td>❌ No</td></tr>
  <tr><td>Memory</td><td>O(V) — stores a level</td><td>O(V) — stores a path</td></tr>
  <tr><td>Time complexity</td><td>O(V + E)</td><td>O(V + E)</td></tr>
  <tr><td>Good for</td><td>Shortest path, level order</td><td>Cycle detection, topological sort</td></tr>
</table>

<h3>Detecting a Cycle (Undirected Graph)</h3>
<pre><code class="language-python">
def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # back edge = cycle
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
</code></pre>
""",
        'sandbox_default': '''# Try BFS on a sample graph
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}
print("BFS from A:", bfs(graph, 'A'))
''',
        'labs': [
            {
                'id': 1,
                'title': 'BFS Shortest Path',
                'description': 'Implement BFS to find the shortest path (in number of edges) between two nodes in an unweighted graph. Return the path as a list of nodes, or an empty list if no path exists.',
                'starter_code': '''from collections import deque

def shortest_path(graph, start, end):
    """
    Return the shortest path from start to end as a list of nodes.
    Return [] if no path exists.
    """
    # YOUR CODE HERE
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

print("Testing shortest_path:")
_test("A to F (2 hops via C)", shortest_path(g, 'A', 'F'), ['A', 'C', 'F'])
_test("A to D",                shortest_path(g, 'A', 'D'), ['A', 'B', 'D'])
_test("A to A (same node)",    shortest_path(g, 'A', 'A'), ['A'])
_test("D to F (no path)",      shortest_path(g, 'D', 'F'), [])
_test("B to F",                shortest_path(g, 'B', 'F'), ['B', 'E', 'F'])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Use a deque as your BFS queue. Start by adding (start, [start]) — the node AND the path so far.',
                    'When you dequeue a node, check if it equals end — if so, return the path.',
                    'For each unvisited neighbor, enqueue (neighbor, path + [neighbor]).',
                    'Track visited nodes in a set to avoid revisiting. Return [] if the queue empties without finding end.',
                    'Special case: if start == end, return [start] immediately.',
                ]
            },
            {
                'id': 2,
                'title': 'Number of Islands',
                'description': 'Given a 2D grid of "1"s (land) and "0"s (water), count the number of islands. An island is surrounded by water and formed by connecting adjacent land cells horizontally or vertically.',
                'starter_code': '''def num_islands(grid):
    """
    Count the number of islands in the grid.
    grid is a list of lists of "1" and "0" strings.
    """
    # YOUR CODE HERE
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

print("Testing num_islands:")
_test("1 large island + 1 isolated cell = 2 islands", num_islands([
    ["1","1","1"],
    ["1","1","0"],
    ["0","0","1"],
]), 2)

_test("3 separate islands", num_islands([
    ["1","0","1"],
    ["0","0","0"],
    ["1","0","1"],
]), 4)

_test("all water", num_islands([
    ["0","0"],
    ["0","0"],
]), 0)

_test("all land = 1 island", num_islands([
    ["1","1"],
    ["1","1"],
]), 1)

_test("classic 3-island", num_islands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
]), 3)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Think of each "1" cell as a graph node. Two adjacent "1"s share an edge.',
                    'Iterate through every cell. When you find a "1", increment your island count and do a DFS/BFS to mark the whole island as visited.',
                    'Marking as visited: change "1" to "0" in-place (or use a visited set of (row, col) tuples).',
                    'In DFS, check 4 directions: up, down, left, right. Make sure to check bounds (0 <= r < rows, 0 <= c < cols).',
                    'The key insight: one DFS from a land cell visits the entire connected island.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What data structure does BFS use internally?',
                'options': ['Stack', 'Queue', 'Heap', 'Linked List'],
                'answer': 1,
                'explanation': 'BFS uses a Queue (FIFO). This ensures nodes are processed level-by-level — all neighbors of the current level are visited before going deeper. A deque from collections is the standard Python choice.'
            },
            {
                'question': 'What is the time complexity of BFS/DFS on a graph with V vertices and E edges?',
                'options': ['O(V)', 'O(E)', 'O(V + E)', 'O(V × E)'],
                'answer': 2,
                'explanation': 'Both BFS and DFS are O(V + E) — we visit each vertex once and traverse each edge once. This makes them extremely efficient for graph traversal problems.'
            },
            {
                'question': 'Which traversal is guaranteed to find the shortest path in an unweighted graph?',
                'options': ['DFS', 'BFS', 'Both', 'Neither'],
                'answer': 1,
                'explanation': 'BFS explores nodes level by level, so the first time it reaches a target node, it has found the shortest path (fewest edges). DFS can find A path, but not necessarily the shortest one.'
            },
            {
                'question': 'In an adjacency list, what does graph["A"] = ["B", "C"] mean?',
                'options': ['A is between B and C', 'Node A has edges to nodes B and C', 'B and C are the same as A', 'A, B, C form a cycle'],
                'answer': 1,
                'explanation': 'An adjacency list maps each node to a list of its direct neighbors. graph["A"] = ["B", "C"] means node A has edges connecting it to B and C.'
            },
            {
                'question': 'Why must we track "visited" nodes in graph traversal?',
                'options': ['To count the nodes', 'To avoid infinite loops in graphs with cycles', 'To sort the results', 'To save memory'],
                'answer': 1,
                'explanation': 'Without a visited set, traversal on a graph with cycles would loop forever (A→B→A→B...). Marking nodes as visited ensures each node is processed exactly once, giving O(V+E) time.'
            },
        ]
    },
    {
        'id': 10,
        'title': 'Dynamic Programming',
        'icon': '⚡',
        'description': 'Master dynamic programming — the technique that turns exponential problems into efficient polynomial solutions.',
        'difficulty': 'Intermediate',
        'estimated_time': '75 min',
        'color': '#dc2626',
        'content': """
<h2>What is Dynamic Programming?</h2>
<p><strong>Dynamic Programming (DP)</strong> solves complex problems by breaking them into simpler overlapping subproblems and storing results to avoid redundant computation.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>"If we've already solved a subproblem, don't solve it again — look up the answer." This transforms exponential-time recursion into polynomial-time solutions.</p>
</div>

<h3>Two Conditions for DP</h3>
<ol>
  <li><strong>Optimal Substructure</strong> — the optimal solution is built from optimal solutions to subproblems</li>
  <li><strong>Overlapping Subproblems</strong> — the same subproblems recur many times</li>
</ol>

<h3>Approach 1: Memoization (Top-Down)</h3>
<p>Write the recursive solution, then cache results in a dictionary.</p>
<pre><code class="language-python">
# Fibonacci — naive recursion: O(2^n)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# With memoization: O(n)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Using Python's built-in cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))  # 12586269025  — instant!
</code></pre>

<h3>Approach 2: Tabulation (Bottom-Up)</h3>
<p>Build the solution iteratively from the smallest subproblems up. No recursion needed.</p>
<pre><code class="language-python">
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib_tab(10))  # 55

# Space-optimized: only need last 2 values
def fib_opt(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
</code></pre>

<h3>Classic Problem: Coin Change</h3>
<p>Given coins of certain denominations, find the minimum number of coins to make amount.</p>
<pre><code class="language-python">
def coin_change(coins, amount):
    # dp[i] = min coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # base case: 0 coins to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 5, 6, 9], 11))  # 2  (coins: 5+6)
print(coin_change([2], 3))            # -1 (impossible)
</code></pre>

<h3>Classic Problem: 0/1 Knapsack</h3>
<pre><code class="language-python">
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = max value using first i items, capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            # Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity]

weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
print(knapsack(weights, values, 8))  # 10  (items with weight 3+5=8 and value 4+6=10)
</code></pre>

<h3>DP Complexity Summary</h3>
<table class="complexity-table">
  <tr><th>Problem</th><th>Time</th><th>Space</th></tr>
  <tr><td>Fibonacci (naive)</td><td>O(2ⁿ)</td><td>O(n)</td></tr>
  <tr><td>Fibonacci (DP)</td><td>O(n)</td><td>O(n) or O(1)</td></tr>
  <tr><td>Coin Change</td><td>O(amount × coins)</td><td>O(amount)</td></tr>
  <tr><td>0/1 Knapsack</td><td>O(n × capacity)</td><td>O(n × capacity)</td></tr>
  <tr><td>Longest Common Subsequence</td><td>O(m × n)</td><td>O(m × n)</td></tr>
</table>
""",
        'sandbox_default': '''# Dynamic Programming: Fibonacci
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(f"fib({i}) = {fib(i)}")

# Coin change
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

print("\\nCoin change [1,5,6,9] -> 11:", coin_change([1,5,6,9], 11))
''',
        'labs': [
            {
                'id': 1,
                'title': 'Climbing Stairs',
                'description': 'You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.',
                'starter_code': '''def climb_stairs(n):
    """
    Return the number of distinct ways to climb n stairs
    (each move is 1 or 2 steps).
    """
    # YOUR CODE HERE
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

print("Testing climb_stairs:")
_test("n=1  -> 1",  climb_stairs(1),  1)
_test("n=2  -> 2",  climb_stairs(2),  2)
_test("n=3  -> 3",  climb_stairs(3),  3)
_test("n=4  -> 5",  climb_stairs(4),  5)
_test("n=5  -> 8",  climb_stairs(5),  8)
_test("n=10 -> 89", climb_stairs(10), 89)
_test("n=20 -> 10946", climb_stairs(20), 10946)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Notice the pattern: ways(n) = ways(n-1) + ways(n-2). To reach step n, you came from step n-1 (1 step) or step n-2 (2 steps).',
                    'Base cases: ways(1) = 1, ways(2) = 2.',
                    'This is identical to Fibonacci! Build a dp array of size n+1.',
                    'Or use two variables (a, b) to save space — O(1) space solution.',
                    'Start with dp[1]=1, dp[2]=2 and fill dp[i] = dp[i-1] + dp[i-2] for i in range(3, n+1).',
                ]
            },
            {
                'id': 2,
                'title': 'Longest Common Subsequence',
                'description': 'Given two strings, return the length of their Longest Common Subsequence (LCS). A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.',
                'starter_code': '''def lcs(text1, text2):
    """
    Return the length of the longest common subsequence of text1 and text2.
    Example: lcs("abcde", "ace") == 3  (the LCS is "ace")
    """
    # YOUR CODE HERE
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

print("Testing lcs:")
_test('"abcde","ace" -> 3',   lcs("abcde", "ace"),     3)
_test('"abc","abc" -> 3',     lcs("abc", "abc"),        3)
_test('"abc","def" -> 0',     lcs("abc", "def"),        0)
_test('"bl","yby" -> 1',      lcs("bl", "yby"),         1)
_test('"oxcpqrsvwf","shmtulqrypy" -> 2', lcs("oxcpqrsvwf","shmtulqrypy"), 2)
_test('"","abc" -> 0',        lcs("", "abc"),           0)
_test('"abc","" -> 0',        lcs("abc", ""),           0)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Create a 2D dp table: dp[i][j] = LCS length of text1[:i] and text2[:j].',
                    'If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1  (extend the LCS by 1).',
                    'Otherwise: dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (best without one of the chars).',
                    'Initialize a (len(text1)+1) × (len(text2)+1) table of zeros.',
                    'Answer is dp[len(text1)][len(text2)].',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What are the two key properties a problem must have for Dynamic Programming to apply?',
                'options': ['Sorted input and unique elements', 'Optimal substructure and overlapping subproblems', 'Linear time and constant space', 'Recursion and iteration'],
                'answer': 1,
                'explanation': 'DP requires: (1) Optimal Substructure — the optimal solution uses optimal solutions to subproblems; (2) Overlapping Subproblems — the same subproblems are solved multiple times. Both must hold for DP to be applicable.'
            },
            {
                'question': 'What is the difference between memoization and tabulation?',
                'options': ['They are the same thing', 'Memoization is top-down (recursive + cache); tabulation is bottom-up (iterative)', 'Memoization is faster; tabulation uses less memory', 'Tabulation is recursive; memoization is iterative'],
                'answer': 1,
                'explanation': 'Memoization (top-down): write the natural recursion, cache results. Tabulation (bottom-up): build a table iteratively from base cases up. Both achieve the same time complexity, but tabulation avoids recursion stack overhead.'
            },
            {
                'question': 'What is the time complexity of computing Fibonacci(n) with memoization?',
                'options': ['O(2ⁿ)', 'O(n²)', 'O(n)', 'O(log n)'],
                'answer': 2,
                'explanation': 'With memoization, each unique subproblem (fib(0) through fib(n)) is solved exactly once. There are n+1 subproblems each taking O(1), giving O(n) total. Without memoization, naive recursion is O(2ⁿ).'
            },
            {
                'question': 'In the Coin Change problem with dp[i] = min coins for amount i, what is the recurrence?',
                'options': ['dp[i] = dp[i-1] + 1', 'dp[i] = min(dp[i - coin] + 1) for each valid coin', 'dp[i] = dp[i//2] + 1', 'dp[i] = dp[i-1] + dp[i-2]'],
                'answer': 1,
                'explanation': 'For each amount i, we try every coin denomination. If we use a coin of value c, we need dp[i-c] coins for the remaining amount, plus 1. We take the minimum across all valid coins: dp[i] = min(dp[i-c]+1 for c in coins if c<=i).'
            },
            {
                'question': 'Why is the climbing stairs problem equivalent to Fibonacci?',
                'options': ['Both involve steps', 'To reach step n, you came from n-1 or n-2 — so ways(n) = ways(n-1) + ways(n-2)', 'Both have O(n) complexity', 'Both use recursion'],
                'answer': 1,
                'explanation': 'To stand on step n, your last move was either 1 step (from n-1) or 2 steps (from n-2). So the number of ways = ways(n-1) + ways(n-2) — exactly the Fibonacci recurrence. This is the classic DP insight: identify the recurrence relation.'
            },
        ]
    },
    # ── EXPERT MODULES ──────────────────────────────────────────────────────────
    # Sources: NeetCode Roadmap (neetcode.io/roadmap), GeeksforGeeks DSA
    # (geeksforgeeks.org/dsa), LeetCode Interview Crash Course
    # (leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms)
    {
        'id': 11,
        'title': 'Heaps & Priority Queues',
        'icon': '🏔️',
        'description': 'Master heaps — the data structure that gives you the min or max element in O(1) and is the backbone of scheduling, Dijkstra, and Top-K problems.',
        'difficulty': 'Expert',
        'estimated_time': '60 min',
        'color': '#7c3aed',
        'content': """
<h2>What is a Heap?</h2>
<p>A <strong>heap</strong> is a complete binary tree that satisfies the <strong>heap property</strong>:</p>
<ul>
  <li><strong>Min-Heap:</strong> every parent ≤ its children → the root holds the <em>minimum</em> element.</li>
  <li><strong>Max-Heap:</strong> every parent ≥ its children → the root holds the <em>maximum</em> element.</li>
</ul>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>A heap is NOT fully sorted — it only guarantees the root is the min/max. This relaxed property is what makes insert and extract each O(log n) while keeping peek O(1).</p>
</div>

<h3>Python's heapq Module</h3>
<p>Python's <code>heapq</code> is a <strong>min-heap</strong> built on a plain list. Use negation for max-heap behavior.</p>
<pre><code class="language-python">
import heapq

# Min-heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 8)
heapq.heappush(heap, 3)

print(heap[0])              # 1  — peek min (O(1))
print(heapq.heappop(heap))  # 1  — extract min (O(log n))
print(heap[0])              # 3  — new min

# Build heap from existing list (O(n) — more efficient than n pushes)
nums = [5, 1, 8, 3, 2]
heapq.heapify(nums)
print(nums[0])              # 1

# Max-heap: negate values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -8)
print(-max_heap[0])         # 8  — peek max
print(-heapq.heappop(max_heap))  # 8  — extract max
</code></pre>

<h3>Heap Complexity</h3>
<table class="complexity-table">
  <tr><th>Operation</th><th>Time</th><th>Notes</th></tr>
  <tr><td>Peek min/max</td><td>O(1)</td><td>Just read root</td></tr>
  <tr><td>Push (insert)</td><td>O(log n)</td><td>Sift up</td></tr>
  <tr><td>Pop (extract min/max)</td><td>O(log n)</td><td>Sift down</td></tr>
  <tr><td>Heapify (build from list)</td><td>O(n)</td><td>Better than n pushes</td></tr>
  <tr><td>Search</td><td>O(n)</td><td>No ordering guarantee</td></tr>
</table>

<h3>Classic Pattern: Top-K Elements</h3>
<p>Find the K largest elements in O(n log K) — much faster than sorting O(n log n) when K is small.</p>
<pre><code class="language-python">
import heapq

def top_k_largest(nums, k):
    # Keep a min-heap of size k
    # The root of this heap is the k-th largest
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest
    return sorted(heap, reverse=True)

print(top_k_largest([3, 1, 5, 12, 2, 11], 3))  # [12, 11, 5]

# Python shortcut:
print(heapq.nlargest(3, [3, 1, 5, 12, 2, 11]))  # [12, 11, 5]
</code></pre>

<h3>Classic Pattern: Merge K Sorted Lists</h3>
<pre><code class="language-python">
import heapq

def merge_k_sorted(lists):
    result = []
    # Push (value, list_index, element_index) for each list's first element
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_i, elem_i = heapq.heappop(heap)
        result.append(val)
        if elem_i + 1 < len(lists[list_i]):
            next_val = lists[list_i][elem_i + 1]
            heapq.heappush(heap, (next_val, list_i, elem_i + 1))

    return result

lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(merge_k_sorted(lists))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
</code></pre>

<h3>When to Use a Heap</h3>
<ul>
  <li>Repeatedly need the min or max of a changing dataset</li>
  <li>Top-K / K-th largest or smallest problems</li>
  <li>Merge K sorted arrays/lists</li>
  <li>Scheduling and task prioritization</li>
  <li>Dijkstra's shortest path (internally uses a min-heap)</li>
  <li>Median of a data stream (two heaps trick)</li>
</ul>
""",
        'sandbox_default': '''import heapq

# Min-heap demo
heap = [5, 1, 8, 3, 2, 7]
heapq.heapify(heap)
print("Min-heap:", heap)
print("Pop in order:", [heapq.heappop(heap) for _ in range(len(heap))])

# Top-3 largest
nums = [10, 4, 7, 2, 15, 9, 3]
print("\\nTop 3 largest:", heapq.nlargest(3, nums))
print("Top 3 smallest:", heapq.nsmallest(3, nums))
''',
        'labs': [
            {
                'id': 1,
                'title': 'K-th Largest Element',
                'description': 'Find the k-th largest element in an unsorted array. You must solve it in O(n log k) time using a heap — do not sort the entire array.',
                'starter_code': '''import heapq

def find_kth_largest(nums, k):
    """
    Return the k-th largest element in nums.
    Example: find_kth_largest([3,2,1,5,6,4], 2) == 5
    Constraint: O(n log k) time using a heap.
    """
    # YOUR CODE HERE
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

print("Testing find_kth_largest:")
_test("[3,2,1,5,6,4] k=2 -> 5",   find_kth_largest([3,2,1,5,6,4], 2),   5)
_test("[3,2,3,1,2,4,5,5,6] k=4 -> 4", find_kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)
_test("[1] k=1 -> 1",              find_kth_largest([1], 1),             1)
_test("[7,6,5,4,3] k=1 -> 7",     find_kth_largest([7,6,5,4,3], 1),     7)
_test("[7,6,5,4,3] k=5 -> 3",     find_kth_largest([7,6,5,4,3], 5),     3)
_test("[1,2] k=2 -> 1",           find_kth_largest([1,2], 2),           1)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Maintain a min-heap of size exactly k. The root will be the k-th largest.',
                    'For each number in nums: push it onto the heap. If heap size > k, pop the minimum.',
                    'After processing all numbers, heap[0] is the k-th largest.',
                    'Why does this work? The heap keeps the k largest elements seen so far, and the smallest of those k is at the root.',
                ]
            },
            {
                'id': 2,
                'title': 'Median of Data Stream',
                'description': 'Design a class that supports adding numbers one at a time and finding the median at any point. Use the two-heaps technique to achieve O(log n) add and O(1) find_median.',
                'starter_code': '''import heapq

class MedianFinder:
    """
    Use two heaps:
    - max_heap (lower half) — store negated values for Python's min-heap
    - min_heap (upper half)
    Invariant: max_heap size == min_heap size OR max_heap size == min_heap size + 1
    """

    def __init__(self):
        # YOUR CODE HERE
        pass

    def add_num(self, num):
        """Add num to the data structure."""
        # YOUR CODE HERE
        pass

    def find_median(self):
        """Return the median of all numbers added so far."""
        # YOUR CODE HERE
        pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if abs(got - expected) < 1e-9:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

print("Testing MedianFinder:")
mf = MedianFinder()
mf.add_num(1)
_test("after [1]",        mf.find_median(), 1.0)
mf.add_num(2)
_test("after [1,2]",      mf.find_median(), 1.5)
mf.add_num(3)
_test("after [1,2,3]",    mf.find_median(), 2.0)
mf.add_num(4)
_test("after [1,2,3,4]",  mf.find_median(), 2.5)
mf.add_num(5)
_test("after [1,2,3,4,5]",mf.find_median(), 3.0)

mf2 = MedianFinder()
mf2.add_num(6)
mf2.add_num(2)
mf2.add_num(9)
_test("after [6,2,9]",    mf2.find_median(), 6.0)
mf2.add_num(1)
_test("after [6,2,9,1]",  mf2.find_median(), 4.0)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Use two heaps: a max-heap for the lower half and a min-heap for the upper half.',
                    'Python has only min-heap, so simulate max-heap by storing negated values.',
                    'Invariant: keep the heaps balanced so max_heap has at most 1 extra element.',
                    'add_num: push to max_heap first. Then if max_heap top > min_heap top, rebalance. Then balance sizes.',
                    'find_median: if sizes are equal, average the two tops. Otherwise return max_heap top (it has the extra element).',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What is the time complexity of extracting the minimum from a min-heap?',
                'options': ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)'],
                'answer': 1,
                'explanation': 'Extracting the min (heappop) is O(log n). The minimum is at the root (O(1) to find), but after removal we must restore the heap property by "sifting down" the replacement element, which takes O(log n) — one swap per level of the tree.'
            },
            {
                'question': 'How do you simulate a max-heap using Python\'s heapq module?',
                'options': ['Use heapq.max()', 'Call heapq.heapify in reverse', 'Store negated values (-x instead of x)', 'Sort the list first'],
                'answer': 2,
                'explanation': 'Python\'s heapq only provides a min-heap. To simulate a max-heap, store -x instead of x. The smallest negative value corresponds to the largest original value. When you pop, negate the result: -heapq.heappop(heap).'
            },
            {
                'question': 'What is the time complexity of building a heap from an existing list of n elements using heapify?',
                'options': ['O(n log n)', 'O(n)', 'O(log n)', 'O(n²)'],
                'answer': 1,
                'explanation': 'heapify is O(n) — counter-intuitively faster than pushing n elements one by one (which is O(n log n)). Most elements are near the bottom of the tree and require very few swaps, so the total work sums to O(n).'
            },
            {
                'question': 'You need the 5 largest elements from a list of 1,000,000 numbers. Which approach is most efficient?',
                'options': ['Sort the list and take the last 5: O(n log n)', 'Use a min-heap of size 5: O(n log 5) ≈ O(n)', 'Linear scan keeping 5 maximums: O(n)', 'Both B and C are equally optimal'],
                'answer': 1,
                'explanation': 'A size-k min-heap is the right tool here. It runs in O(n log k) — effectively O(n) when k is fixed and small — and scales cleanly to any k. A manual linear scan is also O(n) for fixed k, but it is tedious to implement correctly for arbitrary k and does not generalise. Python\'s heapq.nlargest uses exactly this heap approach. Sorting the entire list is O(n log n) and wastes work when you only need the top few elements.'
            },
            {
                'question': 'In the "median of a data stream" problem, why are TWO heaps used instead of one?',
                'options': ['For redundancy', 'A max-heap holds the lower half and a min-heap holds the upper half — their tops give the median in O(1)', 'To reduce memory usage', 'Heaps cannot store duplicate values'],
                'answer': 1,
                'explanation': 'One heap can give you the min or max in O(1), but not the median. By keeping a max-heap of the lower half and a min-heap of the upper half (sizes balanced), the median is always at one or both tops — O(1) access with O(log n) insertions.'
            },
        ]
    },
    {
        'id': 12,
        'title': 'Tries',
        'icon': '🌳',
        'description': 'Explore Tries (prefix trees) — the data structure powering autocomplete, spell-checkers, and IP routing with blazing-fast prefix lookups.',
        'difficulty': 'Expert',
        'estimated_time': '55 min',
        'color': '#b45309',
        'content': """
<h2>What is a Trie?</h2>
<p>A <strong>Trie</strong> (pronounced "try", from re<em>trie</em>val) is a tree where each node represents a single character. Paths from the root to marked nodes spell out complete words.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Words with a common prefix share nodes in the tree. "cat", "car", and "card" all share the path c → a. This makes prefix searching O(L) where L is the word length — independent of how many words are stored.</p>
</div>

<h3>Trie Structure</h3>
<pre><code class="language-python">
class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.is_end = False  # True if this node ends a word
</code></pre>

<h3>Building a Trie</h3>
<pre><code class="language-python">
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        # Returns True if word exists in the trie.
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        # Returns True if any word starts with prefix.
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

trie = Trie()
for word in ["apple", "app", "apt", "bat"]:
    trie.insert(word)

print(trie.search("app"))        # True
print(trie.search("ap"))         # False (no end marker)
print(trie.starts_with("ap"))    # True
print(trie.starts_with("ba"))    # True
print(trie.starts_with("cat"))   # False
</code></pre>

<h3>Trie Complexity</h3>
<table class="complexity-table">
  <tr><th>Operation</th><th>Time</th><th>Space</th></tr>
  <tr><td>Insert word of length L</td><td>O(L)</td><td>O(L) worst case</td></tr>
  <tr><td>Search word of length L</td><td>O(L)</td><td>O(1)</td></tr>
  <tr><td>Prefix check (starts_with)</td><td>O(L)</td><td>O(1)</td></tr>
  <tr><td>Total space (n words, avg L)</td><td>—</td><td>O(n × L)</td></tr>
</table>

<h3>Autocomplete with Trie</h3>
<pre><code class="language-python">
def autocomplete(trie, prefix):
    # Return all words in trie that start with prefix.
    node = trie.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]

    # DFS from the prefix node to collect all complete words
    results = []
    def dfs(node, current):
        if node.is_end:
            results.append(current)
        for char, child in node.children.items():
            dfs(child, current + char)

    dfs(node, prefix)
    return results
</code></pre>

<h3>When to Use a Trie</h3>
<ul>
  <li>Autocomplete / type-ahead search</li>
  <li>Spell-checking</li>
  <li>IP routing (longest prefix match)</li>
  <li>Word games (Boggle, Scrabble)</li>
  <li>Count words with a given prefix</li>
  <li>Word search in a grid (faster than brute-force)</li>
</ul>

<h3>Trie vs Hash Map</h3>
<table class="complexity-table">
  <tr><th>Feature</th><th>Trie</th><th>Hash Map</th></tr>
  <tr><td>Exact word lookup</td><td>O(L)</td><td>O(L) average</td></tr>
  <tr><td>Prefix search</td><td>O(L)</td><td>O(n×L) — must scan all</td></tr>
  <tr><td>Autocomplete</td><td>O(L + results)</td><td>O(n×L)</td></tr>
  <tr><td>Sorted iteration</td><td>Natural (DFS)</td><td>Requires sorting</td></tr>
</table>
""",
        'sandbox_default': '''class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

trie = Trie()
words = ["apple", "app", "apt", "bat", "ball", "ban"]
for w in words: trie.insert(w)

print("search(\'app\'):", trie.search("app"))
print("search(\'ap\'):", trie.search("ap"))
print("starts_with(\'ba\'):", trie.starts_with("ba"))
print("starts_with(\'cat\'):", trie.starts_with("cat"))
''',
        'labs': [
            {
                'id': 1,
                'title': 'Build a Trie',
                'description': 'Implement a Trie with insert, search, and starts_with operations.',
                'starter_code': '''class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert word into the trie."""
        # YOUR CODE HERE
        pass

    def search(self, word):
        """Return True if word is in the trie (exact match)."""
        # YOUR CODE HERE
        pass

    def starts_with(self, prefix):
        """Return True if any inserted word starts with prefix."""
        # YOUR CODE HERE
        pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

t = Trie()
for w in ["apple", "app", "apt", "bat", "ball"]:
    t.insert(w)

print("Testing search:")
_test("search apple -> True",   t.search("apple"), True)
_test("search app   -> True",   t.search("app"),   True)
_test("search ap    -> False",  t.search("ap"),    False)
_test("search bat   -> True",   t.search("bat"),   True)
_test("search ba    -> False",  t.search("ba"),    False)
_test("search cat   -> False",  t.search("cat"),   False)

print("\\nTesting starts_with:")
_test("starts_with ap  -> True",  t.starts_with("ap"),  True)
_test("starts_with ba  -> True",  t.starts_with("ba"),  True)
_test("starts_with bal -> True",  t.starts_with("bal"), True)
_test("starts_with cat -> False", t.starts_with("cat"), False)
_test("starts_with b   -> True",  t.starts_with("b"),   True)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'For insert: traverse from root, creating TrieNode children as needed, then mark node.is_end = True at the last character.',
                    'For search: traverse from root following each character. If any character is missing, return False. At the end check node.is_end.',
                    'For starts_with: same as search but do NOT check is_end — just return True if you reach the end of the prefix without missing a character.',
                    'The difference between search and starts_with is only the final check: search needs is_end=True, starts_with just needs to survive the traversal.',
                ]
            },
            {
                'id': 2,
                'title': 'Word Search in a Grid',
                'description': 'Given a 2D board of characters and a list of words, return all words that exist in the board. A word can be constructed from sequentially adjacent cells (horizontal or vertical). The same cell may not be used more than once per word.',
                'starter_code': '''class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store complete word at end node

def find_words(board, words):
    """
    Return a list of all words from `words` that exist in the board.
    Use a Trie + DFS for efficiency.
    """
    # Build trie from word list
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = w  # Mark end of word

    rows, cols = len(board), len(board[0])
    found = []

    def dfs(node, r, c):
        # YOUR CODE HERE
        pass

    for r in range(rows):
        for c in range(cols):
            if board[r][c] in root.children:
                dfs(root.children[board[r][c]], r, c)

    return found
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    got_s = sorted(got)
    exp_s = sorted(expected)
    if got_s == exp_s:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got_s!r}  expected={exp_s!r}")
        _fail += 1

_pass = _fail = 0

board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain"]
_test("board1 classic", find_words(board1, words1), ["oath", "eat"])

board2 = [["a","b"],["c","d"]]
_test("board2 no match", find_words(board2, ["abdc"]), ["abdc"])
_test("board2 no match2", find_words(board2, ["abcd"]), [])

board3 = [["a"]]
_test("1x1 board found",    find_words(board3, ["a"]), ["a"])
_test("1x1 board not found", find_words(board3, ["b"]), [])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Build a trie from all the target words first. Then DFS from every board cell.',
                    'In the DFS: check if the current board character exists in the current trie node\'s children. If not, stop.',
                    'Mark the current cell as visited by temporarily replacing board[r][c] with "#". Restore it after DFS.',
                    'When node.word is not None, you\'ve found a complete word — add to found and set node.word = None to avoid duplicates.',
                    'Explore 4 directions: (r-1,c), (r+1,c), (r,c-1), (r,c+1). Check bounds before recursing.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What is the time complexity of searching for a word of length L in a Trie?',
                'options': ['O(n) where n is number of words', 'O(L)', 'O(L × n)', 'O(log n)'],
                'answer': 1,
                'explanation': 'Trie search is O(L) where L is the length of the word — completely independent of how many words are stored. You follow exactly L edges from root to the target node. This is what makes Tries superior to hash maps for prefix-based operations.'
            },
            {
                'question': 'In a Trie, what is the difference between search("app") and starts_with("app")?',
                'options': ['No difference', 'search checks is_end at the last node; starts_with only checks the path exists', 'starts_with is faster', 'search only works for single characters'],
                'answer': 1,
                'explanation': 'Both traverse the same path. The difference is at the end: search requires the last node to have is_end=True (the exact word "app" was inserted). starts_with just requires the path to exist — any word starting with "app" would satisfy it.'
            },
            {
                'question': 'Why is a Trie better than a Hash Map for autocomplete?',
                'options': ['Tries use less memory', 'Tries can find all words with a given prefix in O(L + results) vs O(n×L) for hash maps', 'Hash maps cannot store strings', 'Tries have O(1) lookups'],
                'answer': 1,
                'explanation': 'With a hash map, finding all words matching a prefix requires checking every stored word — O(n×L). A trie lets you navigate to the prefix node in O(L), then DFS to collect all matching words. This is why autocomplete systems (search engines, IDEs) use tries.'
            },
            {
                'question': 'What does node.children store in a typical Trie implementation?',
                'options': ['A list of all possible characters', 'A mapping from character to child TrieNode', 'The full words stored in the trie', 'An integer count of children'],
                'answer': 1,
                'explanation': 'Each TrieNode has a dictionary (or array of size 26 for lowercase letters) mapping each character to its child TrieNode. This allows O(1) lookup of the next node for a given character.'
            },
            {
                'question': 'In the Word Search in a Grid problem, why is a Trie used instead of checking each word separately?',
                'options': ['Tries are always faster', 'Multiple words share prefixes in the Trie — one DFS path can match many words simultaneously', 'The grid must be sorted first', 'Tries reduce memory usage'],
                'answer': 1,
                'explanation': 'Without a trie, you\'d DFS from every cell for every word: O(words × cells × 4^L). With a trie, one DFS from a cell explores all words simultaneously by following the trie. When a branch doesn\'t match any word\'s prefix, the DFS prunes immediately.'
            },
        ]
    },
    {
        'id': 13,
        'title': 'Backtracking',
        'icon': '🔙',
        'description': 'Master backtracking — the systematic technique for exploring all possibilities by building candidates incrementally and abandoning paths that cannot lead to a solution.',
        'difficulty': 'Expert',
        'estimated_time': '65 min',
        'color': '#be123c',
        'content': """
<h2>What is Backtracking?</h2>
<p><strong>Backtracking</strong> is a refined brute-force technique. It builds solutions incrementally and <strong>abandons ("backtracks")</strong> a path as soon as it determines the path cannot possibly lead to a valid solution.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Think of it as exploring a decision tree: at each step you make a choice, recurse deeper, then <em>undo</em> that choice ("backtrack") before trying the next option. This "try → recurse → undo" pattern is the backbone of backtracking.</p>
</div>

<h3>The Backtracking Template</h3>
<pre><code class="language-python">
def backtrack(current_state, choices):
    # Base case: solution is complete
    if is_solution(current_state):
        record_solution(current_state)
        return

    for choice in choices:
        if is_valid(choice, current_state):   # pruning
            make_choice(current_state, choice)
            backtrack(current_state, next_choices)
            undo_choice(current_state, choice)  # ← the "backtrack" step
</code></pre>

<h3>Example: Generate All Permutations</h3>
<pre><code class="language-python">
def permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:           # base case: used all numbers
            result.append(current[:])
            return
        for i, num in enumerate(remaining):
            current.append(num)                          # choose
            backtrack(current, remaining[:i] + remaining[i+1:])  # explore
            current.pop()                                # undo

    backtrack([], nums)
    return result

print(permutations([1, 2, 3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</code></pre>

<h3>Example: Subsets (Power Set)</h3>
<pre><code class="language-python">
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])   # every partial state is a valid subset
        for i in range(start, len(nums)):
            current.append(nums[i])     # choose
            backtrack(i + 1, current)   # explore (only forward → no duplicates)
            current.pop()               # undo

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
</code></pre>

<h3>Example: N-Queens Problem</h3>
<pre><code class="language-python">
def solve_n_queens(n):
    result = []
    queens = []   # queens[row] = col of queen in that row

    def is_safe(row, col):
        for r, c in enumerate(queens):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row):
        if row == n:
            # Build board representation
            board = [['.' * c + 'Q' + '.' * (n - c - 1)] for c in queens]
            result.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(row, col):
                queens.append(col)    # choose
                backtrack(row + 1)    # explore
                queens.pop()          # undo

    backtrack(0)
    return result
</code></pre>

<h3>Backtracking Complexity</h3>
<table class="complexity-table">
  <tr><th>Problem</th><th>Time Complexity</th><th>Notes</th></tr>
  <tr><td>Permutations (n items)</td><td>O(n × n!)</td><td>n! permutations, each length n</td></tr>
  <tr><td>Subsets (n items)</td><td>O(n × 2ⁿ)</td><td>2ⁿ subsets, each up to length n</td></tr>
  <tr><td>N-Queens (n×n board)</td><td>O(n!)</td><td>With pruning, much less in practice</td></tr>
  <tr><td>Sudoku (9×9)</td><td>O(9^81) worst</td><td>Pruning makes it fast in practice</td></tr>
</table>

<h3>Pruning — The Key to Efficiency</h3>
<p>Backtracking is only efficient when paired with strong <strong>pruning</strong> (early termination). Always ask: "Can this partial solution possibly become valid?" If not, stop immediately.</p>
<pre><code class="language-python">
# Combination Sum — prune when remaining goes below 0
def combination_sum(candidates, target):
    result = []
    candidates.sort()  # Sort to enable early termination

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:  # ← pruning: no point going further
                break
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result
</code></pre>
""",
        'sandbox_default': '''def permutations(nums):
    result = []
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        for i, num in enumerate(remaining):
            current.append(num)
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()
    backtrack([], nums)
    return result

def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result

print("Permutations of [1,2,3]:")
for p in permutations([1, 2, 3]):
    print(" ", p)

print("\\nSubsets of [1,2,3]:")
for s in subsets([1, 2, 3]):
    print(" ", s)
''',
        'labs': [
            {
                'id': 1,
                'title': 'Combination Sum',
                'description': 'Given a list of distinct integers (candidates) and a target integer, return all unique combinations where the chosen numbers sum to target. The same number may be used unlimited times. Return combinations in any order.',
                'starter_code': '''def combination_sum(candidates, target):
    """
    Return all unique combinations of candidates that sum to target.
    Each candidate may be used any number of times.
    Example: combination_sum([2,3,6,7], 7) -> [[2,2,3],[7]]
    """
    # YOUR CODE HERE
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    got_s  = sorted(tuple(sorted(x)) for x in got)
    exp_s  = sorted(tuple(sorted(x)) for x in expected)
    if got_s == exp_s:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}")
        print(f"    got:      {got_s}")
        print(f"    expected: {exp_s}")
        _fail += 1

_pass = _fail = 0

print("Testing combination_sum:")
_test("[2,3,6,7] target=7",  combination_sum([2,3,6,7], 7),   [[2,2,3],[7]])
_test("[2,3,5] target=8",    combination_sum([2,3,5], 8),      [[2,2,2,2],[2,3,3],[3,5]])
_test("[2] target=1",        combination_sum([2], 1),           [])
_test("[1] target=1",        combination_sum([1], 1),           [[1]])
_test("[1] target=2",        combination_sum([1], 2),           [[1,1]])

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Sort candidates first — this lets you prune early when candidates[i] > remaining.',
                    'Define backtrack(start, current, remaining). start prevents re-using earlier elements, current builds the combination, remaining tracks what\'s left to sum.',
                    'Base case: remaining == 0 → add current[:] to results.',
                    'For each candidate from start onward: if candidate > remaining, break (no point continuing). Otherwise append, recurse with same start index (reuse allowed), then pop.',
                    'The key difference from permutations: use i (not i+1) in the recursive call to allow reuse of the same element.',
                ]
            },
            {
                'id': 2,
                'title': 'Sudoku Solver',
                'description': 'Write a backtracking solver for a 9×9 Sudoku puzzle. The board is given as a list of lists where "." represents empty cells. Fill in the empty cells so every row, column, and 3×3 box contains 1-9 with no repeats. Modify the board in-place.',
                'starter_code': '''def solve_sudoku(board):
    """
    Solve the Sudoku puzzle by modifying board in-place.
    "." represents an empty cell. Returns True if solved, False otherwise.
    """
    def is_valid(row, col, num):
        # Check row, column, and 3x3 box
        # YOUR CODE HERE
        pass

    def backtrack():
        # Find next empty cell, try digits 1-9
        # YOUR CODE HERE
        pass

    backtrack()
    return board
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}")
        for i, (gr, er) in enumerate(zip(got, expected)):
            if gr != er:
                print(f"    row {i}: got {gr}")
                print(f"           exp {er}")
        _fail += 1

_pass = _fail = 0

board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
expected1 = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
result1 = solve_sudoku(board1)
_test("Classic Sudoku puzzle", result1, expected1)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'is_valid(row, col, num): check that num doesn\'t appear in the same row, same column, or same 3×3 box. Box top-left: (row//3*3, col//3*3).',
                    'backtrack(): iterate over all cells. When you find board[r][c] == ".", try digits "1" through "9".',
                    'For each valid digit: set board[r][c] = digit, recurse. If recursion succeeds (returns True), return True.',
                    'If no digit works for this cell, set board[r][c] = "." again (backtrack) and return False.',
                    'Base case: if no empty cell is found, the puzzle is solved — return True.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'What is the essential "backtrack" step in a backtracking algorithm?',
                'options': ['Return False when no solution exists', 'Undo the last choice before trying the next option', 'Sort the input before processing', 'Use a queue instead of recursion'],
                'answer': 1,
                'explanation': 'Backtracking follows a "try → recurse → undo" pattern. After exploring a path and returning from recursion, you must undo the last choice (e.g., pop the last element) to restore the state before trying the next option. Without this step, state leaks between branches.'
            },
            {
                'question': 'What is "pruning" in the context of backtracking?',
                'options': ['Sorting the input', 'Removing elements from the result', 'Stopping exploration of a branch early when it cannot lead to a valid solution', 'Using dynamic programming to cache results'],
                'answer': 2,
                'explanation': 'Pruning is the key optimization in backtracking. If you can determine early that the current partial solution cannot possibly lead to a valid answer, you abandon (prune) that branch immediately. Example: in Combination Sum, if candidates[i] > remaining, no larger candidate can help, so you break early.'
            },
            {
                'question': 'How many total permutations are there for a list of 4 distinct elements?',
                'options': ['4', '8', '16', '24'],
                'answer': 3,
                'explanation': 'The number of permutations of n distinct elements is n! (n factorial). For n=4: 4! = 4×3×2×1 = 24. This is also the worst-case number of leaf nodes in the backtracking decision tree for permutations.'
            },
            {
                'question': 'In the subsets problem, how many subsets does a set of n elements have?',
                'options': ['n', 'n²', '2ⁿ', 'n!'],
                'answer': 2,
                'explanation': 'A set of n elements has 2ⁿ subsets (the power set). For each element, you independently decide to include it or not — 2 choices, n times, giving 2ⁿ combinations. For n=3: 2³=8 subsets: [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].'
            },
            {
                'question': 'Backtracking is most appropriate when:',
                'options': ['The problem has optimal substructure (use DP instead)', 'You need to explore all possible combinations/arrangements with constraints', 'The input is sorted', 'You need O(n) time complexity'],
                'answer': 1,
                'explanation': 'Backtracking shines when you must explore all possible candidates (permutations, subsets, combinations) or find any valid configuration (N-Queens, Sudoku). If subproblems overlap and you only need the optimal value (not all solutions), Dynamic Programming is usually better.'
            },
        ]
    },
    {
        'id': 14,
        'title': 'Advanced Graph Algorithms',
        'icon': '🗺️',
        'description': 'Level up with Dijkstra\'s shortest path, topological sort, and Union-Find — the algorithms behind GPS navigation, build systems, and network connectivity.',
        'difficulty': 'Expert',
        'estimated_time': '75 min',
        'color': '#0f766e',
        'content': """
<h2>Going Beyond BFS/DFS</h2>
<p>Basic BFS/DFS find paths and connected components. Advanced graph algorithms solve harder questions: <em>What is the shortest weighted path? In what order should tasks execute? Are these two nodes in the same network?</em></p>

<h3>1. Dijkstra's Algorithm — Shortest Weighted Path</h3>
<p>Finds the shortest path from a source to all other nodes in a graph with <strong>non-negative edge weights</strong>. Uses a min-heap for efficiency.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Always process the node with the smallest known distance next (greedy). Once a node is popped from the heap, its shortest distance is finalized.</p>
</div>

<pre><code class="language-python">
import heapq

def dijkstra(graph, start):
    # graph: dict of {node: [(neighbor, weight), ...]}
    # Returns: dict of shortest distances from start to every node
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:   # stale entry — skip
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [],
}
print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 3, 'D': 4}
</code></pre>

<p><strong>Complexity:</strong> O((V + E) log V) with a binary heap.</p>

<h3>2. Topological Sort — Ordering Dependencies</h3>
<p>For a <strong>Directed Acyclic Graph (DAG)</strong>, topological sort produces a linear ordering of nodes such that every directed edge u → v has u before v. Used in build systems, course prerequisites, task scheduling.</p>

<pre><code class="language-python">
from collections import deque

def topological_sort(graph):
    # Kahn's Algorithm: BFS + in-degree counting.
    # Returns sorted order, or [] if graph has a cycle.
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque(n for n in graph if in_degree[n] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(graph) else []  # [] = cycle detected

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(topological_sort(graph))  # [0, 1, 2, 3]  or  [0, 2, 1, 3]
</code></pre>

<h3>3. Union-Find (Disjoint Set Union)</h3>
<p>Efficiently tracks which <em>component</em> each node belongs to and merges components. With <strong>path compression</strong> and <strong>union by rank</strong>, nearly O(1) per operation.</p>

<pre><code class="language-python">
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already in same component
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.connected(0, 2))   # True
print(uf.connected(0, 3))   # False
print(uf.components)        # 3  (groups: {0,1,2}, {3}, {4})
</code></pre>

<h3>Complexity Comparison</h3>
<table class="complexity-table">
  <tr><th>Algorithm</th><th>Time</th><th>Use When</th></tr>
  <tr><td>BFS shortest path</td><td>O(V + E)</td><td>Unweighted graph</td></tr>
  <tr><td>Dijkstra</td><td>O((V+E) log V)</td><td>Weighted, non-negative edges</td></tr>
  <tr><td>Bellman-Ford</td><td>O(V × E)</td><td>Negative edge weights</td></tr>
  <tr><td>Topological Sort (Kahn)</td><td>O(V + E)</td><td>DAG — ordering dependencies</td></tr>
  <tr><td>Union-Find (find/union)</td><td>O(α(n)) ≈ O(1)</td><td>Dynamic connectivity</td></tr>
</table>
""",
        'sandbox_default': '''import heapq

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            nd = d + weight
            if nd < dist[neighbor]:
                dist[neighbor] = nd
                heapq.heappush(heap, (nd, neighbor))
    return dist

# Road network example
roads = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}
print("Shortest from A:", dijkstra(roads, "A"))
# Expected: {A:0, B:1, C:3, D:4}
''',
        'labs': [
            {
                'id': 1,
                'title': 'Network Delay Time (Dijkstra)',
                'description': 'There are n nodes in a network (labeled 1 to n). Given a list of travel times as directed edges (u, v, w) — from u to v with weight w — and a starting node k, return the time it takes for all nodes to receive a signal. If it is impossible for all nodes to receive the signal, return -1.',
                'starter_code': '''import heapq

def network_delay_time(times, n, k):
    """
    times: list of (source, target, weight)
    n: number of nodes (labeled 1..n)
    k: starting node
    Returns: max shortest path to any node, or -1 if unreachable
    """
    # YOUR CODE HERE
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

print("Testing network_delay_time:")
_test("example1", network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2)
_test("example2", network_delay_time([[1,2,1]], 2, 1), 1)
_test("unreachable", network_delay_time([[1,2,1]], 2, 2), -1)
_test("single node", network_delay_time([], 1, 1), 0)
_test("two paths", network_delay_time([[1,2,10],[1,3,5],[2,4,1],[3,4,1]], 4, 1), 6)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Build an adjacency list from times: graph[u].append((v, w)).',
                    'Run Dijkstra from node k. dist[node] = shortest time to reach node from k.',
                    'After Dijkstra, if any node has dist = infinity, return -1 (unreachable).',
                    'Otherwise return max(dist.values()) — the time when the last node finally receives the signal.',
                    'Remember: nodes are labeled 1..n, so initialize dist for all nodes 1 through n.',
                ]
            },
            {
                'id': 2,
                'title': 'Number of Connected Components (Union-Find)',
                'description': 'Given n nodes (0 to n-1) and a list of undirected edges, return the number of connected components in the graph. Use Union-Find for O(E × α(n)) time.',
                'starter_code': '''def count_components(n, edges):
    """
    n: number of nodes (0..n-1)
    edges: list of [u, v] undirected edges
    Returns: number of connected components
    """
    # Implement Union-Find here
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        # YOUR CODE HERE
        pass

    def union(x, y):
        # YOUR CODE HERE
        pass

    # YOUR CODE HERE (connect edges and count components)
    pass
''',
                'test_code': '''
def _test(name, got, expected):
    global _pass, _fail
    if got == expected:
        print(f"  PASS  {name}")
        _pass += 1
    else:
        print(f"  FAIL  {name}  got={got!r}  expected={expected!r}")
        _fail += 1

_pass = _fail = 0

print("Testing count_components:")
_test("n=5 edges=[[0,1],[1,2],[3,4]] -> 2",
      count_components(5, [[0,1],[1,2],[3,4]]), 2)
_test("n=5 edges=[[0,1],[1,2],[2,3],[3,4]] -> 1",
      count_components(5, [[0,1],[1,2],[2,3],[3,4]]), 1)
_test("n=3 no edges -> 3",
      count_components(3, []), 3)
_test("n=1 no edges -> 1",
      count_components(1, []), 1)
_test("n=4 edges=[[0,1],[2,3]] -> 2",
      count_components(4, [[0,1],[2,3]]), 2)

print(f"\\n{'='*40}")
print(f"Results: {_pass}/{_pass+_fail} tests passed")
if _fail == 0:
    print("🎉 All tests passed!")
''',
                'hints': [
                    'Start with n components (each node is its own component).',
                    'find(x): if parent[x] != x, recursively find root and apply path compression (parent[x] = find(parent[x])).',
                    'union(x, y): find roots px, py. If same, return False (already connected). Otherwise link by rank and decrement component count.',
                    'Process each edge with union(u, v). Edges that don\'t reduce component count connect already-joined nodes.',
                    'Final answer: the component count after all unions.',
                ]
            },
        ],
        'quiz': [
            {
                'question': 'Why does Dijkstra\'s algorithm fail with negative edge weights?',
                'options': ['It only works on undirected graphs', 'A node\'s distance can be updated after it\'s been finalized, breaking the greedy assumption', 'It requires sorted edges', 'Negative weights cause infinite loops'],
                'answer': 1,
                'explanation': 'Dijkstra\'s greedy assumption is: once a node is popped from the min-heap, its shortest distance is final. Negative edges can create shortcuts discovered later, making a previously "finalized" distance wrong. Bellman-Ford handles negative weights by relaxing all edges V-1 times without this assumption.'
            },
            {
                'question': 'Topological sort is only possible on which type of graph?',
                'options': ['Undirected graphs', 'Directed Acyclic Graphs (DAGs)', 'Complete graphs', 'Weighted graphs'],
                'answer': 1,
                'explanation': 'Topological sort requires a Directed Acyclic Graph (DAG). Direction is needed to define ordering. Cycles make topological sort impossible — if A depends on B and B depends on A, no valid ordering exists. Kahn\'s algorithm detects cycles by checking if all nodes were sorted.'
            },
            {
                'question': 'What does "path compression" do in Union-Find?',
                'options': ['Removes edges from the graph', 'Makes every node point directly to its root, flattening the tree for faster future lookups', 'Merges two components', 'Compresses the adjacency list'],
                'answer': 1,
                'explanation': 'During find(x), path compression makes every node on the path from x to the root point directly to the root. This flattens the tree so future find() calls are nearly O(1). Combined with union by rank, the amortized cost per operation is O(α(n)) — effectively constant.'
            },
            {
                'question': 'In Dijkstra\'s algorithm, why do we skip heap entries where d > dist[node]?',
                'options': ['To save memory', 'These are stale entries — a shorter path was already found and processed', 'To avoid counting a node twice in the result', 'Because negative distances are invalid'],
                'answer': 1,
                'explanation': 'When a shorter path to a node is found, we push a new (shorter_dist, node) entry but don\'t remove the old one (heaps don\'t support efficient deletion). When the old entry is eventually popped, d > dist[node] tells us a better distance is already recorded. Skipping it avoids redundant processing.'
            },
            {
                'question': 'What does topological sort return when the graph has a cycle?',
                'options': ['Raises an exception', 'Returns an empty list (cycle detected)', 'Returns the nodes in any order', 'Returns the cycle itself'],
                'answer': 1,
                'explanation': 'In Kahn\'s algorithm, if a cycle exists, some nodes will never reach in-degree 0 (each node in the cycle always has an incoming edge from another cycle node). The output order will have fewer nodes than the graph, which we check: if len(order) != len(graph), a cycle exists and we return [].'
            },
        ]
    },
]

# Attach levels to each module.
# Beginner = the existing flat content/labs/quiz keys.
# Intermediate & Advanced = from LEVELS_DATA.
for _m in MODULES:
    _mid = _m['id']
    _m['levels'] = {
        'beginner': {
            'content': _m['content'],
            'labs':    _m['labs'],
            'quiz':    _m['quiz'],
        },
        'intermediate': LEVELS_DATA[_mid]['intermediate'],
        'advanced':     LEVELS_DATA[_mid]['advanced'],
    }

