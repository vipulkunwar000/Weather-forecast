from urllib.request import urlopen
def main():
    API_KEY = "6816f97c850698ada526c130afa5674f"
    city = input('Enter a city name: ')

    # open a connection to a URL using urllib2
    web_url = urlopen("https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city)
    # Get a result code and print it
    # 200 returns when request was successful
    print("Result code:"+str(web_url.getcode()))
    # Read the data from url and print it
    data = web_url.read()
    print(data)

    
if __name__=="__main__":
    main()
