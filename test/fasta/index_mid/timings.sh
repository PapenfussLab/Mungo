#!/bin/sh

rm tumour_sample.fa_idx.*

echo "Create text index..."
time ./createTextIndex.py

echo "Create pickle index..."
time ./createPickleIndex.py

echo "Create sqlite3 index..."
time ./createSqliteIndex.py


echo "Lookup text index..."
time ./lookupTextIndex.py

echo "Lookup pickle index..."
time ./lookupPickleIndex.py

echo "Lookup sqlite3 index..."
time ./lookupSqliteIndex.py

