update:
	@helm dependency update

template:
	@helm template --debug -f ./values.yaml --output-dir ./out ovng ./

up:
	helm install \
		-f ./values-$(ENV).yaml \
		--create-namespace \
		--namespace=wazuh \
		ovng \
		./

upgrade:
	helm upgrade \
		-f ./values-$(ENV).yaml \
		--namespace=wazuh \
		ovng \
		./

down:
	helm uninstall --namespace=wazuh ovng
