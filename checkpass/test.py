curl -X POST \
  http://localhost:8001/api/v1/scraper/fda/checkpass/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache,no-cache,no-cache,no-cache' \
  -d '{
    "username": "P1728",
    "password": "*cx4882mx",
    "country": "MX"
}'

curl -X POST \
  http://localhost:8001/api/v1/scraper/fda/checkpass/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache,no-cache,no-cache,no-cache' \
  -d '{
    "username": "aaaP1728",
    "password": "*cx4882mx",
    "country": "MX"
}'