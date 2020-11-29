from alaska_crud import AlaskaCRUD


def test_get_all_bears():
    alaska = AlaskaCRUD()
    number_of_bears = 5
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}
    for b in range(number_of_bears):
        resp_post = alaska.create_bear(data)
        print(f"Created bear id is {resp_post.text}")
        assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    resp_get_all = alaska.get_all_bears()
    assert resp_get_all.status_code == 200, f"Unexpected result: was not able to GET all bears."
    assert len(resp_get_all.json()) >= number_of_bears, f"Unexpected result: not enough bears got."


def test_get_bear():
    alaska = AlaskaCRUD()
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    resp_get = alaska.get_bear_by_id(resp_post.text)
    assert resp_get.status_code == 200, f"Unexpected result: was not able to GET bear with id '{resp_post.text}'."
    assert resp_get.json()['bear_id'] == int(resp_post.text), f"Returned bear_id is different."


def test_get_bear_with_wrong_id():
    alaska = AlaskaCRUD()
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    wrong_id = int(resp_post.text) + 1
    resp_get = alaska.get_bear_by_id(wrong_id)
    assert resp_get.status_code != 200, f"Unexpected result: was able to GET bear with wrong id '{wrong_id}'."


def test_get_info():
    alaska = AlaskaCRUD()
    resp_get = alaska.get_info()
    assert resp_get.status_code == 200, f"Unexpected result: was not able to GET info."

    matching_list = ['CRUD', 'POST', 'GET', 'PUT', 'DELETE', 'bear', 'id', 'bear_type', 'bear_name', 'bear_age',
                     'Example', 'Available types']
    errors = []
    assert len(resp_get.text) > 0, "There was nothing in /info."
    for match in matching_list:
        try:
            assert resp_get.text.find(match) >= 0, f"'{match}' was not found within /info."
        except AssertionError as e:
            errors.append(e)

    assert len(errors) is 0, errors
