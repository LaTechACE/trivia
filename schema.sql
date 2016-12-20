drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  user text not null,
  cwid text not null,
  pin text not null,
  'q0' text not null,
  'q1' text not null,
  'q2' text not null,
  'q3' text not null,
  'q4' text not null,
  'q5' text not null,
  'q6' text not null,
  'q7' text not null,
  'q8' text not null,
  'q9' text not null
);
