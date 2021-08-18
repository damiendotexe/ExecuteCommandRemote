# ExecuteCommandRemote
A Flask project that executes any command you type into the webpage on the host PC.
# Install And Run (requires git)
First, clone the repo by using:

`git clone https://github.com/damiendotexe/ExecuteCommandRemote.git`

Then, CD into the repo and install python dependencies by doing:

`# Windows:
cd ExecuteCommandRemote
py -m pip install flask
`

`# Mac and Linux:
cd ExecuteCommandRemote
python -m pip install flask
`

To start the program, make sure you are in the `ExecuteCommandRemote` directory and type:

`# Windows:
py backend/server.py
`

`# Mac and Linux:
python backend/server.py
`
# Accessing the webpage
After you start the script, it should show an IP, followed by a port (should be 5000). copy that address into a web browser and then should see a webpage that looks like this:
![](https://user-images.githubusercontent.com/81449138/129946099-aa608ddb-d13b-424d-9794-a914eb1d1940.png)
Now all you need to do is type a command in the textbox and press `Submit`.
It should execute whatever command you type in the textbox on the host's machine.
# Note(s)
The webpage only works for people who are connected to the same WiFi as you. (for security reasons)
# Copyright and stuff
(C) damiendotexe (Damien S) 2021.
