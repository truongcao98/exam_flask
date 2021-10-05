from src import app


@app.route('/')
@app.route('/add', methods=['POST'])
def add():
    return "successful success"


@app.route('/edit', methods=['POST'])
def edit():
    return "successful success"


@app.route('/delete', methods=['POST'])
def delete():
    return 'successful delete'


@app.route('/get-product-infor', methods=['GET'])
def get_product_infor():
    return "successful get product infor"


@app.route('/get_product_list', methods=['GET'])
def get_product_list():
    return 'successful get product list'
