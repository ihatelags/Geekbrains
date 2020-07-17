USE vk;

-- Задание 1. Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).

-- старое решение с вложенным запросом (исправленное):
SELECT target_id,
       count(*) AS likes_count,
       (SELECT CONCAT(first_name, ' ', last_name)
       FROM users
       WHERE users.id = likes.user_id) AS name
FROM likes
WHERE target_type_id = 2
  AND target_id IN
    (SELECT *
     FROM
       (SELECT user_id
        FROM profiles
        ORDER BY TIMESTAMPDIFF(YEAR, birthday, NOW())
        LIMIT 10) AS youngest)
GROUP BY target_id


-- новое решение с JOIN:
SELECT p.user_id AS 'User ID',
       COUNT(DISTINCT l.id) AS 'Number of likes',
       p.birthday,
       TIMESTAMPDIFF(YEAR, p.birthday, NOW()) "Возраст"
FROM profiles p
LEFT JOIN likes l ON p.user_id = l.target_id
AND target_type_id =
  (SELECT id
   FROM target_types
   WHERE name = 'users'
   LIMIT 1)
GROUP BY p.user_id
ORDER BY p.birthday DESC
LIMIT 10;

-- 2. Определить кто больше поставил лайков (всего) - мужчины или женщины?
-- старое решение с вложенным запросом:
SELECT
  (SELECT gender
   FROM profiles
   WHERE profiles.user_id = likes.user_id) gender,
       COUNT(user_id) like_count
FROM likes
GROUP BY gender
ORDER BY like_count DESC 

-- новое решение с JOIN:
SELECT p.gender "Пол",
       COUNT(l.user_id) "Поставленные лайки"
FROM likes l
JOIN profiles p ON l.user_id = p.user_id
GROUP BY p.gender
ORDER BY "Поставленные лайки" 


-- 3. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети (критерии активности необходимо определить самостоятельно).
-- Активность буду замерять количеством лайков и постов.


-- старое решение с вложенным запросом (неисправленное):
SELECT name,
       SUM(activity_count) AS activity
FROM (
        (SELECT
           (SELECT CONCAT(first_name, ' ', last_name)
            FROM users AS u
            WHERE u.id = l.user_id) name,
                COUNT(*) activity_count
         FROM likes AS l
         GROUP BY name)
      UNION
        (SELECT
           (SELECT CONCAT(first_name, ' ', last_name)
            FROM users AS u
            WHERE u.id = p.user_id) name,
                COUNT(*) activity_count
         FROM posts AS p
         GROUP BY name)) AS activities
GROUP BY name
ORDER BY activity
LIMIT 10;

-- Комментарии преподавателя: При таком построении запроса в отчёт не попадут пользователи без лайков и постов.

-- Исправленная версия с вложенным запросом, но внутри SELECT, а не FROM:
SELECT CONCAT(first_name, ' ', last_name) Name,
       (
          (SELECT COUNT(*)
           FROM likes l
           WHERE l.user_id = u.id) +
          (SELECT COUNT(*)
           FROM posts p
           WHERE p.user_id = u.id)) Activity
FROM users u
ORDER BY Activity
LIMIT 10;

-- новое решение с JOIN:
SELECT CONCAT(u.first_name, ' ', u.last_name) Name,
       COUNT(l.user_id) + COUNT(p.user_id) Activity
FROM users u
LEFT JOIN likes l ON l.user_id = u.id
LEFT JOIN posts p ON p.user_id = u.id
GROUP BY Name
ORDER BY Activity
LIMIT 10;
