from alaska_crud import AlaskaCRUD


def test_post_bear_simple():
    alaska = AlaskaCRUD()
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."


def test_post_bear_available_types():
    errors = []
    alaska = AlaskaCRUD()
    available_types = ['POLAR', 'BLACK', 'BROWN', 'GUMMY']
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}

    # post available types
    created_bear_ids = []
    for bear_type in available_types:
        data['bear_type'] = bear_type
        resp_post = alaska.create_bear(data)
        print(f"Created bear id is {resp_post.text}")
        try:
            assert resp_post.status_code == 200,\
                f"Unexpected result: was not able to POST with available bear type '{bear_type}'."
        except AssertionError as e:
            errors.append(e)

    # get available types
    for index, bear_id in enumerate(created_bear_ids):
        resp_get = alaska.get_bear_by_id(bear_id)
        try:
            assert resp_get.status_code == 200, f"Unexpected result: was not able to POST with data {data}."
            resp_json = resp_get.json()
            assert resp_json is None, f"Unexpected result: POST json is None."
            assert resp_json['bear_id'] == int(bear_id),\
                f"Could not get bear with id {bear_id} with type {available_types[index]}"
        except AssertionError as e:
            errors.append(e)

    assert len(errors) is 0, errors


def test_post_bear_unavailable_type():
    alaska = AlaskaCRUD()
    data = {"bear_type": "GREEN",
            "bear_name": "mikhail",
            "bear_age": 17.5}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code != 200, f"Unexpected result: was able to POST with unsupported bear type."
