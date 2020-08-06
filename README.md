# Command_Injection

**command_injection.py** uses **requests** library to send post request to target. Target has a command injection vulnerability where you can add another operating system command after necessary ip input. We added **cat /etc/passwd** to see users. This code is primal version. There is not enough output system and no automate system. We can add a .txt file where we store our malicious inputs and send them with a for loop.

**Source**: https://www.btkakademi.gov.tr/portal/course/siber-guvenlik-icin-python-egitimi-9220#!/about
