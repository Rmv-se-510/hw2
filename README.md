
<h2 align="center">
    HW2: Debugging Merge Sort
</h2>

<div align="center">
        <img width="300" height="200" src="https://www.lavivienpost.net/wp-content/uploads/2022/02/merge-sort-400.gif" alt="Merge Sort">
        <br>
</div>

<a href="https://github.com/Rmv-se-510/hw1">Link for HW1</a>

<div align="center">
    
![Codecov](https://codecov.io/github/Rmv-se-510/hw2/branch/main/graph/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-purple.svg?style=flat)](https://github.com/Rmv-se-510/hw2/main/LICENSE)
[![Collaborators](https://img.shields.io/badge/Collaborators-3-orange.svg?style=flat)](https://github.com/Rmv-se-510/hw2/graphs/contributors)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg?style=flat)](https://github.com/Rmv-se-510/hw2/search?l=python)
[![Open Issues](https://img.shields.io/github/issues/Rmv-se-510/hw2)](https://github.com/Rmv-se-510/hw2/issues)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Rmv-se-510/hw2.svg)](https://img.shields.io/github/repo-size/Rmv-se-510/hw2.svg)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
<img alt="Actions Status" src="https://github.com/Rmv-se-510/hw2/workflows/Test/badge.svg">
![Flake8](https://img.shields.io/badge/flake8-passing-brightgreen)
![Radon](https://img.shields.io/badge/radon-passing-brightgreen)
![Pylint](https://img.shields.io/badge/pylint-passing-brightgreen)
![Autopep8](https://img.shields.io/badge/autopep8-passing-brightgreen)

</div>



# Merge Sort

Merge Sort is a classic divide-and-conquer algorithm used for sorting arrays or lists. It operates by recursively dividing the array into two halves, sorting each half, and then merging the sorted halves to produce a sorted array. This approach ensures that the final sorted array is produced in O(n log n) time complexity, making it efficient and stable.

## Table of Contents

- [Algorithm Overview](#algorithm-overview)
- [How It Works](#how-it-works)
- [Implementation](#implementation)
- [Complexity](#complexity)

## Algorithm Overview

1. **Divide**: Split the array into two halves.
2. **Conquer**: Recursively sort each half.
3. **Combine**: Merge the two sorted halves into a single sorted array.

## How It Works

1. **Divide**: If the array has one or zero elements, it is already sorted. Otherwise, divide the array into two halves.
2. **Sort**: Recursively apply Merge Sort to both halves of the array.
3. **Merge**: Merge the two sorted halves into a single sorted array by comparing the elements of both halves and combining them in order.

## Implementation

**rand.py**

Generates an array of random integers between 1 and 20 using the `shuf` command on Unix-based systems. Utilizes Python's `subprocess` module to run external commands.

**hw2_debugging.py**

Implements Merge Sort for sorting arrays and provides a `recombine` function to merge two sorted arrays. Integrates with the random array generator to sort arrays with random values.


## Complexity

- **Time Complexity**: O(n log n) for all cases (best, average, worst).
- **Space Complexity**: O(n) due to the additional space used for merging.

---


### Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Rmv-se-510/hw2.git
   ```

2. Change to the repository directory:
   ```bash
   cd hw2
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the tests to ensure everything works correctly:
   ```bash
   pytest -v
   ```

5. To run the main program:
   ```bash
   python hw2_debugging.py
   ```
   Example:
   ```
   LENOVO@LENOVO MINGW64 ~/OneDrive/Desktop/SOFTWARE ENGINEERING - 510/hw2 (main)
   $ python hw2_debugging.py
   [1, 5, 5, 6, 6, 8, 10, 10, 11, 11, 12, 12, 13, 15, 16, 17, 18, 19, 19, 20]
   ```

---

## Authors and Contributors

- **Meet Vora**  
  Email: [mvora2@ncsu.edu](mailto:mvora2@ncsu.edu)

- **Raj Patel**  
  Email: [rbpatel4@ncsu.edu](mailto:rbpatel4@ncsu.edu)

- **Vihar Shah**  
  Email: [vshah23@ncsu.edu](mailto:vshah23@ncsu.edu)

---
## Contributions

We welcome contributions from the community! If you would like to contribute to this project to optimize the algorithm, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b ST-XYZ`). XYZ denotes the number E.g. ST-001
3. Make your changes and commit them (`git commit -m 'ST-XYZ: Add new feature'`).
4. Push to the branch (`git push origin ST-XYZ`).
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change. Ensure all tests pass before submitting your pull request.
