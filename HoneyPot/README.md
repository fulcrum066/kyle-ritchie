<h1>Basic SSH Honeypot:</h1>
<body>
This project is a Python program which enables users to host a SSH Honeypot server on their computer. External users can connect to the server through their terminal, with all of their interactions, including their log in attempts, being recorded within a log file as well as printed out in the terminal of the user who is running the server. Once the user logs into the server, they will be able type in the commands ‘whoami’, ‘ls’ and ‘pwd’ and send them to the server. The server will then respond to these commands with strings which mimic the responses which an attacker might expect to receive. 
<body/>

<h2>How to run: </h2>
<body>
<p>In order to run the program (the file named 'Basic_SSH_Honeypot.py'), you will need to ensure that you have installed the python socket library, paramiko library and the other libraries which paramiko relies upon, these being cryptography, bcrypt, and pynacl.</p1> 

<p>Once you have started running the program, use the command ‘ssh localhost -p 22’ within a different terminal to access the server. When attempting to log into the SSH Server you will be asked for a password. This password is ‘HelloWorld’.</p>

<p>Once you have connected to the server, if you wish to disconnect, then just type ‘exit’ into the terminal.</p>

</body>

<h2>Resources Used: </h2> 
<li>https://www.youtube.com/watch?v=HO1h57CiF98</li>

<li>Chatgpt</li>
