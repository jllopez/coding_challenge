# Coding Challenge

The purpose of this challenge is to write code and testcases to return the longest word (plain and reversed) in a file.

## Assumptions

1. **Input file:**

   File must follow the following standard:

   ```
   {
       "lowercase_letters": {
           "given_input": "a ab abc abcd abcdefg",
           "expected_output": "abcdefg",
           "expected_output_transposed": "gfedcba"
       },
       "numbers": {
           "given_input": "1324 12 3 0 1325 23 341 13410158 1235 12 1",
           "expected_output": "13410158",
           "expected_output_transposed": "85101431"
       }
   }
   ```

   Why not using a regular file with contents such as:

   ```
   a
   ab
   abc
   abcdefg
   ```

   Because this limits test case reuse. If we want to run the same test with different data we will need to create separate input files for each scenario we want to cover. Also, for each newly created file we will need to open the file, read it, store the contents in a string and finally close it. Since we are storing the contents in a string; why not pass a string in the first place? This problem seems like a good candidate for a Data Driven Test approach.

   **Why Data Driven Test?**

   This allows us to implement an approach where the same test is used with different data. Did I also mention that adding new tests is easier and more readable?

2. **Two or more words with the same size:**

   The last longest word is returned if there are 2 or more words with the same size.

## Requirements

- [Python 3.7.0](https://www.python.org/downloads/release/python-370/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://docs.python.org/3/tutorial/venv.html)
- [Git](https://git-scm.com/downloads)

  **Note:** Creating a virtual environment is a good practice to isolate and control the Python environment to be used in a project. It also helps to overcome permission issues when trying to install new packages.

## Run tests

1. Open a terminal/prompt
2. Run `git clone https://github.com/jllopez/coding_challenge.git` to fetch the projects code
3. Run `cd coding_challenge` to change to the project's root directory
4. Run `python3 -m virtualenv env` to create a virtual environment
5. Run `source env/bin/activate` to activate the virtual environment
6. Run `pip install -r requirements.txt`
7. Run `python test_longest_word_finder.py`

If everything was setup correctly an output similar to this should be displayed in the terminal:

```
Running tests...
----------------------------------------------------------------------
.............
----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK

Generating XML reports...
```

In addition, an XML file with test results should be found under `./test_results`

## Want to run the test with your own data?

Running the test with your own data is easy. All you have to do is add a new entry to `input_file.json`.

For example,

If you want to check what is the longest word in `which word is the loooooooongest one here?` all you have to do is add the following entry at the end of the dictionary in `input_file.json`:

```
"my_new_test": {
"given_input": "which word is the loooooooongest one here?",
"expected_output": "loooooooongest",
"expected_output_transposed": "tsegnooooooool"
}
```
