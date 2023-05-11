-- Keep a log of any SQL queries you execute as you solve the mystery.

.tables
.schema
SELECT * FROM crime_scene_reports;
SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28;
SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';
SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28;
SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw';
SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street';

SELECT bank_accounts.account_number, person_id FROM bank_accounts JOIN (SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street') AS usedAccount ON usedAccount.account_number = bank_accounts.account_number;
SELECT * FROM people JOIN (SELECT bank_accounts.account_number, person_id FROM bank_accounts JOIN (SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street') AS usedAccount ON usedAccount.account_number = bank_accounts.account_number) AS suspect1 ON suspect1.person_id = people.id;

SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit';
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit' AND hour >= 10 AND minute > 15;
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND minute > 15 & minute < 25;
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND 15 < minute AND minute < 25;

SELECT *
FROM (SELECT * FROM people JOIN (SELECT bank_accounts.account_number, person_id FROM bank_accounts JOIN (SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street') AS usedAccount ON usedAccount.account_number = bank_accounts.account_number) AS suspect1 ON suspect1.person_id = people.id) AS suspect2
JOIN (SELECT bakery_security_logs.license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND 15 < minute AND minute < 25) AS bslog ON bslog.license_plate = suspect2.license_plate;

SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

SELECT *
FROM (SELECT *
FROM (SELECT * FROM people JOIN (SELECT bank_accounts.account_number, person_id FROM bank_accounts JOIN (SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street') AS usedAccount ON usedAccount.account_number = bank_accounts.account_number) AS suspect1 ON suspect1.person_id = people.id) AS suspect2
JOIN (SELECT bakery_security_logs.license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND 15 < minute AND minute < 25) AS bslog ON bslog.license_plate = suspect2.license_plate) AS suspect3
JOIN (SELECT caller, receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60) cl ON suspect3.phone_number = cl.caller;

SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29 ORDER BY hour;
SELECT * FROM airports;

SELECT * FROM passengers WHERE flight_id = 36;

SELECT *
FROM (SELECT *
FROM (SELECT *
FROM (SELECT * FROM people JOIN (SELECT bank_accounts.account_number, person_id FROM bank_accounts JOIN (SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street') AS usedAccount ON usedAccount.account_number = bank_accounts.account_number) AS suspect1 ON suspect1.person_id = people.id) AS suspect2
JOIN (SELECT bakery_security_logs.license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND 15 < minute AND minute < 25) AS bslog ON bslog.license_plate = suspect2.license_plate) AS suspect3
JOIN (SELECT caller, receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60) cl ON suspect3.phone_number = cl.caller) AS suspect4
JOIN (SELECT * FROM passengers WHERE flight_id = 36) AS fl_info ON suspect4.passport_number = fl_info.passport_number;

SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = '(367) 555-5533';
SELECT name FROM people WHERE phone_number = '(375) 555-8161';
