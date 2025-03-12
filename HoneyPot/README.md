<h1>Basic SSH Honeypot:</h1>
<body>
This project is a Python program which enables users to host a SSH Honeypot server on their computer. External users can connect to the server through their terminal, with all of their interactions, including their log in attempts, being recorded within a log file as well as printed out in the terminal of the user who is running the server. Once the user logs into the server, they will be able type in the commands ‘whoami’, ‘ls’ and ‘pwd’ and send them to the server. The server will then respond to these commands with strings which mimic the responses which an attacker might expect to receive. 

<h2>How to run: </h2>
In order to run the program, you will need to ensure that you have installed the python socket library, paramiko library and the other libraries which paramiko relies upon, these being cryptography, bcrypt, and pynacl.
</body>

<h2>Resources Used: </h2> 
<li>https://www.youtube.com/watch?v=HO1h57CiF98</li>

<li>Chatgpt</li>
