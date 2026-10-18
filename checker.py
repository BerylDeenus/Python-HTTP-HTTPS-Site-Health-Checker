import sys
import requests

url = input("Enter your url: ")
url1 = url.replace("https://", "").replace("http://", "")

if not url.startswith(("https://", "http://")):
    url = "https://" + url

print(f"\ncheck: {url}\n")

try:
    response = requests.get(url, timeout=5)
    status = response.status_code
    time = round(response.elapsed.total_seconds(), 2)

    if status == 200:
        print("Request successful")
    elif str(status).startswith("4"):
        print("client error, status code: ", status)
    elif str(status).startswith("5"):
        print("server error, status code: ", status)

except requests.exceptions.SSLError:
    print("HTTPS didn't work, redirecting to http...")
    try:
        url1 = "http://" + url1
        response = requests.get(url1, timeout=5)
        status = response.status_code
        time = round(response.elapsed.total_seconds(), 2)
        print("Fallback to HTTP successful")
    except requests.exceptions.RequestException:
        response = False
        print("Fallback to http didn't work either")

except requests.exceptions.RequestException as e:
    response = False
    print("Request failed")
    print("Error:", e)
    print("Health down")
    sys.exit()

if response is not False:
    print("status code: ", status)
    print("time taken:", time)
