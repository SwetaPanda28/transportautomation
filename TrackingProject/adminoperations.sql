
355480020823579
352887078364431

INSERT into user values (1,"vivek","vivek123");

insert into company values
( 1,'companyName','companyAddress1','companyAddress2','companyCity','companyPostalCode','companyState','companyCountry',1234567890,'vivek',1,34.1,56.123)

insert into vehicle values ( 'vehicleName', 'vehicleDriver', 'vehicleType',35,1,1);

select * from user as u
	join company c
	on c.username = u.username
	join device d
	on d.companyID = c.companyID
	join warehouse ws
	on ws.imienumber = d.imienumber
where u.username = "vivek"
