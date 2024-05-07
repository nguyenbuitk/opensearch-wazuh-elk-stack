# Security information and event management

## Components

Server components

- ELK Stack (Opendistro, Logstash, Kibana)
- Wazuh manager

Client components

- Wazuh agent
- Filebeat

## Diagram

![SIEM diagram](/images/diagram.png "SIEM diagram")

# Build dependence

```
helm dependency build
helm dependency update
```

## NOTES

```bash
# Tunning sysctl for elasticsearch
cat << EOF > /etc/sysctl.d/90-elk.conf
vm.max_map_count=262144
EOF

sysctl -p --system

```

## Deploy

```
helm template --debug --output-dir ./out tttt --namespace=wazuh ./


helm install \
    --create-namespace \
    --namespace=wazuh \
    -f ./values.yaml \
    ovng \
    ./

helm upgrade \
    --namespace=wazuh \
    -f ./values.yaml \
    ovng \
    ./

helm uninstall \
    --namespace=wazuh \
    ovng


```

```bash
helm template --debug -f ./values-ovng-preview2.yaml --output-dir ./out ovng ./

## Deploy new
make up ENV=ovng-preview2
## Update existing
make upgrade ENV=ovng-preview2
## Destroy existing
make down ENV=ovng-preview2

kubectl port-forward -n wazuh service/ovng-wazuh-kibana 5601:5601

```
