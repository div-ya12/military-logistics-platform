# Military Logistics Platform — API Contract

This document defines the common APIs used by all project modules.

## 1. Login

### POST /api/login

Used for user authentication.

### Request

```json
{
  "username": "admin",
  "password": "password"
}
```

### Response

```json
{
  "token": "sample-token",
  "role": "admin"
}
```

---

## 2. Locations

### GET /api/locations

Returns all military posts and depots.

### Response

```json
[
  {
    "id": "P1",
    "name": "Post P1",
    "type": "post",
    "x": 10,
    "y": 20,
    "status": "active"
  }
]
```

---

## 3. Inventory

### GET /api/stock?post_id=P1

Returns the current stock available at a post.

### Response

```json
[
  {
    "item": "RATIONS",
    "quantity": 500,
    "unit": "kg"
  },
  {
    "item": "POL",
    "quantity": 900,
    "unit": "L"
  }
]
```

---

## 4. Demand Forecast

### GET /api/forecast?post_id=P1&item=POL

Returns predicted future consumption.

### Response

```json
{
  "dates": [],
  "p10": [],
  "p50": [],
  "p90": []
}
```

* P10 = lower expected demand
* P50 = expected demand
* P90 = higher expected demand

---

## 5. Alerts

### GET /api/alerts

Returns important logistics alerts.

### Response

```json
[
  {
    "id": "A1",
    "severity": "HIGH",
    "post_id": "P3",
    "item": "POL",
    "message": "Fuel shortage predicted",
    "days_left": 6
  }
]
```

---

## 6. Route Planning

### POST /api/route

Calculates the best available route.

### Request

```json
{
  "src": "D1",
  "dst": "P3",
  "closed_edges": []
}
```

### Response

```json
{
  "primary": {
    "route": ["D1", "P2", "P3"],
    "distance": 120
  },
  "fallback": {
    "route": ["D1", "P1", "P3"],
    "distance": 145
  }
}
```

---

## 7. Scenario Simulation

### POST /api/scenario

Used to simulate a future route closure.

### Request

```json
{
  "pass_closure_in_days": 3
}
```

---

## 8. Consumption / Supply Events

### POST /api/events

Used to record consumption and receipt events.

### Example

```json
{
  "post_id": "P3",
  "item": "POL",
  "quantity": 100,
  "event_type": "consumption"
}
```

---

## 9. Offline Synchronization

### POST /api/sync

Used by the offline post application to synchronize stored events.

The synchronized bundle must contain a valid signature for verification.
