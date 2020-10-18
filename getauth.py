def get_auth():
    auth_dict = {}
    with open("keys.txt", "r") as file:
        for line in file:
            var = line.split(' ')
            auth_dict[var[0]] = var[2]
    
    return auth_dict