# Adds what some materials are made of, to be used later in the wordinfo
# ['madera', 'acero', 'arenisca', 'granito', 'caliza', 'pizarra', 'mármol', 'jade', 'plata', 'uranio', 'plastiacero', 'oro', 'bioferrita']
def add_materials(texto):
    # Define BOMs 
    # Buildings, furniture and weapons
    lista_madera = [f"{texto} de madera"]
    lista_acero = [f"{texto} de acero"]
    lista_plata = [f"{texto} de plata"]
    lista_uranio = [f"{texto} de uranio"]
    lista_plastiacero = [f"{texto} de plastiacero"]
    lista_oro = [f"{texto} de oro"]
    lista_bioferrita = [f"{texto} de bioferrita"]
    lista_arenisca = [f"{texto} de arenisca"]
    lista_granito = [f"{texto} de granito"]
    lista_caliza = [f"{texto} de caliza"]
    lista_pizarra = [f"{texto} de pizarra"]
    lista_marmol = [f"{texto} de mármol"]
    lista_jade = [f"{texto} de jade"]
    lista_plata = [f"{texto} de plata"]
    lista_uranio = [f"{texto} de uranio"]
    lista_plastiacero = [f"{texto} de plastiacero"]
    # Textil (furniture and armor)
    lista_tela = [f"{texto} de tela"]
    lista_cuero_ligero = [f"{texto} de cuero ligero"]
    lista_lana_de_oveja = [f"{texto} de lana de oveja"]
    lista_cuero_liso = [f"{texto} de cuero liso"]
    lista_hilodiablo = [f"{texto} de hilodiablo"]
    lista_tela_sintetica = [f"{texto} de tela sintética"]
    lista_lana_de_megaperezoso = [f"{texto} de lana de megaperezoso"]
    lista_lana_de_mufalo = [f"{texto} de lana de múfalo"]
    lista_lana_de_bisonte = [f"{texto} de lana de bisonte"]
    lista_lana_de_alpaca = [f"{texto} de lana de alpaca"]
    lista_piel_de_pajaro = [f"{texto} de piel de pájaro"]
    lista_hipertejido = [f"{texto} de hipertejido"]
    lista_cuero_parcheado = [f"{texto} de cuero parcheado"]
    lista_cuero_de_perro = [f"{texto} de cuero de perro"]
    lista_cuero_de_lagarto = [f"{texto} de cuero de lagarto"]
    lista_piel_de_lobo = [f"{texto} de piel de lobo"]
    lista_pelaje_felino = [f"{texto} de pelaje felino"]
    lista_pelaje_de_zorro = [f"{texto} de pelaje de zorro"]
    lista_piel_de_cerdo = [f"{texto} de piel de cerdo"]
    lista_cuero_de_camello = [f"{texto} de cuero de camello"]
    lista_piel_de_oso = [f"{texto} de piel de oso"]
    lista_pelaje_azul = [f"{texto} de pelaje azul"]
    lista_cuero_de_elefante = [f"{texto} de cuero de elefante"]
    lista_pelaje_grueso = [f"{texto} de pelaje grueso"]
    lista_cuero_temible = [f"{texto} de cuero temible"]
    lista_cuero_de_rinoceronte = [f"{texto} de cuero de rinoceronte"]
    lista_pelaje_de_cuy = [f"{texto} de pelaje de cuy"]
    lista_pelaje_de_chinchilla = [f"{texto} de pelaje de chinchilla"]
    lista_cuero_humano = [f"{texto} de cuero humano"]
    lista_pelaje_de_trumbo = [f"{texto} de pelaje de trumbo "]
    
    
    # Ask the user to select a list
    print("Please select a list:")
    print("1. Madera, Acero, Plata, Uranio, Plastiacero, Oro, Bioferrita")
    print("2. Madera', 'Acero', 'Arenisca', 'Granito', 'Caliza', 'Pizarra', 'Mármol', 'Jade', 'Plata', 'Uranio', 'Plastiacero', 'Oro', 'Bioferrita")
    print("3. Textiles")
    opcion = input("Enter the number corresponding to the desired list: ")
    
    # We display the contents of the selected list and ask the user if he/she agrees with it.
    if opcion == "1":
        print("\nContenido de la lista 1:")
        for material in lista_madera + lista_acero + lista_plata + lista_uranio + lista_plastiacero + lista_oro + lista_bioferrita:
            print(material)
    elif opcion == "2":
        print("\nContenido de la lista 2:")
        for material in lista_madera + lista_acero + lista_arenisca + lista_granito + lista_caliza + lista_pizarra + lista_marmol + lista_jade + lista_plata + lista_uranio + lista_plastiacero + lista_oro + lista_bioferrita:
            print(material)
    elif opcion == "3":
        print("\nContenido de la lista 3:")
        for material in lista_tela + lista_cuero_ligero + lista_lana_de_oveja + lista_cuero_liso + lista_hilodiablo + lista_tela_sintetica + lista_lana_de_megaperezoso + lista_lana_de_mufalo + lista_lana_de_bisonte + lista_lana_de_alpaca + lista_piel_de_pajaro + lista_hipertejido + lista_cuero_parcheado + lista_cuero_de_perro + lista_cuero_de_lagarto + lista_piel_de_lobo + lista_pelaje_felino + lista_pelaje_de_zorro + lista_piel_de_cerdo + lista_cuero_de_camello + lista_piel_de_oso + lista_pelaje_azul + lista_cuero_de_elefante + lista_pelaje_grueso + lista_cuero_temible + lista_cuero_de_rinoceronte + lista_pelaje_de_cuy + lista_pelaje_de_chinchilla + lista_cuero_humano + lista_pelaje_de_trumbo:
            print(material)
    else:
        print("Invalid option")

# Ask the user to enter a text
texto_ingresado = input("Enter a text: ")

# Call the function to add materials to the entered text
add_materials(texto_ingresado)