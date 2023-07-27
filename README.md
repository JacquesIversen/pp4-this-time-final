# Lake Boatandhoes Rental 

This rental company is fortunately fictional and follows a strict businessplan to ensure the predator wildlife of the ecosystem by feeding happy paying tourist to them. The physical part of the store is thought to handle all security policy, payment and local storage. The productstorage of the facility is thought to be endless, as the company recieve thousands of Kayak donations daily from numerous NGO's. This app is designed to make you flick a smile, if that doesn't happen the dev would consider it a failure. 


You'll find the livelink for the site here: 
https://project4-final-c54c1eeb1fef.herokuapp.com/


## Contents

* UX Design
    * Site Goals
    * Agile Planning
    * User Stories
        * User Stories
        * Epics
    * Design
    * Features
    * Technologies Used
    * Deployment
    * Testing
    * Credits



### User Stories


### Developer: (Dev)
- As Dev, I need to install/create the project and app files.
- As Dev, I need to setup base/index.html to extend other html files upon.
- As Dev, I need to setup and proove function of static, media and templates files in directories.
- As Dev, I need to Decide on which CDN, and Script to choose and install.
- As Dev, I need to design a Header and footer to suit design ideas. 
- As Dev, I need to install, implement and test Django-Allauth
- As Dev, I need to Update Procfile and Requirements
- As Dev, I need to Use Django DEBUG functions to locate deployment issues.
- As Dev, I need to locate and listen to the Heroku buildlog to adapt requirements.
- As Dev, I need to deploy the final site, without compromising my ability to still edit the app.

### User: (Customer)
- As a Customer, I want to see what this company has to offer. 
- As a Customer, I want to know how to locate and contact this company.
- As a Customer, I want to be able to book at least 1 product for any given timeperiod.
- As a Customer, I would like multiple options of products.
- As a Customer, I would like multiple options of durations.
- As a Customer, I would like a personal login page.
- As a Customer, I would like to be able to change my password if forgotten. 
- As a Customer, I need to be able to view, delete or change my booking.
- As a logged-in user, I can make a booking so that I can reserve activities for one or more guests at a specific date and time, view and update my existing booking/s or delete any existing booking.
- As a site user, I can view essential information so that I can find out about the business hours, contact number, and other important information.
- As a site user, I can view photos so that I get a feel of the atmosphere and what activities are offered.




### Staff and Company Owner
- As the owner, I would like to have a home page with vital information and a obvious CTA
- As the owner, I would like the booking to be as easy and swift as possible to avoid 2nd. thougts.
- As the owner, I want my staff to easily locate bookings with minimum effort. 
- As the owner, I want the customers to pay beforehand to ensure revenue in the business.
- As the owner, I want the contactform to be an endless and troublefull process to minimize claims and returns.
- As the owner, I want my staff to easily edit and manage inventory and products
- As the owner, I want my staff to have CRUD capabilities in the products pages
- As the owner, I want to limit my dependencies to edit site.
- As Staff, I can manage the bookings so that I can create, view, update, and delete any bookings and avoid any double bookings.
- As Staff, I can manage the bookings so that I can create, view, update, and delete any bookings and avoid any double bookings.
- As Staff, I can monitor todays bookings, revenue and customer amount.


### Admin / Superuser
- As an admin, I can manage registered users so that I can monitor and control user access.
- As an admin, I can add or remove details about the business and its surrounding so that the site information stays updated.
- As an admin, I can access stored booking data.




--- 
pip3 install django
django-admin startproject main .
python3 manage.py startapp home
python3 manage.py startapp staff
pip3 install django-allauth
-- Templates:
ls ../.pip-modules/lib
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates
-- Superuser / admin:
python3 manage.py createsuperuser
-- Crispy forms:
pip3 install django-crispy-forms
pip3 install crispy_bootstrap5
pip3 freeze --local > requirements.txt
-- Img management:
pip3 install pillow

