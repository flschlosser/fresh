Fresh
=======

Tiny python tool to observe a folder and execute commands if the content of the folder changes.


Freshfile
---------

````yaml
# run the commands on start up of Fresh
runOnStart: true

# the root path to check for changes
path: .

# the commands to run when changes have been detected
commands:
  - open -g -a Safari -e http://localhost:8080
  - touch ~/testfile.txt
````

Usage
-----

### download dependencies
`pip install -r requirements.txt`

### create a Freshfile 
`touch Freshfile` (for content see example)

### run
`python3 fresh.py`




License & Authors
-----------------
- Author:: Florian Schlosser

```text
MIT License

Copyright (c) 2018 Florian Schlosser

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```