SELECT * FROM members;
SELECT * FROM memberships;
SELECT * FROM attending;
SELECT * FROM classes;

-- SELECT * FROM classes JOIN attending on classes.id = attending.class_id WHERE member_id = 2;
-- SELECT members.* FROM members INNER JOIN attending on members.id = attending.member_id WHERE class_id = 1;
-- SELECT * FROM members WHERE membership_id = 2;