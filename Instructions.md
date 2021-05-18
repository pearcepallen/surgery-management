# Setup
After cloning the branch on the respository. From the root folder, assuming you have Python and pip installed.
I would recommend creating a Python Virtual Environment. This can be done by following: 

- pip install virtualenv
- virtualenv myenv

This env can then be activated by running:

- myenv\Scripts\activate

If the above command doesn't work, the following should allow it to run for the duration of the program.

- Set-ExecutionPolicy Unrestricted -Force 

After setting up the virtual environment.
In the command terminal, run: 

- pip install -r requirements.txt 

This should download all the packages needed to run the API. 

# Testing
Inside the backend directory, run:
- python manage.py runserver

This should start the application server and allow live requests to the API.

Provisions have been made for an admin user.
- admin@speurgroup.com
- password

The urls all follow the conventions provided in the swagger.yaml file so all endpoints can be called by adding the paths to the development server. (http://127.0.0.1:8000/).

To provide authorization to endpoints. After logging in with provision made. Save the jwt provided and in the headers, add:
- Authorization: 'Bearer {jwt}'.

As a superuser, the changes to the database through the endpoints can be monitored by going to /admin on the application server.
A superuser account can be created with the command:
- python manage.py createsuperuser


Or the provided superusr can be used by signed in with:

- superuser
- speurgroup162

For reference to the names of the models. All attributes are named the same as in the swagger.yaml except for 
- fname: renamed to firstName
- lname: renamed to lastName

And any additional attributes.
These and additional attributes can be checked in the models.py file. 

Additionally, here is a static snapshot of the collection I was working with using Postman albeit without any authentication headers or values and with the {{URL}} environment variable being http://127.0.0.1:8000.
https://www.getpostman.com/collections/90e9f08d636fb79ec74c


# Additional Information

## Assumptions
- Every staff member is a user of the Surgery Management API and vice versa
- The admin that creates the staff member & user profile sets a default password that the user can then use to set a new password.

## Notes
Please ensure all urls are called with an appended slash.

## Format when entering date
YYYY-MM-DD

## Multiple Doctors when Creating Surgery
When entering the ids of doctors upon creation of a surgery, leave a space between ids as the program is written to split upon spaces.

## Invalidate JWTs
Tokens are stateless means of authentication which means they are not stored. As such, after an extensive amount of research, I found that there was no true way of invalidating JWTs on logout without using the database on the server. A token is usually just removed from the client in order to block authentication. I did however implement a blacklist, which though it uses the database, provides a bit more security. 

This was done with the simple jwt blacklist function. By keeping the expiry date for all tokens short and rotating them often through the client. The tokens can be invalidated by adding the refresh token to a blacklist on logout. This blocks new access from being generated without again, signing in with said credentials to get a new refresh token.

The tokens have a somewhat long lifespan to make testing more convenient so when testing the blacklist function. 
Go to backend/settings.py and change the simplejwt configuration at line 59 to 5 mins or less.
- timedelta(days=1) to timedelta(minutes=5)
