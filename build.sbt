organization := "com.esri"

name := "spark-csv-import"

version := "0.1"

isSnapshot := true

publishMavenStyle := true

scalaVersion := "2.11.7"

sparkVersion := "2.1.0"

sparkComponents := Seq("sql")

libraryDependencies ++= Seq(
  "com.esri" % "hex-grid" % "1.1",
  "com.esri" %% "webmercator" % "1.2",
  "com.memsql" %% "memsql-connector" % "2.0.2",
  "org.elasticsearch" %% "elasticsearch-spark-20" % "5.3.1"
)
