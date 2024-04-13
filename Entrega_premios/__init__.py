def mas_influyente(data):
    lista_inf = [(name, (stats[0] * 1.5 + stats[1] * 1.25 + stats[2])) for name, stats in data.items()]
    mas_inf= max(lista_inf, key = lambda x: x[1])
    return mas_inf[0]

def calcular_goles(data):
  goleador_max,goles_max= max(data.items(), key = lambda x: x[1][0])
  return goleador_max, goles_max[0]

def dividir25(n):
   return lambda x : x/n