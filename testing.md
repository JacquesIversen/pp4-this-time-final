Testing for Lake Ale 


## Contents

- ### Validator Testing
    * [Automated Testing](#automated-testing)
    * [W3C Validator](#w3c-validator)
    * [PEP8 Validator](#pep8-validator)
    * [Responsiveness](#responsiveness)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)


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


### [Responsiveness](#responsiveness)
Build has been done so very responsive with a mobile first perspective using inspect function on Google Chrome.


### Home/index Page
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Homepage | Display | Homepage is displayed when url is passed into browser | PASS
Block Title | Display | Title and Favicon displayed | PASS
Navbar | Display | Left side: When user is not logged, "book, pricing & about us" is present | PASS
Navbar | Display | Right side: When user is not logged in, only "Register" and "Login" should be visible. | PASS
Navbar | Display | When user is not logged in "Book here" will send user to login instead. | PASS
Navbar | Display | When user is logged in, Book here will take user to booking | PASS
Navbar | Display | When user is logged in, "Go to your Profile" is visuable, beside "Logout" | PASS
Navbar | Display | When Admin/Staff is logged in, Dashboard is visuable| PASS
IMG Section | Display | Should be displayed below navbar with button inside | PASS
Textarea | Display | Should be displayed below Img, with 3 buttons visible  | PASS
Textarea, Button | Display | When not logged in: top button should display "log in" and send user to login page  | PASS
Textarea, Button | Display | When logged in: top button should display "Make a booking" and send user to booking  | PASS
Footer | Display | Should follow bottom of content | PASS
Footer | Display | Should display requirements | PASS
Footer | Display | Will contain 3 links: "Home", "Pricing" "Staff Login" with "Staff login" sending staff to login --> Dashboard | PASS
Body Section | Click | All links are working | PASS
Navbar | Click | All links are working | PASS
Footer | Click | All links are working | PASS

### Pricing Page
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Pricing | Display | Should Post Variant name, price, information and picture | PASS
Pricing | Display | Navbar and Footer, following Index page | PASS

### About us Page
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
FAQ | Display | Should display 3 columns with 6 questions | PASS
Contact | Display | Contact form below FAQ section, with name, email and message | PASS
Contact | Display | Button should submit input and redirect to mail submitted confimation | PASS
About us | Display | Navbar and Footer, following Index page | PASS

### Booking Page (Logged in)
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Booking | Display | Variants/products on top of each other with break inbetween | PASS
Booking | Display | Variant name, price and information | PASS
Booking | Checkbox | Need to be filled to submit order | PASS
Booking | Checkbox | Will autofill 1 amount | PASS
Booking | input | Will display amount when empty | PASS
Booking | input | Will send inputed value  | PASS
Booking | Button | Will submit og pop up a modal  | PASS
Booking | Modal | Redirect to submission site | PASS

### Booking Submitted Page (Logged in)
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Order Submitted | Display | Links to Profile and Homepage | PASS
Order Submitted | Display | Combined Price | PASS
Order Submitted | Display | Summary of ordered product(s) | PASS

### Profile (Logged in)
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Profile | Display | Display user information | PASS
Profile | Display | CRUD functions in auth | PASS
Profile | Display | Show current Orders | PASS
Profile | Display | Link in table to Order Details | PASS
Profile | Button | Edit should delete and redirect | PASS
Profile | Button | Delete should delete, without confirmation | PASS
Profile | Display | When no orders, table should contain a link to booking | PASS


### Details (Logged in)
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Details | Display | Should display order Number, variant, user who booked, datetime for booking, price | PASS
Details | Button | Delete the order, without confirmation | PASS


### Dashboard (StaffCI / Admin logged in)
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Top column | Display | Show todays total revenue | PASS 
Bottom Table | Display | Show, All table row inputs: | PASS 
Bottom Table | Display | Status should be None, if not changed manually | PASS 
Bottom Table | Button | Status Change when clicked | PASS 
Bottom Table | Dropdown | Should have "Awaiting Pickup" and "Delivered" | PASS 

### User Authentication
Feature | Action | Expected Result | PASS/FAIL 
---|---|---|---
Login | Display | Follows allauth and Crispy forms design  | PASS 
Login | Link | Links working | PASS 
Login | Button | Signs you in and redirect to index | PASS 
Login | Checkbox | Remember me working, outside google Cache | PASS 
Sign up | Display | Follows allauth and Crispy forms design  | PASS
Sign Up | Button | Signs you up and redirect you to index. | PASS
Sign Up | Link | Links working | PASS 
Sign Out | Display | Follows allauth and Crispy forms design | PASS
Sign Out | Button | Signs you out and redirect to index | PASS 
Forgot Password | Display | Follows allauth and Crispy forms design  | PASS
Forgot Password | Button | Redirect user to confirmation  | PASS
Forgot Password | Button | User recieve email | FAIL



## [Bugs](#bugs)

Bugs were found during testing creation of ReadMe
Bugs were found and corrected when Validated
**Remaining Bugs**
Will be in bug section, even though it might belong in features. But lack of 2nd degree validation on the site in general, and confirmation messages/modals. 
















