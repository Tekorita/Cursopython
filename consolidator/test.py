curl -X POST \
  http://stage.b2b.scrapers.instoreview.cl:82/api/v1/consolidate/ \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": 0,
    "category_id": 0,
    "type": "stock",
    "portal": "proconsumo",
    "country": "HN",
    "sources": [
        {
            "id": "stock.csv",
            "s3_key": "for-tests/test-consolidate/proconsumo/stock.csv",
            "dates": []
        }
    ]
}'

curl -X POST \
  http://localhost:8001/api/v1/consolidate/ \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": 0,
    "category_id": 0,
    "type": "stock",
    "portal": "proconsumo",
    "country": "HN",
    "sources": [
        {
            "id": "stock.csv",
            "s3_key": "for-tests/test-consolidate/proconsumo/stock.csv",
            "dates": []
        }
    ]
}'

#pytest scrapers/apps/consolidator/tests/consolidator_tests.py --pdb - s


curl -X POST \
  http://localhost:8001/api/v1/consolidate/ \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": 0,
    "category_id": 0,
    "type": "ventas",
    "portal": "siman-farmacia",
    "country": "HN",
    "sources": [
        {
            "id": "ventas.xlsx",
            "s3_key": "for-tests/test-consolidate/farmacias-siman_HN/ventas.xlsx",
            "dates": []
        }
    ]
}'

curl -X POST \
  http://stage.b2b.scrapers.instoreview.cl:82/api/v1/consolidate/ \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": 0,
    "category_id": 0,
    "type": "ventas",
    "portal": "siman-farmacia",
    "country": "HN",
    "sources": [
        {
            "id": "ventas.xlsx",
            "s3_key": "for-tests/test-consolidate/farmacias-siman_HN/ventas.xlsx",
            "dates": []
        }
    ]
}'

curl -X POST \
  http://stage.b2b.scrapers.instoreview.cl:82/api/v1/consolidate/ \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": 0,
    "category_id": 0,
    "type": "ventas",
    "portal": "siman-farmacia",
    "country": "HN",
    "sources": [
        {
            "id": "ventas.xlsx",
            "s3_key": "for-tests/test-consolidate/farmacias-siman_HN/ventas.xlsx",
            "dates": [
                "2019-09-03"
            ]
            
        }
    ]
}'

curl -X POST \
  http://stage.b2b.scrapers.instoreview.cl:82/api/v1/consolidate/ \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": 0,
    "category_id": 0,
    "type": "ventas",
    "portal": "siman-farmacia",
    "country": "HN",
    "sources": [
        {
            "id": "ventas.xlsx",
            "s3_key": "for-tests/test-consolidate/farmacias-siman_HN/ventas.xlsx",
            "dates": [
                "2019-09-03"
            ]
            
        }
    ]
}'
