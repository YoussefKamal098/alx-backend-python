# **0x03. Unittests and Integration Tests**

## **Introduction**
This project delves into two crucial testing concepts for Python applications: **unit testing** and **integration testing**. These methods are vital for ensuring code reliability, functionality, and maintainability in both isolated and integrated environments.

Testing in Python is predominantly done using the `unittest` framework, which provides comprehensive tools to write, organize, and execute tests. Concepts like mocking, parameterization, and memoization further enhance the effectiveness of tests.

---

## **Unit Tests**
### **Definition**
Unit tests validate the behavior of individual components (functions, methods) in isolation. These tests focus solely on the logic of the code, ensuring that the component produces correct results for various inputs.

### **Key Features**
- **Isolation**: No interaction with external systems (databases, APIs, etc.).
- **Mocking**: Replace external dependencies with mock objects.
- **Efficiency**: Test small, focused code sections.

### **Example**
```python
import unittest
from utils import calculate_sum

class TestCalculateSum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        result = calculate_sum([1, 2, 3])
        self.assertEqual(result, 6)

    def test_sum_empty_list(self):
        result = calculate_sum([])
        self.assertEqual(result, 0)
```

---

## **Integration Tests**
### **Definition**
Integration tests evaluate how different components of the system interact with each other. They test end-to-end workflows to ensure seamless integration.

### **Key Features**
- **Realistic Scenarios**: Simulate real-world operations.
- **Minimal Mocking**: Only mock external services or systems (e.g., HTTP requests).
- **Broader Coverage**: Test interactions between modules and external services.

### **Example**
```python
import unittest
from unittest.mock import patch
from client import fetch_data

class TestFetchData(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        mock_get.return_value.json.return_value = {"data": "value"}
        result = fetch_data("https://api.example.com/data")
        self.assertEqual(result, {"data": "value"})
```

---

## **Core Concepts**

### **1. unittest — Unit Testing Framework**
- The **unittest** module is Python’s built-in framework for organizing and running tests.
- Provides tools for:
    - Asserting conditions (`assertEqual`, `assertTrue`, etc.).
    - Grouping tests into test cases and suites.
    - Setting up and tearing down test environments.

#### Example: Basic Test Case
```python
import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

if __name__ == "__main__":
    unittest.main()
```

---

### **2. unittest.mock — Mock Object Library**
- **mock** allows replacing parts of the system under test with mock objects.
- Common use cases:
    - Mocking APIs, databases, and other external dependencies.
    - Verifying how the tested code interacts with these dependencies.

#### Example: Mocking a Function
```python
from unittest.mock import Mock

# Mocking a function
mock_function = Mock(return_value="mocked!")
print(mock_function())  # Output: mocked!
```

---

### **3. Mocking Read-Only Properties**
- Mocking read-only properties requires the use of `PropertyMock`.

#### Example
```python
from unittest.mock import PropertyMock, patch

class TestClass:
    @property
    def read_only_property(self):
        return "original value"

def test_mock_readonly_property():
    with patch.object(TestClass, 'read_only_property', new_callable=PropertyMock) as mock_property:
        mock_property.return_value = "mocked value"
        obj = TestClass()
        assert obj.read_only_property == "mocked value"
```

---

### **4. Parameterization**
- Parameterized tests allow testing a function or method with multiple sets of inputs.
- The `parameterized` library makes this easier.

#### Example: Parameterized Tests
```python
from parameterized import parameterized
import unittest

class TestAddition(unittest.TestCase):
    @parameterized.expand([
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
    ])
    def test_add(self, a, b, expected):
        self.assertEqual(a + b, expected)
```

---

### **5. Memoization**
- **Memoization** optimizes function performance by caching the results of expensive operations.
- Custom memoization decorators can improve testing efficiency.

#### Example: Memoize Decorator
```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def compute_square(n):
    return n * n
```

#### Example: Testing Memoized Function
```python
import unittest
from unittest.mock import patch

class TestMemoization(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def calculate(self):
                return 42

            @memoize
            def memoized_calculate(self):
                return self.calculate()

        obj = TestClass()
        with patch.object(obj, 'calculate', return_value=42) as mock_method:
            self.assertEqual(obj.memoized_calculate(), 42)
            self.assertEqual(obj.memoized_calculate(), 42)
            mock_method.assert_called_once()
```

---

## **Testing Commands**
- Run all tests:
  ```bash
  python -m unittest discover
  ```
- Run a specific test file:
  ```bash
  python -m unittest test_file.py
  ```

---

## **Project Structure**
```
0x03-Unittests_and_integration_tests/
├── README.md
├── utils.py
├── client.py
├── test_utils.py
├── test_client.py
└── requirements.txt
```

---

## **Resources**
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — Mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization in Python](https://realpython.com/python-memoization/)

---

## **Learning Outcomes**
By completing this project, you will:
1. Differentiate between unit and integration tests.
2. Effectively use mocking with `unittest.mock` and `PropertyMock`.
3. Write parameterized tests to handle diverse input scenarios.
4. Implement memoization to optimize performance and test memoized functions.

With this understanding, you’ll be equipped to build robust, test-driven Python applications! 🚀