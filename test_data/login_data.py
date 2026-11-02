LOGIN_TEST_DATA = [
    {
        "username": "standard_user",
        "password": "secret_sauce",
        "expected": "success",
    },
    {
        "username": "standard_user",
        "password": "wrong_password",
        "expected": "failure",
    },
    {
        "username": "wrong_user",
        "password": "wrong_password",
        "expected": "failure",
    },
]


