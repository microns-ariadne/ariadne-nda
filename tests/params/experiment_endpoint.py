params = {
    'test_get': [
        {
            'uri': '/api/v0.1/experiment/',
            'statuscode': 200,
            'resp': []
        }
    ],
    'test_post': [
        {
            'uri': '/api/v0.1/experiment/',
            'req': {
                'name': 'ECS_test_9',
                'description': 'This is a test'
            },
            'statuscode': 201,
            'resp': {
                'name': 'ECS_test_9',
                'description': 'This is a test'
            }
        },
        {
            'uri': '/api/v0.1/experiment/',
            'req': {
                'description': 'This is a test'
            },
            'statuscode': 400,
            'resp': {
                'message': {'name': ['Missing data for required field.']}
            }
        }
    ]
}
