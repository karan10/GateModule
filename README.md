# GateModule
* This project is supported in Python3
## Usage
* To run this code, run the file present in project root by following command
  ```bash
    python3 gate.py
  ```
* You can play with user attributes and gate condition for different cases present by changing in `gate.py` file
* This project can also be run on Flask server at port 5000 exposing following APIs
  
  1. Get all users
  2. Create user
  3. Get all gates
  4. Create gate
  5. Check if user is allowed to access the feature. [API expects `user_id` & `gate_id`]

Whenever the flask server is started it will create a default user & default gate in memory. You can get the details using get API.

```bash
Attributes supported - ['age', 'gender', 'past_order_amount', 'days_active']
Operators supported - ['<', '<=', '>', '>=', '==', 'AND', 'OR']
```

## Postman collection
[GateModule Collection]([Click to get collection](https://www.getpostman.com/collections/a56923ca0ad0749d67ad))
