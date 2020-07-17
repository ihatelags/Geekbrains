-- Практическое задание тема "Оптимизация запросов"
-- 1. Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users,
-- catalogs и products в таблицу logs помещается время и дата создания записи, название
-- таблицы, идентификатор первичного ключа и содержимое поля name.

USE shop;

DROP TABLE IF EXISTS logs;
CREATE TABLE IF NOT EXISTS logs (
	id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время и дата создания записи',
 	from_table VARCHAR(8) NOT NULL COMMENT 'Исходная таблица',
	from_table_item_id INT UNSIGNED NOT NULL COMMENT 'ID записи в исходной таблице',
	from_table_item_name VARCHAR(255) COMMENT 'Поле name записи в исходной таблице',
	PRIMARY KEY (id)
) COMMENT 'Таблица логов' ENGINE = ARCHIVE;

SELECT * FROM logs;

DELIMITER //

DROP TRIGGER IF EXISTS users_insert;
CREATE TRIGGER users_insert AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO logs (from_table, from_table_item_id, from_table_item_name) VALUES ('users', NEW.id, NEW.name);
END//

DROP TRIGGER IF EXISTS catalogs_insert;
CREATE TRIGGER catalogs_insert AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO logs (from_table, from_table_item_id, from_table_item_name) VALUES ('catalogs', NEW.id, NEW.name);
END//

DROP TRIGGER IF EXISTS products_insert;
CREATE TRIGGER products_insert AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO logs (from_table, from_table_item_id, from_table_item_name) VALUES ('products', NEW.id, NEW.name);
END//

DELIMITER ;

INSERT INTO users (name, age) VALUES ('Ivanov', 18);
INSERT INTO catalogs (name) VALUES ('Блоки питания'), ('Корпуса');
INSERT INTO products (name) VALUES ('FSP 250W');

SELECT * FROM logs;

-- Практическое задание тема "NoSQL"
-- 1. В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов.
HSET addresses '127.0.0.1' 1
HGETALL addresses

HINCRBY addresses '127.0.0.2' 2
HGETALL addresses

HGET addresses '127.0.0.1'

HVALS addresses
HKEYS addresses

-- 2. При помощи базы данных Redis решите задачу поиска имени пользователя по электронному
-- адресу и наоборот, поиск электронного адреса пользователя по его имени.
HSET emails 'ivanov' 'ivanov@gmail.com'
HSET emails 'petrov' 'petrov@me.com'
HSET emails 'sidorov' 'sidorov@icloud.com'

HGET emails 'sidorov'

HSET users 'ivanov@gmail.com' 'ivanov'
HSET users 'petrov@me.com' 'petrov'
HSET users 'sidorov@icloud.com' 'sidorov'

HGET users 'petrov@me.com'

-- 3.Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB.

use shop

db.shop.insert({
"catalogs" : [{"1" : "Процессоры"}, {"2" : "Материнские платы"}, {"3" : "Видеокарты"}, {"4" : "Жесткие диски"}, {"5" : "Оперативная память"}],
"products" : [{"1" : {"name" : "Intel Core i7-8800K", "desc" : "Процессор для настольных персональных компьютеров, основанных на платформе Intel.",
			  "price" : "7890.00", "cat" : "1"}},
			{"2" : {"name" : "AMD FX-8320E", "desc" : "Процессор для настольных персональных компьютеров, основанных на платформе AMD.",
			  "price" : "4780.00", "cat" : "1"}},
			{"3" : {"name" : "Gigabyte H310M S2H", "desc" : "Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX",
			  "price" : "4790.00", "cat" : "2"}}]
}))





