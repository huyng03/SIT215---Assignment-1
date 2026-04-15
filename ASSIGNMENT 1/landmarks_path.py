landmarks = [
    {
        "id": 1,
        "name": "Đức Beer",
        "latitude": 21.02213,
        "longitude": 105.89345
    },
    {
        "id": 2,
        "name": "Times City",
        "latitude": 20.99342,
        "longitude": 105.86853
    },
    {
        "id": 3,
        "name": "Royal City",
        "latitude": 21.00324,
        "longitude": 105.81543
    },
    {
        "id": 4,
        "name": "Hải Long Computer",
        "latitude": 20.97455,
        "longitude": 105.77605
    },
    {
        "id": 5,
        "name": "La Palm Hotel",
        "latitude": 21.03369,
        "longitude": 105.84958
    },
    {
        "id": 6,
        "name": "Hanoi Centre",
        "latitude": 21.0317,
        "longitude": 105.83076
    },
    {
        "id": 7,
        "name": "Keangnam Landmark 72",
        "latitude": 21.01681,
        "longitude": 105.78377
    },
    {
        "id": 8,
        "name": "My Dinh National Stadium",
        "latitude": 21.02046,
        "longitude": 105.76606
    },
    {
        "id": 9,
        "name": "Văn Miếu – Quốc Tử Giám",
        "latitude": 21.02809,
        "longitude": 105.83525
    },
    {
        "id": 10,
        "name": "Olala Café",
        "latitude": 21.03444,
        "longitude": 105.79085
    },
    {
        "id": 11,
        "name": "Lục Thủy Cafe",
        "latitude": 21.02898,
        "longitude": 105.85141
    },
    {
        "id": 12,
        "name": "CIPUTRA Hà Nội",
        "latitude": 21.07537,
        "longitude": 105.81011
    },
    {
        "id": 13,
        "name": "Ba Đình Square",
        "latitude": 21.03753,
        "longitude": 105.836
    },
    {
        "id": 14,
        "name": "Vincom Bà Triệu Mall",
        "latitude": 21.01096,
        "longitude": 105.84957
    },
    {
        "id": 15,
        "name": "Maison de Zen",
        "latitude": 21.05584,
        "longitude": 105.81998
    },
    {
        "id": 16,
        "name": "Lotte Mall Tây Hồ",
        "latitude": 21.07604,
        "longitude": 105.81264
    },
    {
        "id": 17,
        "name": "Ngoại Giao Đoàn",
        "latitude": 21.06622,
        "longitude": 105.79817
    },
    {
        "id": 18,
        "name": "Bảo tàng Lịch sử Quân sự Việt Nam",
        "latitude": 21.0094,
        "longitude": 105.75388
    },
    {
        "id": 19,
        "name": "Splendora Villa",
        "latitude": 21.01566,
        "longitude": 105.7242
    },
    {
        "id": 20,
        "name": "Đại Học Bách Khoa Hà Nội",
        "latitude": 21.00697,
        "longitude": 105.84192
    },
    {
        "id": 21,
        "name": "Vincom Trần Duy Hưng Mall",
        "latitude": 21.00737,
        "longitude": 105.79567
    }
]


paths = [
    {
        "node_a": 1,
        "node_b": 10,
        "distance": 86/1000,
        "time": 1/60,
        "risk": 0.2,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 13,
        "node_b": 11,
        "distance": 0.3,
        "time": 1/60,
        "risk": 0.4,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 10,
        "node_b": 12,
        "distance": 0.8,
        "time": 1/30,
        "risk": 0.4,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 12,
        "node_b": 7,
        "distance": 5.2,
        "time": 13/60,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": True # a -> b
    },
    {
        "node_a": 7,
        "node_b": 19,
        "distance": 0.8,
        "time": 1/20,
        "risk": 0.2,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 9,
        "node_b": 19,
        "distance": 1,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 4,
        "node_b": 9,
        "distance": 0.85,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 15,
        "node_b": 3,
        "distance": 0.5,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 3,
        "node_b": 21,
        "distance": 1.9,
        "time": 1/12,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 20,
        "node_b": 6,
        "distance": 0.55,
        "time": 1/15,
        "risk": 0.3,
        "traffic_congestion": 0.6,
        "is_directed": True # a -> b
    },
    {
        "node_a": 16,
        "node_b": 17,
        "distance": 1.7,
        "time": 7/60,
        "risk": 0.5,
        "traffic_congestion": 0.8,
        "is_directed": True # a -> b
    },
    {
        "node_a": 2,
        "node_b": 17,
        "distance": 0.35,
        "time": 1/30,
        "risk": 0.4,
        "traffic_congestion": 0.6,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 2,
        "node_b": 9,
        "distance": 1.3,
        "time": 1/15,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 9,
        "node_b": 5,
        "distance": 1.2,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": True # a -> b
    },
    {
        "node_a": 5,
        "node_b": 8,
        "distance": 0.4,
        "time": 1/30,
        "risk": 0.3,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 8,
        "node_b": 18,
        "distance": 2,
        "time": 2/15,
        "risk": 0.4,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 18,
        "node_b": 14,
        "distance": 0.5,
        "time": 1,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 9,
        "node_b": 1,
        "distance": 3.2,
        "time": 1/10,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 13,
        "node_b": 12,
        "distance": 0.35,
        "time": 1/60,
        "risk": 0.3,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 21,
        "node_b": 15,
        "distance": 1.2,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 6,
        "node_b": 16,
        "distance": 0.23,
        "time": 1/50,
        "risk": 0.2,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 5,
        "node_b": 20,
        "distance": 3,
        "time": 1/6,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 7,
        "node_b": 9,
        "distance": 1.4,
        "time": 1/12,
        "risk": 0.2,
        "traffic_congestion": 0.3,
        "is_directed": True # a -> b
    },
    {
        "node_a": 14,
        "node_b": 20,
        "distance": 0.95,
        "time": 1/12,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 20,
        "node_b": 21,
        "distance": 2,
        "time": 2/15,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 2,
        "node_b": 4,
        "distance": 1.4,
        "time": 1/10,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 11,
        "node_b": 18,
        "distance": 4.7,
        "time": 11/60,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 3,
        "node_b": 16,
        "distance": 2,
        "time": 1/10,
        "risk": 0.7,
        "traffic_congestion": 0.9,
        "is_directed": True # a -> b
    },
    {
        "node_a": 15,
        "node_b": 14,
        "distance": 4.2,
        "time": 2/15,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 10,
        "node_b": 19,
        "distance": 4.9,
        "time": 11/60,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 6,
        "node_b": 21,
        "distance": 1.3,
        "time": 1/15,
        "risk": 0.3,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 5,
        "node_b": 2,
        "distance": 2,
        "time": 1/12,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": True # a -> b
    },
    {
        "node_a": 20,
        "node_b": 8,
        "distance": 1.4,
        "time": 2/15,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 7,
        "node_b": 18,
        "distance": 1.9,
        "time": 1/10,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 3,
        "node_b": 6,
        "distance": 3.1,
        "time": 9/60,
        "risk": 0.6,
        "traffic_congestion": 0.8,
        "is_directed": True # a -> b
    },
    {
        "node_a": 6,
        "node_b": 5,
        "distance": 2.9,
        "time": 7/60,
        "risk": 0.6,
        "traffic_congestion": 0.8,
        "is_directed": True # a -> b
    },
    {
        "node_a": 2,
        "node_b": 6,
        "distance": 0.9,
        "time": 1/15,
        "risk": 0.6,
        "traffic_congestion": 0.6,
        "is_directed": True # a -> b
    },
]
