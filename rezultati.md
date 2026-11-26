# Rezultāti un interpretācija

## Datu kopa
AI4I 2020 Predictive Maintenance Dataset ir sintētiska datu kopa, kas veidota, lai atspoguļotu rūpniecisko iekārtu sensoru un apkopes datus. Tajā ir 10 000 ierakstu. Avots: UCI Machine Learning Repository, DOI 10.24432/C5HS5C.


## Datu tīrīšana
Tika noņemtas pilnīgi vienādas rindas un ierakstu identifikatori (UDI/UID, Product ID), jo tie nav iekārtas darbības mērījumi. Skripts arī pārbauda trūkstošās vērtības un vajadzības gadījumā tās aizpilda. Šajā datu kopā nav norādītas trūkstošās vērtības, tādēļ aizpildīšana var nebūt nepieciešama. Dati ir saglabāti jaunā failā `tirs.csv`, oriģināls nav mainīts.

## Modeļa rezultāts
- Modeļa accuracy: 0.980
- Bāzes accuracy: 0.966
- Modeļa balanced accuracy: 0.825
- Bāzes balanced accuracy: 0.500
- Recall (atteices klase): 0.659
- Konfūzijas matrica: `[[2394, 21], [29, 56]]` (TN=2394, FP=21, FN=29, TP=56)

Modelis pārspēja bāzes līniju (0.980 pret 0.966 un balanced accuracy 0.825 pret 0.500), jo bāzes līnija vienmēr prognozē klasi `0` (nav atteices) un neatrod nevienu bojājumu. Accuracy rāda kopējo pareizo prognožu daļu, balanced accuracy ņem vērā katru klasi atsevišķi, bet recall (0.659) parāda, ka modelis pamanīja 56 no 85 reālajām atteicēm.


## Ko darītu reālā sistēmā
Ja modelis brīdinātu par iespējamu atteici, tehniķis pārbaudītu iekārtas sensoru rādījumus un ieplānotu apskati, pirms iekārta tiek izmantota tālāk. Prognoze būtu brīdinājums, nevis automātisks pierādījums, ka iekārta ir bojāta.

## Kļūdu sekas
- **Nepamatota trauksme (false positive):** tehniķis velti pārbauda iekārtu, tiek patērēts laiks un var tikt pārtraukts darbs.
- **Nepamanīta atteice (false negative):** modelis nebrīdina, bet iekārta var salūzt un radīt dīkstāvi vai papildu izmaksas. Šajā scenārijā nepamanīta atteice var būt sliktāka, jo problēma netiek novērsta laikus.

## Ko modelis nedrīkst darīt
Modeli nedrīkst izmantot kā vienīgo pamatu, lai automātiski izslēgtu vai atļautu iekārtas darbību. Dati ir sintētiski un modelis var kļūdīties, tāpēc nepieciešama tehniķa pārbaude.

## Pašvērtējums
Man izdevās izveidot datu apstrādes un modeļa apmācības ķēdi. Sākumā grūtības sagādāja darba vides iestatīšana skriptu palaišanai un nelīdzsvaroto klašu rādītāju interpretācija. Nākamreiz es salīdzinātu vairākus modeļus un pārbaudītu, vai prognozes darbojas arī ar reāliem iekārtas datiem.
