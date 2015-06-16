Quick module to read in HTML and tries to identify contacts from the HTML, whether just email, or first,last based matches etc.


Usage
=====


    >>> from html_contact import HtmlContact
    >>> hc = HtmlContact(raw_html)
    >>> contacts = hc.search()

Result list is a list of contacts

    >>> for result in result_list:
    ...     print result.url
    ...
    u'http://www.python.org/psf/
    ...
    
What you get is a list of Contacts() instances, each comes with the following values:
    
```py
self.first_name:         fitst name of the contact
self.last_name:            last_name of the contact
self.email:          email of the contact
```
    
=======
# html_contact
Extracts contact info from website based first/last
