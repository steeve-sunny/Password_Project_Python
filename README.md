🔐 Password Generator & Strength Grader
A Python tool that generates secure passwords on request and grades their strength — built entirely with the Python standard library.

📌 What It Does
You provide a username. The tool does two things:

  1. Generates a unique 16-character password for that user, drawing from letters, digits, and special characters.
  2. Grades the password's strength based on character diversity, returning a plain-English result and a percentage score.

Running the Script
Open password.py and uncomment the two lines at the bottom:

python
print(CreatePassword("alice"))
print(StrengthOfPassword("alice"))

Then run:
terminal
python password.py

Example output:
\nG7#mKpL!qX2&wRvZ
\nThe Strength of the Password is Very Secure, with a strength scale of 100%

🧠 How It Works
Password Generation — CreatePassword(username)

  1. Builds a character pool from uppercase, lowercase, digits, and punctuation
  2. Randomly picks 16 characters
  3. If the generated password already exists, it recursively retries until a unique one is produced
  4. Stores the username → password mapping for later lookup

Strength Grading — StrengthOfPassword(username)
Scores the password 1 point for each character type present:

Character                   |           Example
---------------------------------------------------
Lowercase letters           |          a–z
Uppercase letters           |          A–Z
Digits                      |          0–9
Special characters          |          !@#$...


Score  |   Grade             |   Percentage
--------------------------------------------------
4/4    |   Very Secure       |   100% 
3/4    |   Secure            |   75% 
2/4    |   Not That Secure   |   50% 
1/4    |   Not Secure        |   25%


💡 Python Concepts Used:

  1. Recursion (duplicate password handling)
  2. Dictionaries and lists for in-memory storage
  3. The string and random standard library modules
  4. Conditional logic and percentage-based scoring


👤 Author:
Steeve Sunny — https://github.com/steeve-sunny · https://www.linkedin.com/in/steeve-sunny-261080393/
