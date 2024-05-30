USE Bazy_projekt;

INSERT INTO `uzytkownik`(login, haslo, rodzaj_konta)
VALUES ('Arkadiusz Wojs', 'Wojs222', 1);

INSERT INTO `uzytkownik`(login, haslo, rodzaj_konta)
VALUES ('Cezary Storczyk', 'Storczyk222', 0);


INSERT INTO `uzytkownik`(login, haslo, rodzaj_konta)
VALUES ('Iga Swiatek', 'Swiatek222', 0);


UPDATE `uzytkownik` 
SET haslo = 'nowe222'
WHERE login = 'Cezary Storczyk';