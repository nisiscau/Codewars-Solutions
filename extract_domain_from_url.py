from urllib.parse import urlparse

def domain_name(url):
    if url[:4] == 'http':
        t = urlparse(url).netloc.split('.')
        pointer = 0
        while t[pointer] in ['www','']:
            pointer += 1
        return t[pointer]
    else:
        t = urlparse(url).path.split('.')
        pointer = 0
        while t[pointer] in ['www','']:
            pointer += 1
        return t[pointer]
