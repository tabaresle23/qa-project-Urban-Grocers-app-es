import sender_stand_request
import data

def get_new_user_token():
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    return resp_user.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def negative_assert_code_400(kit_body):
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert resp_kit.status_code == 400
    assert resp_kit.json()["name"] == kit_body["name"]

def positive_assert(kit_body):
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert resp_kit.status_code == 201
    assert resp_kit.json()["name"] == kit_body["name"]

# Prueba 1 El número permitido de caracteres (1):
def test_create_kit_1_char_name_success():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)
#Prueba 2 El numero permitido de caracteres (511)
def test_create_kit_511_char_name_success():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)
#Prueba 3 El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_char_name_negative(negative_assert=None):
    kit_body = get_kit_body("")
    negative_assert(kit_body)
#Prueba 4 El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_char_name_negative(negative_assert=None):
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)
#Prueba 5 Se permiten caracteres especiales
def test_create_kit_special_char_name_success():
    kit_body = get_kit_body("!№%@*")
    positive_assert(kit_body)
#Prueba 6 Se permiten espacios
def test_create_kit_space_char_name_success():
    kit_body = get_kit_body("A Aaa")
    positive_assert(kit_body)
#Prueba 7 Se permiten números
def test_create_kit_123_char_name_success():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)
#Prueba 8 El parámetro no se pasa en la solicitud
def test_create_kit_no_name_char_name_negative(negative_assert=None):
    kit_body = get_kit_body("no name")
    negative_assert(kit_body)
#Prueba 9 Se ha pasa un tipo de parámetro diferente (número)
def test_create_kit_number_name_negative(negative_assert=None):
    kit_body = get_kit_body("number")
    negative_assert(kit_body)