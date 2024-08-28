<h2 align="center">
    Longest Palindromic Substring
</h2>

<br>

<div align="center">
        <img width="800" height="400" src="https://gabrielghe.github.io/assets/themes/images/2016-02-27-manachers-algorithm-longest-palindromic-substring7.gif" alt="Longest Palindromic Substring">
        <br>
        <figcaption>
            Image source: <a href="https://gabrielghe.github.io/university/2016/02/27/manachers-algorithm-longest-palindromic-substring">Longest Palindromic Substring</a>
        </figcaption>
</div>

<br>

<div align="center">

[![License](https://img.shields.io/badge/License-MIT-purple.svg?style=flat)](https://github.com/Rmv-se-510/hw1/main/LICENSE)
[![Collaborators](https://img.shields.io/badge/Collaborators-3-orange.svg?style=flat)](https://github.com/Rmv-se-510/hw1/graphs/contributors)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg?style=flat)](https://github.com/Rmv-se-510/hw1/search?l=python)
[![Open Issues](https://img.shields.io/github/issues/Rmv-se-510/hw1)](https://github.com/Rmv-se-510/hw1/issues)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Rmv-se-510/hw1.svg)](https://img.shields.io/github/repo-size/Rmv-se-510/hw1.svg)
<img alt="Actions Status" src="https://github.com/Rmv-se-510/hw1/workflows/Test/badge.svg">

</div>

## Longest Palindromic Substring

The longest palindromic substring problem is about finding the longest contiguous subsequence within a given string that reads the same forwards and backwards. A palindrome is a sequence of characters that mirrors itself.

### Problem Explanation

Given a string `s`, your task is to find the longest substring in `s` that is a palindrome.

**Example**:
- Input: `babad`
- Output: `bab` (Note: `aba` is also a valid answer)

### Dynamic Programming Approach

The dynamic programming solution is based on maintaining a table where `dp[i][j]` represents whether the substring from index `i` to `j` is a palindrome.

#### Dynamic Programming Equation:

**Base Case**
- All substrings of length 1 are palindromes: `dp[i][i] = True`
- For substrings of length 2, if `s[i] == s[i+1]`, then `dp[i][i+1] = True`.

  <div align="center">
        <img width="800" height="400" src="https://storage.googleapis.com/algodailyrandomassets/curriculum/hard-strings/longest-palindromic-substring-9.JPG" alt="Longest Palindromic Substring">
        <br>
        <figcaption>
            <b>Figure 1:</b> Base case
        </figcaption>
</div>


**Core Logic**
- `dp[i][j] = True` if:
  - `s[i] == s[j]` and
  - `dp[i+1][j-1] == True` (i.e., the inner substring is also a palindrome)
- Otherwise, `dp[i][j] = False`

  <div align="center">
        <img width="800" height="600" src="https://storage.googleapis.com/algodailyrandomassets/curriculum/easy-strings/length-longest-palindromic-subsequence/DP-solution.png" alt="Longest Palindromic Substring">
        <br>
        <figcaption>
            <b>Figure 2:</b> Core logic
        </figcaption>
</div>

**Final Result**
- The largest `dp[i][j]` that holds `True` is the final value.

---

### Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Rmv-se-510/hw1.git
   ```

2. Change to the repository directory:
   ```bash
   cd hw1
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
   python main.py
   ```
