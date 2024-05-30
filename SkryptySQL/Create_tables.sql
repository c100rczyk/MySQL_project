use Bazy_projekt;

CREATE TABLE `uzytkownik` (
	login varchar(50) NOT NULL,
    haslo varchar(50) NOT NULL,
    rodzaj_konta tinyint(1) NOT NULL,
    PRIMARY KEY (login));
    
CREATE TABLE trening (
	id_treningu int(20) NOT NULL AUTO_INCREMENT,
    uzytkowniklogin varchar(50) NOT NULL,
    trening_name varchar(100) NOT NULL,
    termin date NOT NULL,
    godzina time ,
    czy_wykonany tinyint(1),
    PRIMARY KEY (id_treningu));
    
CREATE TABLE `Element_Treningu`(
	id_skladu int(20) NOT NULL AUTO_INCREMENT,
    serie_plan int(10) NOT NULL,
    waga_plan int(10) NOT NULL,
    powtorzenia_plan int(10) NOT NULL,
    serie_wykonane int(10),
    waga_wykoknane int(10),
    powtorzenia_wykonane int(10),
    czas time,
    cwiczenieid_cwiczenia int(20) NOT NULL,
    treningid_treningu int(20) NOT NULL,
    PRIMARY KEY(id_skladu));
    
CREATE TABLE `cwiczenie`(
	id_cwiczenia int(20) NOT NULL AUTO_INCREMENT,
    cwiczenie_name varchar(100) NOT NULL,
    partiaid_partia varchar(100) NOT NULL,
    PRIMARY KEY (id_cwiczenia));
    
CREATE TABLE `partia`(
	id_partia varchar(100) NOT NULL,
    partia_name varchar(100) NOT NULL,
    PRIMARY KEY (id_partia));
    
ALTER TABLE trening ADD CONSTRAINT FKtrening342491 FOREIGN KEY (uzytkowniklogin) REFERENCES uzytkownik(login);
ALTER TABLE Element_Treningu ADD CONSTRAINT FKelement23 FOREIGN KEY (treningid_treningu) REFERENCES trening(id_treningu);
ALTER TABLE Element_Treningu ADD CONSTRAINT FKelement34 FOREIGN KEY (cwiczenieid_cwiczenia) REFERENCES cwiczenie(id_cwiczenia);
ALTER TABLE cwiczenie ADD CONSTRAINT FKcwiczenie90 FOREIGN KEY (partiaid_partia) REFERENCES partia(id_partia);


-- unikalny użytkownik
ALTER TABLE `Bazy_projekt`.`uzytkownik` 
ADD UNIQUE INDEX `login_UNIQUE` (`login` ASC) VISIBLE;
    
    
    
    
    
    
    
    