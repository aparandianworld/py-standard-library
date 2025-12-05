import urllib.parse

sample_url = "https://example.com?name=John&age=30"

parsed_url = urllib.parse.urlparse(sample_url)
print(parsed_url)
print("Scheme: ", parsed_url.scheme)
print("Hostname: ", parsed_url.hostname)
print("Query: ", parsed_url.query)

query_str = urllib.parse.parse_qs(parsed_url.query)
print(query_str)

query_str = urllib.parse.parse_qsl(parsed_url.query)
print(query_str)

original_url = urllib.parse.urlunparse(parsed_url)
print(original_url)

samples = [
    "Hello World",
    "john.doe@example.com",
    "café & crème brûlée",
    "foo=bar&baz=qux",
    "this is a long sentence with spaces and special chars: @#$%^&*()",
]

for item in samples:
    print(urllib.parse.quote(item))
    print(urllib.parse.quote_plus(item))

query_data = {
    "name": "John",
    "age": "30",
    "city": "New York",
}

param_values = urllib.parse.urlencode(query_data)
print(param_values)
