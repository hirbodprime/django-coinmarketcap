# requirements 
``` sudo apt install python3-venv ```  
``` python -m venv myvenv ```  
``` cd myvenv/bin/ && source activate ```  
``` pip install -r req.txt ```  

# install coinmarkecaoscraper from pip (one of the dependencies)
```
pip install git+https://github.com/hirbodprime/coinmarketcap.git
```


## how to run
### first create a superuser
```   
python3 manage.py createsuperuser 
```  

### Then create the database
### have in mind you don't need to do makemigrations because the files are already in the project
```
python3 manage.py migrate
```
### Then run the project
```
python3 manage.py runserver
```
## in your chrome type
### home page 
```
127.0.0.1:8000/ 
```

### to scrape coinmarketcap.com 
```
127.0.0.1:8000/coin/scrape-coins/ 
```
### to see data as json
```
127.0.0.1:8000/coin/get-coins/ 
```
### to see single data using symbol
```
127.0.0.1:8000/get-coin/<str:symbol>
```
### to see single logo using symbol
```
127.0.0.1:8000/get-logo/<str:symbol>
```



