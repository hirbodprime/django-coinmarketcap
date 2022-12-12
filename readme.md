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
### Then run the project
```
python3 manage.py runserver
```
## in your chrome type
### to scrape coinmarketcap.com 
```
127.0.0.1:8000/coin/data/ 
```
### to see data as json
```
127.0.0.1:8000/coin/json-data/ 
```
### to see single data using symbol
```
127.0.0.1:8000/coin-data/<str:symbol>
```




