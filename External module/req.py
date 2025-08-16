import requests 

r=requests.get('https://api.github.com/events')
with open('req.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)
print("Data has been written to events.txt")