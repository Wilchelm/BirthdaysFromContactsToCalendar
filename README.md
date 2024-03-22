# BirthdaysFromContactsToCalendar
Jest to program napisany w języku Python, który generuje plik kalendarza zawierający wydarzenia związane z urodzinami osób znajdujących się w kontaktach wyeksportowanych do pliku Contacts.vcf. <br />
Oprócz samego programu w języku Python dołączony jest także skrypt .bat pozwalący uruchomić program w systemie Windows.
# Windows
W celu uruchomienia programu należy zainstalować aplikację Python ze sklepy Microsoft Store.
# Instrukcja
* Otwórz aplikacje do kontaktów na swoim urządzeniu
* Wyeksportuj kontakty z wcześniej wymienionej aplikacji i nazwij plik Contacts.vcf
* Uruchom program
* Następnie zaimportuj plik Birthdays.ics do kalendarza
<!-- end of the list -->
W celu dodania większej liczby osób należy otworzyć plik Contacts.vcf w edytorze tekstu. <br />
Następnie dodać w nowej linii FN:Nazwa, w kolejnej BDAY:rok-miesiąc-dzień jak BDAY:1899-01-01.<br />
Wydarzenia będą dodane każdego roku jako "Nazwa ma urodziny"<br />
Po zaimportowaniu kalendarza należy pamiętać o ustawieniu powiadomień.
