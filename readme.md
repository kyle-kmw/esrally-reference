## About this project
This is a reference example of a very simple esrally custom track that uses a Parameter Source function to populate terms queries with random values obtained by a csv file.

## Prerequisites
The system running the track must have esrally installed (This was tested using esrally 2.7.0) and must point to an existing elasticsearch index (See the example command)

## Running the track

The track can be run with the following command:

```sh
esrally race --track-path=reference-track.json --pipeline=benchmark-only --target-hosts=<hostname>:<port> --client-options="use_ssl:true,verify_certs:false,basic_auth_user:'<username>',basic_auth_password:'<password>'"
```

Output should look something like:
```sh
    ____        ____
   / __ \____ _/ / /_  __
  / /_/ / __ `/ / / / / /
 / _, _/ /_/ / / / /_/ /
/_/ |_|\__,_/_/_/\__, /
                /____/

[INFO] Race id is [fa9fc5af-822a-4371-b1c5-76df4ff1583c]
[INFO] Racing on track [reference-track], challenge [just-search] and car ['external'] with version [8.4.3].

Running term                                                                   [100% done]

------------------------------------------------------
    _______             __   _____
   / ____(_)___  ____ _/ /  / ___/_________  ________
  / /_  / / __ \/ __ `/ /   \__ \/ ___/ __ \/ ___/ _ \
 / __/ / / / / / /_/ / /   ___/ / /__/ /_/ / /  /  __/
/_/   /_/_/ /_/\__,_/_/   /____/\___/\____/_/   \___/
------------------------------------------------------

|                                                         Metric |   Task |        Value |   Unit |
|---------------------------------------------------------------:|-------:|-------------:|-------:|
|                     Cumulative indexing time of primary shards |        |  0.000116667 |    min |
|             Min cumulative indexing time across primary shards |        |  0.000116667 |    min |
|          Median cumulative indexing time across primary shards |        |  0.000116667 |    min |
|             Max cumulative indexing time across primary shards |        |  0.000116667 |    min |
|            Cumulative indexing throttle time of primary shards |        |  0           |    min |
|    Min cumulative indexing throttle time across primary shards |        |  0           |    min |
| Median cumulative indexing throttle time across primary shards |        |  0           |    min |
|    Max cumulative indexing throttle time across primary shards |        |  0           |    min |
|                        Cumulative merge time of primary shards |        |  0           |    min |
|                       Cumulative merge count of primary shards |        |  0           |        |
|                Min cumulative merge time across primary shards |        |  0           |    min |
|             Median cumulative merge time across primary shards |        |  0           |    min |
|                Max cumulative merge time across primary shards |        |  0           |    min |
|               Cumulative merge throttle time of primary shards |        |  0           |    min |
|       Min cumulative merge throttle time across primary shards |        |  0           |    min |
|    Median cumulative merge throttle time across primary shards |        |  0           |    min |
|       Max cumulative merge throttle time across primary shards |        |  0           |    min |
|                      Cumulative refresh time of primary shards |        |  0.00025     |    min |
|                     Cumulative refresh count of primary shards |        |  5           |        |
|              Min cumulative refresh time across primary shards |        |  0.00025     |    min |
|           Median cumulative refresh time across primary shards |        |  0.00025     |    min |
|              Max cumulative refresh time across primary shards |        |  0.00025     |    min |
|                        Cumulative flush time of primary shards |        |  0.000233333 |    min |
|                       Cumulative flush count of primary shards |        |  1           |        |
|                Min cumulative flush time across primary shards |        |  0.000233333 |    min |
|             Median cumulative flush time across primary shards |        |  0.000233333 |    min |
|                Max cumulative flush time across primary shards |        |  0.000233333 |    min |
|                                        Total Young Gen GC time |        |  0           |      s |
|                                       Total Young Gen GC count |        |  0           |        |
|                                          Total Old Gen GC time |        |  0           |      s |
|                                         Total Old Gen GC count |        |  0           |        |
|                                                     Store size |        |  3.73274e-06 |     GB |
|                                                  Translog size |        |  5.12227e-08 |     GB |
|                                         Heap used for segments |        |  0           |     MB |
|                                       Heap used for doc values |        |  0           |     MB |
|                                            Heap used for terms |        |  0           |     MB |
|                                            Heap used for norms |        |  0           |     MB |
|                                           Heap used for points |        |  0           |     MB |
|                                    Heap used for stored fields |        |  0           |     MB |
|                                                  Segment count |        |  1           |        |
|                                    Total Ingest Pipeline count |        |  0           |        |
|                                     Total Ingest Pipeline time |        |  0           |      s |
|                                   Total Ingest Pipeline failed |        |  0           |        |
|                                                 Min Throughput |   term | 10.04        |  ops/s |
|                                                Mean Throughput |   term | 10.06        |  ops/s |
|                                              Median Throughput |   term | 10.05        |  ops/s |
|                                                 Max Throughput |   term | 10.08        |  ops/s |
|                                        50th percentile latency |   term |  3.93354     |     ms |
|                                        90th percentile latency |   term |  4.39151     |     ms |
|                                        99th percentile latency |   term |  4.90391     |     ms |
|                                       100th percentile latency |   term |  6.80371     |     ms |
|                                   50th percentile service time |   term |  2.90223     |     ms |
|                                   90th percentile service time |   term |  3.37675     |     ms |
|                                   99th percentile service time |   term |  3.90057     |     ms |
|                                  100th percentile service time |   term |  5.34934     |     ms |
|                                                     error rate |   term |  0           |      % |


--------------------------------
[INFO] SUCCESS (took 31 seconds)
```