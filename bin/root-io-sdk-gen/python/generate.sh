rm -r -f ../../../sdk
openapi-generator-cli generate -i ../openapi.yml -g python -o ../../../  -c config.yaml  
rm openapitools.json	

