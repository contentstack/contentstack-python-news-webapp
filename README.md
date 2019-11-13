[![Contentstack](https://www.contentstack.com/docs/static/images/contentstack.png)](https://www.contentstack.com/)  
  
## Example WebApp for Contentstack-python  
  
### Prerequisite  
  
*You will need Python 3 installed on your machine. You can install it from* [here](https://www.python.org/ftp/python/3.7.4/python-3.7.4-macosx10.9.pkg).  
 

*Creating **webapp** using flask and contentstack*  


### Setup and Installation  
  
*To use the Contentstack Python SDK to your existing project, perform the steps given below:*  

*create project name contentstack-news*
```
mkdir contentstack-news
cd contentstack-news
```
*Open the terminal and create virtual environment*

```
python3 -m venv venv
```

activate the virtual environment

```
. venv/bin/activate
```

*create app.py named python file inside the directory contentstack-news*

***Install flask and contentstack***  

```
pip install flask
pip install contentstack
```
  

*Put python code structure from [flask]([https://palletsprojects.com/p/flask/](https://palletsprojects.com/p/flask/))  in your app.py*


     
```  
from flask import Flask 
import contentstack     
app = Flask(__name__)      

@app.route('/')  
def home(): 
	# Initialise contentstack by writting below code snippet
	stack = contentstack.Stack(api_key='api_key', access_token='access_token', environment='environment') 
	query = stack.content_type('content_type_id').query() 
	response = query.find() 
return jsonfy({'response': response}) 

```

Run the project by following command:  
  
  ```
   export FLASK_APP=news_app.py
   flask run
 * Serving Flask app "news_app" 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)   
  ```