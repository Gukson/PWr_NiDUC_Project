
# Sortownia Paczek - NiDUC projekt PWr



**1. Sortowanie:**

    1. pierwsze sortowanie wyszukuje priorytety
    2. sortujemy po pierwszej cyfrze kodu pocztowego
    3. sortujemy po drugiej cyfrze kodu pocztowego


**2. Założenia co do struktury kodu**

    - Sortowania
        - Sekcja
            - Maszyny
                - Oprogramowanie	
                - wytrzymałosć
                - prdkość / szybkośc sortowania
    
    - Paczka
        - adres
            - Imię Nazwisko
            - Adres, kod pocztowy
        - flag 
            - priorytet
            - delikatny towar


**3. Reszta założeń**

    * Sortowania pracuje z założenia max 16h dziennie (np. od 6 do 22)
    * aby spełnić warunki umowy SLA sortowani musi przesortować x paczek dziennie. Jeżeli nie wyrobi się z paczkami danego dnia, to te przechodzą na następny dzień.
    * Aby nadrobienie sortowania było możliwe całkowity czas potrzebny na przesortowania wszytkich paczek musi wynosic z założenia nie więcej niż 15h w dniu gdzie wszytskei maszyny są sprawna.
    * Rodzaje maszyn:
        * Maszyny sortujące typu 1 i 2
        * maszyny transportujące paczki między punktami
    * Przykładowe założenia co do liczb, aby móc od czegoś zacząć:
        * pracownia musi dziennie 100 000 paczek
 

**4. założenia co do statystyk i oczekiwanych wniosków**:

    1. szukamy wykresu prawdopodobieństwa spełnienia umowy od ilości paczek założonych w umowie? 
