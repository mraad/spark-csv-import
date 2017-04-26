package com.esri

import com.memsql.spark.connector._
import org.apache.spark.sql.types.{IntegerType, StructField, StructType}
import org.apache.spark.sql.{Row, SparkSession}

object MemApp extends App {
  val spark = SparkSession
    .builder()
    .master("local[*]")
    .appName("MemApp")
    .config("spark.ui.enabled", false)
    .config("spark.memsql.host", "localhost")
    .config("spark.memsql.user", "root")
    .config("spark.memsql.password", "")
    .getOrCreate()

  try {
    // import spark.implicits._

    val rows = Seq(
      Row(11111),
      Row(22222),
      Row(33333)
    )
    val rdd = spark.sparkContext.parallelize(rows)

    val schema = new StructType(Array(
      StructField("objectid", IntegerType)
    ))

    spark
      .sqlContext
      .createDataFrame(rdd, schema)
      .saveToMemSQL("dmat", "dmat")
  }
  finally {
    spark.stop()
  }
}