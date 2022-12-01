from dragon_rest.dragons import DragonAPI

miners = [
    '192.168.1.68',
    '192.168.1.114'
]

dragon_host = miners[1]
api = DragonAPI(
    dragon_host,
    username='admin',
    password='KX26d'
)


if __name__ == '__main__':
    r = api.summary()
    print(r)
