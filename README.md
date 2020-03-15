# Shipping Label Web App

### Setup
1. Install Python (if you haven't already)
2. Clone this repository and `cd` into it
3. If you have virtualenv installed, go to the next step. Otherwise start following instructions in VirtualEnv Setup
4. Enter your virtualenv (if you'd like)
5. Run `pip install -r requirements.txt`
6. `cd` into `shipping` and run `python manage.py runserver`
7. Create a superuser by running `python manage.py createsuperuser`
8. Head to http://127.0.0.1:8000/login/ and login with the credentials you just made.
9. Enter shipping and parcel information and hit submit
10. To logout, go to http://127.0.0.1:8000/logout/

### VirtualEnv Setup
1. Run `pip install virtualenv` in the top folder
2. Run `virtualenv env`
3. To enter the virtual environment, run `source env/bin/activate`
4. To deactivate the virtual environment just run `deactivate`
5. If you're having issues, check the links in the debugging section of README

### Creating Extra Users
For testing purposes, you can create extra users!
1. Go to http://127.0.0.1:8000/admin/ and login with superuser credentials
2. Create a new user by clicking Add next to Users
3. Enter credentials for this user
4. Logout of admin by going to http://127.0.0.1:8000/logout/
5. Log into the new account by going to http://127.0.0.1:8000/login/


### Design Choices
I decided to only store the shipment label url and tracking numbers in the database for each user rather than storing the address information and parcel information that the user inputs. For security reasons, I made it so users will only be able to see their own shipments. You can test this by creating different users and creating different shipping labels. When you load the page, the shipments for each user should be uniquely listed below the forms. This web app was created using Django, Django REST, and Bootstrap! Please email me if you have any questions about certain design choices that I made.

### Debugging
If you're getting an error saying `No rates found.`, this is because EasyPost couldn't find a rate for the specified package dimensions. For testing purposes, inputting 10 for all fields should succeed.

Installing pip: https://pip.pypa.io/en/stable/installing/
VirtualEnv: https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
