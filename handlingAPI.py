import requests  #Used to make HTTP requests (GET, POST, etc.) in Python.

def fetch_random_user_freeapi():
     url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
     response= requests.get(url) #Sends a GET request to the given URL and stores the server’s reply.
     
     data= response.json()    #Converts the API response into a Python dictionary (JSON → dict).
     if data ["success"] and "data" in data : #Checks whether the API call succeeded and contains expected data
         user_data  =  data["data"]
         username = user_data  ["login"]["username"]
         country = user_data  ["location"]["country"]
         
         
         return username,country
     else :
        raise Exception("failed to fetch user data ")   #Manually throw an error if something goes wrong.
    

def main(): 
     try:
         username,country= fetch_random_user_freeapi()
         print(f"username : {username} \n country : {country}")
     except Exception as e:
         print(str(e)) 


if __name__ == "__main__": #Ensures the main() function runs only when you run the script directly (not when imported).
     main()


import requests 

def fetch_random_jokes_freeapi():
     url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
     response = requests.get(url)
     data = response.json()

     if data["success"] and "data" in data:
         joke_data = data["data"]
        
         # Check for the single-part joke format first
         if "content" in joke_data:
             return joke_data["content"]
        
         # Else, check for the two-part joke format#         elif "setup" in joke_data and "punchline" in joke_data:
             setup = joke_data["setup"]
             punchline = joke_data["punchline"]
             # Return a formatted string for the two-part joke
             return f"Setup: {setup}\nPunchline: {punchline}"
     # If neither format works or the request failed, raise an error
     raise Exception("Failed to fetch a joke or the format was unexpected.")
    
def main():
     try:
         # This variable will now hold either the single joke or the formatted two-part joke
         joke = fetch_random_jokes_freeapi()
         print(f"\n{joke}")
          
     except Exception as e:
         print(str(e))

if __name__ == "__main__":
     main()

import requests 

def fetch_random_stocks_freeapi():
     url="https://api.freeapi.app/api/v1/public/stocks"
     response=requests.get(url)
     data= response.json()
    
    
     if data ["success"] and "data" in data :

         user_data= data["data"]


import requests

url = "https://api.freeapi.app/api/v1/public/stocks"

try:
    # Make API call
    res = requests.get(url, timeout=10)   # timeout for safety
    res.raise_for_status()                # raise error if status != 200

    # Convert to JSON
    jsondata = res.json()

    # Check if API returned success
    if jsondata.get("success") and "data" in jsondata:
        company = jsondata["data"]
        newd = company.get("data", [])

        if not newd:
            print("No stock data found.")
        else:
            # Loop through stocks
            for stock in newd:
                print(
                    f"{stock.get('Name', 'N/A')} ++ {stock.get('CurrentPrice', 'N/A')} +++ {stock.get('StockPE', 'N/A')}"
                )
    else:
        print("API did not return expected data.")

except requests.exceptions.RequestException as e:
    print("Error fetching data from API:", e)

except Exception as e:
    print("Something went wrong:", e)

