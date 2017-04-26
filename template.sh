#!/usr/bin/env bash
export INDEX=dmat
curl -XDELETE "local192:9200/_template/${INDEX}?pretty"
curl -XPUT "local192:9200/_template/${INDEX}?pretty" -d @${INDEX}.json
