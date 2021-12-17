import numpy
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import pickle

# creating database

pickle_file = open('model.pkl', 'rb')
model = pickle.load(pickle_file)

app = Flask(__name__)

# Initialize the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:manebuchu@localhost:5432/Bigmart'
app.config['SQLALCHEMY_ECHO'] = False  # set true to see all db activities in log
db = SQLAlchemy(app)


class Bigmart(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # unique id to track the entries
    productType = db.Column(db.String(60))
    OutletSize = db.Column(db.String(60))
    LocationType = db.Column(db.String(60))
    OutletType = db.Column(db.String(60))
    predict = db.Column(db.String(60))

    def __init__(self, productType, OutletSize, LocationType, OutletType, predictResp):
        self.productType = productType
        self.OutletSize = OutletSize
        self.LocationType = LocationType
        self.OutletType = OutletType
        self.predict = predictResp


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "ok", 200
    return 'index.html'  # we have to add streamlit link over here\


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        params = request.values
        productType = params.get('ProductType')
        locationType = params.get('LocationType')
        outletSize = params.get('OutletSize')
        outletType = params.get('OutletType')
        predictResponse = model.predict([[productType, locationType, outletSize, outletType]])
        bigmart = Bigmart(productType=productType, LocationType=locationType, OutletSize=outletSize,
                          OutletType=outletType, predictResp=numpy.array_str(predictResponse))
        db.create_all()
        db.session.add(bigmart)
        db.session.commit()
        return numpy.array_str(predictResponse)




if __name__ == '__main__':
    app.run(debug=True)
