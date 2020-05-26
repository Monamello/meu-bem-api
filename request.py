import requests
import json
from unicodedata import normalize
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads
from bson import json_util


def request_map():
    data = '{"documents":[{"id":0},{"id":1}],"categories":[{"id":1,"subcategories":[]},{"id":2,"subcategories":[]},{"id":3,"subcategories":[]},{"id":5,"subcategories":[]},{"id":6,"subcategories":[]},{"id":7,"subcategories":[]},{"id":9,"subcategories":[]}],"places":[{"id":0},{"id":76},{"id":105},{"id":97},{"id":53},{"id":140},{"id":35},{"id":106},{"id":166},{"id":107},{"id":70},{"id":13},{"id":66},{"id":54},{"id":111},{"id":75},{"id":15},{"id":64},{"id":56},{"id":109},{"id":55},{"id":22},{"id":24},{"id":110},{"id":71},{"id":40},{"id":34},{"id":73},{"id":57},{"id":108},{"id":98},{"id":112},{"id":91},{"id":113},{"id":74},{"id":94},{"id":85},{"id":36},{"id":51},{"id":88},{"id":58},{"id":159},{"id":160},{"id":161},{"id":162},{"id":163},{"id":25},{"id":72},{"id":14},{"id":59},{"id":31},{"id":82},{"id":95},{"id":96},{"id":115},{"id":99},{"id":141},{"id":89},{"id":93},{"id":26},{"id":39},{"id":50},{"id":19},{"id":47},{"id":30},{"id":142},{"id":116},{"id":68},{"id":118},{"id":77},{"id":117},{"id":100},{"id":119},{"id":120},{"id":122},{"id":123},{"id":167},{"id":124},{"id":20},{"id":127},{"id":128},{"id":129},{"id":130},{"id":121},{"id":131},{"id":164},{"id":132},{"id":155},{"id":125},{"id":135},{"id":136},{"id":137},{"id":133},{"id":134},{"id":86},{"id":139},{"id":168},{"id":69},{"id":138},{"id":165},{"id":18},{"id":29},{"id":43},{"id":32},{"id":49},{"id":38},{"id":44},{"id":21},{"id":27},{"id":48},{"id":60},{"id":46},{"id":45},{"id":37},{"id":42},{"id":90},{"id":78},{"id":52},{"id":103},{"id":41},{"id":104},{"id":157},{"id":23},{"id":143},{"id":102},{"id":87},{"id":81},{"id":65},{"id":146},{"id":84},{"id":147},{"id":148},{"id":33},{"id":63},{"id":67},{"id":79},{"id":169},{"id":144},{"id":145},{"id":62},{"id":126},{"id":61},{"id":101},{"id":149},{"id":150},{"id":83},{"id":16},{"id":17},{"id":28},{"id":151},{"id":152},{"id":158},{"id":153},{"id":154},{"id":80},{"id":114}],"status":[{"id":6},{"id":1},{"id":7},{"id":3},{"id":2},{"id":5},{"id":4}],"communityAssets":[],"enterprises":[{"id":1}],"organs":[{"id":1}],"programs":[],"sectors":[{"id":1816},{"id":142},{"id":1561},{"id":156},{"id":1163},{"id":319},{"id":101},{"id":1651},{"id":1323},{"id":486},{"id":1670},{"id":1673},{"id":1672},{"id":1945},{"id":1590},{"id":1583},{"id":1568},{"id":1566},{"id":991}],"classifications":[{"id":7},{"id":5},{"id":4},{"id":15},{"id":6},{"id":8},{"id":13}],"contracteds":[],"period":{"initialDate":1451613600000,"finalDate":1609383600000}}'

    headers = {'Content-type': 'application/json;charset=UTF-8'}

    request = requests.post(
        'http://obrasgov.pmf.sc.gov.br/obras-gov-backend/source/obrasgov/contract/list', data=data, headers=headers)

    save_json(request)


def save_json(request):
    with open('request_json.json', 'w') as f:
        json.dump(json.loads(request.content), f, indent=4)
    save_in_db()


def save_in_db():
    client = MongoClient()
    db = client.obras_municipais
    bens = db.bens

    with open('request_json.json') as f:
        obras = json.load(f)

    bens.insert_many(obras).inserted_ids


def list_items_db():
    client = MongoClient()
    db = client.obras_municipais
    bens = db.bens.find()
    json_bens = dumps(list(bens), default=json_util.default)

    return json_bens


def list_collections_from_mongo():
    client = MongoClient()
    db = client.obras_municipais
    collections = db.list_collections()

    return collections