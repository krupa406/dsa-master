# levels_data.py — Intermediate & Advanced level content for all 14 DSA modules
# Used by modules_data.py to attach levels to each module dict.

LEVELS_DATA = {

    # =========================================================
    # MODULE 1: Arrays & Lists
    # =========================================================
    1: {
        'intermediate': {
            'content': '''
<h2>Arrays: Intermediate Techniques</h2>
<p>You can already create and traverse lists. Now we tackle the classic patterns that appear in interviews and real codebases: two pointers, sliding window, and prefix sums.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Most O(n²) brute-force array problems can be reduced to O(n) with a smart pointer or running total trick.</p>
</div>

<h3>Two-Pointer Technique</h3>
<p>Keep one pointer at each end and march them toward each other.</p>
<pre><code class="language-python">
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

print(two_sum_sorted([1, 2, 4, 6, 8], 10))  # (2, 4)
</code></pre>

<h3>Sliding Window</h3>
<p>Maintain a window of fixed or variable size and slide it across the array, updating a running result.</p>
<pre><code class="language-python">
def max_sum_window(arr, k):
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best

print(max_sum_window([2, 1, 5, 1, 3, 2], 3))  # 9  (5+1+3)
</code></pre>

<h3>Prefix Sums</h3>
<p>Pre-compute cumulative sums so any range query becomes O(1).</p>
<pre><code class="language-python">
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        prefix[i + 1] = prefix[i] + v
    return prefix

def range_sum(prefix, l, r):   # inclusive [l, r]
    return prefix[r + 1] - prefix[l]

arr = [3, 1, 4, 1, 5, 9, 2]
p = build_prefix(arr)
print(range_sum(p, 1, 4))  # 11  (1+4+1+5)
</code></pre>

<h3>Useful Built-ins</h3>
<pre><code class="language-python">
nums = [4, 2, 7, 1, 9]
print(sorted(nums))               # new sorted list
print(sorted(nums, reverse=True)) # descending
nums.sort()                       # in-place

# enumerate gives (index, value)
for i, v in enumerate(nums):
    print(i, v)

# zip pairs two lists
a = [1, 2, 3]
b = ['x', 'y', 'z']
print(list(zip(a, b)))  # [(1,'x'), (2,'y'), (3,'z')]
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Two Sum (Sorted Array)',
                    'description': '''<p>Given a <strong>sorted</strong> list of integers and a target value, return the <strong>indices</strong> (0-based) of the two numbers that add up to the target.</p>
<p>Use the <strong>two-pointer</strong> technique for O(n) time.</p>
<pre><code class="language-python">two_sum_sorted([1, 2, 4, 6, 8], 10)  # (2, 4)
two_sum_sorted([1, 3, 5, 7], 8)       # (1, 3)
</code></pre>''',
                    'starter_code': '''def two_sum_sorted(arr, target):
    # Use two pointers: left starts at 0, right at end
    left, right = 0, len(arr) - 1
    while left < right:
        # TODO: compute current sum and adjust pointers
        pass
    return None
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Two Sum Sorted tests...")
_test("basic", two_sum_sorted([1, 2, 4, 6, 8], 10), (2, 4))
_test("front pair", two_sum_sorted([1, 3, 5, 7], 4), (0, 1))
_test("back pair", two_sum_sorted([1, 3, 5, 7], 12), (2, 3))
_test("no match", two_sum_sorted([1, 2, 3], 10), None)
print("All tests passed")
''',
                    'hints': [
                        'Start left=0 and right=len(arr)-1.',
                        'If arr[left]+arr[right] < target, move left up; if > target, move right down.',
                        'Return (left, right) as a tuple when the sum equals the target.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Max Sum Subarray of Size K',
                    'description': '''<p>Given a list of integers and a window size <code>k</code>, return the maximum sum of any contiguous subarray of length <code>k</code>.</p>
<p>Use the <strong>sliding window</strong> pattern — O(n) time.</p>
<pre><code class="language-python">max_sum_window([2, 1, 5, 1, 3, 2], 3)  # 9
max_sum_window([1, 4, 2, 9, 7], 2)      # 16
</code></pre>''',
                    'starter_code': '''def max_sum_window(arr, k):
    # Compute the sum of the first window
    window = sum(arr[:k])
    best = window
    # Slide the window: add the new element, drop the leftmost
    for i in range(k, len(arr)):
        # TODO: slide window and update best
        pass
    return best
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Max Sum Window tests...")
_test("basic", max_sum_window([2, 1, 5, 1, 3, 2], 3), 9)
_test("pairs", max_sum_window([1, 4, 2, 9, 7], 2), 16)
_test("full", max_sum_window([5, 1, 3], 3), 9)
_test("k=1",  max_sum_window([3, 7, 2], 1), 7)
print("All tests passed")
''',
                    'hints': [
                        'Start by summing the first k elements.',
                        'For each new index i (from k onward): window += arr[i] - arr[i-k].',
                        'Track the maximum window sum seen so far.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'What is the time complexity of the two-pointer approach for two-sum on a sorted array?',
                    'options': ['O(n²)', 'O(n log n)', 'O(n)', 'O(1)'],
                    'answer': 2,
                    'explanation': 'Each pointer moves at most n steps total, giving O(n) time.'
                },
                {
                    'question': 'In a sliding window of size k over n elements, how many windows are there?',
                    'options': ['k', 'n', 'n - k + 1', 'n * k'],
                    'answer': 2,
                    'explanation': 'The window starts at index 0 and ends when its right edge reaches n-1, giving n-k+1 windows.'
                },
                {
                    'question': 'What does prefix[i+1] - prefix[l] compute (using the prefix-sum array)?',
                    'options': ['Sum of all elements', 'Sum from index l to i (inclusive)', 'Sum from 0 to i', 'Element at index i'],
                    'answer': 1,
                    'explanation': 'prefix[r+1] - prefix[l] gives the sum of arr[l..r] inclusive.'
                },
                {
                    'question': 'Which Python built-in returns a NEW sorted list without modifying the original?',
                    'options': ['list.sort()', 'sorted()', 'list.reverse()', 'reversed()'],
                    'answer': 1,
                    'explanation': 'sorted() returns a new list; list.sort() sorts in-place and returns None.'
                },
                {
                    'question': 'What does enumerate([\'a\', \'b\', \'c\']) yield?',
                    'options': ['(\'a\',0),(\'b\',1),(\'c\',2)', '(0,\'a\'),(1,\'b\'),(2,\'c\')', '[0,1,2]', '(\'a\',\'b\',\'c\')'],
                    'answer': 1,
                    'explanation': 'enumerate yields (index, value) tuples starting at index 0.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Arrays: Advanced Patterns</h2>
<p>At the advanced level we tackle problems that require combining multiple techniques: dynamic programming on arrays, interval manipulation, and in-place transformations.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Hard array problems usually reduce to either "track the best so far" (DP) or "sort + sweep" (interval problems).</p>
</div>

<h3>Kadane\'s Algorithm — Maximum Subarray Sum</h3>
<pre><code class="language-python">
def max_subarray(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)   # extend or restart
        best = max(best, cur)
    return best

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
</code></pre>

<h3>Merge Overlapping Intervals</h3>
<pre><code class="language-python">
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:          # overlap
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# [[1,6],[8,10],[15,18]]
</code></pre>

<h3>Product of Array Except Self (No Division)</h3>
<pre><code class="language-python">
def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    # Left pass: out[i] = product of all to the left
    for i in range(1, n):
        out[i] = out[i-1] * nums[i-1]
    # Right pass: multiply by product of all to the right
    right = 1
    for i in range(n-1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out

print(product_except_self([1,2,3,4]))  # [24,12,8,6]
</code></pre>

<h3>Dutch National Flag — Three-way Partition</h3>
<pre><code class="language-python">
def sort_colors(nums):
    lo, mid, hi = 0, 0, len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
    return nums

print(sort_colors([2,0,2,1,1,0]))  # [0,0,1,1,2,2]
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': "Kadane's Algorithm",
                    'description': '''<p>Implement <code>max_subarray(arr)</code> that returns the largest sum of any contiguous subarray using <strong>Kadane\'s algorithm</strong>.</p>
<p>Must handle arrays with all negative numbers.</p>
<pre><code class="language-python">max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # 6
max_subarray([-3, -1, -4])                        # -1
</code></pre>''',
                    'starter_code': '''def max_subarray(arr):
    # Start both best and cur at the first element
    best = cur = arr[0]
    for x in arr[1:]:
        # TODO: either extend current subarray or start fresh at x
        pass
    return best
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Kadane tests...")
_test("classic", max_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)
_test("all neg", max_subarray([-3,-1,-4]), -1)
_test("all pos", max_subarray([1,2,3,4]), 10)
_test("single",  max_subarray([7]), 7)
print("All tests passed")
''',
                    'hints': [
                        'cur = max(x, cur + x) decides: restart at x, or extend the current subarray.',
                        'Update best = max(best, cur) after each step.',
                        'Initialise both best and cur to arr[0] to handle all-negative arrays.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Merge Overlapping Intervals',
                    'description': '''<p>Given a list of <code>[start, end]</code> intervals, merge all overlapping ones and return the result sorted by start time.</p>
<pre><code class="language-python">merge_intervals([[1,3],[2,6],[8,10],[15,18]])  # [[1,6],[8,10],[15,18]]
merge_intervals([[1,4],[4,5]])                  # [[1,5]]
</code></pre>''',
                    'starter_code': '''def merge_intervals(intervals):
    # Sort by start time first
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        # TODO: check overlap with last merged interval and merge or append
        pass
    return merged
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Merge Intervals tests...")
_test("basic",   merge_intervals([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
_test("touch",   merge_intervals([[1,4],[4,5]]), [[1,5]])
_test("no merge",merge_intervals([[1,2],[3,4]]), [[1,2],[3,4]])
_test("all one", merge_intervals([[1,10],[2,3],[4,8]]), [[1,10]])
print("All tests passed")
''',
                    'hints': [
                        'Sort intervals by start time before processing.',
                        'Two intervals overlap if the new start <= merged[-1][1].',
                        'On overlap, update merged[-1][1] = max(merged[-1][1], end).',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'What is the time and space complexity of Kadane\'s algorithm?',
                    'options': ['O(n²) time, O(n) space', 'O(n) time, O(1) space', 'O(n log n) time, O(1) space', 'O(n) time, O(n) space'],
                    'answer': 1,
                    'explanation': 'Kadane\'s does one pass (O(n)) and only stores two variables (O(1) space).'
                },
                {
                    'question': 'In the product-except-self problem, why can\'t we simply use division?',
                    'options': ['Division is too slow', 'The array may contain zeros', 'Python doesn\'t support division', 'It changes the array'],
                    'answer': 1,
                    'explanation': 'If any element is zero the total product is 0, and dividing by zero is undefined.'
                },
                {
                    'question': 'What is the first step when merging overlapping intervals?',
                    'options': ['Sort by end time', 'Sort by start time', 'Find the maximum end', 'Remove duplicates'],
                    'answer': 1,
                    'explanation': 'Sorting by start time ensures we always process intervals left-to-right, making overlap detection a simple comparison.'
                },
                {
                    'question': 'In the Dutch National Flag algorithm, how many pointers are used?',
                    'options': ['1', '2', '3', '4'],
                    'answer': 2,
                    'explanation': 'Three pointers: lo (boundary for 0s), mid (current element), hi (boundary for 2s).'
                },
                {
                    'question': 'cur = max(x, cur + x) in Kadane\'s decides to:',
                    'options': ['Pick the larger array element', 'Restart the subarray at x or extend it', 'Track the global maximum', 'Sort the array'],
                    'answer': 1,
                    'explanation': 'If cur + x < x, the running sum became a drag — it\'s better to start fresh at x.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 2: Strings
    # =========================================================
    2: {
        'intermediate': {
            'content': '''
<h2>Strings: Intermediate Techniques</h2>
<p>Beyond basic slicing, strings reward pattern recognition: anagrams, palindromes, and frequency maps are everywhere in technical interviews.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Strings are immutable sequences — treat character counts (hashmaps) as your primary tool.</p>
</div>

<h3>Character Frequency Maps</h3>
<pre><code class="language-python">
from collections import Counter

word = "banana"
freq = Counter(word)
print(freq)  # Counter({'a': 3, 'n': 2, 'b': 1})

# Check anagram
def is_anagram(s, t):
    return Counter(s) == Counter(t)

print(is_anagram("listen", "silent"))  # True
</code></pre>

<h3>Sliding Window on Strings</h3>
<pre><code class="language-python">
def longest_unique(s):
    seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best

print(longest_unique("abcabcbb"))  # 3
</code></pre>

<h3>Palindrome Check (Two Pointers)</h3>
<pre><code class="language-python">
def is_palindrome(s):
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1; right -= 1
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
</code></pre>

<h3>String Formatting & f-Strings</h3>
<pre><code class="language-python">
name = "Alice"
score = 95.5
print(f"Name: {name}, Score: {score:.1f}")   # Score: 95.5
print(f"{'centred':^20}")                    # padded centred
print(f"{42:05d}")                           # 00042 (zero-padded)
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Valid Anagram',
                    'description': '''<p>Write <code>is_anagram(s, t)</code> that returns <code>True</code> if <code>t</code> is an anagram of <code>s</code> (same characters, same counts, any order).</p>
<p>Do <strong>not</strong> use <code>sorted()</code> — use a frequency map.</p>
<pre><code class="language-python">is_anagram("listen", "silent")  # True
is_anagram("hello", "world")    # False
</code></pre>''',
                    'starter_code': '''def is_anagram(s, t):
    if len(s) != len(t):
        return False
    # Build a frequency map by hand (dict)
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t:
        # TODO: decrement count; if it goes below 0 or missing, return False
        pass
    return True
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Anagram tests...")
_test("listen/silent", is_anagram("listen","silent"), True)
_test("hello/world",   is_anagram("hello","world"),   False)
_test("same",          is_anagram("abc","abc"),        True)
_test("diff len",      is_anagram("ab","abc"),         False)
_test("repeat",        is_anagram("aab","bba"),        False)
print("All tests passed")
''',
                    'hints': [
                        'Build a freq dict counting each char in s.',
                        'For each char in t, decrement freq[ch]. If the char is missing or count < 0, return False.',
                        'After the loop, all values in freq should be 0.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Longest Substring Without Repeating Characters',
                    'description': '''<p>Implement <code>longest_unique(s)</code> that returns the length of the longest substring without repeating characters.</p>
<pre><code class="language-python">longest_unique("abcabcbb")  # 3  ("abc")
longest_unique("bbbbb")     # 1  ("b")
longest_unique("pwwkew")    # 3  ("wke")
</code></pre>''',
                    'starter_code': '''def longest_unique(s):
    seen = {}   # char -> last seen index
    left = 0
    best = 0
    for right, ch in enumerate(s):
        # If ch was seen and is inside the current window, move left
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        # TODO: record ch position and update best
    return best
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Longest Unique tests...")
_test("abcabcbb", longest_unique("abcabcbb"), 3)
_test("bbbbb",    longest_unique("bbbbb"),    1)
_test("pwwkew",   longest_unique("pwwkew"),   3)
_test("empty",    longest_unique(""),         0)
_test("all diff", longest_unique("abcde"),    5)
print("All tests passed")
''',
                    'hints': [
                        'Use a dict mapping each char to its most recent index.',
                        'When a repeated char is found inside the window, move left to seen[ch]+1.',
                        'best = max(best, right - left + 1) after each step.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'What does Counter("aabb") return?',
                    'options': ["{'a':1,'b':1}", "{'a':2,'b':2}", "['a','a','b','b']", "{'ab':2}"],
                    'answer': 1,
                    'explanation': "Counter counts each element's frequency: {'a':2,'b':2}."
                },
                {
                    'question': 'Two strings are anagrams if they have:',
                    'options': ['The same length', 'The same characters in the same order', 'The same characters with the same frequencies', 'No repeated characters'],
                    'answer': 2,
                    'explanation': 'Anagrams share the same characters and counts but may differ in order.'
                },
                {
                    'question': 'In the sliding window for longest unique substring, what does the "left" pointer represent?',
                    'options': ['The start of the longest substring found', 'The left boundary of the current valid window', 'The index of the last repeated character', 'The centre of the string'],
                    'answer': 1,
                    'explanation': 'left is the start of the current window; it advances when a repeated character is found inside the window.'
                },
                {
                    'question': 'What does f"{42:05d}" produce?',
                    'options': ['42000', '00042', '42   ', '  42 '],
                    'answer': 1,
                    'explanation': ':05d means zero-pad to width 5 in decimal, giving 00042.'
                },
                {
                    'question': 'Which approach is faster for palindrome checking on long strings?',
                    'options': ['s == s[::-1]', 'Two-pointer from both ends', 'Counter comparison', 'Converting to list'],
                    'answer': 1,
                    'explanation': 'Two pointers can short-circuit on the first mismatch; s[::-1] always creates a full reversed copy.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Strings: Advanced Patterns</h2>
<p>Advanced string problems demand combining frequency maps with window shrinking, understanding string hashing, and implementing classic algorithms like KMP.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>When the constraint is "contains all characters of pattern", reach for a variable sliding window with a need-counter.</p>
</div>

<h3>Minimum Window Substring</h3>
<pre><code class="language-python">
from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    best = ""
    left = 0
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:          # valid window found
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            window = s[left:right+1]
            if not best or len(window) < len(best):
                best = window
            need[s[left]] += 1
            missing += 1
            left += 1
    return best

print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
</code></pre>

<h3>Group Anagrams</h3>
<pre><code class="language-python">
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))
        groups[key].append(w)
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat','tea','ate'],['tan','nat'],['bat']]
</code></pre>

<h3>Rabin-Karp Rolling Hash</h3>
<pre><code class="language-python">
def search_rk(text, pattern):
    n, m = len(text), len(pattern)
    BASE, MOD = 31, 10**9 + 7
    ph = sum(ord(pattern[i]) * pow(BASE, i, MOD) for i in range(m)) % MOD
    th = sum(ord(text[i])    * pow(BASE, i, MOD) for i in range(m)) % MOD
    if ph == th and text[:m] == pattern: return 0
    for i in range(1, n - m + 1):
        th = (th - ord(text[i-1])) * pow(BASE, MOD-2, MOD) % MOD
        th = (th + ord(text[i+m-1]) * pow(BASE, m-1, MOD)) % MOD
        if th == ph and text[i:i+m] == pattern:
            return i
    return -1

print(search_rk("hello world", "world"))  # 6
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Group Anagrams',
                    'description': '''<p>Write <code>group_anagrams(words)</code> that groups all anagrams together. The order of groups and the order within each group do not matter.</p>
<pre><code class="language-python">group_anagrams(["eat","tea","tan","ate","nat","bat"])
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]  (any order)
</code></pre>''',
                    'starter_code': '''def group_anagrams(words):
    groups = {}
    for w in words:
        # TODO: create a key that is the same for all anagrams of w
        key = None  # replace this
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return list(groups.values())
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")

def _normalise(result):
    return sorted([sorted(g) for g in result])

print("Running Group Anagrams tests...")
res = group_anagrams(["eat","tea","tan","ate","nat","bat"])
exp = [["ate","eat","tea"],["nat","tan"],["bat"]]
if _normalise(res) == _normalise(exp): _pass("basic grouping")
else: _fail(f"basic grouping: {res}")

res2 = group_anagrams(["a"])
if _normalise(res2) == [["a"]]: _pass("single word")
else: _fail(f"single: {res2}")

res3 = group_anagrams(["abc","bca","cab","xyz"])
exp3 = [["abc","bca","cab"],["xyz"]]
if _normalise(res3) == _normalise(exp3): _pass("two groups")
else: _fail(f"two groups: {res3}")

print("All tests passed")
''',
                    'hints': [
                        'The key for each anagram group should be the same regardless of letter order.',
                        'tuple(sorted(word)) is a reliable hashable key.',
                        'Use a dict mapping key -> list of words.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Encode and Decode Strings',
                    'description': '''<p>Design <code>encode(words)</code> and <code>decode(s)</code> so that a list of strings can be serialised to a single string and recovered exactly.</p>
<p>Handle empty strings and strings containing any character.</p>
<pre><code class="language-python">words = ["hello","world","","foo"]
assert decode(encode(words)) == words
</code></pre>''',
                    'starter_code': '''def encode(words):
    # Prefix each word with its length and a separator, e.g. "5#hello"
    result = ""
    for w in words:
        result += str(len(w)) + "#" + w
    return result

def decode(s):
    words = []
    i = 0
    while i < len(s):
        # TODO: read the length, skip "#", extract the word
        pass
    return words
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")

def _rt(label, words):
    if decode(encode(words)) == words: _pass(label)
    else: _fail(f"{label}: round-trip failed for {words}")

print("Running Encode/Decode tests...")
_rt("basic",       ["hello","world"])
_rt("empty word",  ["","foo",""])
_rt("special",     ["a#b","1#2"])
_rt("single",      ["only"])
_rt("empty list",  [])
print("All tests passed")
''',
                    'hints': [
                        'Use a length-prefix scheme: "5#hello3#foo".',
                        'In decode, find the "#" by scanning from i, parse the int before it.',
                        'Extract s[j+1 : j+1+length] then move i to j+1+length.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In the minimum window substring problem, what does the "missing" counter track?',
                    'options': ['Characters not yet seen', 'Characters needed that haven\'t been satisfied', 'Length of the window', 'Number of unique characters'],
                    'answer': 1,
                    'explanation': '"missing" counts how many characters from t still need to be covered by the current window.'
                },
                {
                    'question': 'What is the canonical key used when grouping anagrams?',
                    'options': ['The original string', 'The reversed string', 'The sorted tuple of characters', 'The character set'],
                    'answer': 2,
                    'explanation': 'tuple(sorted(word)) produces the same key for all anagrams because sorting yields a canonical order.'
                },
                {
                    'question': 'What is the purpose of rolling hash in Rabin-Karp?',
                    'options': ['To sort characters', 'To update the hash in O(1) when the window slides', 'To compare strings character-by-character', 'To compress the text'],
                    'answer': 1,
                    'explanation': 'Rolling hash removes the leftmost character and adds the new rightmost one in O(1), avoiding O(m) rehashing.'
                },
                {
                    'question': 'Why must we verify text[i:i+m] == pattern after a hash match in Rabin-Karp?',
                    'options': ['Hashes can collide (false positives)', 'Hashes are always wrong', 'To measure performance', 'Python requires it'],
                    'answer': 0,
                    'explanation': 'Hash collisions are possible — two different strings can produce the same hash, so a character-level check confirms the true match.'
                },
                {
                    'question': 'defaultdict(list) differs from dict in that:',
                    'options': ['It is faster', 'Missing keys automatically get an empty list as default', 'It preserves insertion order', 'It only stores strings'],
                    'answer': 1,
                    'explanation': 'defaultdict(list) calls list() for any missing key, so you never need to check "if key not in d" before appending.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 3: Linked Lists
    # =========================================================
    3: {
        'intermediate': {
            'content': '''
<h2>Linked Lists: Intermediate Techniques</h2>
<p>Mastering linked list manipulation means mastering pointer rewiring. Key patterns: fast/slow pointers, in-place reversal, and finding the middle.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>The fast/slow (Floyd\'s) pointer trick solves cycle detection, midpoint finding, and kth-from-end in a single pass.</p>
</div>

<h3>Finding the Middle Node</h3>
<pre><code class="language-python">
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow   # slow is at the middle

# Build 1->2->3->4->5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(find_middle(head).val)  # 3
</code></pre>

<h3>Reversing a Linked List</h3>
<pre><code class="language-python">
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Result: 5->4->3->2->1
</code></pre>

<h3>Cycle Detection (Floyd\'s Algorithm)</h3>
<pre><code class="language-python">
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Reverse a Linked List',
                    'description': '''<p>Given the head of a singly linked list, reverse it in-place and return the new head.</p>
<p>Use the <code>Node</code> class already defined in the starter code.</p>
<pre><code class="language-python">to_list(reverse(from_list([1,2,3,4,5])))  # [5,4,3,2,1]
</code></pre>''',
                    'starter_code': '''class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def from_list(lst):
    head = None
    for v in reversed(lst):
        head = Node(v, head)
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        # TODO: rewire curr.next to point to prev, then advance
        pass
    return prev
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Reverse Linked List tests...")
_test("5 nodes", to_list(reverse(from_list([1,2,3,4,5]))), [5,4,3,2,1])
_test("2 nodes", to_list(reverse(from_list([1,2]))),       [2,1])
_test("1 node",  to_list(reverse(from_list([7]))),         [7])
_test("empty",   to_list(reverse(None)),                   [])
print("All tests passed")
''',
                    'hints': [
                        'Save curr.next before overwriting it.',
                        'Set curr.next = prev, then prev = curr, then curr = saved next.',
                        'When the loop ends, prev is the new head.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Find Middle of Linked List',
                    'description': '''<p>Return the <strong>middle node</strong> of a linked list. For even-length lists return the <em>second</em> middle.</p>
<pre><code class="language-python">find_middle(from_list([1,2,3,4,5])).val  # 3
find_middle(from_list([1,2,3,4])).val    # 3  (second middle)
</code></pre>''',
                    'starter_code': '''class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def from_list(lst):
    head = None
    for v in reversed(lst):
        head = Node(v, head)
    return head

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        # TODO: advance slow by 1, fast by 2
        pass
    return slow
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Find Middle tests...")
_test("odd 5",  find_middle(from_list([1,2,3,4,5])).val, 3)
_test("even 4", find_middle(from_list([1,2,3,4])).val,   3)
_test("1 node", find_middle(from_list([9])).val,          9)
_test("2 nodes",find_middle(from_list([1,2])).val,        2)
print("All tests passed")
''',
                    'hints': [
                        'Use two pointers: slow moves 1 step, fast moves 2 steps.',
                        'When fast reaches the end (None or last node), slow is at the middle.',
                        'For even-length lists this naturally lands on the second middle.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In the fast/slow pointer technique, fast moves:',
                    'options': ['1 node at a time', '2 nodes at a time', '3 nodes at a time', 'As fast as possible'],
                    'answer': 1,
                    'explanation': 'Fast advances two nodes per iteration; slow advances one. When fast reaches the end, slow is at the middle.'
                },
                {
                    'question': 'After reversing a linked list, what does the variable "prev" hold?',
                    'options': ['The original head', 'None', 'The new head (original tail)', 'The middle node'],
                    'answer': 2,
                    'explanation': 'After the reversal loop, prev is the last node processed — which is the original tail, now the new head.'
                },
                {
                    'question': 'Floyd\'s cycle detection works because:',
                    'options': ['Fast pointer is always ahead', 'If there\'s a cycle, fast eventually laps slow and they meet', 'Linked lists can\'t have cycles', 'Both pointers restart from head'],
                    'answer': 1,
                    'explanation': 'In a cycle, fast gains one node per step on slow. They must eventually occupy the same node.'
                },
                {
                    'question': 'What is the time complexity of reversing a linked list of n nodes?',
                    'options': ['O(1)', 'O(log n)', 'O(n)', 'O(n²)'],
                    'answer': 2,
                    'explanation': 'Each node is visited exactly once, so the reversal is O(n).'
                },
                {
                    'question': 'To save the next node before rewiring in reversal, we do:',
                    'options': ['prev = curr.next', 'nxt = curr.next', 'curr = curr.next', 'head = curr.next'],
                    'answer': 1,
                    'explanation': 'nxt = curr.next saves the next node so we can advance curr after rewiring curr.next = prev.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Linked Lists: Advanced Patterns</h2>
<p>Advanced challenges include reversing sub-lists, merging sorted lists, and detecting/removing cycles with exact entry-point finding.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Most hard linked-list problems combine reversal + two-pointer + careful pointer bookkeeping. Draw it out before coding.</p>
</div>

<h3>Merge Two Sorted Lists</h3>
<pre><code class="language-python">
def merge_sorted(l1, l2):
    dummy = Node(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1; l1 = l1.next
        else:
            cur.next = l2; l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
</code></pre>

<h3>Reverse Nodes in k-Groups</h3>
<pre><code class="language-python">
def reverse_k_group(head, k):
    def get_kth(curr, k):
        while curr and k:
            curr = curr.next; k -= 1
        return curr

    dummy = Node(0); dummy.next = head
    group_prev = dummy
    while True:
        kth = get_kth(group_prev, k)
        if not kth: break
        group_next = kth.next
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr; curr = nxt
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
    return dummy.next
</code></pre>

<h3>Find Cycle Entry Point</h3>
<pre><code class="language-python">
def cycle_entry(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast: break
    else:
        return None   # no cycle
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow   # entry point
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Merge Two Sorted Linked Lists',
                    'description': '''<p>Given the heads of two sorted linked lists, merge them into one sorted list and return the head.</p>
<pre><code class="language-python">to_list(merge_sorted(from_list([1,3,5]), from_list([2,4,6])))
# [1,2,3,4,5,6]
</code></pre>''',
                    'starter_code': '''class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def from_list(lst):
    head = None
    for v in reversed(lst):
        head = Node(v, head)
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def merge_sorted(l1, l2):
    dummy = Node(0)
    cur = dummy
    while l1 and l2:
        # TODO: pick the smaller node and advance that pointer
        pass
    # Attach the remaining list
    cur.next = l1 or l2
    return dummy.next
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Merge Sorted tests...")
_test("basic",   to_list(merge_sorted(from_list([1,3,5]), from_list([2,4,6]))), [1,2,3,4,5,6])
_test("one empty", to_list(merge_sorted(from_list([1,2]), from_list([]))), [1,2])
_test("both empty", to_list(merge_sorted(from_list([]), from_list([]))), [])
_test("overlap", to_list(merge_sorted(from_list([1,2,4]), from_list([1,3,4]))), [1,1,2,3,4,4])
print("All tests passed")
''',
                    'hints': [
                        'Use a dummy head node to simplify edge cases.',
                        'Compare l1.val and l2.val; attach the smaller node to cur.next.',
                        'After the loop, attach whichever list is non-empty.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Remove Nth Node From End',
                    'description': '''<p>Remove the <strong>n-th node from the end</strong> of a linked list in a single pass.</p>
<pre><code class="language-python">to_list(remove_nth(from_list([1,2,3,4,5]), 2))  # [1,2,3,5]
to_list(remove_nth(from_list([1]), 1))           # []
</code></pre>''',
                    'starter_code': '''class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def from_list(lst):
    head = None
    for v in reversed(lst):
        head = Node(v, head)
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def remove_nth(head, n):
    dummy = Node(0); dummy.next = head
    fast = slow = dummy
    # Advance fast by n+1 steps
    for _ in range(n + 1):
        fast = fast.next
    # Move both until fast is None
    while fast:
        # TODO: advance both pointers
        pass
    # slow is just before the node to remove
    slow.next = slow.next.next
    return dummy.next
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Remove Nth tests...")
_test("remove 2nd from end", to_list(remove_nth(from_list([1,2,3,4,5]), 2)), [1,2,3,5])
_test("remove last",         to_list(remove_nth(from_list([1,2,3]), 1)),     [1,2])
_test("remove only",         to_list(remove_nth(from_list([1]), 1)),         [])
_test("remove first",        to_list(remove_nth(from_list([1,2]), 2)),       [2])
print("All tests passed")
''',
                    'hints': [
                        'Use a dummy node before head to handle edge cases (removing head).',
                        'Advance fast n+1 steps ahead of slow.',
                        'When fast is None, slow.next is the node to delete — set slow.next = slow.next.next.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Why is a dummy head node useful in linked list problems?',
                    'options': ['It speeds up traversal', 'It eliminates special cases when the head itself might be modified', 'It reduces memory usage', 'It auto-sorts the list'],
                    'answer': 1,
                    'explanation': 'A dummy node before the real head means "remove head" uses the same code path as removing any other node.'
                },
                {
                    'question': 'In "remove nth from end", why do we advance fast by n+1 (not n) steps?',
                    'options': ['Off-by-one error fix', 'So slow stops at the node BEFORE the target (needed for deletion)', 'To handle cycles', 'To reach the tail faster'],
                    'answer': 1,
                    'explanation': 'We need slow to be one node before the target so we can set slow.next = slow.next.next. n+1 gap achieves this.'
                },
                {
                    'question': 'merge_sorted uses a dummy node. What does dummy.next hold after the merge?',
                    'options': ['The last merged node', 'The new head of the merged list', 'None', 'The original l1 head'],
                    'answer': 1,
                    'explanation': 'dummy.next always points to the first real node of the merged list — returned as the new head.'
                },
                {
                    'question': 'What does cur.next = l1 or l2 accomplish at the end of merge_sorted?',
                    'options': ['Creates a cycle', 'Attaches whichever list still has remaining nodes', 'Reverses the remaining nodes', 'Detaches the dummy'],
                    'answer': 1,
                    'explanation': 'When one list is exhausted, the other may still have nodes. "l1 or l2" returns the non-None (non-empty) list.'
                },
                {
                    'question': 'The cycle entry-point algorithm requires a second phase where:',
                    'options': ['Fast restarts from head at double speed', 'Slow restarts from head and both move one step at a time until they meet', 'Both pointers reset to head', 'We count the cycle length'],
                    'answer': 1,
                    'explanation': 'By mathematical proof, resetting slow to head and walking both one step at a time makes them meet exactly at the cycle entry.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 4: Stacks & Queues
    # =========================================================
    4: {
        'intermediate': {
            'content': '''
<h2>Stacks & Queues: Intermediate Techniques</h2>
<p>Once you know push/pop and enqueue/dequeue, the next step is using stacks for expression evaluation and queues for BFS.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>A <strong>monotonic stack</strong> maintains elements in strictly increasing or decreasing order, enabling O(n) solutions to "next greater element" problems.</p>
</div>

<h3>Monotonic Stack — Next Greater Element</h3>
<pre><code class="language-python">
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []   # stores indices
    for i, v in enumerate(nums):
        while stack and nums[stack[-1]] < v:
            idx = stack.pop()
            result[idx] = v
        stack.append(i)
    return result

print(next_greater([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]
</code></pre>

<h3>Evaluate Reverse Polish Notation</h3>
<pre><code class="language-python">
def eval_rpn(tokens):
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }
    for tok in tokens:
        if tok in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[tok](a, b))
        else:
            stack.append(int(tok))
    return stack[0]

print(eval_rpn(["2","1","+","3","*"]))  # 9
</code></pre>

<h3>Queue via Two Stacks</h3>
<pre><code class="language-python">
class MyQueue:
    def __init__(self):
        self.inbox  = []
        self.outbox = []

    def push(self, x):
        self.inbox.append(x)

    def pop(self):
        self._shift()
        return self.outbox.pop()

    def peek(self):
        self._shift()
        return self.outbox[-1]

    def _shift(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Valid Parentheses',
                    'description': '''<p>Write <code>is_valid(s)</code> that returns <code>True</code> if the string of brackets is valid (every opener has a matching closer in correct order).</p>
<pre><code class="language-python">is_valid("()[]{}")   # True
is_valid("([)]")     # False
is_valid("{[]}")     # True
</code></pre>''',
                    'starter_code': '''def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            # TODO: check if stack top matches the expected opener
            pass
    return len(stack) == 0
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Valid Parentheses tests...")
_test("simple",   is_valid("()[]{}"), True)
_test("nested",   is_valid("{[]}"),   True)
_test("wrong ord",is_valid("([)]"),   False)
_test("only open",is_valid("((("),    False)
_test("empty",    is_valid(""),       True)
print("All tests passed")
''',
                    'hints': [
                        'Push opening brackets onto the stack.',
                        'For closing brackets, check if the stack is non-empty AND stack[-1] == pairs[ch].',
                        'If the check fails, return False immediately. At the end, return stack == [].',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Daily Temperatures (Monotonic Stack)',
                    'description': '''<p>Given a list of daily temperatures, return a list where each element is the number of days until a warmer temperature. If none exists, use 0.</p>
<pre><code class="language-python">daily_temps([73,74,75,71,69,72,76,73])
# [1, 1, 4, 2, 1, 1, 0, 0]
</code></pre>''',
                    'starter_code': '''def daily_temps(temps):
    result = [0] * len(temps)
    stack = []   # stores indices of unresolved days
    for i, t in enumerate(temps):
        # While the current temp is warmer than the top of stack
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            # TODO: store the wait (i - idx) in result[idx]
            pass
        stack.append(i)
    return result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Daily Temperatures tests...")
_test("classic", daily_temps([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
_test("desc",    daily_temps([90,80,70,60]),             [0,0,0,0])
_test("asc",     daily_temps([60,70,80,90]),             [1,1,1,0])
_test("single",  daily_temps([50]),                      [0])
print("All tests passed")
''',
                    'hints': [
                        'Push indices onto the stack (not values).',
                        'When temps[i] > temps[stack[-1]], you found the warmer day for the top index.',
                        'result[idx] = i - idx gives the number of days to wait.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'A monotonic stack maintains elements in:',
                    'options': ['Random order', 'Sorted order globally', 'Strictly increasing or decreasing order', 'Insertion order'],
                    'answer': 2,
                    'explanation': 'A monotonic stack pops elements that violate the monotonicity property, keeping the stack always sorted.'
                },
                {
                    'question': 'In RPN evaluation, for token "-", operands are popped as b then a. The result is:',
                    'options': ['b - a', 'a - b', 'a + b', '|a - b|'],
                    'answer': 1,
                    'explanation': 'The last pushed operand is b (right operand). a - b respects the original expression order.'
                },
                {
                    'question': 'The amortised time complexity of next_greater using a monotonic stack is:',
                    'options': ['O(n²)', 'O(n log n)', 'O(n)', 'O(1)'],
                    'answer': 2,
                    'explanation': 'Each element is pushed and popped at most once, giving O(n) total work despite the nested loop.'
                },
                {
                    'question': 'In the two-stack queue, the outbox is only refilled when:',
                    'options': ['A new item is pushed', 'The outbox is empty and a pop/peek is needed', 'The inbox overflows', 'Every 10 operations'],
                    'answer': 1,
                    'explanation': 'Lazy transfer: elements are moved from inbox to outbox only when outbox is empty, keeping amortised O(1) per operation.'
                },
                {
                    'question': 'is_valid("([)]") returns False because:',
                    'options': ['Unequal bracket counts', 'The closing ) matches ( but ] was expected on top', 'There are 4 brackets', 'Python rejects mixed brackets'],
                    'answer': 1,
                    'explanation': 'When ) is encountered, the stack top is [ (from the inner [), not (, so the match fails.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Stacks & Queues: Advanced Patterns</h2>
<p>At this level we implement specialised structures — min-stack in O(1), sliding window maximum with a deque, and LRU cache.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>A <strong>monotonic deque</strong> maintains a sliding-window maximum/minimum in O(1) per element by evicting elements that can never be the answer.</p>
</div>

<h3>Min Stack (O(1) getMin)</h3>
<pre><code class="language-python">
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        m = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(m)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self): return self.stack[-1]
    def get_min(self): return self.min_stack[-1]
</code></pre>

<h3>Sliding Window Maximum (Deque)</h3>
<pre><code class="language-python">
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()   # stores indices, front is index of max
    result = []
    for i, v in enumerate(nums):
        while dq and nums[dq[-1]] <= v:
            dq.pop()           # remove smaller elements from back
        dq.append(i)
        if dq[0] == i - k:    # front is outside window
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
# [3, 3, 5, 5, 6, 7]
</code></pre>

<h3>LRU Cache</h3>
<pre><code class="language-python">
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Min Stack',
                    'description': '''<p>Implement a stack that supports push, pop, top, and <strong>get_min</strong> — all in O(1) time.</p>
<pre><code class="language-python">ms = MinStack()
ms.push(3); ms.push(5); ms.push(1)
ms.get_min()  # 1
ms.pop()
ms.get_min()  # 3
</code></pre>''',
                    'starter_code': '''class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []   # tracks running minimum

    def push(self, val):
        self.stack.append(val)
        # TODO: push the new minimum onto min_stack
        pass

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running MinStack tests...")
ms = MinStack()
ms.push(3); ms.push(5); ms.push(1)
_test("min after 3 pushes", ms.get_min(), 1)
ms.pop()
_test("min after pop 1",    ms.get_min(), 3)
ms.push(0)
_test("min after push 0",   ms.get_min(), 0)
_test("top",                ms.top(),     0)
print("All tests passed")
''',
                    'hints': [
                        'min_stack[i] stores the minimum of all elements from the bottom up to index i.',
                        'On push: new_min = min(val, min_stack[-1]) if min_stack else val.',
                        'On pop: pop both stack and min_stack simultaneously.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Sliding Window Maximum',
                    'description': '''<p>Return the maximum value in each sliding window of size <code>k</code> over <code>nums</code>. Use a deque for O(n) time.</p>
<pre><code class="language-python">max_sliding_window([1,3,-1,-3,5,3,6,7], 3)
# [3, 3, 5, 5, 6, 7]
</code></pre>''',
                    'starter_code': '''from collections import deque

def max_sliding_window(nums, k):
    dq = deque()   # indices; front holds index of current max
    result = []
    for i, v in enumerate(nums):
        # Remove elements smaller than v from the back
        while dq and nums[dq[-1]] <= v:
            dq.pop()
        dq.append(i)
        # Remove front if it\'s outside the window
        if dq[0] == i - k:
            dq.popleft()
        # Add to result once we have a full window
        if i >= k - 1:
            # TODO: append the maximum (front of deque) to result
            pass
    return result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Sliding Window Max tests...")
_test("classic", max_sliding_window([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
_test("k=1",     max_sliding_window([4,2,7],1),              [4,2,7])
_test("k=n",     max_sliding_window([1,2,3],3),              [3])
_test("desc",    max_sliding_window([5,4,3,2,1],2),          [5,4,3,2])
print("All tests passed")
''',
                    'hints': [
                        'The deque stores indices in decreasing order of their values.',
                        'Pop from the back when the new element is >= the back element (it\'s useless).',
                        'The front of the deque is always the index of the current window maximum.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In MinStack, why do we maintain a parallel min_stack?',
                    'options': ['To sort the elements', 'To track the minimum at every stack depth in O(1)', 'To reduce memory usage', 'To support peek operations'],
                    'answer': 1,
                    'explanation': 'min_stack[i] records the minimum of all elements up to depth i, so get_min() is a simple O(1) peek.'
                },
                {
                    'question': 'In the sliding window maximum deque, the front always holds:',
                    'options': ['The smallest element in the window', 'The index of the maximum element in the current window', 'The most recently added element', 'The window size'],
                    'answer': 1,
                    'explanation': 'Smaller elements behind a large element can never be the window max, so they are removed; the front is always the largest.'
                },
                {
                    'question': 'LRU cache evicts which entry when full?',
                    'options': ['Most recently used', 'Largest value', 'Least recently used', 'Random entry'],
                    'answer': 2,
                    'explanation': 'LRU = Least Recently Used. The entry accessed longest ago is evicted first.'
                },
                {
                    'question': 'OrderedDict.move_to_end(key) is used in LRU cache to:',
                    'options': ['Delete the key', 'Mark it as most recently used', 'Mark it as least recently used', 'Sort the cache'],
                    'answer': 1,
                    'explanation': 'Moving a key to the end marks it as the most recently used, so the front remains the least recently used.'
                },
                {
                    'question': 'What is the time complexity per element of the deque-based sliding window maximum?',
                    'options': ['O(k)', 'O(n)', 'O(1) amortised', 'O(log n)'],
                    'answer': 2,
                    'explanation': 'Each element is added and removed from the deque at most once, giving O(1) amortised per element.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 5: Binary Trees
    # =========================================================
    5: {
        'intermediate': {
            'content': '''
<h2>Binary Trees: Intermediate Techniques</h2>
<p>Beyond basic traversal lies tree construction, level-order processing, and path problems.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>BFS (level-order) uses a queue; DFS (pre/in/post-order) uses recursion or an explicit stack. Choose based on what you need to collect.</p>
</div>

<h3>Level-Order Traversal (BFS)</h3>
<pre><code class="language-python">
from collections import deque

def level_order(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
</code></pre>

<h3>Maximum Depth</h3>
<pre><code class="language-python">
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
</code></pre>

<h3>Path Sum</h3>
<pre><code class="language-python">
def has_path_sum(root, target):
    if not root: return False
    if not root.left and not root.right:
        return root.val == target
    return (has_path_sum(root.left,  target - root.val) or
            has_path_sum(root.right, target - root.val))
</code></pre>

<h3>Lowest Common Ancestor (BST)</h3>
<pre><code class="language-python">
def lca_bst(root, p, q):
    while root:
        if p < root.val and q < root.val:
            root = root.left
        elif p > root.val and q > root.val:
            root = root.right
        else:
            return root.val
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Level Order Traversal',
                    'description': '''<p>Return the values of a binary tree level by level (BFS). Each level is a separate list.</p>
<pre><code class="language-python">level_order(root)
#      1
#     / \\
#    2   3
#   / \\
#  4   5
# => [[1], [2,3], [4,5]]
</code></pre>''',
                    'starter_code': '''from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree():
    root = TreeNode(1)
    root.left  = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    return root

def level_order(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            # TODO: enqueue left and right children if they exist
        result.append(level)
    return result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Level Order tests...")
root = make_tree()
_test("basic", level_order(root), [[1],[2,3],[4,5]])
_test("empty", level_order(None), [])
single = TreeNode(42)
_test("single", level_order(single), [[42]])
print("All tests passed")
''',
                    'hints': [
                        'Use a deque and process exactly len(queue) nodes per level.',
                        'After popping a node, add its non-None children to the queue.',
                        'Collect node values in a level list, then append that to result.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Maximum Path Sum',
                    'description': '''<p>Find the maximum sum of any root-to-leaf path in a binary tree.</p>
<pre><code class="language-python">max_path_sum(root)
#       1
#      / \\
#     2   3    => 6  (1->2 gives 3, 1->3 gives 4... wait: 1+2=3, 1+3=4 but full paths)
# Actually root=1,left=2,right=3 => max path sum = 1+3 = 4
</code></pre>''',
                    'starter_code': '''class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    def dfs(node):
        if not node: return 0
        # Get max path from left and right children (ignore negatives)
        left  = max(dfs(node.left),  0)
        right = max(dfs(node.right), 0)
        # TODO: return the best single-side path from this node upward
        return node.val + max(left, right)
    return dfs(root)
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Max Path Sum tests...")
r1 = TreeNode(1, TreeNode(2), TreeNode(3))
_test("simple", max_path_sum(r1), 4)
r2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
_test("complex", max_path_sum(r2), 27)
single = TreeNode(7)
_test("single", max_path_sum(single), 7)
print("All tests passed")
''',
                    'hints': [
                        'Use DFS returning the best single-arm path from each node.',
                        'Ignore negative child contributions with max(dfs(child), 0).',
                        'Return node.val + max(left, right) to propagate upward.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Level-order traversal uses which data structure?',
                    'options': ['Stack', 'Queue', 'Set', 'Priority queue'],
                    'answer': 1,
                    'explanation': 'BFS (level-order) uses a FIFO queue to process nodes level by level.'
                },
                {
                    'question': 'max_depth of a tree with only a root node is:',
                    'options': ['0', '1', '2', 'Undefined'],
                    'answer': 1,
                    'explanation': 'The base case returns 0 for None; the root contributes 1, so a single-node tree has depth 1.'
                },
                {
                    'question': 'In has_path_sum, when do we check against the target?',
                    'options': ['At every node', 'Only at leaf nodes', 'Only at the root', 'At nodes with two children'],
                    'answer': 1,
                    'explanation': 'A root-to-leaf path ends at a leaf (no children), so that is the only place to verify the accumulated sum.'
                },
                {
                    'question': 'LCA in a BST works by:',
                    'options': ['Visiting all nodes', 'Moving left if both values are smaller, right if both are larger, else the current node is LCA', 'Counting depths', 'Reversing the tree'],
                    'answer': 1,
                    'explanation': 'BST ordering lets us navigate directly: both < root → go left; both > root → go right; otherwise the root splits them, making it the LCA.'
                },
                {
                    'question': 'In level_order, why do we iterate range(len(queue)) at the start of each outer loop?',
                    'options': ['To limit memory', 'To process exactly the nodes on the current level before new children are added', 'To reverse the level', 'To sort each level'],
                    'answer': 1,
                    'explanation': 'len(queue) captures the number of nodes at the current level. Processing exactly that many nodes ensures we collect one complete level before moving to the next.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Binary Trees: Advanced Patterns</h2>
<p>Serialisation, tree construction from traversals, and diameter calculation push you to master DFS state management.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Any binary tree can be uniquely reconstructed from its preorder + inorder traversals. Serialisation/deserialisation is just structured DFS.</p>
</div>

<h3>Serialize / Deserialize a Binary Tree</h3>
<pre><code class="language-python">
def serialize(root):
    result = []
    def dfs(node):
        if not node: result.append("N"); return
        result.append(str(node.val))
        dfs(node.left); dfs(node.right)
    dfs(root)
    return ",".join(result)

def deserialize(data):
    vals = iter(data.split(","))
    def dfs():
        v = next(vals)
        if v == "N": return None
        node = TreeNode(int(v))
        node.left  = dfs()
        node.right = dfs()
        return node
    return dfs()
</code></pre>

<h3>Diameter of a Binary Tree</h3>
<pre><code class="language-python">
def diameter(root):
    best = [0]
    def depth(node):
        if not node: return 0
        l = depth(node.left)
        r = depth(node.right)
        best[0] = max(best[0], l + r)
        return 1 + max(l, r)
    depth(root)
    return best[0]
</code></pre>

<h3>Build Tree from Preorder + Inorder</h3>
<pre><code class="language-python">
def build_tree(preorder, inorder):
    if not preorder: return None
    root_val = preorder[0]
    idx = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left  = build_tree(preorder[1:idx+1], inorder[:idx])
    root.right = build_tree(preorder[idx+1:],  inorder[idx+1:])
    return root
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Diameter of a Binary Tree',
                    'description': '''<p>The diameter is the length of the longest path between any two nodes (number of edges). It may or may not pass through the root.</p>
<pre><code class="language-python">diameter(root)
#       1
#      / \\
#     2   3
#    / \\
#   4   5    => 3  (path 4->2->1->3 or 5->2->1->3)
</code></pre>''',
                    'starter_code': '''class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter(root):
    best = [0]
    def depth(node):
        if not node: return 0
        l = depth(node.left)
        r = depth(node.right)
        # TODO: update best[0] with l + r (path through this node)
        return 1 + max(l, r)
    depth(root)
    return best[0]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Diameter tests...")
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
_test("classic", diameter(root), 3)
_test("single",  diameter(TreeNode(1)), 0)
line = TreeNode(1, TreeNode(2, TreeNode(3)))
_test("line", diameter(line), 2)
print("All tests passed")
''',
                    'hints': [
                        'depth(node) returns the maximum depth from node downward.',
                        'The diameter through a node = left_depth + right_depth.',
                        'Update best[0] = max(best[0], l + r) before returning.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Serialize and Deserialize a Binary Tree',
                    'description': '''<p>Implement <code>serialize(root)</code> and <code>deserialize(data)</code> so any binary tree can be stored and recovered.</p>
<pre><code class="language-python">root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
assert to_list(deserialize(serialize(root))) == to_list(root)
</code></pre>''',
                    'starter_code': '''class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    result = []
    def dfs(node):
        if not node:
            result.append("N")
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(result)

def deserialize(data):
    vals = iter(data.split(","))
    def dfs():
        v = next(vals)
        if v == "N": return None
        node = TreeNode(int(v))
        # TODO: recursively build left and right subtrees
        return node
    return dfs()

def to_vals(root):
    # Preorder for comparison
    if not root: return []
    return [root.val] + to_vals(root.left) + to_vals(root.right)
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Serialize/Deserialize tests...")
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
_test("roundtrip", to_vals(deserialize(serialize(root))), [1,2,3,4,5])
_test("empty",     to_vals(deserialize(serialize(None))), [])
single = TreeNode(42)
_test("single",    to_vals(deserialize(serialize(single))), [42])
print("All tests passed")
''',
                    'hints': [
                        'Use "N" to represent None nodes in the serialized string.',
                        'Preorder DFS (root, left, right) makes deserialization straightforward.',
                        'In deserialize, build node.left = dfs() then node.right = dfs().',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'The diameter of a tree is the:',
                    'options': ['Height of the tree', 'Number of nodes', 'Longest path between any two nodes (in edges)', 'Width of the widest level'],
                    'answer': 2,
                    'explanation': 'Diameter = maximum number of edges on any path between two nodes; it may pass through any node.'
                },
                {
                    'question': 'In the diameter algorithm, best[0] = max(best[0], l+r) uses a list because:',
                    'options': ['Lists are faster', 'Python closures can mutate mutable objects like lists, unlike reassigning integers', 'It stores multiple diameters', 'Recursion requires lists'],
                    'answer': 1,
                    'explanation': 'In Python 3 a nested function can read an outer integer but cannot rebind it without "nonlocal". A list is a mutable workaround.'
                },
                {
                    'question': 'To serialize a tree we use preorder DFS (root first) because:',
                    'options': ['It is the fastest traversal', 'The root is processed first, making deserialization trivial — the next value is always the root of the current subtree', 'It produces the shortest string', 'Postorder does not work'],
                    'answer': 1,
                    'explanation': 'Preorder guarantees we write the root before its children, so during deserialization the next token is always the root of the current subproblem.'
                },
                {
                    'question': 'build_tree needs both preorder AND inorder because:',
                    'options': ['Preorder alone does not uniquely define the tree', 'Python requires two inputs', 'Inorder is faster to process', 'Preorder gives left subtree size'],
                    'answer': 0,
                    'explanation': 'Preorder identifies the root; inorder tells us which nodes are in the left vs right subtree. Together they uniquely reconstruct the tree.'
                },
                {
                    'question': 'What does depth(None) return in the diameter algorithm?',
                    'options': ['1', '-1', '0', 'None'],
                    'answer': 2,
                    'explanation': 'The base case "if not node: return 0" defines a None node as having depth 0.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 6: Searching Algorithms
    # =========================================================
    6: {
        'intermediate': {
            'content': '''
<h2>Searching: Intermediate Techniques</h2>
<p>Binary search extends far beyond sorted arrays. Any problem with a monotonic predicate ("is X feasible?") can be binary searched on the answer.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>"Binary search on the answer" — if you can check whether a value is feasible in O(n), you can find the optimal value in O(n log n).</p>
</div>

<h3>Search in Rotated Sorted Array</h3>
<pre><code class="language-python">
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[lo] <= nums[mid]:      # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                           # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print(search_rotated([4,5,6,7,0,1,2], 0))  # 4
</code></pre>

<h3>Find Peak Element</h3>
<pre><code class="language-python">
def find_peak(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
</code></pre>

<h3>Binary Search on Answer — Minimum Max Subarray Sum</h3>
<pre><code class="language-python">
def can_split(nums, m, mid):
    parts, cur = 1, 0
    for x in nums:
        if cur + x > mid:
            parts += 1; cur = 0
        cur += x
    return parts <= m

def split_array(nums, m):
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_split(nums, m, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Search in Rotated Sorted Array',
                    'description': '''<p>A sorted array was rotated at an unknown pivot. Find the index of <code>target</code>, or return -1 if not found. O(log n) required.</p>
<pre><code class="language-python">search_rotated([4,5,6,7,0,1,2], 0)  # 4
search_rotated([4,5,6,7,0,1,2], 3)  # -1
</code></pre>''',
                    'starter_code': '''def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # Determine which half is sorted
        if nums[lo] <= nums[mid]:   # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                        # right half is sorted
            # TODO: handle search in the sorted right half
            pass
    return -1
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Rotated Search tests...")
_test("find 0",     search_rotated([4,5,6,7,0,1,2], 0), 4)
_test("not found",  search_rotated([4,5,6,7,0,1,2], 3), -1)
_test("find 4",     search_rotated([4,5,6,7,0,1,2], 4), 0)
_test("no rotate",  search_rotated([1,2,3,4,5], 3),     2)
print("All tests passed")
''',
                    'hints': [
                        'Determine which half is sorted by comparing nums[lo] and nums[mid].',
                        'If the right half is sorted and target is in (nums[mid], nums[hi]], move lo up.',
                        'Otherwise move hi down.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Find Minimum in Rotated Sorted Array',
                    'description': '''<p>Find the minimum element in a rotated sorted array in O(log n).</p>
<pre><code class="language-python">find_min([3,4,5,1,2])  # 1
find_min([4,5,6,7,0,1,2])  # 0
find_min([1])  # 1
</code></pre>''',
                    'starter_code': '''def find_min(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            # Minimum is in the right half
            lo = mid + 1
        else:
            # TODO: minimum is in the left half (including mid)
            pass
    return nums[lo]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Find Min tests...")
_test("basic",   find_min([3,4,5,1,2]),       1)
_test("longer",  find_min([4,5,6,7,0,1,2]),   0)
_test("single",  find_min([1]),               1)
_test("no rot",  find_min([1,2,3,4,5]),       1)
print("All tests passed")
''',
                    'hints': [
                        'Compare nums[mid] with nums[hi] (not nums[lo]) to decide which half has the minimum.',
                        'If nums[mid] > nums[hi], the rotation point is in the right half: lo = mid + 1.',
                        'Otherwise hi = mid (mid could be the minimum itself).',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In a rotated sorted array search, the key insight is:',
                    'options': ['One of the two halves is always sorted', 'The pivot is always at the middle', 'The array has no duplicates', 'Binary search cannot be applied'],
                    'answer': 0,
                    'explanation': 'After computing mid, at least one of [lo..mid] or [mid..hi] must be sorted. We use that sorted half to decide which direction to search.'
                },
                {
                    'question': '"Binary search on the answer" works when:',
                    'options': ['The answer space is random', 'There is a monotonic feasibility function over the answer space', 'The input is sorted', 'The answer is always the median'],
                    'answer': 1,
                    'explanation': 'If "is answer <= X feasible?" transitions from False to True at exactly one point, binary search finds that point.'
                },
                {
                    'question': 'find_peak compares nums[mid] with nums[mid+1]. If nums[mid] < nums[mid+1]:',
                    'options': ['The peak is to the left', 'The peak is to the right (move lo = mid+1)', 'mid is the peak', 'The array is sorted'],
                    'answer': 1,
                    'explanation': 'The slope is rising to the right, so the peak must be somewhere to the right (or at mid+1).'
                },
                {
                    'question': 'In find_min for a rotated array, we compare nums[mid] with nums[hi] because:',
                    'options': ['nums[lo] is always the minimum', 'Comparing with hi tells us which side the rotation discontinuity is on', 'mid is always the rotation point', 'lo is undefined'],
                    'answer': 1,
                    'explanation': 'If nums[mid] > nums[hi], the drop (rotation point) is to the right of mid. Otherwise it is at or to the left of mid.'
                },
                {
                    'question': 'What is the time complexity of binary search?',
                    'options': ['O(n)', 'O(n log n)', 'O(log n)', 'O(1)'],
                    'answer': 2,
                    'explanation': 'Each iteration halves the search space, giving log₂(n) iterations — O(log n) time.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Searching: Advanced Patterns</h2>
<p>At this level we search in 2D matrices, combine binary search with other structures, and understand how search underpins many optimisation algorithms.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>A sorted 2D matrix can be treated as a flattened 1D array for binary search, or traversed from a corner using the staircase search in O(m+n).</p>
</div>

<h3>Search a 2D Matrix</h3>
<pre><code class="language-python">
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target: return True
        elif val < target: lo = mid + 1
        else: hi = mid - 1
    return False
</code></pre>

<h3>Kth Smallest in Sorted Matrix</h3>
<pre><code class="language-python">
def kth_smallest(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[-1][-1]
    while lo < hi:
        mid = (lo + hi) // 2
        count = sum(
            min(bisect.bisect_right(row, mid), n)
            for row in matrix
        )
        if count < k: lo = mid + 1
        else: hi = mid
    return lo
</code></pre>

<h3>Median of Two Sorted Arrays</h3>
<pre><code class="language-python">
def find_median(A, B):
    if len(A) > len(B): A, B = B, A
    m, n = len(A), len(B)
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = (m + n + 1) // 2 - i
        maxA = A[i-1] if i > 0 else float(\'-inf\')
        minA = A[i]   if i < m else float(\'inf\')
        maxB = B[j-1] if j > 0 else float(\'-inf\')
        minB = B[j]   if j < n else float(\'inf\')
        if maxA <= minB and maxB <= minA:
            if (m + n) % 2 == 0:
                return (max(maxA, maxB) + min(minA, minB)) / 2
            return max(maxA, maxB)
        elif maxA > minB: hi = i - 1
        else: lo = i + 1
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Search a 2D Matrix',
                    'description': '''<p>Each row of the matrix is sorted left-to-right, and the first element of each row is greater than the last element of the previous row. Search for <code>target</code> in O(log(m·n)).</p>
<pre><code class="language-python">matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
search_matrix(matrix, 3)   # True
search_matrix(matrix, 13)  # False
</code></pre>''',
                    'starter_code': '''def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        # Convert flat index to 2D coordinates
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            # TODO: move hi
            pass
    return False
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running 2D Matrix Search tests...")
m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
_test("found 3",    search_matrix(m, 3),  True)
_test("not found",  search_matrix(m, 13), False)
_test("first elem", search_matrix(m, 1),  True)
_test("last elem",  search_matrix(m, 60), True)
print("All tests passed")
''',
                    'hints': [
                        'Treat the matrix as a flat sorted array of m*n elements.',
                        'mid // n gives the row; mid % n gives the column.',
                        'The logic is identical to standard binary search once you have val.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Capacity to Ship Packages (Binary Search on Answer)',
                    'description': '''<p>Given package weights and <code>days</code>, return the minimum ship capacity such that all packages can be shipped within <code>days</code> days (maintaining order).</p>
<pre><code class="language-python">ship_capacity([1,2,3,4,5,6,7,8,9,10], 5)  # 15
ship_capacity([3,2,2,4,1,4], 3)             # 6
</code></pre>''',
                    'starter_code': '''def ship_capacity(weights, days):
    def can_ship(capacity):
        day_count, load = 1, 0
        for w in weights:
            if load + w > capacity:
                day_count += 1
                load = 0
            load += w
        return day_count <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(mid):
            hi = mid
        else:
            # TODO: minimum capacity must be higher
            pass
    return lo
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Ship Capacity tests...")
_test("classic", ship_capacity([1,2,3,4,5,6,7,8,9,10], 5), 15)
_test("simple",  ship_capacity([3,2,2,4,1,4], 3),           6)
_test("1 day",   ship_capacity([1,2,3], 1),                  6)
_test("all 1",   ship_capacity([1,1,1,1], 2),                2)
print("All tests passed")
''',
                    'hints': [
                        'The minimum possible capacity is max(weights) (each package must fit).',
                        'The maximum possible capacity is sum(weights) (ship everything in 1 day).',
                        'Binary search between lo and hi; if can_ship(mid) is True, try smaller: hi = mid.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In the 2D matrix search, mid // n gives:',
                    'options': ['The column index', 'The row index', 'The value at mid', 'The number of rows'],
                    'answer': 1,
                    'explanation': 'Integer division of the flat index by the number of columns n gives the row; the remainder (mid % n) gives the column.'
                },
                {
                    'question': 'In "binary search on the answer", the search space is:',
                    'options': ['The input array', 'The range of possible answer values', 'The indices', 'The number of test cases'],
                    'answer': 1,
                    'explanation': 'We binary search over all possible answer values (e.g. capacities) and use a feasibility check to narrow down.'
                },
                {
                    'question': 'The staircase search on an m×n matrix starts from:',
                    'options': ['Top-left corner', 'Bottom-right corner', 'Top-right (or bottom-left) corner', 'Centre'],
                    'answer': 2,
                    'explanation': 'Starting from the top-right (or bottom-left) corner, we can always eliminate a row or column per step, giving O(m+n).'
                },
                {
                    'question': 'Median of two sorted arrays has time complexity:',
                    'options': ['O(m+n)', 'O((m+n) log(m+n))', 'O(log(min(m,n)))', 'O(mn)'],
                    'answer': 2,
                    'explanation': 'We binary search on the shorter array, halving the shorter array each iteration — O(log(min(m,n))).'
                },
                {
                    'question': 'In ship_capacity, lo is initialised to max(weights) because:',
                    'options': ['It is a random starting point', 'The ship must carry at least the heaviest single package', 'It is the expected answer', 'min always equals max'],
                    'answer': 1,
                    'explanation': 'A capacity smaller than the heaviest package cannot ship that package at all, making it infeasible.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 7: Sorting Algorithms
    # =========================================================
    7: {
        'intermediate': {
            'content': '''
<h2>Sorting: Intermediate Techniques</h2>
<p>Now that you know the basics, we implement merge sort and quicksort — the workhorses of competitive programming and system design.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Merge sort guarantees O(n log n) and is stable; quicksort is O(n log n) on average with O(1) extra space but can degrade to O(n²) on bad pivots.</p>
</div>

<h3>Merge Sort</h3>
<pre><code class="language-python">
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
</code></pre>

<h3>Quicksort with Lomuto Partition</h3>
<pre><code class="language-python">
def quicksort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo < hi:
        pivot_idx = partition(arr, lo, hi)
        quicksort(arr, lo, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1
</code></pre>

<h3>Counting Sort (for integers in known range)</h3>
<pre><code class="language-python">
def counting_sort(arr, max_val):
    counts = [0] * (max_val + 1)
    for x in arr: counts[x] += 1
    result = []
    for v, c in enumerate(counts):
        result.extend([v] * c)
    return result

print(counting_sort([4,2,2,8,3,3,1], 8))
# [1, 2, 2, 3, 3, 4, 8]
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Implement Merge Sort',
                    'description': '''<p>Implement <code>merge_sort(arr)</code> that returns a new sorted list using the divide-and-conquer merge sort algorithm.</p>
<pre><code class="language-python">merge_sort([5,2,8,1,9,3])  # [1,2,3,5,8,9]
merge_sort([])             # []
</code></pre>''',
                    'starter_code': '''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # TODO: append the smaller element and advance its pointer
        pass
    # Append any remaining elements
    return result + left[i:] + right[j:]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Merge Sort tests...")
_test("basic",     merge_sort([5,2,8,1,9,3]), [1,2,3,5,8,9])
_test("empty",     merge_sort([]),            [])
_test("single",    merge_sort([7]),           [7])
_test("sorted",    merge_sort([1,2,3]),       [1,2,3])
_test("reversed",  merge_sort([3,2,1]),       [1,2,3])
_test("dups",      merge_sort([3,1,2,3,1]),   [1,1,2,3,3])
print("All tests passed")
''',
                    'hints': [
                        'Compare left[i] and right[j]; append the smaller one and advance that pointer.',
                        'After the while loop, append any remaining elements with result + left[i:] + right[j:].',
                        'merge_sort recursively sorts the two halves before merging.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Sort Colors (Dutch National Flag)',
                    'description': '''<p>Given an array containing only 0, 1, and 2, sort it in-place in one pass without using Python\'s sort.</p>
<pre><code class="language-python">arr = [2,0,2,1,1,0]
sort_colors(arr)
arr  # [0,0,1,1,2,2]
</code></pre>''',
                    'starter_code': '''def sort_colors(nums):
    lo, mid, hi = 0, 0, len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            # TODO: swap nums[mid] with nums[hi] and shrink hi
            pass
    return nums
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Sort Colors tests...")
_test("classic", sort_colors([2,0,2,1,1,0]), [0,0,1,1,2,2])
_test("all 0s",  sort_colors([0,0,0]),       [0,0,0])
_test("all 2s",  sort_colors([2,2,2]),       [2,2,2])
_test("mixed",   sort_colors([1,0,2]),       [0,1,2])
print("All tests passed")
''',
                    'hints': [
                        'Three pointers: lo (next 0 position), mid (current), hi (next 2 position).',
                        'If nums[mid]==2: swap with nums[hi] and decrement hi (do NOT increment mid — the swapped value is unchecked).',
                        'If nums[mid]==0: swap with nums[lo], increment both lo and mid.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Merge sort is stable because:',
                    'options': ['It uses recursion', 'Equal elements maintain their relative order from the original array', 'It is in-place', 'It uses a pivot'],
                    'answer': 1,
                    'explanation': 'When merging, equal elements from the left half are chosen first (left[i] <= right[j]), preserving original order.'
                },
                {
                    'question': 'What is the worst-case time complexity of quicksort?',
                    'options': ['O(n log n)', 'O(n)', 'O(n²)', 'O(log n)'],
                    'answer': 2,
                    'explanation': 'When the pivot is always the smallest or largest element (e.g., sorted input with last-element pivot), partitioning is unbalanced and O(n²) results.'
                },
                {
                    'question': 'Counting sort is NOT applicable when:',
                    'options': ['The array has duplicates', 'The range of values is unknown or very large', 'The array is already sorted', 'The array has negative numbers'],
                    'answer': 1,
                    'explanation': 'Counting sort needs an array of size max_value+1. If the range is huge, memory usage becomes impractical.'
                },
                {
                    'question': 'In Lomuto partition, after the loop we swap arr[i+1] with arr[hi]. This places:',
                    'options': ['The pivot at the start', 'The pivot in its correct sorted position', 'The largest element at the end', 'Nothing — it is a no-op'],
                    'answer': 1,
                    'explanation': 'i+1 is the first position where elements are > pivot. Swapping puts the pivot there, correctly partitioning the array.'
                },
                {
                    'question': 'In Dutch National Flag, why do we NOT increment mid after swapping with hi?',
                    'options': ['mid is already correct', 'The value swapped from hi is unchecked — it might be 0, 1, or 2', 'hi has already been processed', 'mid only moves left'],
                    'answer': 1,
                    'explanation': 'The element swapped from position hi is new and unclassified. We must inspect it at the current mid position before moving forward.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Sorting: Advanced Patterns</h2>
<p>At the advanced level, we use sorting as a stepping stone: custom comparators, external sort, and problems where the act of sorting itself encodes the solution.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Heap sort achieves O(n log n) in-place with O(1) extra space. Tim sort (Python\'s built-in) is a hybrid merge/insertion sort optimised for real-world data.</p>
</div>

<h3>Heap Sort</h3>
<pre><code class="language-python">
def heapify(arr, n, i):
    largest = i
    l, r = 2*i+1, 2*i+2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
</code></pre>

<h3>Largest Number (Custom Comparator)</h3>
<pre><code class="language-python">
import functools

def largest_number(nums):
    strs = [str(x) for x in nums]
    strs.sort(key=functools.cmp_to_key(
        lambda a, b: (1 if a+b > b+a else -1 if a+b < b+a else 0)
    ), reverse=True)
    result = "".join(strs)
    return "0" if result[0] == "0" else result

print(largest_number([3,30,34,5,9]))  # "9534330"
</code></pre>

<h3>K Closest Points to Origin</h3>
<pre><code class="language-python">
import heapq

def k_closest(points, k):
    return heapq.nsmallest(
        k, points,
        key=lambda p: p[0]**2 + p[1]**2
    )

print(k_closest([[1,3],[-2,2],[5,8]], 1))  # [[-2,2]]
</code></pre>

<h3>Tim Sort internals (overview)</h3>
<p>Python\'s <code>list.sort()</code> uses Tim sort — a hybrid of merge sort and insertion sort. It detects natural runs of already-sorted data (real-world lists are often partially sorted), uses insertion sort for short runs (&lt; 64 elements), and merges runs with a merge strategy that keeps the run stack balanced.</p>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Largest Number',
                    'description': '''<p>Given a list of non-negative integers, arrange them to form the largest possible number and return it as a string.</p>
<pre><code class="language-python">largest_number([3,30,34,5,9])  # "9534330"
largest_number([10,2])          # "210"
</code></pre>''',
                    'starter_code': '''import functools

def largest_number(nums):
    strs = [str(x) for x in nums]
    def compare(a, b):
        # TODO: return 1 if a+b should come before b+a, -1 otherwise
        if a + b > b + a:
            return 1
        elif a + b < b + a:
            return -1
        return 0
    strs.sort(key=functools.cmp_to_key(compare), reverse=True)
    result = "".join(strs)
    # Edge case: all zeros
    return "0" if result[0] == "0" else result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Largest Number tests...")
_test("classic",  largest_number([3,30,34,5,9]), "9534330")
_test("pair",     largest_number([10,2]),          "210")
_test("all zeros",largest_number([0,0]),           "0")
_test("single",   largest_number([5]),             "5")
print("All tests passed")
''',
                    'hints': [
                        'Convert all numbers to strings first.',
                        'Comparator: a should come before b if a+b > b+a (string concatenation comparison).',
                        'Sort in descending order of the custom comparator, then join.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Meeting Rooms II (Min Heap)',
                    'description': '''<p>Given meeting intervals, return the minimum number of conference rooms required.</p>
<pre><code class="language-python">min_rooms([[0,30],[5,10],[15,20]])  # 2
min_rooms([[7,10],[2,4]])           # 1
</code></pre>''',
                    'starter_code': '''import heapq

def min_rooms(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x: x[0])
    heap = []   # stores end times of ongoing meetings
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)   # room becomes free
        # TODO: push current meeting's end time onto heap
    return len(heap)
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Meeting Rooms tests...")
_test("classic", min_rooms([[0,30],[5,10],[15,20]]), 2)
_test("no overlap", min_rooms([[7,10],[2,4]]),       1)
_test("all overlap",min_rooms([[1,10],[2,9],[3,8]]), 3)
_test("empty",   min_rooms([]),                      0)
print("All tests passed")
''',
                    'hints': [
                        'Sort meetings by start time.',
                        'Use a min-heap of end times. If the earliest-ending meeting finishes before the new start, reuse its room.',
                        'The heap size at the end is the number of rooms needed.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Heap sort has space complexity:',
                    'options': ['O(n)', 'O(log n)', 'O(1)', 'O(n log n)'],
                    'answer': 2,
                    'explanation': 'Heap sort sorts in-place using only O(1) extra space (the recursive heapify call stack is O(log n) but typically considered negligible).'
                },
                {
                    'question': 'In largest_number, why do we compare a+b with b+a as strings?',
                    'options': ['String comparison is faster', 'Concatenation order determines which arrangement produces the larger number', 'Numeric comparison would overflow', 'Python requires string comparison'],
                    'answer': 1,
                    'explanation': 'If "34" + "3" = "343" > "3" + "34" = "334", then 34 should come first. String comparison of the concatenated pairs is the correct ordering.'
                },
                {
                    'question': 'In meeting rooms, a min-heap of end times allows us to:',
                    'options': ['Find the longest meeting', 'Check in O(log n) whether the earliest-ending room is free for the next meeting', 'Sort meetings', 'Count unique start times'],
                    'answer': 1,
                    'explanation': 'heap[0] is always the earliest end time. If it is <= the new meeting\'s start, that room is free — a O(1) check with O(log n) pop/push.'
                },
                {
                    'question': 'Tim sort performs insertion sort on runs shorter than:',
                    'options': ['8 elements', '32 elements', '64 elements', '128 elements'],
                    'answer': 2,
                    'explanation': 'Tim sort uses insertion sort for runs shorter than ~64 elements (the "minrun" threshold), because insertion sort is very fast on small or nearly-sorted arrays.'
                },
                {
                    'question': 'heapq in Python implements a:',
                    'options': ['Max-heap', 'Min-heap', 'Balanced BST', 'Sorted list'],
                    'answer': 1,
                    'explanation': 'Python\'s heapq is a min-heap — heap[0] is always the smallest element.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 8 — Hash Tables  (already defined above)
    # =========================================================
    8: {
        'intermediate': {
            'content': '''
<h2>Hash Tables: Intermediate Techniques</h2>
<p>Python dicts and sets are hash tables. At this level we master frequency counting patterns, two-sum variants, and LRU-style caching.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Most "find a pair/triple" problems can be reduced to a single-pass O(n) scan using a hash set or hash map to store previously seen values.</p>
</div>

<h3>Two Sum (Unsorted)</h3>
<pre><code class="language-python">
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i

print(two_sum([2,7,11,15], 9))  # [0,1]
</code></pre>

<h3>Subarray Sum Equals K (Prefix Hash)</h3>
<pre><code class="language-python">
def subarray_sum(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count

print(subarray_sum([1,1,1], 2))  # 2
</code></pre>

<h3>Longest Consecutive Sequence</h3>
<pre><code class="language-python">
def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for n in s:
        if n - 1 not in s:      # start of a sequence
            length = 1
            while n + length in s:
                length += 1
            best = max(best, length)
    return best

print(longest_consecutive([100,4,200,1,3,2]))  # 4
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Two Sum',
                    'description': '''<p>Given an unsorted list and a <code>target</code>, return the indices of the two numbers that add up to the target. Each input has exactly one solution.</p>
<pre><code class="language-python">two_sum([2,7,11,15], 9)   # [0,1]
two_sum([3,2,4], 6)        # [1,2]
</code></pre>''',
                    'starter_code': '''def two_sum(nums, target):
    seen = {}   # value -> index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        # TODO: store x in seen with its index
    return []
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if sorted(got) == sorted(exp): _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Two Sum tests...")
_test("basic",    two_sum([2,7,11,15], 9),  [0,1])
_test("middle",   two_sum([3,2,4], 6),      [1,2])
_test("neg",      two_sum([-1,-2,-3,-4,-5], -8), [2,4])
_test("same val", two_sum([3,3], 6),        [0,1])
print("All tests passed")
''',
                    'hints': [
                        'For each element x, check if target - x is already in the seen dict.',
                        'If yes, return [seen[complement], i].',
                        'After checking, store seen[x] = i.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Longest Consecutive Sequence',
                    'description': '''<p>Given an unsorted list, return the length of the longest sequence of consecutive integers. Must run in O(n).</p>
<pre><code class="language-python">longest_consecutive([100,4,200,1,3,2])  # 4  (1,2,3,4)
longest_consecutive([0,3,7,2,5,8,4,6,0,1])  # 9
</code></pre>''',
                    'starter_code': '''def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for n in s:
        if n - 1 not in s:   # n is the start of a sequence
            length = 1
            while n + length in s:
                # TODO: extend the sequence
                pass
            best = max(best, length)
    return best
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Longest Consecutive tests...")
_test("classic",  longest_consecutive([100,4,200,1,3,2]),      4)
_test("long",     longest_consecutive([0,3,7,2,5,8,4,6,0,1]), 9)
_test("empty",    longest_consecutive([]),                      0)
_test("single",   longest_consecutive([5]),                    1)
print("All tests passed")
''',
                    'hints': [
                        'Convert nums to a set for O(1) lookups.',
                        'Only start counting from n where n-1 is NOT in the set (sequence start).',
                        'Inside the while loop, increment length to extend the sequence.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Two Sum uses a hash map instead of sorting because:',
                    'options': ['Sorting is wrong', 'Hash map gives O(n) time vs O(n log n) for sort + two pointers', 'Hash maps are always faster', 'The array is unsorted'],
                    'answer': 1,
                    'explanation': 'A single O(n) pass with a hash map (O(1) lookup) beats the O(n log n) sort + O(n) two-pointer approach.'
                },
                {
                    'question': 'In subarray_sum, {0:1} is initialised in seen because:',
                    'options': ['To avoid key errors', 'A prefix sum equal to k means a subarray from index 0 to the current index sums to k', 'To count the empty subarray', 'It is required by Python'],
                    'answer': 1,
                    'explanation': 'If prefix[i] - k == 0, then the subarray from the start (index 0) to i has sum k. Starting with {0:1} counts this case correctly.'
                },
                {
                    'question': 'In longest_consecutive, why do we only start counting when n-1 is NOT in the set?',
                    'options': ['To avoid revisiting numbers mid-sequence', 'n-1 is always negative', 'Sets do not support subtraction', 'To find the maximum element'],
                    'answer': 0,
                    'explanation': 'Starting only at sequence beginnings (where no predecessor exists) avoids re-scanning the same sequence from every element, keeping the overall time O(n).'
                },
                {
                    'question': 'The average time complexity of a dict lookup in Python is:',
                    'options': ['O(n)', 'O(log n)', 'O(1)', 'O(n²)'],
                    'answer': 2,
                    'explanation': 'Python dicts are hash tables with O(1) average-case get/set due to direct hashing.'
                },
                {
                    'question': 'Which Python type should you use for O(1) membership testing?',
                    'options': ['list', 'tuple', 'set', 'deque'],
                    'answer': 2,
                    'explanation': 'set uses a hash table internally, giving O(1) average-case "in" checks. list "in" is O(n).'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Hash Tables: Advanced Patterns</h2>
<p>Advanced hash table problems involve designing custom data structures, handling collisions carefully, and combining hashing with other techniques.</p>

<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Many "O(1) with history" problems are solved by combining a hash map (for fast lookup) with a doubly-linked list (for fast order maintenance) — the LRU cache pattern.</p>
</div>

<h3>LRU Cache (Full Implementation)</h3>
<pre><code class="language-python">
class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key; self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head = DLinkedNode()   # dummy head (most recent)
        self.tail = DLinkedNode()   # dummy tail (least recent)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self._remove(node); self._add_to_front(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DLinkedNode(key, value)
        self.cache[key] = node
        self._add_to_front(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
</code></pre>

<h3>Design HashMap from Scratch</h3>
<pre><code class="language-python">
class MyHashMap:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key): return key % self.size

    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value); return
        bucket.append((key, value))

    def get(self, key):
        for k, v in self.buckets[self._hash(key)]:
            if k == key: return v
        return -1

    def remove(self, key):
        b = self.buckets[self._hash(key)]
        self.buckets[self._hash(key)] = [(k,v) for k,v in b if k != key]
</code></pre>

<h3>Consistent Hashing (concept)</h3>
<p>In distributed systems, consistent hashing maps both servers and keys onto a circular ring. When a server is added or removed, only keys that "wrap around" to the new server boundary are remapped — O(k/n) keys move instead of O(k).</p>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Design HashMap',
                    'description': '''<p>Implement a hash map from scratch supporting <code>put</code>, <code>get</code>, and <code>remove</code> without using Python\'s built-in dict.</p>
<p>Use separate chaining (list of buckets) to handle collisions.</p>
<pre><code class="language-python">m = MyHashMap()
m.put(1, 10); m.put(2, 20)
m.get(1)     # 10
m.get(3)     # -1
m.remove(1)
m.get(1)     # -1
</code></pre>''',
                    'starter_code': '''class MyHashMap:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        for k, v in self.buckets[self._hash(key)]:
            if k == key:
                return v
        # TODO: return -1 if key not found
        pass

    def remove(self, key):
        h = self._hash(key)
        # TODO: rebuild the bucket without the matching key
        pass
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running MyHashMap tests...")
m = MyHashMap()
m.put(1, 10); m.put(2, 20)
_test("get 1",    m.get(1),  10)
_test("get miss", m.get(3),  -1)
m.put(1, 99)
_test("update",   m.get(1),  99)
m.remove(1)
_test("after del",m.get(1),  -1)
_test("get 2",    m.get(2),  20)
print("All tests passed")
''',
                    'hints': [
                        'get: iterate the bucket; return v if k == key; return -1 at the end.',
                        'remove: rebuild the bucket list filtering out the matching key.',
                        'Use self.buckets[self._hash(key)] to access the right bucket.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Find All Duplicates in an Array',
                    'description': '''<p>Given an array of n integers where each integer is in [1, n], find all elements that appear <strong>twice</strong>. Solve in O(n) time and O(1) extra space (no extra set/dict).</p>
<pre><code class="language-python">find_duplicates([4,3,2,7,8,2,3,1])  # [2,3]  (any order)
find_duplicates([1,1,2])             # [1]
</code></pre>''',
                    'starter_code': '''def find_duplicates(nums):
    result = []
    for x in nums:
        idx = abs(x) - 1       # map value to index
        if nums[idx] < 0:
            result.append(abs(x))   # seen before
        else:
            nums[idx] = -nums[idx]  # mark as visited
    # Restore the array (optional but clean)
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    # TODO: return result
    pass
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")

def _test(label, got, exp):
    if sorted(got) == sorted(exp): _pass(f"{label} => {sorted(got)}")
    else: _fail(f"{label}: expected {sorted(exp)}, got {sorted(got)}")

print("Running Find Duplicates tests...")
_test("classic",  find_duplicates([4,3,2,7,8,2,3,1]), [2,3])
_test("one dup",  find_duplicates([1,1,2]),            [1])
_test("no dup",   find_duplicates([1,2,3]),            [])
print("All tests passed")
''',
                    'hints': [
                        'Use the sign of nums[abs(x)-1] as a "visited" flag.',
                        'If the element at the mapped index is already negative, the value has been seen before — it\'s a duplicate.',
                        'Return result after the loop.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In a doubly-linked list LRU cache, why is removal O(1)?',
                    'options': ['Because the list is sorted', 'Because each node stores both prev and next pointers, allowing direct unlinking', 'Because Python lists have O(1) remove', 'Because the cache is small'],
                    'answer': 1,
                    'explanation': 'With prev and next pointers, removing a node is just two pointer updates — no traversal needed.'
                },
                {
                    'question': 'In separate chaining, what happens on a hash collision?',
                    'options': ['The old value is overwritten', 'A new bucket is created', 'The new key-value pair is appended to the existing bucket list', 'The insert fails'],
                    'answer': 2,
                    'explanation': 'Separate chaining stores all keys that hash to the same index in a list (chain) at that bucket.'
                },
                {
                    'question': 'The find_duplicates trick uses the array\'s own values as:',
                    'options': ['Counters', 'Indices into a visited flags encoded via sign', 'Sorted keys', 'Backup storage'],
                    'answer': 1,
                    'explanation': 'Values are in [1,n] so abs(x)-1 maps each value to a valid index. Negating the element at that index encodes "seen" without extra space.'
                },
                {
                    'question': 'What is the average load factor threshold before a hash table resizes?',
                    'options': ['0.25', '0.5', '0.75', '1.0'],
                    'answer': 2,
                    'explanation': 'Most implementations (including Python\'s dict) resize when the load factor exceeds ~0.75 to balance memory and collision rate.'
                },
                {
                    'question': 'Consistent hashing is useful in distributed systems because:',
                    'options': ['It sorts data', 'It minimises the number of keys that need to be remapped when servers are added/removed', 'It prevents collisions', 'It requires no hash function'],
                    'answer': 1,
                    'explanation': 'With consistent hashing on a ring, only O(k/n) keys move when a server is added or removed, versus O(k) with a naive modulo hash.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 9: Graphs
    # =========================================================
    9: {
        'intermediate': {
            'content': '''
<h2>Graphs: Intermediate Techniques</h2>
<p>You know BFS and DFS basics. Now apply them to detect cycles, find connected components, and solve shortest-path problems on unweighted graphs.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>BFS gives shortest paths on unweighted graphs; DFS gives cycle detection and topological order. Both run in O(V+E).</p>
</div>
<h3>BFS Shortest Path</h3>
<pre><code class="language-python">
from collections import deque

def bfs_shortest(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == end: return path
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, path + [nbr]))
    return []
</code></pre>
<h3>Connected Components (DFS)</h3>
<pre><code class="language-python">
def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b); graph[b].append(a)
    visited = set()
    count = 0
    def dfs(node):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited: dfs(nbr)
    for i in range(n):
        if i not in visited:
            dfs(i); count += 1
    return count
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Number of Islands',
                    'description': '''<p>Given an m x n grid of "1" (land) and "0" (water), count the number of islands using DFS.</p>
<pre><code class="language-python">grid = [["1","1","0"],["0","1","0"],["0","0","1"]]
num_islands(grid)  # 2
</code></pre>''',
                    'starter_code': '''def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

import copy
print("Running Num Islands tests...")
g1 = [["1","1","0"],["0","1","0"],["0","0","1"]]
_test("two islands", num_islands(copy.deepcopy(g1)), 2)
g2 = [["1","1","1"],["0","1","0"],["1","1","1"]]
_test("one island",  num_islands(copy.deepcopy(g2)), 1)
g3 = [["0","0"],["0","0"]]
_test("no island",   num_islands(copy.deepcopy(g3)), 0)
print("All tests passed")
''',
                    'hints': [
                        'DFS from each "1" cell, marking visited cells as "0".',
                        'Each top-level DFS call represents one island.',
                        'Increment count after each DFS call.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Number of Connected Components',
                    'description': '''<p>Given n nodes and a list of undirected edges, return the number of connected components using DFS.</p>
<pre><code class="language-python">count_components(5, [[0,1],[1,2],[3,4]])  # 2
</code></pre>''',
                    'starter_code': '''def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfs(nbr)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1
    return count
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Connected Components tests...")
_test("two comps",  count_components(5, [[0,1],[1,2],[3,4]]), 2)
_test("all linked", count_components(4, [[0,1],[1,2],[2,3]]), 1)
_test("no edges",   count_components(3, []),                  3)
print("All tests passed")
''',
                    'hints': [
                        'Build an adjacency list for the undirected graph.',
                        'DFS from each unvisited node, marking all reachable nodes as visited.',
                        'Each top-level DFS call is one connected component.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'BFS on an unweighted graph finds the shortest path measured by:',
                    'options': ['Total weight', 'Number of edges', 'Number of vertices visited', 'Alphabetical order'],
                    'answer': 1,
                    'explanation': 'BFS explores layer by layer; the first time a node is reached it is via the fewest edges.'
                },
                {
                    'question': 'In num_islands DFS, why set grid[r][c]="0" instead of using a visited set?',
                    'options': ['It is faster', 'It modifies in-place avoiding extra O(m*n) memory', 'It sorts the grid', 'It is required by Python'],
                    'answer': 1,
                    'explanation': 'Marking cells in-place avoids allocating a separate visited matrix, using O(1) extra space (besides the recursion stack).'
                },
                {
                    'question': 'An adjacency list uses O(V+E) space. An adjacency matrix uses:',
                    'options': ['O(V)', 'O(E)', 'O(V²)', 'O(V*E)'],
                    'answer': 2,
                    'explanation': 'An adjacency matrix has a cell for every pair (i,j), so V² cells regardless of the number of edges.'
                },
                {
                    'question': 'How many connected components does a tree with n nodes have?',
                    'options': ['n', 'n-1', '1', '2'],
                    'answer': 2,
                    'explanation': 'A tree is by definition a connected acyclic graph — it always has exactly 1 connected component.'
                },
                {
                    'question': 'DFS time complexity on a graph with V vertices and E edges is:',
                    'options': ['O(V²)', 'O(V+E)', 'O(E log V)', 'O(V log E)'],
                    'answer': 1,
                    'explanation': 'Each vertex is visited once (O(V)) and each edge is examined once from each endpoint (O(E)).'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Graphs: Advanced Patterns</h2>
<p>Dijkstra, Bellman-Ford, topological sort, and Union-Find for hard competitive-programming graph problems.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Dijkstra gives single-source shortest paths on non-negative weights in O((V+E) log V) with a min-heap.</p>
</div>
<h3>Dijkstra Algorithm</h3>
<pre><code class="language-python">
import heapq

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
</code></pre>
<h3>Topological Sort (Kahn BFS)</h3>
<pre><code class="language-python">
from collections import deque

def topo_sort(n, edges):
    indegree = [0]*n; adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); indegree[v] += 1
    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while queue:
        u = queue.popleft(); order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0: queue.append(v)
    return order if len(order) == n else []
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Network Delay Time (Dijkstra)',
                    'description': '''<p>Find the minimum time for a signal from node <code>k</code> to reach all n nodes. Return -1 if not possible.</p>
<pre><code class="language-python">network_delay([[2,1,1],[2,3,1],[3,4,1]], 4, 2)  # 2
</code></pre>''',
                    'starter_code': '''import heapq

def network_delay(times, n, k):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, w in times:
        graph[u].append((v, w))
    dist = {i: float("inf") for i in range(1, n+1)}
    dist[k] = 0
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    max_dist = max(dist.values())
    return max_dist if max_dist < float("inf") else -1
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Network Delay tests...")
_test("basic",       network_delay([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2)
_test("unreachable", network_delay([[1,2,1]], 2, 2),                 -1)
_test("single node", network_delay([], 1, 1),                         0)
print("All tests passed")
''',
                    'hints': [
                        'Run Dijkstra from node k.',
                        'Answer is max(dist.values()).',
                        'If any value is inf, return -1.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Course Schedule (Cycle Detection)',
                    'description': '''<p>Given n courses and prerequisites, return True if it is possible to finish all (no cycle in the prerequisite graph).</p>
<pre><code class="language-python">can_finish(2, [[1,0]])       # True
can_finish(2, [[1,0],[0,1]]) # False
</code></pre>''',
                    'starter_code': '''from collections import deque

def can_finish(n, prerequisites):
    indegree = [0]*n
    adj = [[] for _ in range(n)]
    for a, b in prerequisites:
        adj[b].append(a)
        indegree[a] += 1
    queue = deque(i for i in range(n) if indegree[i] == 0)
    processed = 0
    while queue:
        u = queue.popleft()
        processed += 1
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return processed == n
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Can Finish tests...")
_test("linear",    can_finish(2, [[1,0]]),         True)
_test("cycle",     can_finish(2, [[1,0],[0,1]]),   False)
_test("no prereq", can_finish(3, []),               True)
print("All tests passed")
''',
                    'hints': [
                        'Build an indegree array and adjacency list.',
                        'Start BFS from nodes with indegree 0.',
                        'Return processed == n — if a cycle exists, some nodes never reach indegree 0.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Dijkstra fails on graphs with:',
                    'options': ['Large edge weights', 'Negative edge weights', 'Many vertices', 'Cycles'],
                    'answer': 1,
                    'explanation': 'Negative weights can invalidate Dijkstra\'s greedy assumption that the first time a node is popped it has the optimal distance.'
                },
                {
                    'question': 'Topological sort exists only for:',
                    'options': ['Undirected graphs', 'Directed Acyclic Graphs (DAGs)', 'Complete graphs', 'Trees'],
                    'answer': 1,
                    'explanation': 'Cycles make it impossible to order nodes such that all edges point forward — only DAGs have valid topological orderings.'
                },
                {
                    'question': 'In network_delay, the answer is max(dist.values()) because:',
                    'options': ['We want the total time', 'The last node to receive the signal determines when ALL nodes have received it', 'Min would give wrong answer', 'Dijkstra returns a max'],
                    'answer': 1,
                    'explanation': 'All nodes must receive the signal. The bottleneck is the node that takes the longest to reach.'
                },
                {
                    'question': 'In can_finish, processed < n after BFS means:',
                    'options': ['Some edges were skipped', 'A cycle exists — those nodes never get indegree 0', 'The graph is disconnected', 'BFS was too slow'],
                    'answer': 1,
                    'explanation': 'Nodes in a cycle always have at least one predecessor in the cycle keeping their indegree above 0.'
                },
                {
                    'question': 'Dijkstra with a binary heap has time complexity:',
                    'options': ['O(V²)', 'O(E log V)', 'O((V+E) log V)', 'O(VE)'],
                    'answer': 2,
                    'explanation': 'Each vertex is popped once (O(V log V)) and each edge relaxation may push to the heap (O(E log V)): total O((V+E) log V).'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 10: Dynamic Programming
    # =========================================================
    10: {
        'intermediate': {
            'content': '''
<h2>Dynamic Programming: Intermediate</h2>
<p>Classic 1D and 2D DP patterns: coin change, longest common subsequence, and edit distance.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>When a problem has overlapping subproblems and optimal substructure, fill a table bottom-up instead of recomputing recursively.</p>
</div>
<h3>Coin Change (Min Coins)</h3>
<pre><code class="language-python">
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

print(coin_change([1,5,6,9], 11))  # 2
</code></pre>
<h3>Longest Common Subsequence</h3>
<pre><code class="language-python">
def lcs(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Coin Change',
                    'description': '''<p>Return the fewest coins to make <code>amount</code>. Return -1 if not possible.</p>
<pre><code class="language-python">coin_change([1,5,6,9], 11)  # 2
coin_change([2], 3)           # -1
</code></pre>''',
                    'starter_code': '''def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Coin Change tests...")
_test("basic",      coin_change([1,5,6,9], 11), 2)
_test("impossible", coin_change([2], 3),          -1)
_test("zero",       coin_change([1], 0),           0)
print("All tests passed")
''',
                    'hints': [
                        'dp[a] = min(dp[a], dp[a-c]+1) for each valid coin.',
                        'dp[0] = 0 is the base case.',
                        'Return -1 if dp[amount] is still inf.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'House Robber',
                    'description': '''<p>Rob houses along a street — you cannot rob two adjacent houses. Return the max amount you can rob.</p>
<pre><code class="language-python">rob([2,7,9,3,1])  # 12  (2+9+1)
rob([1,2,3,1])    # 4   (1+3)
</code></pre>''',
                    'starter_code': '''def rob(nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    prev2, prev1 = 0, 0
    for x in nums:
        curr = max(prev1, prev2 + x)
        prev2 = prev1
        prev1 = curr
    return prev1
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running House Robber tests...")
_test("classic", rob([2,7,9,3,1]), 12)
_test("basic",   rob([1,2,3,1]),    4)
_test("single",  rob([5]),          5)
_test("two",     rob([2,3]),        3)
print("All tests passed")
''',
                    'hints': [
                        'curr = max(prev1, prev2 + x): either skip this house (prev1) or rob it (prev2 + x).',
                        'You only need the previous two values — O(1) space.',
                        'The answer is prev1 after processing all houses.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In coin_change DP, dp[0]=0 because:',
                    'options': ['Zero coins make amount zero', 'It avoids index errors', 'Both above', 'Python default'],
                    'answer': 2,
                    'explanation': 'dp[0]=0 is the logical base (0 coins for amount 0) and anchors all other transitions.'
                },
                {
                    'question': 'House Robber uses O(1) space because:',
                    'options': ['Only the last two dp values are ever needed', 'The array is sorted', 'It uses recursion', 'dp values are constant'],
                    'answer': 0,
                    'explanation': 'dp[i] only depends on dp[i-1] and dp[i-2], so we replace the table with two rolling variables.'
                },
                {
                    'question': 'LCS dp[i][j] when s[i-1]==t[j-1] equals:',
                    'options': ['dp[i-1][j-1]', 'dp[i-1][j-1]+1', 'max(dp[i-1][j],dp[i][j-1])', '0'],
                    'answer': 1,
                    'explanation': 'Matching characters extend the LCS by 1: dp[i][j] = dp[i-1][j-1] + 1.'
                },
                {
                    'question': 'What does "optimal substructure" mean?',
                    'options': ['The algorithm is fast', 'The optimal solution is built from optimal solutions of its subproblems', 'Subproblems are independent', 'The table is triangular'],
                    'answer': 1,
                    'explanation': 'Optimal substructure guarantees that solving subproblems optimally and combining them gives the globally optimal answer.'
                },
                {
                    'question': 'Time complexity of coin_change DP is:',
                    'options': ['O(amount)', 'O(coins)', 'O(coins * amount)', 'O(2^amount)'],
                    'answer': 2,
                    'explanation': 'We iterate over amount values and for each try every coin: O(coins * amount).'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Dynamic Programming: Advanced</h2>
<p>Interval DP, word break, and space-optimised rolling arrays for the hardest problems.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Space-optimise any 2D DP where dp[i][j] depends only on the previous row by keeping just two rows (prev and curr).</p>
</div>
<h3>Word Break</h3>
<pre><code class="language-python">
def word_break(s, word_dict):
    n = len(s)
    dp = [False]*(n+1); dp[0] = True
    words = set(word_dict)
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True; break
    return dp[n]
</code></pre>
<h3>Unique Paths (Grid DP)</h3>
<pre><code class="language-python">
def unique_paths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
</code></pre>
<h3>Longest Palindromic Subsequence</h3>
<pre><code class="language-python">
def lps(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (dp[i+1][j-1] if length > 2 else 0) + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Word Break',
                    'description': '''<p>Return True if <code>s</code> can be segmented into words from <code>word_dict</code>.</p>
<pre><code class="language-python">word_break("leetcode", ["leet","code"])       # True
word_break("catsandog",["cats","dog","sand"]) # False
</code></pre>''',
                    'starter_code': '''def word_break(s, word_dict):
    n = len(s)
    words = set(word_dict)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Word Break tests...")
_test("leet+code", word_break("leetcode",["leet","code"]),        True)
_test("impossible",word_break("catsandog",["cats","dog","sand"]), False)
_test("single",    word_break("word",["word"]),                   True)
print("All tests passed")
''',
                    'hints': [
                        'dp[i] = True means s[0:i] is segmentable.',
                        'For each i, check all j < i: if dp[j] and s[j:i] in words, set dp[i]=True.',
                        'Return dp[n].',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Unique Paths',
                    'description': '''<p>Count paths from top-left to bottom-right of m x n grid (only right or down moves).</p>
<pre><code class="language-python">unique_paths(3, 7)  # 28
unique_paths(3, 2)  # 3
</code></pre>''',
                    'starter_code': '''def unique_paths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Unique Paths tests...")
_test("3x7", unique_paths(3,7), 28)
_test("3x2", unique_paths(3,2),  3)
_test("1x1", unique_paths(1,1),  1)
print("All tests passed")
''',
                    'hints': [
                        'The first row and column are all 1s (only one way to reach them).',
                        'dp[i][j] = dp[i-1][j] + dp[i][j-1].',
                        'Return dp[m-1][n-1].',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Word break dp[0]=True because:',
                    'options': ['Empty string is trivially segmentable', 'First word always matches', 'It avoids index errors', 'Python default'],
                    'answer': 0,
                    'explanation': 'The empty prefix has nothing to segment — dp[0]=True is the correct base case.'
                },
                {
                    'question': 'unique_paths(m,n) equals combinatorially:',
                    'options': ['m*n', 'm+n-2', 'C(m+n-2, m-1)', '2^(m+n)'],
                    'answer': 2,
                    'explanation': 'm+n-2 total steps; choose m-1 to go down: C(m+n-2,m-1).'
                },
                {
                    'question': 'Space-optimised LCS uses two arrays because:',
                    'options': ['LCS is symmetric', 'dp[i][j] only needs dp[i-1][*] and dp[i][j-1]', 'Python limits memory', 'The table is sparse'],
                    'answer': 1,
                    'explanation': 'Only the previous row (prev) and current row (curr) are needed at any time.'
                },
                {
                    'question': 'LPS (longest palindromic subsequence) of "bbbab" is:',
                    'options': ['3', '4', '5', '2'],
                    'answer': 1,
                    'explanation': '"bbbb" is a palindromic subsequence of length 4 (skip the a).'
                },
                {
                    'question': 'Bottom-up DP avoids recursion stack overflow because:',
                    'options': ['It uses more memory', 'It fills a table iteratively without recursive calls', 'It memoizes', 'Python limits recursion'],
                    'answer': 1,
                    'explanation': 'Iterative table-filling never uses the call stack beyond O(1) depth.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 11: Heaps & Priority Queues
    # =========================================================
    11: {
        'intermediate': {
            'content': '''
<h2>Heaps: Intermediate</h2>
<p>Python\'s heapq is a min-heap. Negate values for max-heap behaviour. Key patterns: top-K, K-way merge.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>A min-heap of size K finds the K largest elements in O(n log K) — much better than sorting when K is small.</p>
</div>
<h3>K Largest Elements</h3>
<pre><code class="language-python">
import heapq

def k_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)
    return sorted(heap, reverse=True)
</code></pre>
<h3>Merge K Sorted Lists</h3>
<pre><code class="language-python">
def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst: heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, li, idx = heapq.heappop(heap)
        result.append(val)
        if idx+1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][idx+1], li, idx+1))
    return result
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Kth Largest Element',
                    'description': '''<p>Find the Kth largest element using a min-heap of size K.</p>
<pre><code class="language-python">kth_largest([3,2,1,5,6,4], 2)  # 5
</code></pre>''',
                    'starter_code': '''import heapq

def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Kth Largest tests...")
_test("k=2", kth_largest([3,2,1,5,6,4], 2), 5)
_test("k=4", kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)
_test("k=1", kth_largest([1], 1), 1)
print("All tests passed")
''',
                    'hints': [
                        'Build a min-heap from the first k elements.',
                        'For each remaining element larger than heap[0], replace it.',
                        'heap[0] is the Kth largest.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Top K Frequent Elements',
                    'description': '''<p>Return the K most frequent elements (any order).</p>
<pre><code class="language-python">top_k_frequent([1,1,1,2,2,3], 2)  # [1,2]
</code></pre>''',
                    'starter_code': '''import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if sorted(got)==sorted(exp): _pass(f"{label} => {sorted(got)}")
    else: _fail(f"{label}: expected {sorted(exp)}, got {sorted(got)}")

print("Running Top K Frequent tests...")
_test("basic",  top_k_frequent([1,1,1,2,2,3], 2), [1,2])
_test("single", top_k_frequent([1], 1),             [1])
print("All tests passed")
''',
                    'hints': [
                        'Count frequencies with Counter.',
                        'heapq.nlargest(k, freq.keys(), key=lambda x: freq[x]) returns the top K.',
                        'Order within result does not matter.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'heapq in Python is a:',
                    'options': ['Max-heap', 'Min-heap', 'Sorted list', 'BST'],
                    'answer': 1,
                    'explanation': 'heapq always maintains the smallest element at index 0 (min-heap).'
                },
                {
                    'question': 'To simulate a max-heap with heapq you:',
                    'options': ['Use heapq.max()', 'Push negated values', 'Sort first', 'Use a deque'],
                    'answer': 1,
                    'explanation': 'Pushing -x and negating on pop turns the min-heap behaviour into max-heap behaviour.'
                },
                {
                    'question': 'heapq.heapify() runs in:',
                    'options': ['O(n log n)', 'O(n)', 'O(log n)', 'O(n²)'],
                    'answer': 1,
                    'explanation': 'Bottom-up heapification is O(n) — not O(n log n) like repeated insertion.'
                },
                {
                    'question': 'Merging K sorted lists using a heap is O(n log k) because:',
                    'options': ['n elements each requiring O(log k) heap operations', 'The heap size is n', 'Sorting takes log k', 'K lists each have n elements'],
                    'answer': 0,
                    'explanation': 'There are n total elements; each push/pop from the heap of size k costs O(log k).'
                },
                {
                    'question': 'heapq.heapreplace(heap, x) is better than pop+push because:',
                    'options': ['It is O(log n) vs O(2 log n)', 'It can grow the heap', 'It checks x > heap[0]', 'It returns None'],
                    'answer': 0,
                    'explanation': 'heapreplace atomically replaces the root and sifts down once instead of two separate heap operations.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Heaps: Advanced</h2>
<p>Two-heap median maintenance, task scheduling, and custom comparator heaps.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Two heaps (max-heap for lower half, min-heap for upper half) maintain the running median in O(log n) per insertion.</p>
</div>
<h3>Find Median from Data Stream</h3>
<pre><code class="language-python">
import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap (negated)
        self.hi = []   # min-heap

    def add_num(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self):
        if len(self.lo) > len(self.hi): return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2
</code></pre>
<h3>K Closest Points to Origin</h3>
<pre><code class="language-python">
def k_closest(points, k):
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2+p[1]**2)
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Find Median from Data Stream',
                    'description': '''<p>Design MedianFinder supporting add_num and find_median in O(log n) and O(1) respectively.</p>
<pre><code class="language-python">mf = MedianFinder()
mf.add_num(1); mf.add_num(2); mf.find_median()  # 1.5
mf.add_num(3); mf.find_median()  # 2.0
</code></pre>''',
                    'starter_code': '''import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap (negated)
        self.hi = []   # min-heap

    def add_num(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self):
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got == exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running MedianFinder tests...")
mf = MedianFinder()
mf.add_num(1); mf.add_num(2)
_test("even", mf.find_median(), 1.5)
mf.add_num(3)
_test("odd",  mf.find_median(), 2.0)
print("All tests passed")
''',
                    'hints': [
                        'lo (max-heap via negation) holds the smaller half; hi (min-heap) holds the larger half.',
                        'Keep |lo| >= |hi| at all times.',
                        'Median = -lo[0] if sizes differ, else (-lo[0]+hi[0])/2.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'K Closest Points to Origin',
                    'description': '''<p>Return the K closest points to (0,0) measured by squared Euclidean distance.</p>
<pre><code class="language-python">k_closest([[1,3],[-2,2],[5,8]], 1)  # [[-2,2]]
</code></pre>''',
                    'starter_code': '''import heapq

def k_closest(points, k):
    heap = []
    for x, y in points:
        dist_sq = x*x + y*y
        heapq.heappush(heap, (-dist_sq, [x, y]))
        if len(heap) > k:
            heapq.heappop(heap)
    return [p for _, p in heap]
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _norm(pts): return sorted([sorted(p) for p in pts])
def _test(label, got, exp):
    if _norm(got)==_norm(exp): _pass(label)
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running K Closest tests...")
_test("k=1", k_closest([[1,3],[-2,2],[5,8]], 1), [[-2,2]])
_test("k=2", k_closest([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]])
print("All tests passed")
''',
                    'hints': [
                        'Use a max-heap of size k (negate dist_sq).',
                        'Pop the farthest when heap exceeds k.',
                        'Return [p for _, p in heap].',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In the two-heap median finder, lo holds:',
                    'options': ['The largest half', 'The smallest half', 'All numbers', 'Just the median'],
                    'answer': 1,
                    'explanation': 'lo (max-heap) holds the smaller half; hi (min-heap) holds the larger half.'
                },
                {
                    'question': 'Median when both heaps are equal size:',
                    'options': ['lo[0]', 'hi[0]', '(-lo[0] + hi[0]) / 2', 'lo[0] + hi[0]'],
                    'answer': 2,
                    'explanation': 'Two middle elements: max of lower half (-lo[0]) and min of upper half (hi[0]). Average of both.'
                },
                {
                    'question': 'For K closest points, negating dist_sq makes the min-heap behave as:',
                    'options': ['A sorted list', 'A max-heap — largest negative = smallest distance', 'A FIFO queue', 'A BST'],
                    'answer': 1,
                    'explanation': 'Negating distances makes the smallest negative value (most negative = largest distance) appear at the top — effectively a max-heap of distances.'
                },
                {
                    'question': 'heapq operations time complexity:',
                    'options': ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)'],
                    'answer': 1,
                    'explanation': 'heappush and heappop each run in O(log n) — one sift up/down.'
                },
                {
                    'question': 'Task scheduler uses a max-heap because:',
                    'options': ['Tasks are strings', 'The most frequent task must be scheduled first to minimise idle time', 'Min-heap does not work', 'Python default'],
                    'answer': 1,
                    'explanation': 'Greedily scheduling the highest-frequency task first minimises the required idle slots between repetitions.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 12: Tries
    # =========================================================
    12: {
        'intermediate': {
            'content': '''
<h2>Tries: Intermediate</h2>
<p>A Trie enables O(m) insert/search where m is the word length — ideal for prefix-based queries.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Each node has a children dict and an is_end flag. Shared prefixes share nodes, saving memory and enabling fast prefix lookups.</p>
</div>
<h3>Trie Implementation</h3>
<pre><code class="language-python">
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self): self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Implement a Trie',
                    'description': '''<p>Implement insert, search, and starts_with for a Trie.</p>
<pre><code class="language-python">t = Trie(); t.insert("apple")
t.search("apple")    # True
t.search("app")      # False
t.starts_with("app") # True
</code></pre>''',
                    'starter_code': '''class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self): self.root = TrieNode()

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
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got==exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Trie tests...")
t = Trie(); t.insert("apple")
_test("search apple",    t.search("apple"),    True)
_test("search app",      t.search("app"),      False)
_test("starts_with app", t.starts_with("app"), True)
_test("starts_with xyz", t.starts_with("xyz"), False)
t.insert("app")
_test("search app now",  t.search("app"),      True)
print("All tests passed")
''',
                    'hints': [
                        'search returns node.is_end.',
                        'starts_with returns True after traversing the prefix.',
                        'setdefault(ch, TrieNode()) simplifies insert.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Replace Words',
                    'description': '''<p>Replace each word in the sentence with its shortest root from the dictionary.</p>
<pre><code class="language-python">replace_words(["cat","bat","rat"], "the cattle was rattled by the battery")
# "the cat was rat by the bat"
</code></pre>''',
                    'starter_code': '''class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def replace_words(dictionary, sentence):
    root = TrieNode()
    for w in dictionary:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.word = w

    def find_root(word):
        node = root
        for ch in word:
            if ch not in node.children: break
            node = node.children[ch]
            if node.word: return node.word
        return word

    return " ".join(find_root(w) for w in sentence.split())
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got==exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Replace Words tests...")
_test("classic", replace_words(["cat","bat","rat"],"the cattle was rattled by the battery"), "the cat was rat by the bat")
_test("no match", replace_words(["a"],"xyz abc"), "xyz a")
print("All tests passed")
''',
                    'hints': [
                        'Insert roots into a Trie, marking node.word at each root endpoint.',
                        'For each word, traverse until a root node is found.',
                        'Return the root if found, else the original word.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Trie search time for a word of length m:',
                    'options': ['O(n) where n=word count', 'O(m)', 'O(m log n)', 'O(26m)'],
                    'answer': 1,
                    'explanation': 'We traverse exactly m nodes, independent of how many words are stored.'
                },
                {
                    'question': 'starts_with differs from search in that it does not check:',
                    'options': ['Children existence', 'is_end flag', 'Character matching', 'Root node'],
                    'answer': 1,
                    'explanation': 'starts_with only verifies the path exists — not that it ends a complete word.'
                },
                {
                    'question': 'A Trie uses a dict of children rather than an array because:',
                    'options': ['Dicts are ordered', 'Dicts save memory for sparse alphabets', 'Arrays are slower', 'Python has no arrays'],
                    'answer': 1,
                    'explanation': 'Most nodes have few children; a dict allocates only present characters.'
                },
                {
                    'question': 'setdefault(ch, TrieNode()) in Trie insert:',
                    'options': ['Overwrites existing child', 'Inserts only if absent; returns existing or new node', 'Deletes ch', 'Uppercases ch'],
                    'answer': 1,
                    'explanation': 'dict.setdefault(key, default) returns the existing value if key is present; otherwise inserts and returns the default.'
                },
                {
                    'question': 'Space complexity of a Trie with n words of average length m:',
                    'options': ['O(n)', 'O(m)', 'O(n*m)', 'O(n+m)'],
                    'answer': 2,
                    'explanation': 'In the worst case (no shared prefixes) every character of every word creates a node: O(n*m).'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Tries: Advanced</h2>
<p>Binary tries for XOR problems, Word Search II with pruning, and compressed (Patricia) tries.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>A binary trie on bit representations finds the maximum XOR pair in O(32n) - linear in the number of elements.</p>
</div>
<h3>Maximum XOR (Binary Trie)</h3>
<pre><code class="language-python">
def find_max_xor(nums):
    root = {}
    for n in nums:
        node = root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if bit not in node: node[bit] = {}
            node = node[bit]
    def query(n):
        node = root; xor = 0
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            want = 1 - bit
            if want in node:
                xor |= (1 << i); node = node[want]
            else: node = node[bit]
        return xor
    return max(query(n) for n in nums)

print(find_max_xor([3,10,5,25,2,8]))  # 28
</code></pre>
<h3>Word Search II (Trie + DFS)</h3>
<pre><code class="language-python">
def find_words(board, words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node["#"] = w

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(node, r, c):
        ch = board[r][c]
        if ch not in node: return
        nxt = node[ch]
        if "#" in nxt:
            result.append(nxt["#"])
            del nxt["#"]
        board[r][c] = "#"
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and board[nr][nc]!="#":
                dfs(nxt, nr, nc)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(root, r, c)
    return sorted(result)
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Maximum XOR of Two Numbers',
                    'description': '''<p>Find the maximum XOR of any two numbers in nums using a binary trie.</p>
<pre><code class="language-python">find_max_xor([3,10,5,25,2,8])  # 28
</code></pre>''',
                    'starter_code': '''def find_max_xor(nums):
    root = {}

    def insert(num):
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node: node[bit] = {}
            node = node[bit]

    def query(num):
        node = root; xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit
            if want in node:
                xor |= (1 << i)
                node = node[want]
            else:
                node = node[bit]
        return xor

    for n in nums: insert(n)
    return max(query(n) for n in nums)
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got==exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Max XOR tests...")
_test("classic", find_max_xor([3,10,5,25,2,8]), 28)
_test("pair",    find_max_xor([1,2]),             3)
_test("zeros",   find_max_xor([0,0]),             0)
print("All tests passed")
''',
                    'hints': [
                        'Insert all numbers bit-by-bit (MSB first).',
                        'Query: greedily take the opposite bit to maximise XOR.',
                        'Fallback to same bit when opposite is absent.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Word Search II',
                    'description': '''<p>Find all words from the list that exist in the board (adjacent cells, no reuse).</p>
<pre><code class="language-python">board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
find_words(board, ["oath","pea","eat","rain"])  # ["eat","oath"]
</code></pre>''',
                    'starter_code': '''def find_words(board, words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node["#"] = w

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(node, r, c):
        ch = board[r][c]
        if ch not in node: return
        nxt = node[ch]
        if "#" in nxt:
            result.append(nxt["#"])
            del nxt["#"]   # avoid duplicates
        board[r][c] = "#"
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and board[nr][nc]!="#":
                dfs(nxt, nr, nc)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(root, r, c)
    return sorted(result)
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if sorted(got)==sorted(exp): _pass(f"{label} => {sorted(got)}")
    else: _fail(f"{label}: expected {sorted(exp)}, got {sorted(got)}")

print("Running Word Search II tests...")
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
_test("classic", find_words(board, ["oath","pea","eat","rain"]), ["eat","oath"])
board2 = [["a"]]
_test("single",  find_words(board2, ["a"]), ["a"])
print("All tests passed")
''',
                    'hints': [
                        'Build a Trie from all words; "#" marks word endpoints.',
                        'DFS from each cell, following the Trie as you explore the grid.',
                        'Mark cells with "#" to prevent reuse; restore after backtracking.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'A binary trie for 32-bit integers has depth:',
                    'options': ['16', '32', '64', 'Variable'],
                    'answer': 1,
                    'explanation': 'One level per bit; 32-bit integers need 32 levels.'
                },
                {
                    'question': 'In max XOR we prefer the opposite bit because:',
                    'options': ['Same bits XOR to 0; opposite bits XOR to 1 maximising that position', 'It reduces comparisons', 'XOR is commutative', 'Trie stores only 0s'],
                    'answer': 0,
                    'explanation': 'XOR(1,0)=XOR(0,1)=1. Choosing the opposite bit sets that bit of the result to 1, maximising the XOR value.'
                },
                {
                    'question': 'In Word Search II, why do we delete nxt["#"] after finding a word?',
                    'options': ['Memory saving', 'To prevent adding the same word twice from different paths', 'To speed up DFS', 'Python requires it'],
                    'answer': 1,
                    'explanation': 'Multiple DFS paths could reach the same word endpoint. Deleting "#" ensures each word appears at most once in the result.'
                },
                {
                    'question': 'Compressed tries (Patricia trees) reduce space by:',
                    'options': ['Removing duplicate words', 'Merging long single-child chains into one edge', 'Using arrays instead of dicts', 'Sorting words'],
                    'answer': 1,
                    'explanation': 'Long chains with no branching are merged into a single labelled edge, reducing node count significantly.'
                },
                {
                    'question': 'In Word Search II, marking board[r][c]="#" prevents:',
                    'options': ['Finding palindromes', 'Reusing the same cell in a single path', 'DFS from starting there', 'Trie traversal errors'],
                    'answer': 1,
                    'explanation': 'We cannot revisit a cell within one DFS path (the same word). "#" is not a valid character, so the DFS will not continue from that cell.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 13: Backtracking
    # =========================================================
    13: {
        'intermediate': {
            'content': '''
<h2>Backtracking: Intermediate</h2>
<p>Systematically explore all possibilities, pruning branches that cannot lead to valid solutions.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Template: choose an option, explore recursively, unchoose (undo). This guarantees completeness without exponential memory.</p>
</div>
<h3>Subsets</h3>
<pre><code class="language-python">
def subsets(nums):
    result = []
    def bt(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            bt(i+1, path)
            path.pop()
    bt(0, [])
    return result
</code></pre>
<h3>Combination Sum</h3>
<pre><code class="language-python">
def combination_sum(candidates, target):
    result = []
    candidates.sort()
    def bt(start, path, rem):
        if rem == 0: result.append(path[:]); return
        for i in range(start, len(candidates)):
            if candidates[i] > rem: break
            path.append(candidates[i])
            bt(i, path, rem - candidates[i])
            path.pop()
    bt(0, [], target)
    return result
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Generate All Subsets',
                    'description': '''<p>Return all subsets (power set) of nums. No duplicates.</p>
<pre><code class="language-python">subsets([1,2,3])
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
</code></pre>''',
                    'starter_code': '''def subsets(nums):
    result = []
    def bt(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            bt(i+1, path)
            path.pop()
    bt(0, [])
    return result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _norm(res): return sorted([sorted(s) for s in res])
def _test(label, got, exp):
    if _norm(got)==_norm(exp): _pass(label)
    else: _fail(f"{label}: expected {_norm(exp)}, got {_norm(got)}")

print("Running Subsets tests...")
_test("3 elems", subsets([1,2,3]), [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]])
_test("empty",   subsets([]),     [[]])
_test("single",  subsets([5]),    [[],[5]])
print("All tests passed")
''',
                    'hints': [
                        'Record the current path as a subset before the loop.',
                        'path.append -> recurse(i+1) -> path.pop.',
                        '2^n subsets total.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Combination Sum',
                    'description': '''<p>Find all unique combinations summing to target. Each candidate can be reused.</p>
<pre><code class="language-python">combination_sum([2,3,6,7], 7)  # [[2,2,3],[7]]
</code></pre>''',
                    'starter_code': '''def combination_sum(candidates, target):
    result = []
    candidates.sort()
    def bt(start, path, rem):
        if rem == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > rem: break
            path.append(candidates[i])
            bt(i, path, rem - candidates[i])   # i allows reuse
            path.pop()
    bt(0, [], target)
    return result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _norm(res): return sorted([sorted(c) for c in res])
def _test(label, got, exp):
    if _norm(got)==_norm(exp): _pass(label)
    else: _fail(f"{label}: expected {_norm(exp)}, got {_norm(got)}")

print("Running Combination Sum tests...")
_test("basic",  combination_sum([2,3,6,7],7), [[2,2,3],[7]])
_test("two",    combination_sum([2,3],5),     [[2,3]])
_test("no sol", combination_sum([5],3),        [])
print("All tests passed")
''',
                    'hints': [
                        'Sort candidates to enable the break pruning.',
                        'Pass i (not i+1) to allow reuse of the same candidate.',
                        'Append path[:] when rem==0.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'path.pop() in backtracking is the "unchoose" step that:',
                    'options': ['Clears memory', 'Restores state for the next loop iteration', 'Prevents recursion', 'Sorts the path'],
                    'answer': 1,
                    'explanation': 'Without undoing the choice, subsequent iterations would incorrectly build on the previous one.'
                },
                {
                    'question': 'In combination_sum, passing start=i (not i+1) allows:',
                    'options': ['Sorted output', 'Reuse of the same candidate multiple times', 'Permutations', 'Deduplication'],
                    'answer': 1,
                    'explanation': 'i keeps the current candidate available in the next recursive call, enabling combinations like [2,2,2,...].'
                },
                {
                    'question': 'Number of subsets of n elements:',
                    'options': ['n!', 'n²', '2^n', 'n'],
                    'answer': 2,
                    'explanation': 'Each element is included or excluded: 2 choices per element = 2^n subsets.'
                },
                {
                    'question': 'The "break" when candidates[i] > rem works because:',
                    'options': ['Candidates are random', 'Candidates are sorted — all subsequent candidates are also > rem', 'Backtracking skips automatically', 'Loop ends naturally'],
                    'answer': 1,
                    'explanation': 'After sorting, if one candidate exceeds rem, all following candidates do too.'
                },
                {
                    'question': 'Backtracking worst-case complexity is typically:',
                    'options': ['O(n log n)', 'O(n²)', 'Exponential', 'O(n)'],
                    'answer': 2,
                    'explanation': 'Without pruning, backtracking explores the entire decision tree — exponential in depth and branching factor.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Backtracking: Advanced</h2>
<p>N-Queens, Sudoku solver, and palindrome partitioning push pruning to the limit.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Effective pruning is the difference between seconds and timeout. Always check ALL constraints before recursing.</p>
</div>
<h3>N-Queens</h3>
<pre><code class="language-python">
def solve_n_queens(n):
    result = []
    cols = set(); d1 = set(); d2 = set()
    board = [["."]*n for _ in range(n)]
    def bt(row):
        if row == n:
            result.append(["".join(r) for r in board]); return
        for col in range(n):
            if col in cols or (row-col) in d1 or (row+col) in d2: continue
            cols.add(col); d1.add(row-col); d2.add(row+col)
            board[row][col] = "Q"
            bt(row+1)
            board[row][col] = "."
            cols.discard(col); d1.discard(row-col); d2.discard(row+col)
    bt(0); return result
</code></pre>
<h3>Palindrome Partitioning</h3>
<pre><code class="language-python">
def partition(s):
    result = []
    def is_pal(sub): return sub == sub[::-1]
    def bt(start, path):
        if start == len(s): result.append(path[:]); return
        for end in range(start+1, len(s)+1):
            sub = s[start:end]
            if is_pal(sub):
                path.append(sub); bt(end, path); path.pop()
    bt(0, []); return result
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'N-Queens',
                    'description': '''<p>Place N queens on an N x N board so no two attack each other. Return all valid configurations.</p>
<pre><code class="language-python">len(solve_n_queens(4))  # 2
len(solve_n_queens(1))  # 1
</code></pre>''',
                    'starter_code': '''def solve_n_queens(n):
    result = []
    cols = set(); d1 = set(); d2 = set()
    board = [["."]*n for _ in range(n)]

    def bt(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row-col) in d1 or (row+col) in d2:
                continue
            cols.add(col); d1.add(row-col); d2.add(row+col)
            board[row][col] = "Q"
            bt(row+1)
            board[row][col] = "."
            cols.discard(col); d1.discard(row-col); d2.discard(row+col)

    bt(0)
    return result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got==exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running N-Queens tests...")
_test("n=1", len(solve_n_queens(1)), 1)
_test("n=4", len(solve_n_queens(4)), 2)
_test("n=5", len(solve_n_queens(5)), 10)
print("All tests passed")
''',
                    'hints': [
                        'Track cols, d1 (row-col), d2 (row+col) for attacked positions.',
                        'Skip any column where a constraint is violated.',
                        'Discard (undo) all three sets after backtracking.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Palindrome Partitioning',
                    'description': '''<p>Partition s so every substring is a palindrome. Return all valid partitions.</p>
<pre><code class="language-python">partition("aab")  # [["a","a","b"],["aa","b"]]
</code></pre>''',
                    'starter_code': '''def partition(s):
    result = []
    def is_pal(sub): return sub == sub[::-1]
    def bt(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start+1, len(s)+1):
            sub = s[start:end]
            if is_pal(sub):
                path.append(sub)
                bt(end, path)
                path.pop()
    bt(0, [])
    return result
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _norm(res): return sorted([sorted(p) for p in res])
def _test(label, got, exp):
    if _norm(got)==_norm(exp): _pass(label)
    else: _fail(f"{label}: expected {_norm(exp)}, got {_norm(got)}")

print("Running Palindrome Partitioning tests...")
_test("aab", partition("aab"), [["a","a","b"],["aa","b"]])
_test("a",   partition("a"),   [["a"]])
print("All tests passed")
''',
                    'hints': [
                        'Only recurse when s[start:end] is a palindrome.',
                        'path.append -> bt(end) -> path.pop.',
                        'Base case: start == len(s).',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'In N-Queens, d1 = row - col is the same for all cells on a:',
                    'options': ['Row', 'Column', 'Top-left to bottom-right diagonal', 'Top-right to bottom-left diagonal'],
                    'answer': 2,
                    'explanation': 'All cells on the same main diagonal share the same row-col value.'
                },
                {
                    'question': 'N-Queens places one queen per row because:',
                    'options': ['Rows are faster to iterate', 'The recursive structure guarantees one queen per row, eliminating row conflicts automatically', 'Columns must be exhausted first', 'Python loop constraint'],
                    'answer': 1,
                    'explanation': 'Each recursive call handles exactly one row. One queen per row is enforced by the recursion structure itself.'
                },
                {
                    'question': 'Palindrome partitioning checks is_pal before recursing to:',
                    'options': ['Sort partitions', 'Prune invalid branches early', 'Limit depth', 'Deduplicate'],
                    'answer': 1,
                    'explanation': 'If s[start:end] is not a palindrome, extending it cannot help — so we skip without recursing.'
                },
                {
                    'question': 'The number of N-Queens solutions grows:',
                    'options': ['Linearly', 'Slower than n!', 'Faster than 2^n', 'Exactly n²'],
                    'answer': 1,
                    'explanation': 'Diagonal constraints prune heavily; solutions grow much slower than n! For n=8: 92 solutions; n=13: 73712.'
                },
                {
                    'question': 'Pruning improves backtracking by:',
                    'options': ['Sorting input', 'Cutting entire subtrees where all extensions violate constraints', 'Memoizing repeated states', 'Limiting recursion depth'],
                    'answer': 1,
                    'explanation': 'When a partial solution already violates a constraint, no extension of it can succeed. Pruning skips the entire subtree.'
                },
            ]
        }
    },

    # =========================================================
    # MODULE 14: Advanced Graph Algorithms
    # =========================================================
    14: {
        'intermediate': {
            'content': '''
<h2>Advanced Graphs: Intermediate</h2>
<p>Minimum spanning trees with Kruskal and Prim, and Bellman-Ford for negative-weight shortest paths.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Kruskal greedily adds the cheapest edge that does not form a cycle (Union-Find); Prim grows one connected MST component from a seed node.</p>
</div>
<h3>Kruskal MST</h3>
<pre><code class="language-python">
def kruskal(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa == pb: return False
        parent[pa] = pb; return True
    edges.sort(key=lambda e: e[2])
    return sum(w for u,v,w in edges if union(u,v))
</code></pre>
<h3>Bellman-Ford</h3>
<pre><code class="language-python">
def bellman_ford(n, edges, src):
    dist = [float("inf")] * n; dist[src] = 0
    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u]+w < dist[v]: dist[v] = dist[u]+w
    for u,v,w in edges:
        if dist[u]+w < dist[v]: return None  # negative cycle
    return dist
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Min Cost to Connect All Points',
                    'description': '''<p>Return the minimum cost (Manhattan distance) to connect all points using Prim\'s algorithm.</p>
<pre><code class="language-python">min_cost_connect([[0,0],[2,2],[3,10],[5,2],[7,0]])  # 20
</code></pre>''',
                    'starter_code': '''import heapq

def min_cost_connect(points):
    n = len(points)
    visited = set()
    heap = [(0, 0)]
    total = 0
    while len(visited) < n:
        cost, i = heapq.heappop(heap)
        if i in visited: continue
        visited.add(i); total += cost
        for j in range(n):
            if j not in visited:
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                heapq.heappush(heap, (dist, j))
    return total
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got==exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Min Cost Connect tests...")
_test("classic", min_cost_connect([[0,0],[2,2],[3,10],[5,2],[7,0]]), 20)
_test("two pts", min_cost_connect([[0,0],[1,1]]),                     2)
_test("one pt",  min_cost_connect([[0,0]]),                           0)
print("All tests passed")
''',
                    'hints': [
                        'Use Prim: start from point 0 with cost 0.',
                        'Push (manhattan_dist, j) for all unvisited j.',
                        'Add cost when popping, skip if already visited.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Cheapest Flights Within K Stops',
                    'description': '''<p>Find cheapest price from src to dst with at most k stops (Bellman-Ford variant). Return -1 if impossible.</p>
<pre><code class="language-python">cheapest_flight(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)  # 200
</code></pre>''',
                    'starter_code': '''def cheapest_flight(n, flights, src, dst, k):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(k+1):
        temp = dist[:]
        for u, v, w in flights:
            if dist[u] + w < temp[v]:
                temp[v] = dist[u] + w
        dist = temp
    return dist[dst] if dist[dst] < float("inf") else -1
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got==exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Cheapest Flight tests...")
_test("k=1",      cheapest_flight(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1), 200)
_test("k=0",      cheapest_flight(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0), 500)
_test("no route", cheapest_flight(3,[[0,1,100]],0,2,1),                      -1)
print("All tests passed")
''',
                    'hints': [
                        'Iterate k+1 times (k stops = k+1 edges).',
                        'Use a copy temp=dist[:] to prevent same-round updates.',
                        'Return -1 if dist[dst] remains inf.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Kruskal requires edges to be sorted by:',
                    'options': ['Vertex label', 'Weight ascending', 'BFS order', 'Random'],
                    'answer': 1,
                    'explanation': 'Greedy edge selection processes cheapest edges first.'
                },
                {
                    'question': 'Bellman-Ford runs n-1 iterations because:',
                    'options': ['It has n-1 edges', 'A simple shortest path has at most n-1 edges', 'Python loop limit', 'Each node relaxes once'],
                    'answer': 1,
                    'explanation': 'A simple path between any two nodes uses at most n-1 edges; n-1 passes are sufficient to propagate all shortest paths.'
                },
                {
                    'question': 'In cheapest_flight we copy dist to temp each round to:',
                    'options': ['Speed up iteration', 'Ensure each round extends paths by exactly one hop', 'Avoid negative cycles', 'Detect disconnected nodes'],
                    'answer': 1,
                    'explanation': 'Using the copy prevents using distances updated in the same round, enforcing the "one more hop per round" constraint.'
                },
                {
                    'question': 'Prim differs from Kruskal in that it:',
                    'options': ['Sorts edges globally', 'Grows one MST component from a seed, adding the cheapest adjacent edge each step', 'Uses Union-Find', 'Works only on directed graphs'],
                    'answer': 1,
                    'explanation': 'Prim maintains a single growing component; Kruskal processes all edges globally by weight.'
                },
                {
                    'question': 'Bellman-Ford detects a negative cycle by checking if any edge can still be relaxed after n-1 passes. This works because:',
                    'options': ['All paths are found in n-1 passes; further relaxation implies a cycle reduces the path', 'Negative weights always form cycles', 'It is a Python feature', 'Union-Find detects it'],
                    'answer': 0,
                    'explanation': 'After n-1 passes, all shortest paths are final (no negative cycles). If any edge can still be relaxed, a negative cycle exists.'
                },
            ]
        },
        'advanced': {
            'content': '''
<h2>Advanced Graphs: Advanced Level</h2>
<p>Floyd-Warshall all-pairs shortest paths, Kosaraju\'s SCC, and topological sort for course scheduling.</p>
<div class="concept-box">
  <h4>🔑 Key Idea</h4>
  <p>Floyd-Warshall: dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]) for every intermediate node k. O(V³) but finds all-pairs in one shot.</p>
</div>
<h3>Floyd-Warshall</h3>
<pre><code class="language-python">
def floyd_warshall(n, edges):
    INF = float("inf")
    dp = [[INF]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 0
    for u,v,w in edges: dp[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k]+dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k]+dp[k][j]
    return dp
</code></pre>
<h3>Course Schedule II (Topo Sort)</h3>
<pre><code class="language-python">
from collections import deque

def find_order(n, prerequisites):
    indegree = [0]*n; adj = [[] for _ in range(n)]
    for a,b in prerequisites: adj[b].append(a); indegree[a] += 1
    q = deque(i for i in range(n) if indegree[i]==0)
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v]==0: q.append(v)
    return order if len(order)==n else []
</code></pre>
''',
            'labs': [
                {
                    'id': 1,
                    'title': 'Floyd-Warshall All-Pairs Shortest Path',
                    'description': '''<p>Compute shortest paths between every pair of nodes.</p>
<pre><code class="language-python">dist = floyd_warshall(4, [(0,1,3),(1,2,1),(2,3,2),(0,3,10)])
dist[0][3]  # 6
</code></pre>''',
                    'starter_code': '''def floyd_warshall(n, edges):
    INF = float("inf")
    dp = [[INF]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 0
    for u, v, w in edges: dp[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    return dp
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")
def _test(label, got, exp):
    if got==exp: _pass(f"{label} => {got}")
    else: _fail(f"{label}: expected {exp}, got {got}")

print("Running Floyd-Warshall tests...")
dist = floyd_warshall(4, [(0,1,3),(1,2,1),(2,3,2),(0,3,10)])
_test("0->3 via relay", dist[0][3], 6)
_test("0->2",           dist[0][2], 4)
_test("self",           dist[1][1], 0)
print("All tests passed")
''',
                    'hints': [
                        'dp[i][i]=0; dp[u][v]=w for each edge.',
                        'Three nested loops with k as intermediate node.',
                        'dp[i][j] = dp[i][k] + dp[k][j] when that is smaller.',
                    ]
                },
                {
                    'id': 2,
                    'title': 'Course Schedule II',
                    'description': '''<p>Return a valid course order to finish all n courses given prerequisites. Return [] if impossible (cycle).</p>
<pre><code class="language-python">find_order(4, [[1,0],[2,0],[3,1],[3,2]])  # [0,1,2,3] or [0,2,1,3]
find_order(2, [[1,0],[0,1]])               # []
</code></pre>''',
                    'starter_code': '''from collections import deque

def find_order(n, prerequisites):
    indegree = [0]*n
    adj = [[] for _ in range(n)]
    for a, b in prerequisites:
        adj[b].append(a)
        indegree[a] += 1
    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return order if len(order) == n else []
''',
                    'test_code': '''
def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): raise AssertionError(f"  FAIL: {msg}")

def _test_order(label, order, n, prereqs):
    if len(order) != n:
        if prereqs and not order: _pass(f"{label} (correctly detected cycle)")
        else: _fail(f"{label}: expected order of {n} courses, got {order}")
        return
    pos = {c:i for i,c in enumerate(order)}
    for a,b in prereqs:
        if pos[b] >= pos[a]: _fail(f"{label}: {b} should come before {a}"); return
    _pass(label)

print("Running Find Order tests...")
_test_order("diamond", find_order(4,[[1,0],[2,0],[3,1],[3,2]]), 4, [[1,0],[2,0],[3,1],[3,2]])
_test_order("cycle",   find_order(2,[[1,0],[0,1]]),             2, [[1,0],[0,1]])
_test_order("none",    find_order(3,[]),                        3, [])
print("All tests passed")
''',
                    'hints': [
                        'Kahn\'s BFS: start from all nodes with indegree 0.',
                        'Decrement indegree of neighbours; add to queue if it hits 0.',
                        'Return order only if len(order)==n; otherwise a cycle exists.',
                    ]
                },
            ],
            'quiz': [
                {
                    'question': 'Floyd-Warshall time complexity:',
                    'options': ['O(V+E)', 'O(V² log V)', 'O(V³)', 'O(E log V)'],
                    'answer': 2,
                    'explanation': 'Three nested loops each running V times: O(V³).'
                },
                {
                    'question': 'A valid topological order exists iff the graph is:',
                    'options': ['Connected', 'A DAG', 'Weighted', 'Complete'],
                    'answer': 1,
                    'explanation': 'Only Directed Acyclic Graphs can be topologically ordered; cycles make it impossible.'
                },
                {
                    'question': 'In find_order, len(order) < n after BFS means:',
                    'options': ['Some courses have no prerequisites', 'A cycle prevents some nodes from ever reaching indegree 0', 'BFS ended early', 'Graph is sparse'],
                    'answer': 1,
                    'explanation': 'Cycle nodes always have a predecessor in the cycle keeping their indegree > 0.'
                },
                {
                    'question': 'Floyd-Warshall detects a negative cycle when:',
                    'options': ['dp[i][i]>0', 'dp[i][i]<0 for some i', 'All paths are 0', 'Graph is disconnected'],
                    'answer': 1,
                    'explanation': 'A negative self-distance dp[i][i]<0 means node i is on a negative-weight cycle.'
                },
                {
                    'question': 'Kosaraju\'s SCC runs DFS twice because:',
                    'options': ['It needs two passes to sort', 'Pass 1 computes finish order; Pass 2 on reversed graph follows that order to identify SCCs', 'Python requires two loops', 'The graph is undirected'],
                    'answer': 1,
                    'explanation': 'Pass 1 on the original graph determines finish times. Pass 2 on the reversed graph, processed in reverse finish order, identifies exactly the SCCs.'
                },
            ]
        }
    },
}

