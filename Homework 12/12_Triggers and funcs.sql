
USE courseproject;

DELIMITER //
DROP TRIGGER IF EXISTS courseproject_companyemployees_not_null_insert//
CREATE TRIGGER courseproject_companyemployees_not_null_insert BEFORE INSERT ON companyemployees
FOR EACH ROW
begin
    IF NEW.firstname IS NULL OR NEW.lastname IS NULL OR NEW.middlename Is NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ФИО не могут быть пустыми';
    END IF;
   
    IF NEW.department_id NOT IN (SELECT id FROM department)  THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ошибка присвоения отдела';
    END IF;
   
    IF NEW.department_id NOT IN (SELECT id FROM FunctionEmployees)  THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Нет такой должности';
    END IF;
END//
DELIMITER ;


DELIMITER //
DROP TRIGGER IF EXISTS courseproject_companyemployees_not_null_delete//
CREATE TRIGGER courseproject_companyemployees_not_null_delete BEFORE DELETE ON companyemployees
FOR EACH ROW
begin
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Установите флаг "Уволен"';    
END//
DELIMITER ;


-- процедура добавления сотрудника
DELIMITER //
DROP PROCEDURE IF EXISTS `add_user`//
CREATE PROCEDURE `add_user`(firstname varchar(100), 
              lastname VARCHAR(100), 
              middlename VARCHAR(100), 
              department VARCHAR(100), 
              namefunction VARCHAR(100),
              birthday_at DATE,
              OUT tran_result varchar(20))
BEGIN
    DECLARE `_rollback` BOOL DEFAULT 0;   
    DECLARE code varchar(100);
    DECLARE error_string varchar(100);
 
 
    DECLARE id_department bigint unsigned;
    DECLARE id_namefunction bigint unsigned;
    
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
      SET `_rollback` = 1;
  GET stacked DIAGNOSTICS CONDITION 1
          code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
      set tran_result := concat('Error occured. Code: ', code, '. Text: ', error_string);
    end;
   
    SET id_department = (SELECT id FROM department WHERE name = department);
    SET id_namefunction = (SELECT id FROM functionemployees f WHERE f.namefunction = namefunction);
   
  START TRANSACTION;
  
  INSERT INTO CompanyEmployees(firstname, lastname, middlename, department_id, function_id, birthday_at)
  VALUES (firstname, lastname, middlename, id_department, id_namefunction, birthday_at);
    
  IF `_rollback` THEN
      set tran_result = 'ROLLBACK';
           ROLLBACK;
       ELSE
      set tran_result := 'COMMIT';
          COMMIT;
      END IF;
END//

DELIMITER ;

call `add_user`('user1_1', 'user1_2', 'user1_3', 'Отдел 1', 'Монтажник', '1999-07-25', @ouT_data);

SELECT @ouT_data;

-- Расчет стоимости комлектующих на изделие
DELIMITER //
DROP FUNCTION IF EXISTS price_components_in_products//
CREATE FUNCTION price_components_in_products (id_products BIGINT UNSIGNED)
RETURNS FLOAT NO SQL
BEGIN
  DECLARE SUMM float;

  SET SUMM = (SELECT SUM(cc.price * pc.count) AS 'цена'
        FROM Products_Component pc
        JOIN Component_Counts cc ON pc.component_id = cc.component_id
        WHERE pc.products_id = id_products);
  RETURN SUMM;
END//
DELIMITER ;