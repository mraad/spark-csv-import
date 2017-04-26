# SPARK CSV IMPORT

```
docker\
 run -d\
 -p 3306:3306\
 -p 9000:9000\
 --name memsql\
 memsql/quickstart
```

```
docker run --rm -it --link=memsql:memsql memsql/quickstart memsql-shell
```

```
create database if not exists dmat;
use dmat;
drop table if exists dmat;
create table dmat (
    objectid INTEGER default null,
    lon DOUBLE default null,
    lat DOUBLE default null,
    shape GEOGRAPHYPOINT default null,
    hex50 TEXT default null,
    hex100 TEXT default null,
    hex200 TEXT default null,
    hex500 TEXT default null,
    hex1000 TEXT default null,
    mx DOUBLE default null,
    my DOUBLE default null,
    index (hex50),
    index (hex100),
    index (hex200),
    index (hex500),
    index (hex1000),
    index (shape)
  );
exit;
```

### Reference

- https://github.com/memsql/memsql-spark-connector
