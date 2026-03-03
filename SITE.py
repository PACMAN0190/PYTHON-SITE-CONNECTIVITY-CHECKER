import urllib.request
import urllib.error

def check_site(url):
    print("\nChecking connectivity checker program")

    if not url.startswith("http"):
        url = "https://" + url

    try:
        response = urllib.request.urlopen(url)
        print("✅ Connected to", url, "successfully")
        print("Response code:", response.getcode())

    except urllib.error.HTTPError as e:
        print("⚠️ HTTP Error:", e.code)

    except urllib.error.URLError as e:
        print("❌ Failed to reach the server")
        print("Reason:", e.reason)

print("This is a site connectivity checker program")
input_url = input("Input the URL of the site you want to check: ")
check_site(input_url)
