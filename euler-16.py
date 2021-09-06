def vsota_števk_potenc(osnova,potenca):
    število = osnova ** potenca
    vsota = 0
    while število != 0:
        vsota += število % 10
        število = število // 10
    return vsota


vsota_števk_potenc(2,1000)