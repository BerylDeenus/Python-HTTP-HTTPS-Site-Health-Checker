Python site health checker & protocol fallback
A light Python script for network uptime and health checking. The script will format the input url for you, check http response status codes, and falls back to http:// if an SSL certificate error is encountered. 
Features
>Automated protocol formatting
> SSL fallback mechanism
> Response time measurement
> Error reporting
> Error handling
Automated protocol formatting
The script will add https:// if none is provided in the input
SSL fallback mechanism
The script will catch SSLError exceptions if one is thrown, and will try a secondary fallback to http://
Response time measurement
The script will measure the total time taken for the request, using the following formula
(elapsed.total_seconds())
Error reporting
The following categorisation of errors will be reported:
> 200: Success 
> 4xx: Client Errors (e.g. 404, 403) 
> 5xx: Server Errors (e.g. 500, 502) 
error handling
This script will handle network timeouts and unreachable domains using requests.exceptions.RequestException
> Make sure to have Python 3.x and the requests library installed.
pip install requests
Usage
You can clone/download the repo, then run the python script.
python health_checker.py
Then enter any domain or url when prompted:
Enter your url: github.com
check: https://github.com
Request successful
status code: 200
time taken: 0.22
Code overview
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
print("HTTPS didn't work, redirecting to HTTP...")
try:
url1 = "http://" + url1
response = requests.get(url1, timeout=5)
status = response.status_code
time = round(response.elapsed.total_seconds(), 2)
except requests.exceptions.RequestException:
print("Fallback to HTTP didn't work either.")
except requests.exceptions.RequestException as e:
print("Request failed due to:", e)
print("Health: DOWN")
if 'status' in locals():
print("status code: ", status)
print("time taken:", time)
 Future improvements
> Support batch url processing from a external .txt file.
> Implement a loop to continually check health on set intervals.
