INSERT INTO memberships (level) VALUES ("Gold");
INSERT INTO memberships (level) VALUES ("Silver");
INSERT INTO members (first_name, last_name, membership_id) VALUES ("Brian", "Kerr", 1);
INSERT INTO members (first_name, last_name, membership_id) VALUES ("Tina", "Munro", 2);
INSERT INTO classes (name, capacity, time) VALUES ("Body Pump", 12, "2022-05-27 15:20");
INSERT INTO classes (name, capacity, time) VALUES ("Body Attack", 12, "2022-05-26 15:20:00");
INSERT INTO attending (member_id, class_id) VALUES (1, 1);
INSERT INTO attending (member_id, class_id) VALUES (1, 2);

