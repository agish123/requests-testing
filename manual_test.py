import requests
import time


try:
    response = requests.get("https://self-signed.badssl.com/", verify=False)
    print(response.text)
except Exception as e:
    print(f"SSL Error: {e}")


response = requests.get("https://httpbin.org/redirect/6", allow_redirects=True)
print(f"Redirects: {len(response.history)}, Final URL: {response.url}")


start = time.time()
response = requests.get("https://httpbin.org/delay/10", timeout=2)
print(f"Time taken: {time.time() - start}")


response = requests.get("invalid-url")
print(f"Error: {response.reason}")


headers = {"Content-Type": "application/json"}
response = requests.post("https://httpbin.org/post", headers=headers, data="{}")
print(f"Headers received: {response.json()['headers']}")