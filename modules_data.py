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
                'explanation': '"banana" contains "an" at positions 1 and 3: b[an]an[a] — wait, "an" appears at index 1 ("an") and index 3 ("an"). Count = 2.'
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
    <li><strong>Height</strong>: Longest path from root to a leaf</li>
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
  <tr><td>Bubble Sort</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>Yes ✅</td></tr>
  <tr><td>Selection Sort</td><td>O(n²)</td><td>O(n²)</td><td>O(n²)</td><td>No ❌</td></tr>
  <tr><td>Insertion Sort</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>Yes ✅</td></tr>
  <tr><td>Python's sort()</td><td>O(n)</td><td>O(n log n)</td><td>O(n log n)</td><td>Yes ✅</td></tr>
</table>
<p><small>Stable = equal elements maintain their original order</small></p>
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
]
