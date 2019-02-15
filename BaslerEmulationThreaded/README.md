### Vaiheet Basler kameroiden emulointiin

'Rekisteröidy' ja lataa Pylon >5.1.0 https://www.baslerweb.com/en/sales-support/downloads/software-downloads/#type=pylonsoftware;version=all;os=windows

Aseta uusi järjestelmämuuttuja PYLON_CAMEMU = x , x= kameroiden määrä
https://docs.baslerweb.com/en/camera_emulation.htm#MiniTOCBookMark6

CMD : setx PYLON_CAMEMU "1" / 1 emuloitu kamera

Nyt Basler_pypylon_emulated_opencv.py suorittaen pitäisi näkyä Baslerin testigradientti.