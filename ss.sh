#!/usr/bin/env bash
spark-submit\
 --master local[*]\
 --conf spark.ui.enabled=false\
 --conf spark.es.nodes=local192\
 --conf spark.memsql.host=localhost\
 --conf spark.memsql.user=root\
 --conf spark.memsql.password=""\
 --packages com.esri:webmercator_2.11:1.2,com.esri:hex-grid_2.11:1.2,org.elasticsearch:elasticsearch-spark-20_2.11:5.3.1\
 target/scala-2.11/spark-csv-import_2.11-0.1.jar

# --jars /Users/mraad_admin/.m2/repository/com/esri/webmercator_2.11/1.2/webmercator_2.11-1.2.jar,/Users/mraad_admin/.m2/repository/com/esri/hex-grid/1.2/hex-grid-1.2.jar\
