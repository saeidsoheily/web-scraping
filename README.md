Example codes and experiments around Web Scraping

Web scraping is an automatic way to retrieve unstructured data from website and store them in a structured format.
Web scraping just works like a bot person browsing different pages website and copy paste down all the contents.
When you run the code, it will send a request to the server and the data is contained in the response you get.

If website stores all their information on the HTML front end, one can directly use code to download the HTML contents and extract out useful information.
However, if website stores data in API and the website queries the API each time when user visit the website,
one can simulate the request and directly query data from the API, which is more complicated than the first approach especially if authentication or token is required.

The most commonly used library for web scraping in Python are Beautiful Soup, Requests and Selenium.
Beautiful Soup helps you parse the HTML or XML documents into the readable format. It allows to search different elements within the documents and helps to retrieve required information faster.
Requests is a Python module which you can send HTTP requests to retrieve contents, and helps to access website HTML contents or API by sending Get or Post requests.
Selenium is widely used for website testing and allows to automate different events (clicking, scrolling, etc) on the website to get the results you want.


- requests_webscraping_ebay.py: web scraping (ebay website) using Beautiful Soup and Requests. 
To run in terminal: $ python3  requests_webscraping_ebay.py  <https://www.ebay.fr/...> 

