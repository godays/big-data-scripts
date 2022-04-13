#!/usr/bin/env bash
set -x

HADOOP_STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar
INPUT_IDS_HDFS_PATH=$1
OUTPUT_HDFS_PATH=$2
JOB_NAME=$3


hdfs dfs -rm -r -skipTrash $OUTPUT_HDFS_PATH > /dev/null

yarn jar $HADOOP_STREAMING_JAR \
        -files mapper.py,reducer.py \
        -D mapreduce.job.name=$JOB_NAME \
        -numReduceTasks 5 \
        -mapper 'python3 mapper.py' \
        -reducer 'python3 reducer.py' \
        -input /data/ids_part \
        -output $OUTPUT_HDFS_PATH

hdfs dfs -cat $OUTPUT_HDFS_PATH/part-00000 | head -n 50