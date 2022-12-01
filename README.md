# FANTSO

## Autor projektu: 
- **Ondřej Repko**

## Konzultanti
- [Štěpán Krautwurst](https://github.com/stallion7)
- [Tomáš Fryčka](https://github.com/kektoor)
- [Jakub Heisig](https://github.com/ncplyn)
- [Jan Slivka](https://github.com/HansS04)
- [Sofja Klopcová]()
 
 ## Hudební webová stránka s použitím Django 
Jakožto maturitní projekt jsem se rozhodl vytvořit web, přes který by si uživatel mohl importovat **vlastní MP3 soubory** a následně si hudbu přehrát. **Souborové ID3 Tagy by se přečetly a zobrazily na stránce** společně s funkcí přehrání a dalších několika podpůrných funkcí (Tlačítka Forward/Backward, Randomizer..). Dále by se na webové stránce dokázal uživatel přihlásit skrz **Log-in systém**.

## Proč jsem si vybral tento projekt?
Tento projekt jsem si vybral, jelikož odjakživa miluji hudbu a tvorbu webových stránek. Také jsem se chtěl zdokonalit v pracování jak s jazykem _Python_, tak i s _Djangem_, což je tento projekt pro mě jako stvořený.

## Cíle
- Import MP3 souborů a celých alb
- Přečtení ID3 Tagů a zobrazení v responzivní podobě na stránce (včetně grafiky)
- Funkce Fronta, Randomizer, Zobrazení textu, Vyhledání skladby na portálu Youtube a autora na Wikipedia
- Log-in systém
- Určitá kustomizace stránky (Dark/White theme, Pozadí, Téma, UI..)

## Použité Technologie
- Django
- Python
- Docker Desktop
- HTML, CSS, Bootstrap 5.1
- Mutagen library
- Různé JS a Python knihovny

## Časový harmonogram a postup

#### Září
- Nalezení velice užitečných JS knihoven a funkcí, které v projektu využiji (colour palletes, příjemně vypadající animace, gradient background efekty)
- Studování a plánování backendu 
- Designování frontendu a vybírání správných barev/pozic

#### Říjen
- Při pushování commitu do repozitáře se mi projekt celý vymazal a 4.10.2022 jsem musel začít od začátku
- Testování aplikace, zdali vše správně funguje
- Studování Djanga a Pythonu
- Konzultace se spolužáky ohledně projektu
#### Listopad
- 6.11 - Oficiální start vytváření kódu (vložení a linknutí modelů, aplikací)
- 9.11 - Změna z Django CMS Quickstart na Django z důvodu neefektivnosti a uvědomění, že základní Django je lepší volba (vytvořen nový repozitář).
- 10.11 - Vložení modulů a vytvoření kódu pro autentifikaci uživatele
- 11.11 - Zhotovení navbaru
- 14.11 - Vytvoření CSS kódu pro pozadí Log-In stránky
- 15.11 - Log-In fórum
- 16.11 - Log-In dokončeno (následuje reset hesla, guest account a front-end loginu)
- 21.11 - Frontend indexu a loginu (reset hesla nelze a guest account je zbytečný), uživatel se nyní může přihlásit a zobrazit si base.html
- 25.11 - Přepracování loginu, bugfixy a routing + vytvoření loga
- 29.11 - Přidání responzivního navbaru

#### Prosinec
- 1.12 - Zasazení html stránek do bloků, bugfixy, zlepšení registrace, začátek backendu, bootstrap 


# Zdroje
### Použité technologie a programy:
1. https://www.python.org
2. https://www.jetbrains.com/pycharm/
3. https://getbootstrap.com/docs/5.1/getting-started/introduction/
4. https://www.docker.com/products/docker-desktop/
5. https://mutagen.readthedocs.io/en/latest/user/id3.html
### Tutoriály, inspirace:
1. https://docs.djangoproject.com/en/4.1/intro/tutorial01/
2. https://docs.djangoproject.com/en/4.1/intro/reusable-apps/
3. https://www.instagram.com/webdevlessons/
4. https://css.gg/app
5. https://www.instagram.com/p/Cg4M5pqvke5/
6. https://youtu.be/1UvTNMH7zDo
7. https://www.w3schools.com
8. https://codepen.io/yuhomyan/pen/WNwGywp









