
<h2 align="center">
    HW2: Debugging Merge Sort
</h2>

<div align="center">
        <img width="300" height="200" src="https://www.lavivienpost.net/wp-content/uploads/2022/02/merge-sort-400.gif" alt="Merge Sort">
        <br>
</div>

<a href="https://github.com/Rmv-se-510/hw1">Link for HW1</a>

<div align="center">
    
[![cov](https://img.shields.io/badge/coverage-100%25-green)](https://github.com/Rmv-se-510/hw2/actions/runs/11079775494)
[![License](https://img.shields.io/badge/License-MIT-purple.svg?style=flat)](https://github.com/Rmv-se-510/hw2/main/LICENSE)
[![Collaborators](https://img.shields.io/badge/Collaborators-3-orange.svg?style=flat)](https://github.com/Rmv-se-510/hw2/graphs/contributors)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg?style=flat)](https://github.com/Rmv-se-510/hw2/search?l=python)
[![Open Issues](https://img.shields.io/github/issues/Rmv-se-510/hw2)](https://github.com/Rmv-se-510/hw2/issues)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Rmv-se-510/hw2.svg)](https://img.shields.io/github/repo-size/Rmv-se-510/hw2.svg)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
<img alt="Actions Status" src="https://github.com/Rmv-se-510/hw2/workflows/Test/badge.svg">
[![Flake8](https://img.shields.io/badge/flake8-10.00-green)](https://github.com/Rmv-se-510/hw2/actions/runs/10843072509)
[![Radon](https://img.shields.io/badge/radon-3.33-green)](https://github.com/Rmv-se-510/hw2/actions/runs/11079775494)
[![Pylint](https://img.shields.io/badge/pylint-10.00-green)](https://github.com/Rmv-se-510/hw2/actions/runs/11079775494)
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


## Directory Structure

- **`post_traces`**: Contains logs and screenshots generated after running static analysis tools like *autopep8*, *flake8*, *pylint*, and *radon*. It includes:
  - `merge_sort_traces`: Screenshots and text files of the results after refactoring merge sort.
  - `selection_sort_screenshots`: Screenshots documenting the debugging process for Selection Sort.

- **`pre_traces`**: Holds screenshots and text files from static analysis before refactoring, specifically for merge sort.

- **`sorting_algorithms`**: Contains the implementations of the Merge Sort and Selection Sort algorithms.

- **`tests`**: Includes test cases for Merge Sort and Selection Sort.

- **`work_dir`**: Contains various debugging files and logs used during the development and debugging process, organized by debugging method (e.g., print debugging, log debugging, pdb debugging).

```
hw2
│   .gitignore
│   coverage.json
│   hw2_debugging.py
│   LICENSE.md
│   rand.py
│   README.md
│   requirements.txt
│   
├───.github
│   └───workflows
│           automate.yml
│
├───post_traces
│   ├───merge_sort_traces
│   │   ├───screenshots
│   │   │       autopep8_after_running_first_time.png
│   │   │       autopep8_output_after_running_first_time.png
│   │   │       flake8_after_refactoring.png
│   │   │       flake8_output_after_refactor.png
│   │   │       pylint_after_refactoring.png
│   │   │       pylint_output_after_refactoring.png
│   │   │       radon_output_ss.png
│   │   │       radon_output_txt.png
│   │   │
│   │   └───txt_files
│   │           post_autopep8_formatted.txt
│   │           post_flake8_output.txt
│   │           post_pylint_refactor.txt
│   │           post_radon_refactor.txt
│   │
│   └───selection_sort_screenshots
│           1_selection_sort_bug.png
│           2_selection_sort_print_debug.png
│           3_selection_sort_log_debug.png
│           4_selection_sort_log_fixing_temp_variable_issue.png
│           5_selection_sort_pdb_debug.png
│           6_selection_sort_test_case_pass.png
│
├───pre_traces
│   └───merge_sort_traces
│       ├───screenshots
│       │       autopep8_before_refactor.png
│       │       autopep8_before_refactor_2.png
│       │       flake8_before_refactor.png
│       │       flake8_before_refactor_2.png
│       │       pylint_before_refactor.png
│       │       pylint_before_refactor_2.png
│       │       radon_before_refactor.png
│       │       radon_before_refactor_2.png
│       │
│       └───txt_files
│               autopep8_before_refactor.txt
│               flake8_before_refactor.txt
│               pylint_before_refactor.txt
│               radon_before_refactor.txt
│
├───sorting_algorithms
│   │   mergeSort.py
│   │   selectionSort.py
│
├───tests
│   │   test_merge_sort.py
│   │   test_selection_sort.py
│
├───work_dir
│   ├───debuging
│   │       debugging.py
│   │
│   ├───fixing_log_debugging
│   │       debugging.py
│   │       partial_debugging.log
│   │
│   ├───log_debugging
│   │       debugging.log
│   │       debugging.py
│   │
│   ├───pdb_debugging
│   │       debugging.py
│   │
│   └───print_debugging
│           debugging.py
```

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
