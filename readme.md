## About this project
This is a reference example of a very simple esrally custom track that uses a Parameter Source function to populate terms queries with random values obtained by a csv file.

## Prerequisites
The system running the track must have esrally installed (This was tested using esrally 2.7.0) and must point to an existing elasticsearch index (See the example command)

## Running the track

The track can be run with the following command:

```sh
esrally race --track-path=reference-track.json --pipeline=benchmark-only --target-hosts=<hostname>:<port> --client-options="use_ssl:true,verify_certs:false,basic_auth_user:'<username>',basic_auth_password:'<password>'"
```