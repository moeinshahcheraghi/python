import requests


def genrate_qr_code(text , file_name):
    url = "https://api.qrserver.com/v1/create-qr-code/"
    p = {
        
        "size" : "200*200",
        "data" : text      
    }
    
    responcse = requests.get(url , params=p) 
    with open(file_name,"wb") as file :
        file.write(responcse.content)
        
        
genrate_qr_code("https://rahnama.com","rahnama.jpg")
