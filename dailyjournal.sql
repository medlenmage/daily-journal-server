drop table if exists Entries;
drop table if exists Moods;

CREATE TABLE `Entries` (
  `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `concept` TEXT NOT NULL,
  `entry` TEXT NOT NULL,
  `date` INTEGER NOT NULL,
  `moodId` INTEGER NOT NULL,
  FOREIGN KEY(`moodId`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
  `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `label` TEXT NOT NULL
);

INSERT INTO `Entries` VALUES (null, "12345", "123", 1598458543321, 1);
INSERT INTO `Entries` VALUES(null, "abc", "123", 1598458548239, 2);
INSERT INTO `Entries` VALUES(null, "Delete", "Now Deleting", 1598458559152, 1);
INSERT INTO `Entries` VALUES(null, "ANGRY", "jij", 1598557358781, 3);
INSERT INTO `Entries` VALUES(null, "678", "Now Deleting", 1598557373697, 4);

INSERT INTO `Moods` VALUES(null, "Happy");
INSERT INTO `Moods` VALUES(null, "Sad");
INSERT INTO `Moods` VALUES(null, "Angry");
INSERT INTO `Moods` VALUES(null, "Ok");

select * from Entries;
select * from Moods;
