# Forgot Password

The database was designed with all users of the Surgery Management API having an email assigned. An email that should be unique to that specific user. The Forgot Password feature utilizes this email to allow a user to change their password. 
- The user should enter their email and if it is registed, a verification code is sent to the user's email that has been assigned to the user. 
- The user should then input this verification code through the client and if the code is indeed correct (matches the verification code assigned to the user). 
- The user will be able to enter a new password that will update their user password and clear the verfication code assigned to the user.

The enpoints used to implement Forgot Password are the:
- /reset
- /new
endpoints. The reset endpoint generate the random string and sends while the new endpoint is used to change the password.