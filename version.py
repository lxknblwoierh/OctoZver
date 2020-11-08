#Connectiong to server and check version
    
    def Version(self):
        link = "http://webpoint.si/version.txt"
        f = requests.get(link)
        if f.text != version:
            print("version not match")
            layout = GridLayout(cols = 1, padding = 10)
            popupLabel = Label(text = "      Your app is not updated \nUpdate app and will work again \n Current version is: " + str(f.text) +"\n     Your version is: " + str(version), font_size='18sp')
            layout.add_widget(popupLabel)
            popup = Popup(title ='Error', title_size='18sp', content = layout, size_hint =(None, None), size =(300, 300), auto_dismiss=False)
            popup.open()
