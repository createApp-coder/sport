from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
kv='''
Screen:
    GridLayout:
        rows: 3
        
        MDTextField:
            id: mdtext
            hint_text: "Inserire un'associazione / ente sportivo, religioso o culturale"
            mode: "rectangle"

        MDRaisedButton:
            text: "Cerca Informazioni. . . "
            size_hint_x: 3
            size_hint_y: 0.4
            on_press:app.maps()

        MDLabel:
            id: TextLabel
            text: "Benvenuto, inserire nella barra superiore un'associazione. . "
'''

class my_app(MDApp):
    def build(self):
        self.window=GridLayout()
        self.window.cols = 1
        Window.size=(365,645)
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "400"

        

        return Builder.load_string(kv)
    
    def maps(self):
        
        
        v = self.root.ids["mdtext"].text
        if not v:
            print("Error. .  .")
        if v == "ASD Promobasket Marigliano 2003":
            
            
            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='http://basketmarigliano.it/ ')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='ASD Promobasket Marigliano 2003 ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
           
            def information(instance):
                texts = '''La pallacanestro (o basket) è uno sport di squadra in cui due formazioni composte da 5 giocatori ciascuna si affrontano per segnare con un pallone nel canestro avversario, secondo regole prefissate e con un punteggio che varia dalla posizione di tiro.


https://www.google.com/maps/search/ASD Promobasket Marigliano 2003'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
            
            
        if v == "RaggioSunBoys Onlus":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            

            layout.add_widget(closButton)
            l = Label(text='http://www.raggiosunboys.it/')
            layout.add_widget(l)
            

            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            

            def information(instance):
                texts = '''Organizza corsi di attività motoria e di conoscenza e avviamento alla disciplina sportiva di atletica leggera per le persone che versano in condizioni di svantaggio economico, sociale e familiare.
Organizza corsi di attività motoria e di conoscenza delle discipline sportive per le persone con disabilità fisica o intellettiva.


