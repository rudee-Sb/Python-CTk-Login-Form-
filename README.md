# Login Project

This project is a Python-based login system with advanced features such as "Remember Me", "Show Password", and "Reset Password".
The project is implemented using several modules including **smtplib**, **os**, **PIL**, **MIME**, **CTkMessagebox**, and **customtkinter**.

## Features

- ***Remember Me :*** 
  - Option for users to stay logged in. The user information is stored in a **credentials.txt** file, from which the credentials are retrieved using the os module.  
- ***Show Password :***
  - Click the "Show Password" checkbox to toggle the visibilty of your password.
- ***Reset Password :***
  - Allows users to reset their password.It also has a validating feature which ensure that the new password and confirm password are the same or else it gives a warning.
- ***Verification Email :***
  - Sends a verification email to the registered email of user after a successful login.
- ***Custom theme :***
  - Custom theme for a fresh and vibrant look. 

## Requirements

Ensure you have the following Python modules installed :

- smtplib
- os
- PIL
- MIME
- CTkMessagebox
- customtkinter

You can install the required packages using pip :

```bash
pip install customtkinter
```
## Installation

1. Clone the repository :
   ``` bash
   git clone
   https://github.com/rudee-Sb/Python-CTk-Login-Form.git
   cd login-project
   ```
2. Install the required packages :
   ``` bash
   pip install -r
   requirements.txt
   ```
3. Run the application :
   ``` bash
   python main.py
   ```

## Dependecies
- *smtplib* and *ssl* module for sending emails.
- *os* for navigating to the *.txt* file and other related tasks.
- *PIL* for image processing.
- *MIME* for email formatting.
- *CTkMessagebox* for custom message boxes
- *JSON* file for a custom theme.
- *customtkinter* for creating the gui.

## Contributing

Feel free to fork this repository,make your changes and submit a pull request.
Contributions are welcomw!!

**Note:** Remember to update the email settings and file paths according to your computer's configuration.
## 

For any issue or questions, please open an issue on the repository or contact me at rudrabhau844@gmail.com .













