ips = []

def ajout(ip):
    ips.append(ip)
    return ip

def suppression(ip):
    ips.remove(ip)
    return ip

def affiche():
    for i in range(len(ips)):
        print(ips[i])

if __name__ == "__main__":
    ajout("175.56.98.75")
    ajout("145.26.54.8")
    ajout("184.56.145.68")
    ajout("245.75.148.23")
    suppression("175.56.98.75")
    affiche()


