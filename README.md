# LeetCode Python Practice 6 🐍

## 📌 About This Project

This repository contains my **Python programming and LeetCode practice solutions**.
The purpose of this project is to improve my problem-solving skills, Python programming knowledge, and understanding of Data Structures and Algorithms (DSA).

## 🎯 Objectives

* Learn Python programming step by step
* Practice coding problems regularly
* Improve logical and problem-solving skills
* Learn Data Structures and Algorithms
* Practice LeetCode-style problems
* Maintain my coding practice on GitHub

## 🛠️ Technologies Used

* **Python 3**
* **LeetCode**
* **Visual Studio Code**
* **Git**
* **GitHub**

## 📚 Topics Covered

### Python Basics

* Variables
* Data Types
* Input and Output
* Operators
* Conditional Statements
* Loops
* Functions

### Python Data Structures

* Strings
* Lists
* Tuples
* Sets
* Dictionaries

### Problem Solving

* Number Problems
* String Problems
* Array Problems
* Searching
* Sorting
* Hashing
* Two Pointers
* Sliding Window

### DSA

* Stack
* Queue
* Linked List
* Trees
* Binary Search
* Recursion
* Graphs
* Dynamic Programming

## 💻 Example

### Two Sum

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()

nums = [2, 7, 11, 15]
target = 9

print(solution.twoSum(nums, target))
```

### Output

```text
[0, 1]
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed.

Check the version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/aishuaishu45793-gif/leetcode-python6.py.git
```

### 3. Open the Project

Open the folder in **Visual Studio Code**.

### 4. Run a Python File

```bash
python filename.py
```

## 📁 Suggested Project Structure

```text
leetcode-python6.py/
│
├── README.md
├── hello_world.py
├── variables.py
├── strings.py
├── arrays.py
├── two_sum.py
├── palindrome.py
├── fizz_buzz.py
├── sorting.py
└── searching.py
```

## 🔄 My Problem-Solving Process

For each problem, I follow these steps:

1. Understand the problem
2. Identify the inputs and outputs
3. Create a simple approach
4. Write the Python solution
5. Test with different examples
6. Check edge cases
7. Improve the solution if possible
8. Save the solution to GitHub

## 📈 Learning Progress

* [x] Python Basics
* [x] Variables and Data Types
* [x] Conditional Statements
* [x] Loops
* [x] Functions
* [x] Strings
* [x] Lists
* [x] Dictionaries
* [ ] Advanced DSA
* [ ] Dynamic Programming
* [ ] Advanced Graph Algorithms

## 🔧 GitHub Workflow

After solving new problems:

```bash
git add .
git commit -m "Add new LeetCode practice problems"
git push
```

## 🎓 Learning Outcomes

Through this project, I am developing:

* Python programming skills
* Logical thinking
* Problem-solving ability
* DSA fundamentals
* Debugging skills
* Git and GitHub skills
* Consistent coding practice

## 🚀 Future Goals

* Solve more LeetCode problems
* Improve time and space complexity
* Learn advanced DSA
* Solve medium and hard problems
* Build Python projects
* Prepare for technical interviews

## 👩‍💻 Author

**Aishwarya**

This repository is part of my continuous journey to learn **Python, LeetCode, and Data Structures & Algorithms**.

---

⭐ If you find this repository useful, feel free to explore the code and practice along with me.
