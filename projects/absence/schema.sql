drop table if exists absence;
create table absence (
  id integer primary key autoincrement,
  user_id integer not null,
  absence_status integer,
  absence_type integer,
  absence_start date,
  absence_end date
);