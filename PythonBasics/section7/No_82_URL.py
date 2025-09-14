url = "https://www.kaggle.com/datasets"

# arr = url.split("/")
# print(arr)

protocol = url[ : url.find(":")]
print(protocol)

domain = url[url.find(".") + 1: url.rfind(".")]
print(domain)

resource = url[url.rfind("/"): ]
print(resource)

