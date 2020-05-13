import model

def izpis_igre(igra):
    tekst = (
        "===================================================\n\n"
        "Število preostalih poizkusov : {stevilo_preostalih_poskusov} \n\n"
        "{pravilni_del_gesla}\n\n"
        "Neuspeli poskusi: {neuspeli_poskusi} \n\n"
        "====================================================="
    ).format(
        stevilo_preostalih_poskusov=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.nepravilni_ugibi()    
    )
    
    
    return tekst


def izpis_zmage():
    tekst = (
        "===================================\n\n"
        "Wiiiii, zmaga! Geslo je bilo: {geslo} \n\n"
    ).format(
        geslo = igra.geslo()  
    )
    return tekst

def izpis_poraza():
    tekst = (
        "================================== \n\n"
        "BOOOO, poraz! Geslo je bilo: {geslo} \n\n"
    ).format(
        geslo = igra.geslo()  
    )
    return tekst

def zahtevaj_vnos():
    return input("Črka: ")

def pozeni_vmesnik():

    igra = model.nova_igra()
    while True:
        #najprej izpišemo stanje da vidimo kakšno je
        print(izpis_igre(igra))
        #čakamo na črko od uporabnika
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        if igra.zmaga():
            print(izpis_zmage(igra))
            ponovni_zagon = input("Za ponovni zagon vpišite: 1.")
            if ponovni_zagon == "1":
                igra  = model.nova_igra()
            else:
                break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break

#zaženi igro:
pozeni_vmesnik()

