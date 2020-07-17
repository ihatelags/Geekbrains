USE courseproject;

-- Представление - все документы
CREATE or replace VIEW view_documents AS
SELECT 
	d.id AS 'id документа',
	d.name AS 'Название документа',
	(SELECT name FROM DocumentType WHERE d.type_id = id) AS 'Тип документа',
	(SELECT concat(CE.firstname, ' ', CE.lastname, ' ', CE.middlename) FROM CompanyEmployees CE WHERE d.creator_id = CE.id) AS 'Ведущий',
	(SELECT concat(CE.firstname, ' ', CE.lastname, ' ', CE.middlename) FROM CompanyEmployees CE WHERE d.checking_id = CE.id) AS 'Проверяющий',
	(SELECT concat(CE.firstname, ' ', CE.lastname, ' ', CE.middlename) FROM CompanyEmployees CE WHERE d.mod_id = CE.id) AS 'Изменил',
	d.create_date AS 'Дата создания',
	d.last_mod_date AS 'Дата последнего изменения',
	d.decimal_number AS 'Децимальный номер',
	d.pathfile AS 'Расположение файла'
FROM documents d;

-- Представление - все сотрудники
CREATE or replace VIEW view_employees AS
SELECT 
	CE.id AS 'id сотрудника',
	concat(CE.firstname, ' ', CE.lastname, ' ', CE.middlename) AS 'ФИО',
	(SELECT d.name FROM department AS d WHERE d.id = CE.department_id) AS 'Отдел',
	(SELECT f.namefunction FROM functionemployees AS f WHERE f.id = CE.function_id) AS 'Должность',
	(YEAR(now()) - YEAR(CE.birthday_at)) AS 'Возраст, лет',
	CE.employed_at AS 'Дата устройства на работу',
	(CASE
    WHEN CE.dismissed = 1 
        THEN 'Уволен'    
    ELSE '-' 
	END) AS 'Уволен'
FROM CompanyEmployees CE;