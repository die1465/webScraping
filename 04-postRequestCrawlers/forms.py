import requests

"""
<form method="post" action="processing.php">
First name: <input type="text" name="firstname">
<br>
Last name: <input type="text" name="lastname"><br> 
<input type="submit" value="Submit">
</form>

The names of the input fields determine the names 
of the variable parameters that will be POSTed to the server
make sure that your variable names match up.

look for the name of the field you want to submit data on
and
when I post it should be on the action link not the page itself
"""
parameters = {'firstname': 'lion', 'lastname': 'eagle'}
r = requests.post("http://pythonscraping.com/pages/processing.php", parameters)
print(r.text)
