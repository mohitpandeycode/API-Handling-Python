import requests

def get_jokes_from_api():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        jokes_data = data["data"]["data"]
        for i in range(0, len(jokes_data)):
            jokes = jokes_data[i]["content"]
            print (i+1,":",jokes,"\n")    
    else:
        raise Exception("No data found!!!")

def post_data_from_api():
    url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/post"
    data = {
        'name': 'mohit',
        'age': '65'
    }
# Make a POST request to the API
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Data posted successfully!")
    else:
        print("Failed to post data.")

def main():
    get = get_jokes_from_api()
    post = post_data_from_api()
    print(f" jokes: {get}")

main() 