https://www.google.com/maps/search/RaggioSunBoys Onlus'''

                vs = self.root.ids["TextLabel"].text = texts
                
            popup = Popup(title='RaggioSunBoys Onlus ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
                
        
            closButton.bind(on_press=popup.dismiss)
           
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Asd San Giovanni Battista Faibano 2021":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''Email: asdsangiovannibattista@pec.it
            phone: +39 3384223242''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Asd San Giovanni Battista Faibano 2021 ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''A Faibano di Marigliano nasce l'Associazione sportiva dilettantistica (San Giovanni Battista Faibano 2021) che sarà presentata lunedì prossimo 7 giugno 2021, alle ore 20.15, presso la ex sede dell'azienda 'o Sole 'e Napule in Largo San Francesco a Faibano di Marigliano.


https://www.google.com/maps/search/Asd San Giovanni Battista Faibano 2021'''

                vs = self.root.ids["TextLabel"].text = texts
                
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "ASD CENTRO SPORTIVO AZZURRO":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l= Label(text='''
            Nome: Allocca Pasquale
            Email: vito040266@gmail.com
            phone: +39 3393037391''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='ASD CENTRO SPORTIVO AZZURRO ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''Il C.S.A.è un'associazione nata nel settembre del 1999, dalla collaborazione di un gruppo di amici che condividevano la passione per lo sport


https://www.google.com/maps/search/ASD CENTRO SPORTIVO AZZURRO'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
        
            
            
        if v == "TYA PALLAVOLO MARIGLIANO (FIPAV)":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''
    Email:
    tyapallavolomariglianossd@gmail.com''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='TYA PALLAVOLO MARIGLIANO (FIPAV) ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''Gioco che si disputa tra due squadre di sei giocatori ciascuna su un terreno di 18 × 9 m, diviso in due parti da una rete, tesa tra due paletti, a metà della sua lunghezza: le due formazioni devono rinviarsi la palla colpendola con qualsiasi parte del corpo senza lasciarle toccare terra e con un massimo di tre colpi a opera di tre giocatori diversi nella stessa area; specialità olimpica


https://www.google.com/maps/search/TYA PALLAVOLO MARIGLIANO (FIPAV)'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "new cap marigliano 2018 asd":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l=Label(text='''
    http://www.newcapmarigliano2018.it/
    phone: +39 3393148638''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='new cap marigliano 2018 asd ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''La New Cap Marigliano 2018 asd nasce, come dice appunto la denominazione, nel 2018 grazie alla voglia ed passione di alcuni amici di tenere alto il movimento del basket femminile del paese, sulla scorta degli splendidi risultati ottenuti negli anni appena precedenti dalla Nuova Atletica Basket.


https://www.google.com/maps/search/new cap marigliano 2018 asd'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "CERCIELLO ANTONIO":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(287,50))
            layout.add_widget(closButton)
            l = Label(text='''
Email: asdpallavolomarigliano@gmail.com
phone: +39 3927632893''')
            layout.add_widget(l)
            mapButton = Button(text="Mappa",size_hint=(None,None),size=(287,50))
            layout.add_widget(mapButton)
            
            popup = Popup(title='CERCIELLO ANTONIO ',
                      content = layout,
                      size_hint =(None,None),size=(310,310))
            def backmap(instance):
                url =f"https://www.google.com/maps/search/CERCIELLO ANTONIO"
                webbrowser.open(url)
            

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            mapButton.bind(on_press=backmap)
            
            v=popup.open()
            
            
            
        if v == "Fortitudo Euritmica asd":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l=Label(text='''
            Email: Raimondo.zirilli@libero.it
            
            tipo di sport: Rugby''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Fortitudo Euritmica asd ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''MARIGLIANO- La BLACKNIGHTS A.S.D.RUGBY FORTITUDO EURITMICA è una società rugbistica del territorio, che nella persona del presidente Zirilli Raimondo, come consuetudine ormai da 16 anni, promuove all’interno delle scuole mariglianesi progetti di MINI RUGBY finalizzati all’educazione e alla formazione degli alunni, socializzazione, rispetto dei principi e delle regole


https://www.google.com/maps/search/Fortitudo Euritmica asd'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Pattinaggio Artistico Alusìa (Giannattasio Gennaro)":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''
            Info: info@alusia.it
            phone: +39 3474182120 ''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Pattinaggio Artistico Alusìa (Giannattasio Gennaro) ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''Nel pattinaggio artistico gli atleti si esibiscono individualmente, in coppia o in gruppi ed eseguono esercizi di varia difficoltà sia sui pattini a quattro ruote che sui pattini in linea per esaltare, in modo spettacolare, ivalori tecnici e artistici della disciplina


https://www.google.com/maps/search/Pattinaggio Artistico Alusìa (Giannattasio Gennaro)'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Tya pallavolo femminile":
            
            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l= Label(text='''Email: expomax@tiscali.it
                             ''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Tya pallavolo femminile ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''La partita è divisa in set che vengono vinti dalla prima squadra che arriva a 25 punti, con almeno due punti di margine dall'altra. In caso di parità sul punteggio di 24-24 si va avanti ad oltranza finché il margine di una delle due squadre non raggiunge i due punti


https://www.google.com/maps/search/Tya pallavolo femminile'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "ASD Accademia Le Ballet":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''Email: accademialeballet@gmail.com
                              ''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='ASD Accademia Le Ballet ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''La parola ballerina viene usata in tutto il mondo per indicare una danzatrice del balletto, "Ballet" in Francese,un diminutivo di "Ballo", che deriva dal Latino "Ballo" , "Ballare", che a sua volta deriva dal Greco "βαλλίζω" (Ballizo), "per la danza, a saltare su"


https://www.google.com/maps/search/ASD Accademia Le Ballet'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
           
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "minotaur boxe":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l= Label(text= '''
            Email: gioboxe@libero.it
            phone: +39 3389951781 ''')
            
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='minotaur boxe ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''la boxe è un insieme di sport da combattimento incentrati sul colpire, in cui due avversari si affrontano in un combattimento usando almeno i pugni, e possibilmente coinvolgendo altre azioni come calci, gomitate, ginocchiate e testate, a seconda delle regole


https://www.google.com/maps/search/minotaur boxe'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Emivan":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''
            Email: emivanasd@gmail.com
            Nome: Siciliano Ivan
            phone: +39 3510815000''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Emivan',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''Centro Sportivo Emivan, 📍Via Aniello Alise 90, Marigliano (NA), ℹ️ 3510815000


https://www.google.com/maps/search/Emivan'''
                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "ASD EMIVAN":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''
            Email: emivanasd@gmail.com
            phone: +39 3510815000''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='ASD EMIVAN ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))

            
            def information(instance):
                texts = '''Centro Sportivo Emivan, 📍Via Aniello Alise 90, Marigliano (NA), ℹ️ 3510815000


https://www.google.com/maps/search/Emivan'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Mob Performing Arts":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''Email: mobperformingarts@gmail.com
                              ''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Mob Performing Arts ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
           
            def information(instance):
                texts = '''Giovani allievi danno vita alla musica, fondendo tradizione e innovazione in ogni movimento


https://www.google.com/maps/search/Mob Performing Arts'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Asd Corpo in movimento":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''
Email: corpoinmovimentoasd@gmail.com
phone: +39 3333171111''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Asd Corpo in movimento ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''Se un corpo cambia posizione nel tempo allora è in moto. Tutto si muove e anche ciò che apparentemente sembra fermo sulla superficie terrestre si muove rispetto al Sole e alle stelle. Il sistema di riferimento che dobbiamo sempre considerare è la Terra, altrimenti viene specificato un altro sistema di riferimento


https://www.google.com/maps/search/Asd Corpo in movimento'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Fitdance":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''
Email: desdemonavigliotta@gmail.com
phone: +39 3807635954''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Fitdance ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            
            def information(instance):
                texts = '''Lo Fit Dance mette assieme il meglio di discipline diverse: l'aerobica, prima di tutto, utilissima per tonificare il corpo, e la danza latino-americana, ritmata e divertente


https://www.google.com/maps/search/Fitdance'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Centro Studi Danza Azzurro":
            

            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''phone: +39 3278112330 ''')
            layout.add_widget(l)
            
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Centro Studi Danza Azzurro ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
                
            def information(instance):
                texts = '''Il duro e costante allenamento favorisce lo sviluppo della muscolatura, in particolare quella dei polpacci, delle cosce, dei glutei e delle braccia. Questa disciplina migliora la coordinazione, l'elasticità e l'equilibrio e insegna l'eleganza e il portamento


https://www.google.com/maps/search/Centro Studi Danza Azzurro'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            
            infButton.bind(on_press=information)
            v=popup.open()
            
            
            
        if v == "Accademia Danzart":
            
            from kivy.uix.popup import Popup
            from kivy.uix.gridlayout import GridLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            layout = GridLayout(cols=1)
            closButton = Button(text="Esci",size_hint=(None,None),size=(275,50))
            layout.add_widget(closButton)
            l = Label(text='''
            Email:luigiamato10@tin.it
            phone: +39 3385449470''')
            layout.add_widget(l)
            infButton = Button(text="Info.",size_hint=(None,None),size=(275,30))
            layout.add_widget(infButton)
            popup = Popup(title='Accademia Danzart ',
                      content = layout,
                      size_hint =(None,None),size=(300,300))
            
            def information(instance):
                texts = '''Danzart academy nasce nel 2003 da un connubio perfetto di passione, professionalità ed esperienza artistica


https://www.google.com/maps/search/Accademia Danzart'''

                vs = self.root.ids["TextLabel"].text = texts
                
        
            closButton.bind(on_press=popup.dismiss)
            infButton.bind(on_press=information)
            v=popup.open()
   
        
if __name__ == '__main__':
    my_app().run()
