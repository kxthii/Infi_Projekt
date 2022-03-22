create database if not exists Sport;
use Sport;


create table if not exists Sportart
(
	Sportart_ID int auto_increment unique key primary key,
    Sportart varchar(60)

);


create table if not exists Sportgruppe
(
    Sportgruppen_ID int auto_increment unique key primary key,
    Gruppenname varchar(64),
    Gründungsdatum date,
    Maskotchen varchar(64),
    Sportart_ID int
);


create table if not exists Sportler
(
    Sportler_ID int auto_increment unique key primary key,
    Geburtsdatum date,
    Vorname varchar(64),
    Nachname varchar(64),
    Größe varchar(64)
);


create table if not exists Sportgruppe_Sportler
(
    Sportgruppe_Sportler_ID int auto_increment unique key primary key,
    Sportler_ID int,
    Sportgruppen_ID int
);


alter table Sportgruppe_Sportler add constraint Sportler_ID foreign key (Sportler_ID) references Sportler(Sportler_ID);
alter table Sportgruppe_Sportler add constraint Sportgruppen_ID foreign key (Sportgruppen_ID) references Sportgruppe(Sportgruppen_ID);
alter table Sportgruppe add constraint Sportart_ID foreign key (Sportart_ID) references Sportart(Sportart_ID);




