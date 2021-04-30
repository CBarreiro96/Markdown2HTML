<div align="center"><img src="https://user-images.githubusercontent.com/66263776/98416555-43fa9b80-204d-11eb-800a-df8e19b62655.jpg" width="500" height= "200"> </div>

# <div align="center"><img src="https://user-images.githubusercontent.com/66263776/98705433-b6b88f00-234b-11eb-97b7-cb193f7424f4.png" width="20" height= "30">    Markdown2HTML <img src="https://user-images.githubusercontent.com/66263776/98705433-b6b88f00-234b-11eb-97b7-cb193f7424f4.png" width="20" height= "30"></div>

## :scroll: Description :scroll:

## :memo: Activities :memo:
<details>
    <summary><b> 1. Start a Script</b></summary>

# :scroll: Description :scroll:
Write a script <font color="red">```markdown2html.py```</font> that takes an argument 2 strings:

* First argument is the name of the Markdown file
* Second argument is the output file name

**Requirements:**

* If the number of arguments is less than 2: print in STDERR <font color="red"> ```Usage: ./markdown2html.py README.md README.html``` </font> and exit 1
* If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
* Otherwise, print nothing and exit 0
---
#### ACTION (STEP 1)
>./markdown2html.py
#### OUTPUT
> Usage: ./markdown2html.py README.md README.html
---
#### ACTION (STEP 2)
>echo $?
#### OUTPUT
> 1
---
#### ACTION (STEP 3)
>./markdown2html.py README.md README.html 
#### OUTPUT
> Missing README.md
---
#### ACTION (STEP 4)
>echo $?
#### OUTPUT
> 1
---
### ACTION (STEP 5)
```console
user@vagrant:~/$ echo "Test" > README.md
user@vagrant:~/$ ./markdown2html.py README.md README.html 
user@vagrant:~/$ 
```
---

</details>