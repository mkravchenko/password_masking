# password_masking

##### Script that creates password masking filters for logging in dictionaries.
#### Script can be simply changed for any condition.

For example:
````
{'login': 'test_login', 
'some_field': {'password': 'new'},
'pass': 'Tes1qt!'}`
````
will print as:
````
{'login': 'test_login', 
'some_field': {'password': '***'},
'pass': '*******'}`
````
