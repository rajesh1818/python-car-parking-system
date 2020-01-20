import requests

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=testing&language=english&route=p&numbers=9167348801"

headers = {

'authorization': "Sog3kv96uUJAM0chVWziGPRarN8QZq4ytjXpsLE25CIFY1ODfBFspoThHlCzet4afvOx0WAZ75VMInJB",

'Content-Type': "application/x-www-form-urlencoded",

'Cache-Control': "no-cache",

}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)



#+12026843839