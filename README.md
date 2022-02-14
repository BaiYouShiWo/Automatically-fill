# Automatically-fill
## 1.What the project does
 Run the Tianxuenet software on the Xiaoyao Android simulator, and automatically fill in the answers of English listening on the premise of having answers.
 
## 2.Why this project is created
  What's interesting is that I do all the things just because I can't fill in a little part of answer and then go on to fill in the next part,the app is designed to prevent students quickly fill in the answers you got from your classmates.

## 3.How to get started with the project
  Most importantly,we need the answer of the English listening test(for example,I got this from my schoolmates who had finished this homework),and put these information in         "keywords_list.txt".but you have to know that the answer are required to have a format like "1.x 2.y 3.z ..."
*** 
  And then a VirtualBox Android is needed ,and run TianXuewang on it,and start a listening test.
***
  The last step is to run the main.py .
***
  tips:and the "text_pretreatment.py" in the file is just help you to remove the";" in the text ,it's not important.

## 4.environment:
  The environment I'm using is Python 3.8.8 (you can run "python -m pip install -r requirements.txt"to got the needed package)
  The editor I use is vscode
  
## Description of the directory structure
- README.md                   *// help*
- main.py                     *// mian project*
- text_pretreatment.py        *//text pretreatment*
- photo
  - 2.jpg                  *// the picture that Program intercept*
- keywords_list.txt           *//put the answer in it*
- requirements.txt            *//help you to install packages*

## what the project will be changed
- [x] The accuracy of filling is higher, the test can reach more than 20 points
- [ ] add a function to compare image similarity ,so it can reduce the number of loops
- [ ] Let's spruce up the code

###### My ability is limited so I hope you can bear with my messy code style🙏🙏🙏
