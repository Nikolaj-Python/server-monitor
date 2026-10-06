def check_server(cpu, ram):
    if cpu > 80 or ram > 80:
        return "WARNING"
    return "ONLINE"


print(check_server(65, 50))

def check_disk(disk):
    if disk > 90:
        return "CRITICAL"
    return "OK"


print(check_disk(75))