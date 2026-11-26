# Rezultātu interpretācija un lēmums


## Kas ir dati un no kurienes tie nāk?
Dati ir par Scania kravas automašīnu gaisa spiediena sistēmas (APS) darbību. Tie ir UCI Machine Learning Repository datu kopas APS Failure at Scania Trucks ieraksti.


## Kas datos bija nepareizi un ko izdarīju?
Datu failā trūkstošās vērtības bija apzīmētas ar `na`. Tīrīšanas skripts atzīmēja tās kā trūkstošas, noņēma dublikātus un pilnīgi tukšas kolonnas, skaitliskajās pazīmēs trūkstošās vērtības aizpildīja ar mediānu, un izmeta rindas bez mērķa klases.


## Ko modelis prognozē un cik labi?
Modelis prognozē, vai ieraksts ir saistīts ar APS komponentes atteici (`pos`) vai nav (`neg`). Pēc `python modelis.py` palaišanas šeit ieraksti izdrukātos modeļa accuracy un bāzes līnijas accuracy. Accuracy salīdzinājums ir vajadzīgs, bet, tā kā `pos` klase ir reta, svarīgi ir arī recall: cik no reālajiem atteices gadījumiem modelis atrod.

- Modeļa accuracy: (ieraksti no izvada)
- Bāzes līnijas accuracy: (ieraksti no izvada)
- Secinājums: (vai modelis pārspēja bāzes līniju? ko parāda recall?)

## Ko darītu ar prognozi reālā sistēmā?
Ja modelis norādītu uz iespējamu APS problēmu, sistēma izveidotu pārbaudes pieteikumu tehniķim. Tehniķis apskatītu mērījumus un pārbaudītu sistēmu; prognoze pati par sevi nebūtu remonta pavēle.

## Kas notiek, ja modelis kļūdās?
- **Nepamatota trauksme (false positive):** tehniķis velti veic papildu pārbaudi, tērē laiku un resursus.
- **Nepamanīta problēma (false negative):** sistēmas defekts netiek atzīmēts, un var rasties dārgāks bojājums vai transportlīdzekļa dīkstāve. Šajā uzdevumā nepamanīta problēma ir sliktāka, jo var radīt lielākas sekas, tomēr reālas drošības pārbaudes jāveic neatkarīgi no modeļa.

## Ko ar modeli nedrīkst darīt?
Nedrīkst izmantot šo modeli, lai automātiski izlemtu, ka kravas automašīna ir droša un to drīkst izlaist reisā. Modelis ir mācīts uz vēsturisku datu kopas un var kļūdīties; to nevar aizstāt ar kvalificēta tehniķa pārbaudi.

## Pašvērtējums
Man izdevās izveidot datu tīrīšanas un klasifikācijas procesu. (Pielāgo šo teikumu pēc faktiskā izpildes rezultāta.)
Man neizdevās / man bija grūtības ar: (ieraksti reālo grūtību).
Nākamreiz es: (ieraksti, ko uzlabotu, piemēram, salīdzinātu citu modeli vai vairāk izpētītu kļūdu gadījumus).
