from utilidades import *
while True:

    print("\n===== MENÚ =====")

    print("1. Mostrar grados")

    print("2. BFS")

    print("3. Dijkstra")

    print("4. Comparar rutas")

    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":

        mostrar_grados(grafo)
    elif opcion == "2":

        origen = input("Ciudad de origen: ")

        niveles = bfs(grafo, origen)

        for ciudad in niveles:

            print(ciudad, "->", niveles[ciudad], "escalas")
    elif opcion == "3":

        origen = input("Ciudad de origen: ")

        distancias = dijkstra(grafo, origen)

        print()

        for ciudad in distancias:

            print(ciudad, ":", distancias[ciudad], "km")
    elif opcion == "4":

        origen = input("Ciudad origen: ")

        destino = input("Ciudad destino: ")

        ruta = obtener_ruta(grafo, origen, destino)

        print("\nRuta con menos escalas:")

        print(" -> ".join(ruta))

        print("\nAhora compare esa ruta con las distancias obtenidas por Dijkstra.")
    elif opcion == "5":

        print("Fin del programa")

        break