def check_server(cpu, ram):
    if cpu > 80 or ram > 80:
        return "WARNING"
    return "ONLINE"


print(check_server(65, 50))