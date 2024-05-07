FROM docker.elastic.co/logstash/logstash-oss:6.8.23

RUN bin/logstash-plugin install logstash-output-syslog
RUN bin/logstash-plugin install logstash-codec-json
