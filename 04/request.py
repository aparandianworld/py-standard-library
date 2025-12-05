import urllib.request

sample_url = "http://httpbun.com/get"

try:
    response = urllib.request.urlopen(sample_url)
    if response.getcode() == 200:
        data = response.read().decode("utf-8")
        print(data)
        headers = response.getheaders()
        print(headers)
        content_length = response.getheader("Content-Length")
        print(content_length)
        content_type = response.getheader("Content-Type")
        print(content_type)

except Exception as e:
    print(e)
