from alaska_crud import AlaskaCRUD


def test_put_bear_simple():
    errors = []
    alaska = AlaskaCRUD()
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}
    new_data = {"bear_type": "BROWN",
                "bear_name": "alex",
                "bear_age": 22}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    resp_put = alaska.update_bear(resp_post.text, new_data)
    print(resp_put.text)
    assert resp_put.status_code == 200,\
        f"Unexpected result: was not able to PUT with new data {new_data}."

    resp_get = alaska.get_bear_by_id(resp_post.text)
    resp_json = resp_get.json()
    for key in new_data:
        try:
            assert new_data[key] == resp_json[key], f"Wrong data value for '{key}'. " \
                                                    f"Expected is '{new_data[key]}'. Actual is '{resp_json[key]}'"
        except AssertionError as e:
            errors.append(e)

    assert len(errors) is 0, errors


def test_put_bear_unavailable_type():
    alaska = AlaskaCRUD()
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}
    new_data = {"bear_type": "GREEN",
                "bear_name": "alex",
                "bear_age": 22}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    resp_put = alaska.update_bear(resp_post.text, new_data)
    assert resp_put.status_code != 200, f"Unexpected result: was able to PUT with unsupported bear type."
