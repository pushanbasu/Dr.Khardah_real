from flask import Flask, render_template,request
import pymongo

app=Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    client = pymongo.MongoClient("mongodb+srv://pushan:drkhardahreal@drkhardahcluster.obroa.mongodb.net/Dr_Khardah_db?retryWrites=true&w=majority")
    db = client['Dr_Khardah_db']
    collection = db['Dr_Khardah_table']


    if (request.method=='POST'):
        specialization=request.form['specialization']
        day=request.form['day']

        #r=collection.find({})
        r=collection.find({'spl':specialization,'day':day})

        anyday=collection.find({'spl':specialization, 'day':day})
        n=collection.count_documents({'spl':specialization,'day':day})
        suggestions_on_no_match=collection.find({'spl':specialization, 'day':'na'})

    if (n>0 and day !='na'):
        return render_template('result.html', result=r, n=n)
    elif (specialization=='select_the_specialization' or day == 'choose_a_day'):
        return render_template('Error.html')
    elif (specialization!='select_the_specialization' and day == 'na'):
        return render_template('any_day.html', anyday=anyday, s=specialization)
    elif (n==0):
        return render_template('suggestion_on_null.html',n=n,suggestions=suggestions_on_no_match, s=specialization)




if __name__=="__main__":
    app.run()



