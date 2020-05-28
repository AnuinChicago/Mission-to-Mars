from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

#conn = 'mongodb://localhost:27017'
#client = Pymongo.MongoClient(conn)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# set database (used this first time to create db)
#db=client.mars_db

@app.route('/')
def index():
    mars_results = mongo.db.mars_result.find_one()
    return render_template('index.html', mars_results=mars_results)


@app.route('/scrape')
def scrape():
    mars_results =mongo.db.mars_result
    mars_data = scrape_mars.scrape()
    #db.mars_results.insert_one(mars_data)
    mars_results.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
