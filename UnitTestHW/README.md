# The Basics: Leetcode
## Install Requirements  
In the folder UnitTestHW, run the following command:
```sh
pip install -r requirements.txt
```
or just:  

```sh
pip install pytest
```
## [FizzBuzz](https://leetcode.com/problems/fizz-buzz/)  

9c disliked the fact that Newbie kept playing video games day after day, so he told Newbie to do some Leetcode.
Soon enough, Newbie said he couldn't finish the Fizzbuzz problem.

>   Derived from Leetcode:  
>   fizzBuzz(i) = "FizzBuzz" if i is divisible by 3 and 5.  
>   fizzBuzz(i) = "Fizz" if i is divisible by 3.  
>   fizzBuzz(i) = "Buzz" if i is divisible by 5.  
>   fizzBuzz(i) = i (as a string) if none of the above conditions are true.  

### (a) Basic Unit Test (2 points)  
1. Finish test_fizzbuzz.py in Fizz Buzz/Basic  

2. **Run pytest in that same folder. You should get a result saying ``` 1 failed, 3 passed in <time>s ```**  

### (b) Class Unit Test (2 points)  
1. Finish test_fizzbuzz.py in Fizz Buzz/Class  
> test_main is similar to an integration test  
> test_invalid_input is an edge case  
> test_invalid_input should pass，as the test itself expects an error  

2. **Run pytest in that same folder. You should get a result saying ``` 2 failed, 5 passed in <time>s ```**  

## [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) (4 points)  

9c mocks Newbie's poor coding skills.  
"How 'bout this. You pick another easy question, and I'll solve a random question from 1~100 in leetcode's question base. If you win, you get a new video game to play."  
"What if you win?" Newbie replies.  
"I don't get nothing. I just wanna show off how I'm better than you B)" 9c says.  
(Google's random picker picks the number 10, which is a HARD question.)  
9c: "ARE YOU KIDDING M-"  
(With the new video game, Newbie is even lazier than before.)  
### Parametrize  

> This test is more like a Black Box test, **you do not need to know how isMatch() works**, just test if the inputs will produce the correct outputs.  
> the xfail part can be ignored for now.  
1. Use **one** function to test all testcases in Regular Expression Matching/test_solution:  

2. **Run pytest. You should get a result saying ``` 1 failed, 6 passed in <time>s ```**  

### xfail  

3. Remove the """'s  
4. Put the failed testcase into this new function.  
5. **Run pytest. You should get a result saying ``` 6 passed, 1 xfailed in <time>s ```**  

## Extra
- Title's redirect you to the actual Leetcode problem (not very important for the homework though)  
- [Pytest Tutorial – How to Test Python Code](https://www.youtube.com/watch?v=cHYq1MRoyI0) teaches everything you need to know and more.  
- python has a unittest module that you can also learn about.  

-----

### Unit Test Assignment (8%)

- **Objective:**  
  Complete the unit tests for two problems: FizzBuzz and Regular Expression Matching.

- **Instructions & Steps:**  
  **(a) FizzBuzz Testing**
  - **Basic Unit Test (2 points):**
    1. Complete the file `test_fizzbuzz.py` located in the `Fizz Buzz/Basic` folder.
    2. Run pytest in that folder; the expected result is:  
       ```
       1 failed, 3 passed in <time>s
       ```
  - **Class Unit Test (2 points):**
    1. Complete the file `test_fizzbuzz.py` in the `Fizz Buzz/Class` folder.
    2. Note:  
       - `test_main` acts as an integration test.
       - `test_invalid_input` should correctly handle edge cases by raising an error.
    3. Run pytest; the expected result is:  
       ```
       2 failed, 5 passed in <time>s
       ```

  **(b) Regular Expression Matching Testing (4 points)**
  - **Parametrized Testing:**
    1. Use a single function to run all test cases found in `Regular Expression Matching/test_solution`.
    2. Run pytest; the expected result is:  
       ```
       1 failed, 6 passed in <time>s
       ```
  - **Handling xfail Tests:**
    1. Remove the triple quotes surrounding the xfail test.
    2. Move the failed test case into a new function.
    3. Re-run pytest; the expected outcome is:  
       ```
       6 passed, 1 xfailed in <time>s
       ```

- **Submission Requirements:**  
  Commit and push all updated test files and any changes made to your repository.