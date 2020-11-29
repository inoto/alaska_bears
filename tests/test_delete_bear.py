from alaska_crud import AlaskaCRUD


def test_delete_all_bears():
    alaska = AlaskaCRUD()
    number_of_bears = 5
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}
    for b in range(number_of_bears):
        resp_post = alaska.create_bear(data)
        print(f"Created bear id is {resp_post.text}")
        assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    resp_delete_all = alaska.delete_all_bears()
    assert resp_delete_all.status_code == 200, f"Unexpected result: was not able to DELETE all bears."

    resp_get_all = alaska.get_all_bears()
    assert resp_get_all.status_code == 200, f"Unexpected result: was not able to GET all bears."
    assert len(resp_get_all.json()) is 0, f"Unexpected result: not enough bears got."


def test_delete_bear():
    alaska = AlaskaCRUD()
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    resp_get = alaska.delete_bear_by_id(resp_post.text)
    assert resp_get.status_code == 200, f"Unexpected result: was not able to DELETE bear with id '{resp_post.text}'."

    resp_get = alaska.get_bear_by_id(resp_post.text)
    assert resp_get.status_code != 200, f"Unexpected result: was able to GET bear with id '{resp_post.text}'."


def test_delete_bear_with_wrong_id():
    alaska = AlaskaCRUD()
    data = {"bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5}

    resp_post = alaska.create_bear(data)
    print(f"Created bear id is {resp_post.text}")
    assert resp_post.status_code == 200, f"Unexpected result: was not able to POST with data {data}."

    wrong_id = int(resp_post.text) + 1
    resp_get = alaska.delete_bear_by_id(wrong_id)
    assert resp_get.status_code != 200, f"Unexpected result: was able to DELETE bear with wrong id '{wrong_id}'."
