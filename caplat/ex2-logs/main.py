from http_client import HttpClient

def main():
    client = HttpClient("http://localhost:9514")
    
    # Question 1: GET method
    params = {'id': '315155531', 'year': '1999'}
    response = client.get("/test_get_method", params=params)

    # Question 2: POST method
    body = {
        "id": 315155531,    
        "year": 1999,
        "requestId": response.text
    }
    response = client.post("/test_post_method", body)
    
    # Question 3: PUT method
    params = {'id': response.json()['message']}
    body = {
        "id": ((315155531 - 145987)%34),    
        "year": (1999 + 785)%62,
    }
    response = client.put("/test_put_method", params=params, json=body)

    # Question 4: DELETE method
    params = {'id': response.json()['message']}
    response = client.delete("/test_delete_method", params=params)

if __name__ == "__main__":
    main()