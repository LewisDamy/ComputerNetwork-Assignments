
data = []


'''--->>>>> TESTE SEM VPN - WIFI/ISOLADO <<<<<<<---
RESULTADO
    Uplink capacity: 29.75 Mbps
        Uplink bytes transferred: 68.562 MB
    Downlink capacity: 58.612 Mbps
        Downlink bytes transferred: 127.978 MB
    Latency:
        Idle Latency:
            31.417 milliseconds

REDUNDANCY TRY 2
    Uplink capacity: 27.748 Mbps
        Uplink bytes transferred: 116.218 MB
    Downlink capacity: 178.514 Mbps
        Downlink bytes transferred: 127.978 MB
    Latency:
        Idle Latency:
            19.375 milliseconds

REDUNDANCY TRY 3
    Capacity:
    Uplink capacity: 29.819 Mbps
        Uplink bytes transferred: 107.171 MB
    Downlink capacity: 158.775 Mbps
        Downlink bytes transferred: 499.072 MB
    Latency:
    Idle Latency:
        28.708 milliseconds
'''

'''--->>>>> TESTE COM VPN (USA - Auto/Miami) - WIFI/ISOLADO <<<<<<<--- 

REDUNDANCY TRY 1
    Uplink capacity: 22.000 Mbps
        Uplink bytes transferred: 57.562 MB
    Downlink capacity: 277.390 Mbps
        Downlink bytes transferred: 769.737 MB
    Latency:
    Idle Latency:
        151.333 milliseconds   

REDUNDANCY TRY 2
    Uplink capacity: 13.942 Mbps
        Uplink bytes transferred: 17.156 MB
    Downlink capacity: 252.814 Mbps
        Downlink bytes transferred: 321.736 MB
    Latency:
    Idle Latency:
        150.583 milliseconds

REDUNDANCY TRY 3
    Uplink capacity: 26.884 Mbps
        Uplink bytes transferred: 50.124 MB
    Downlink capacity: 269.489 Mbps
        Downlink bytes transferred: 675.546 MB
    Latency:
    Idle Latency:
        152.958 milliseconds
'''

'''--->>>>> TESTE COM VPN (ITA - Auto/Roma) - WIFI/ISOLADO <<<<<<<--- 

REDUNDANCY TRY 1
    Uplink capacity: 18.453 Mbps
        Uplink bytes transferred: 25.359 MB
    Downlink capacity: 226.030 Mbps
        Downlink bytes transferred: 307.950 MB
    Latency:
    Idle Latency:
        305.500 milliseconds

REDUNDANCY TRY 2
    Uplink capacity: 16.801 Mbps
        Uplink bytes transferred: 46.874 MB
    Downlink capacity: 262.249 Mbps
        Downlink bytes transferred: 727.490 MB
    Latency:
    Idle Latency:
            279.792 milliseconds

REDUNDANCY TRY 3
    Uplink capacity: 18.241 Mbps
        Uplink bytes transferred: 46.500 MB
    Downlink capacity: 272.757 Mbps
        Downlink bytes transferred: 709.305 MB
    Latency:
    Idle Latency:
            275.167 milliseconds
'''

'''--->>>>> TESTE COM VPN (SOUTH AFRICA - Auto/Johannesburg) - WIFI/ISOLADO <<<<<<<--- 

REDUNDANCY TRY 1
    Capacity:
    Uplink capacity: 11.608 Mbps
        Uplink bytes transferred: 20.453 MB
    Downlink capacity: 215.644 Mbps
        Downlink bytes transferred: 350.610 MB
    Latency:
    Idle Latency:
        396.250 milliseconds

REDUNDANCY TRY 2
    Capacity:
    Uplink capacity: 13.382 Mbps
        Uplink bytes transferred: 30.953 MB
    Downlink capacity: 286.910 Mbps
        Downlink bytes transferred: 483.346 MB
    Latency:
    Idle Latency:
        426.917 milliseconds

REDUNDANCY TRY 3
    Uplink capacity: 12.366 Mbps
        Uplink bytes transferred: 24.828 MB
    Downlink capacity: 266.859 Mbps
        Downlink bytes transferred: 451.980 MB
    Latency:
    Idle Latency:
        405.917 milliseconds    
'''

'''--->>>>> TESTE COM VPN (JAPAN - Auto/Tokyo) - WIFI/ISOLADO <<<<<<<--- 

REDUNDANCY TRY 1
    Uplink capacity: 8.538 Mbps
        Uplink bytes transferred: 11.281 MB
    Downlink capacity: 197.050 Mbps
        Downlink bytes transferred: 342.543 MB
    Latency:
    Idle Latency:
        730.083 milliseconds

REDUNDANCY TRY 2
    Uplink capacity: 13.422 Mbps
        Uplink bytes transferred: 26.218 MB
    Downlink capacity: 263.683 Mbps
        Downlink bytes transferred: 443.362 MB
    Latency:
    Idle Latency:
        325.458 milliseconds

REDUNDANCY TRY 3
    Uplink capacity: 7.585 Mbps
        Uplink bytes transferred: 30.390 MB
    Downlink capacity: 20.347 Mbps
        Downlink bytes transferred: 73.638 MB
    Latency:
    Idle Latency:
        361.625 milliseconds
'''

'''--->>>>> TESTE COM VPN (AUSTRALIA- Auto/Brisbane) - WIFI/ISOLADO <<<<<<<--- 

REDUNDANCY TRY 1
    Uplink capacity: 9.553 Mbps
        Uplink bytes transferred: 39.796 MB
    Downlink capacity: 93.388 Mbps
        Downlink bytes transferred: 368.766 MB
    Latency:
    Idle Latency:
        505.625 milliseconds

REDUNDANCY TRY 2
    Uplink capacity: 7.038 Mbps
        Uplink bytes transferred: 14.500 MB
    Downlink capacity: 54.773 Mbps
        Downlink bytes transferred: 114.287 MB
    Latency:
    Idle Latency:
        374.667 milliseconds

REDUNDANCY TRY 3
    Uplink capacity: 7.004 Mbps
        Uplink bytes transferred: 16.609 MB
    Downlink capacity: 63.109 Mbps
        Downlink bytes transferred: 149.163 MB
    Latency:
    Idle Latency:
        399.083 milliseconds

'''



''' ---------------- STRESS TEST ----------------

TESTE COM VPN (AUSTRALIA- Auto/Brisbane) - WIFI
    - 4 Videos 4K
        - mantendo buffer health ~10 seg
        - conexão internet: 45 Mbps (cada)
    - 5 Videos 4K
        - mantendo buffer health ~6 seg
        - conexão internet: 20 Mbps (cada)
        - um dos videos era interrompido para aumento de buffer
    
TESTE COM VPN (USA- Auto/Miami) - WIFI
    - 4 Videos 4K
        - mantendo buffer health ~10 seg
        - conexão internet: 150 Mbps (cada)
    - 5 Videos 4K
        - mantendo buffer health ~10 seg
        - fps 10% capacidade
        - conexão internet: 20 Mbps (cada)
        - todos "funcionavam" mas com muito travamento devido ao framework baixissimo

'''