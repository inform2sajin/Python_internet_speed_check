import speedtest as st

def speed_Test():
    #run internet speed test and display result
    test = st.Speedtest()
    
    #download speed
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download speed in MBPS: ",down_speed)
    
    #upload speed
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload speed in MBPS: ",up_speed)
    
    #ping
    ping = test.results.ping
    print("Ping: ",ping)
    
speed_Test()