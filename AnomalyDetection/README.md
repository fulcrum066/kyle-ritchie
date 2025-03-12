<h1>Anomaly Detection:</h1>
<body>
Description: In this project, I am attempting to create a program which can detect anomalies in sets of data collected from my home network. Many modern network security systems collect data on the behaviour of their users within the system, as well as the types of packets being sent throughout it. What I am attempting to do is create a custom packet sniffer to collect data on the types of packets which enter my home network, and as well as create an algorithm which can analyse this data and detect anomalies within it.

Currently I have almost finished creating the packet sniffer by following the YouTube playlist listed within the ‘Resources Used’ section. The code which I have written is currently identical to the code demonstrated within the videos in the YouTube playlist aside from the main function. I will need to make modifications to this code so that the packet sniffer works with packets at layer 3 of the OSI model, rather than packets at layer 1. I will need to make these modifications as I have discovered that the functions provided by the python socket library which are usable on macOS devices cannot capture packets which are at layer 1 of the OSI model, and can instead only capture packets which are at the lowest, layer 3. 

</body>

<h2>Resources Used: </h2>
<li>https://www.youtube.com/watch?v=WGJC5vT5YJo&list=PL6gx4Cwl9DGDdduy0IPDDHYnUx66Vc4ed&index=1</li>

<li>Chatgpt</li>
