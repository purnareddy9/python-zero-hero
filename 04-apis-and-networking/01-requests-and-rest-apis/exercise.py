"""
Lesson 01 (Module 04): Exercise — JSON API Consumer

Task:
Write a function `fetch_sample_json_title(api_url: str = "https://httpbin.org/json")`:
1. Sends an HTTP GET request with a 5-second timeout.
2. If `status_code == 200`, parse the JSON and extract:
   `title = response_json["slideshow"]["title"]`
3. Return `(True, title)`.
4. If network error occurs or status is not 200, return `(False, error_message)`.
"""
import requests

# TODO: Implement fetch_sample_json_title

if __name__ == "__main__":
    pass
