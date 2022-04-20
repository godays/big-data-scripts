#!/usr/bin/env bash
set -x

HADOOP_STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar
HDFS_OUTPUT_DIR="streaming_wc_result"
NUM_REDUCERS=8
INPUT_IDS_HDFS_PATH=$1
OUTPUT_HDFS_PATH=$2
JOB_NAME=$3

hdfs dfs -rm -r -skipTrash ${OUTPUT_HDFS_PATH}

# Wordcount
( yarn jar $HADOOP_STREAMING_JAR \
    -D mapreduce.job.name=JOB_NAME \
    -D stream.num.map.output.key.fields=2 \
    -D stream.num.reduce.output.key.fields=2 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2" \
    -files mapper.py,reducer.py \
    -numReduceTasks 5 \
    -mapper 'python3 mapper.py' \
    -combiner 'python3 reducer.py' \
    -reducer 'python3 reducer.py' \
    -input ${INPUT_IDS_HDFS_PATH} \
    -output ${OUTPUT_HDFS_PATH}_tmp &&

# Global sorting as we use only 1 reducer
yarn jar $HADOOP_STREAMING_JAR \
    -files reducer_2.py \
    -D mapreduce.job.name=JOB_NAME \
    -D stream.num.map.output.key.fields=3 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k3,3nr" \
    -input ${OUTPUT_HDFS_PATH}_tmp \
    -output ${OUTPUT_HDFS_PATH} \
    -numReduceTasks 1 \
    -mapper cat \
    -reducer 'python3 reducer_2.py'
) || echo "Error happens"

hdfs dfs -rm -r -skipTrash ${OUTPUT_HDFS_PATH}_tmp

hdfs dfs -cat $OUTPUT_HDFS_PATH/part-00000 | head -n 50