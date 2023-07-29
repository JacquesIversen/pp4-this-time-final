Testing for Lake Ale 


## Contents

- ### Validator Testing
    * [Automated Testing](#automated-testing)
    * [W3C Validator](#w3c-validator)
    * [PEP8 Validator](#pep8-validator)
    * [Responsiveness](#responsiveness)
    * [Lighthouse](#lighthouse)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)
  * [Resolved Bugs](#resolved-bugs)
  * [Unresolved Bugs](#unresolved-bugs)



### [W3C Validator](#w3c-validator)

**HTML**
[W3C](https://validator.w3.org/) was used to validate all HTML code used in this project. It was also used to validate CSS.

All Html pages used in this project has been inputted in validator with bugs cleared, including allauth templates used.

**CSS**

No errors validating CSS

![CSS Validation](/docs/testing/css.png)

### [PEP8 Validator](#pep8validator)

To verify that the Python Code  I tested it in the Code Institute's [PEP8 Validator](https://pep8ci.herokuapp.com/). All python files, who have been devoloped have been tested, only files present to bugs/errors will be listed: 

Python IntelliSense is a very helping tool, when writing Python, all errors passed in pep8, was also displayed in IDE.

Errors displayed are solved simultaneously


- staff/views.py 
  - Whitespace
  - Line too Long
  - Empty lines between code
  - No new line at end of file

- settings.py
  - Line too long x6
  - Too many blank lines x1
  - Trailing whitespace x1
  - AUTH_PASSWORD_VALIDATORS line 142-159 to continue error with too long lines

- home/models.py
  - Line 20 too long, not fixed:

- home/views.py
  - Blank line contains whitespace (x4)
  - Trailing whitespace (x4)
  - Missing whitespace (x2)
  - Too many blank lines (x2)
  - Line too long: 



