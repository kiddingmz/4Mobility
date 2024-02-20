from flask import Flask, jsonify, request, Blueprint
import json

app = Flask(__name__)
api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

users = [
    {
        'id': 1,
        'name': 'John Doe'
    },
    {
        'id': 2,
        'name': 'Jane Doe'
    }
]
'''
    Users API
    GET /api/v1/user
    GET /api/v1/user/<id>
    POST /api/v1/user
    PUT /api/v1/user/<id>
    DELETE /api/v1/user/<id>
'''


@api_v1.route('/user', methods=['GET'])
def get_all_users():
    """Get all users"""
    return jsonify(users)


@api_v1.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """Get user by id"""
    for user in users:
        if user['id'] == user_id:
            return user
    return None


@api_v1.route('/user', methods=['POST'])
def create_user():
    """Create a new user"""
    user = request.get_json()
    users.append(user)
    return jsonify(user)


@api_v1.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user by id"""
    user = request.get_json()
    for i, u in enumerate(users):
        if u['id'] == user_id:
            users[i] = user
            return jsonify(user)
    return None


@api_v1.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user by id"""
    for i, user in enumerate(users):
        if user['id'] == user_id:
            del users[i]
            return jsonify(users)
    return None


'''
    Routes API
    GET /api/v1/route
    GET /api/v1/route/<id>
    POST /api/v1/route
    PUT /api/v1/route/<id>
    DELETE /api/v1/route/<id>
'''

routes = [
    {
        'id': 1,
        'name': 'Route 1'
    },
    {
        'id': 2,
        'name': 'Route 2'
    }
]


@api_v1.route('/route', methods=['GET'])
def get_all_routes():
    """Get all routes"""
    return jsonify(routes)


@api_v1.route('/route/<int:route_id>', methods=['GET'])
def get_route_by_id(route_id):
    """Get route by id"""
    for route in routes:
        if route['id'] == route_id:
            return route
    return None


@api_v1.route('/route', methods=['POST'])
def create_route():
    """Create a new route"""
    route = request.get_json()
    routes.append(route)
    return jsonify(route)


@api_v1.route('/route/<int:route_id>', methods=['PUT'])
def update_route(route_id):
    """Update route by id"""
    route = request.get_json()
    for i, r in enumerate(routes):
        if r['id'] == route_id:
            routes[i] = route
            return jsonify(route)
    return None


@api_v1.route('/route/<int:route_id>', methods=['DELETE'])
def delete_route(route_id):
    """Delete route by id"""
    for i, route in enumerate(routes):
        if route['id'] == route_id:
            del routes[i]
            return jsonify(routes)
    return None


'''
    Buses API
    GET /api/v1/bus
    GET /api/v1/bus/<id>
    POST /api/v1/bus
    PUT /api/v1/bus/<id>
    DELETE /api/v1/bus/<id>
'''

buses = [
    {
        'id': 1,
        'name': 'Bus 1'
    },
    {
        'id': 2,
        'name': 'Bus 2'
    }
]


@api_v1.route('/bus', methods=['GET'])
def get_all_buses():
    """Get all buses"""
    return jsonify(buses)


@api_v1.route('/bus/<int:bus_id>', methods=['GET'])
def get_bus_by_id(bus_id):
    """Get bus by id"""
    for bus in buses:
        if bus['id'] == bus_id:
            return bus
    return None


@api_v1.route('/bus', methods=['POST'])
def create_bus():
    """Create a new bus"""
    bus = request.get_json()
    buses.append(bus)
    return jsonify(bus)


@api_v1.route('/bus/<int:bus_id>', methods=['PUT'])
def update_bus(bus_id):
    """Update bus by id"""
    bus = request.get_json()
    for i, b in enumerate(buses):
        if b['id'] == bus_id:
            buses[i] = bus
            return jsonify(bus)
    return None


@api_v1.route('/bus/<int:bus_id>', methods=['DELETE'])
def delete_bus(bus_id):
    """Delete bus by id"""
    for i, bus in enumerate(buses):
        if bus['id'] == bus_id:
            del buses[i]
            return jsonify(buses)
    return None


'''
    Bus_Stops API
    GET /api/v1/bus_stop
    GET /api/v1/bus_stop/<id>
    POST /api/v1/bus_stop
    PUT /api/v1/bus_stop/<id>
    DELETE /api/v1/bus_stop/<id>
'''

bus_stops = [
    {
        'id': 1,
        'name': 'Bus Stop 1'
    },
    {
        'id': 2,
        'name': 'Bus Stop 2'
    }
]


@api_v1.route('/bus_stop', methods=['GET'])
def get_all_bus_stops():
    """Get all bus_stops"""
    return jsonify(bus_stops)


@api_v1.route('/bus_stop/<int:bus_stop_id>', methods=['GET'])
def get_bus_stop_by_id(bus_stop_id):
    """Get bus_stop by id"""
    for bus_stop in bus_stops:
        if bus_stop['id'] == bus_stop_id:
            return bus_stop
    return None


@api_v1.route('/bus_stop', methods=['POST'])
def create_bus_stop():
    """Create a new bus_stop"""
    bus_stop = request.get_json()
    bus_stops.append(bus_stop)
    return jsonify(bus_stop)


@api_v1.route('/bus_stop/<int:bus_stop_id>', methods=['PUT'])
def update_bus_stop(bus_stop_id):
    """Update bus_stop by id"""
    bus_stop = request.get_json()
    for i, b in enumerate(bus_stops):
        if b['id'] == bus_stop_id:
            bus_stops[i] = bus_stop
            return jsonify(bus_stop)
    return None


@api_v1.route('/bus_stop/<int:bus_stop_id>', methods=['DELETE'])
def delete_bus_stop(bus_stop_id):
    """Delete bus_stop by id"""
    for i, bus_stop in enumerate(bus_stops):
        if bus_stop['id'] == bus_stop_id:
            del bus_stops[i]
            return jsonify(bus_stops)
    return None


app.register_blueprint(api_v1)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
