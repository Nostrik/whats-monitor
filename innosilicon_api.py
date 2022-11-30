from dragon_rest.dragons import DragonAPI

dragon_host = ''
api = DragonAPI(
    dragon_host,
    username='admin',
    password='dragonadmin'
)

r = api.summary()
print(r)


