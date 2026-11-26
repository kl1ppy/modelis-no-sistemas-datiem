# Rezultāti un interpretācija

## Datu kopa
AI4I 2020 Predictive Maintenance Dataset ir sintētiska datu kopa, kas veidota, lai atspoguļotu rūpniecisko iekārtu sensoru un apkopes datus. Tajā ir 10 000 ierakstu. Avots: UCI Machine Learning Repository, DOI 10.24432/C5HS5C.


## Datu tīrīšana
Tika noņemtas pilnīgi vienādas rindas un ierakstu identifikatori (UDI/UID, Product ID), jo tie nav iekārtas darbības mērījumi. Skripts arī pārbauda trūkstošās vērtības un vajadzības gadījumā tās aizpilda. Šajā datu kopā nav norādītas trūkstošās vērtības, tādēļ aizpildīšana var nebūt nepieciešama. Dati ir saglabāti jaunā failā, oriģināls nav mainīts.

## Modeļa rezultāts
Pēc `python modelis.py` palaišanas šeit ieraksti izvadītos skaitļus:
- Modeļa accuracy: ___
- Bāzes accuracy: ___
- Modeļa balanced accuracy: ___
- Bāzes balanced accuracy: ___
- Recall (atteices klase): ___
- Konfūzijas matrica: ___

Accuracy rāda kopējo pareizo prognožu daļu. Balanced accuracy vidējo pareizību ņem vērā katrai klasei atsevišķi, kas ir noderīgi, jo atteices ir retākas nekā normāla darbība. Recall parāda, cik no īstajām atteicēm modelis pamanīja.


## Ko darītu reālā sistēmā
Ja modelis brīdinātu par iespējamu atteici, tehniķis pārbaudītu iekārtas sensoru rādījumus un ieplānotu apskati, pirms iekārta tiek izmantota tālāk. Prognoze būtu brīdinājums, nevis automātisks pierādījums, ka iekārta ir bojāta.

## Kļūdu sekas
- **Nepamatota trauksme (false positive):** tehniķis velti pārbauda iekārtu, tiek patērēts laiks un var tikt pārtraukts darbs.
- **Nepamanīta atteice (false negative):** modelis nebrīdina, bet iekārta var salūzt un radīt dīkstāvi vai papildu izmaksas. Šajā scenārijā nepamanīta atteice var būt sliktāka, jo problēma netiek novērsta laikus.

## Ko modelis nedrīkst darīt
Modeli nedrīkst izmantot kā vienīgo pamatu, lai automātiski izslēgtu vai atļautu iekārtas darbību. Dati ir sintētiski un modelis var kļūdīties, tāpēc nepieciešama tehniķa pārbaude.

## Pašvērtējums
Man izdevās izveidot datu apstrādes un modeļa apmācības ķēdi. Neizdevās pilnībā izvērtēt modeli, kamēr nav palaisti skripti un pārbaudīti faktiskie rezultāti. Nākamreiz es salīdzinātu vairākus modeļus un pārbaudītu, vai prognozes darbojas arī ar reāliem iekārtas datiem.
