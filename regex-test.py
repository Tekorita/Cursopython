import re 
  
def Find(string): 
    findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    print(url) 
    return url 
    
      
# Driver Code 
string = 'My Profile: https://auth.geeksforgeeks.org / user / Chinmoy % 20Lenka / articles in the portal of http://www.geeksforgeeks.org/' 
 
print("Urls: ", Find(string))