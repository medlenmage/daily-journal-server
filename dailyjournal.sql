 select
      a.id,
      a.concept,
      a.entry,
      a.date,
      a.moodId
  from entries a
  WHERE a.entry LIKE "%"||'ing'||"%"
