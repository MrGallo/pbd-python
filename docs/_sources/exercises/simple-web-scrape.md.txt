# Simple Web Scrape


In Java, reading text from a web page isn't much more difficult than reading from a text file! Download the following code and get it to compile.


## Files Needed


```eval_rst
* :download:`simple_web_scrape.py <examples/simple_web_scrape.py>`
```



```python
import requests


SECRET_URL = "https://raw.githubusercontent.com/MrGallo/pbd-python/master/web-files/secret-data.txt"
request = requests.get(SECRET_URL)
secrets = request.text

print(secrets)

```

What You Should See
-------------------
```
This file contains secret information...

```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
half credit or less.


1. Change the URL to read text from a different web location.


---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)