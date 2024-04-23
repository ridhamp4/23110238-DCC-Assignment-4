from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL
import pandas as pd
app = Flask(__name__,static_folder='./templates')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ridham1001'
app.config['MYSQL_DB'] = 'db23110238'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("index.html")

@app.route('/purchase',methods = ["GET","POST"])
def purchase():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM purchase_details")
    purchase_whole_table = cur.fetchall()
    cur.close()
    return render_template('purchase.html', data=purchase_whole_table)

@app.route('/purchasebond',methods = ["GET","POST"])
def purchasebond():
    if request.method=='POST':
        cur = mysql.connection.cursor()
        # bond = request.args
        print(dict(request.form))
        cur.execute("SELECT * FROM purchase_details WHERE `Bond Number` = %s", (request.form["bond"],))
        purchase_bond = cur.fetchall()
        cur.close()
        return render_template('purchase.html', data=purchase_bond)
    
@app.route('/purchasereference',methods = ["GET","POST"])
def purchasereference():
    if request.method=='POST':
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM purchase_details WHERE `Reference No URN` = '{dict(request.form)['reference']}'")
        purchase_whole_table = cur.fetchall()
        cur.close()
        return render_template('purchase.html', data=purchase_whole_table)

@app.route('/purchasename',methods = ["GET","POST"])
def purchasename():
    if request.method=='POST':
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM purchase_details WHERE `Name of the Purchaser` = '{dict(request.form)['name']}'")
        purchase_name = cur.fetchall()
        cur.close()
        return render_template('purchase.html', data=purchase_name)

@app.route('/purchaseprefix',methods = ["GET","POST"])
def purchaseprefix():
    if request.method=='POST':
        cur = mysql.connection.cursor()
        prefixx = dict(request.form)['prefix']
        print(prefixx)
        cur.execute(f"SELECT * FROM purchase_details WHERE Prefix = '{prefixx}'")
        purchase_prefix = cur.fetchall()
        cur.close()
        return render_template('purchase.html', data=purchase_prefix)

@app.route('/purchasedenomination',methods = ["GET","POST"])
def purchasedenomination():
    cur = mysql.connection.cursor()
    # print(dict(request.form)['denomination'])
    denomination = dict(request.form)['denomination']
    print(denomination)
    cur.execute(f"SELECT * FROM purchase_details WHERE Denominations = {denomination}")
    purchase_prefix = cur.fetchall()
    cur.close()
    return render_template('purchase.html', data=purchase_prefix)

@app.route('/purchasebranchcode',methods = ["GET","POST"])
def purchasebranchcode():
    cur = mysql.connection.cursor()
    branch = dict(request.form)['branchcode']
    cur.execute(f"SELECT * FROM purchase_details WHERE `Issue Branch Code` = '{branch}'")
    purchase_branchcode = cur.fetchall()
    cur.close()
    return render_template('purchase.html', data=purchase_branchcode)

@app.route('/purchaseissueteller',methods = ["GET","POST"])
def purchaseissueteller():
    cur = mysql.connection.cursor()
    issueteller = dict(request.form)['issueteller']
    print(issueteller)
    cur.execute(f"SELECT * FROM purchase_details WHERE `Issue Teller` = {issueteller}")
    purchase_issueteller = cur.fetchall()
    cur.close()
    return render_template('purchase.html', data=purchase_issueteller)

@app.route('/purchaseJD',methods = ["GET","POST"])
def purchaseJD():
    cur = mysql.connection.cursor()
    JD = dict(request.form)['JD']
    print(JD)
    cur.execute(f"SELECT * FROM purchase_details WHERE `Journal Date` = '{JD}'")
    purchase_JD = cur.fetchall()
    cur.close()
    return render_template('purchase.html', data=purchase_JD)

@app.route('/purchaseDOP',methods = ["GET","POST"])
def purchaseDOP():
    cur = mysql.connection.cursor()
    DOP = dict(request.form)['DOP']
    print(DOP)
    cur.execute(f"SELECT * FROM purchase_details WHERE `Date of Purchase` = '{DOP}'")
    purchase_DOP = cur.fetchall()
    cur.close()
    return render_template('purchase.html', data=purchase_DOP)

@app.route('/purchaseDOE',methods = ["GET","POST"])
def purchaseDOE():
    cur = mysql.connection.cursor()
    DOE = dict(request.form)['DOE']
    print(DOE)
    cur.execute(f"SELECT * FROM purchase_details WHERE `Date of Expiry` = '{DOE}'")
    purchase_DOE = cur.fetchall()
    cur.close()
    return render_template('purchase.html', data=purchase_DOE)

@app.route('/Q1e2',methods = ["GET","POST"])
def Q1e2():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Purchaser`) from purchase_details")
    dropdown = cur.fetchall()
    cur.close()
    return render_template('Q1e2.html',dropdown_data=dropdown, q2 = [0,0,0,0,0])

@app.route('/Q1e2no',methods = ["GET","POST"])
def Q1e2no():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Purchaser`) from purchase_details")
    dropdown = cur.fetchall()
    cur.close()
    if request.method=='POST':
        no = dict(request.form)
        print(no)
        #2019
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2019')")
        no_of_bonds_2019 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2019')")
        try:
            money_spent_2019 = cur.fetchall()
            money_spent_2019 = int(money_spent_2019[0][0])
        except:
            money_spent_2019 = 0
        print(no_of_bonds_2019[0][0])
        cur.close()
        #2020
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2020')")
        no_of_bonds_2020 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        # no = dict(request.method)
        cur.execute(f"select sum(Denominations) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2020')")
        try:
            money_spent_2020 = cur.fetchall()
            money_spent_2020 = int(money_spent_2020[0][0])
        except:
            money_spent_2020 = 0
        cur.close()
        #2021
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2021')")
        no_of_bonds_2021 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2021')")
        try:
            money_spent_2021 = cur.fetchall()
            money_spent_2021 = int(money_spent_2021[0][0])
        except:
            money_spent_2021 = 0
        cur.close()
        #2022
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2022')")
        no_of_bonds_2022 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2022')")
        try:
            money_spent_2022 = cur.fetchall()
            money_spent_2022 = int(money_spent_2022[0][0])
        except:
            money_spent_2022 = 0
        cur.close()
        #2023
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2023')")
        no_of_bonds_2023 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from purchase_details where (`Name of the Purchaser` = '{no['no']}') and (right(`Journal Date`,4)= '2023')")
        try:
            money_spent_2023 = cur.fetchall()
            money_spent_2023 = int(money_spent_2023[0][0])
        except:
            money_spent_2023 = 0
        cur.close()
        return render_template('Q1e2.html',q2=[no['no'],money_spent_2019,money_spent_2020,money_spent_2021,money_spent_2022,money_spent_2023, int(no_of_bonds_2019[0][0]),int(no_of_bonds_2020[0][0]),int(no_of_bonds_2021[0][0]),(no_of_bonds_2022[0][0]),(no_of_bonds_2023[0][0])], dropdown_data = dropdown)

# @app.route('/Q1e5',methods = ["GET","POST"])
# def Q1e5():
#     cur = mysql.connection.cursor()
#     cur.execute("select distinct(`Name of the Purchaser`) from purchase_details")
#     dropdown = cur.fetchall()
#     cur.close()
#     return render_template('Q1e5.html',dropdown_data=dropdown)






@app.route('/redemption',methods = ["GET","POST"])
def redemption():
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM redemption_details")
    redemption_whole_table = cur.fetchall()
    cur.close()
    return render_template('redemption.html', data=redemption_whole_table)

@app.route('/redemptionbond',methods = ["GET","POST"])
def redemptionbond():
    if request.method=='POST':
        cur = mysql.connection.cursor()
        # bond = request.args
        print(dict(request.form))
        cur.execute("SELECT * FROM redemption_details WHERE `Bond Number` = %s", (request.form["bond"],))
        redemption_bond = cur.fetchall()
        cur.close()
        return render_template('redemption.html', data=redemption_bond)

@app.route('/redemptionname',methods = ["GET","POST"])
def redemptionname():
    if request.method=='POST':
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM redemption_details WHERE `Name of the Political Party` = '{dict(request.form)['name']}'")
        redemption_name = cur.fetchall()
        cur.close()
        return render_template('redemption.html', data=redemption_name)

@app.route('/redemptionprefix',methods = ["GET","POST"])
def redemptionprefix():
    if request.method=='POST':
        cur = mysql.connection.cursor()
        prefixx = dict(request.form)['prefix']
        print(prefixx)
        cur.execute(f"SELECT * FROM redemption_details WHERE Prefix = '{prefixx}'")
        redemption_prefix = cur.fetchall()
        cur.close()
        return render_template('purchase.html', data=redemption_prefix)

@app.route('/redemptiondenomination',methods = ["GET","POST"])
def redemptiondenomination():
    cur = mysql.connection.cursor()
    # print(dict(request.form)['denomination'])
    denomination = dict(request.form)['denomination']
    print(denomination)
    cur.execute(f"SELECT * FROM redemption_details WHERE Denominations = {denomination}")
    redemption_denomination = cur.fetchall()
    cur.close()
    return render_template('redemption.html', data=redemption_denomination)

@app.route('/redemptionbranchcode',methods = ["GET","POST"])
def redemptionbranchcode():
    cur = mysql.connection.cursor()
    branch = dict(request.form)['branchcode']
    cur.execute(f"SELECT * FROM redemption_details WHERE `Pay Branch Code` = '{branch}'")
    redemption_branchcode = cur.fetchall()
    cur.close()
    return render_template('redemption.html', data=redemption_branchcode)

@app.route('/redemptionpayteller',methods = ["GET","POST"])
def redemptionpayteller():
    cur = mysql.connection.cursor()
    payteller = dict(request.form)['payteller']
    print(payteller)
    cur.execute(f"SELECT * FROM redemption_details WHERE `Pay Teller` = '{payteller}'")
    purchase_payteller = cur.fetchall()
    cur.close()
    return render_template('redemption.html', data=purchase_payteller)

@app.route('/redemptionacname',methods = ["GET","POST"])
def redemptionacname():
    cur = mysql.connection.cursor()
    acname = dict(request.form)['acname']
    print(acname)
    cur.execute(f"SELECT * FROM redemption_details WHERE `Account no. of Political Party` = '{acname}'")
    redemption_acname = cur.fetchall()
    cur.close()
    return render_template('redemption.html', data=redemption_acname)

@app.route('/redemptionDOE',methods = ["GET","POST"])
def redemptionDOE():
    cur = mysql.connection.cursor()
    DOE = dict(request.form)['DOE']
    print(DOE)
    cur.execute(f"SELECT * FROM redemption_details WHERE `Date of Encashment` = '{DOE}'")
    redemption_DOE = cur.fetchall()
    cur.close()
    return render_template('redemption.html', data=redemption_DOE)

@app.route('/Q1e3',methods = ["GET","POST"])
def Q1e3():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Political Party`) from redemption_details")
    dropdown = cur.fetchall()
    cur.close()
    return render_template('Q1e3.html',dropdown_data=dropdown, q2 = [0,0,0,0,0])

@app.route('/Q1e3no',methods = ["GET","POST"])
def Q1e3no():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Political Party`) from redemption_details")
    dropdown = cur.fetchall()
    cur.close()
    if request.method=='POST':
        no = dict(request.form)
        print(no)
        #2019
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2019')")
        no_of_bonds_2019 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2019')")
        try:
            money_spent_2019 = cur.fetchall()
            money_spent_2019 = int(money_spent_2019[0][0])
        except:
            money_spent_2019 = 0
        print(no_of_bonds_2019[0][0])
        cur.close()
        #2020
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2020')")
        no_of_bonds_2020 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2020')")
        try:
            money_spent_2020 = cur.fetchall()
            money_spent_2020 = int(money_spent_2020[0][0])
        except:
            money_spent_2020 = 0
        print(no_of_bonds_2020[0][0])
        cur.close()
        #2021
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2021')")
        no_of_bonds_2021 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2021')")
        try:
            money_spent_2021 = cur.fetchall()
            money_spent_2021 = int(money_spent_2021[0][0])
        except:
            money_spent_2021 = 0
        print(no_of_bonds_2021[0][0])
        cur.close()
        #2022
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2022')")
        no_of_bonds_2022 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2022')")
        try:
            money_spent_2022 = cur.fetchall()
            money_spent_2022 = int(money_spent_2022[0][0])
        except:
            money_spent_2022 = 0
        print(no_of_bonds_2022[0][0])
        cur.close()
        #2023
        cur = mysql.connection.cursor()
        cur.execute(f"select distinct count(*) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2023')")
        no_of_bonds_2023 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute(f"select sum(Denominations) from redemption_details where (`Name of the Political Party` = '{no['no']}') and (right(`Date of Encashment`,4)= '2023')")
        try:
            money_spent_2023 = cur.fetchall()
            money_spent_2023 = int(money_spent_2023[0][0])
        except:
            money_spent_2023 = 0
        print(no_of_bonds_2023[0][0])
        cur.close()
        return render_template('Q1e3.html',q2=[no['no'],money_spent_2019,money_spent_2020,money_spent_2021,money_spent_2022,money_spent_2023, int(no_of_bonds_2019[0][0]),int(no_of_bonds_2020[0][0]),int(no_of_bonds_2021[0][0]),(no_of_bonds_2022[0][0]),(no_of_bonds_2023[0][0])], dropdown_data = dropdown)

@app.route('/Q1e4',methods = ["GET","POST"])
def Q1e4():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Political Party`) from redemption_details")
    dropdown = cur.fetchall()
    cur.close()
    return render_template('Q1e4.html',dropdown_data=dropdown)

@app.route('/Q1e4no',methods = ["GET","POST"])
def Q1e4no():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Political Party`) from redemption_details")
    dropdown = cur.fetchall()
    cur.close()
    if request.method=='POST':
        cur = mysql.connection.cursor()
        no = dict(request.form)
        cur.execute(f"SELECT pd.`Name of the Purchaser`, SUM(pd.Denominations) AS total_denomination FROM purchase_redemption_details AS pd WHERE pd.`Name of the Political Party` = '{no['no']}' GROUP BY pd.`Name of the Purchaser`")
        table4 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        no = dict(request.form)
        cur.execute(f"SELECT SUM(pd.Denominations) AS total_denomination FROM purchase_redemption_details AS pd WHERE pd.`Name of the Political Party` = '{no['no']}'")
        total = cur.fetchall()
        cur.close()
        return render_template('Q1e4.html', partyname = no['no'], amt = total[0][0], dropdown_data = dropdown, tableq4 = table4)

@app.route('/Q1e5',methods = ["GET","POST"])
def Q1e5():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Purchaser`) from purchase_details")
    dropdown = cur.fetchall()
    cur.close()
    return render_template('Q1e5.html',dropdown_data=dropdown,)

@app.route('/Q1e5no',methods = ["GET","POST"])
def Q1e5no():
    cur = mysql.connection.cursor()
    cur.execute("select distinct(`Name of the Purchaser`) from purchase_details")
    dropdown = cur.fetchall()
    cur.close()
    if request.method=='POST':
        cur = mysql.connection.cursor()
        no = dict(request.form)
        cur.execute(f"SELECT purchaser_group.`Name of the Political Party`, SUM(purchaser_group.total_denomination) AS total_denomination FROM (SELECT pd.`Name of the Political Party`, pd.`Name of the Purchaser`, SUM(pd.Denominations) AS total_denomination FROM purchase_redemption_details AS pd WHERE pd.`Name of the Purchaser` = '{no['no']}' GROUP BY pd.`Name of the Political Party`, pd.`Name of the Purchaser`) AS purchaser_group GROUP BY purchaser_group.`Name of the Political Party`")
        table4 = cur.fetchall()
        cur.close()
        cur = mysql.connection.cursor()
        no = dict(request.form)
        cur.execute(f"SELECT SUM(Denominations) FROM purchase_details WHERE (`Name of the Purchaser`= '{no['no']}') AND (Status = 'Paid')")
        total = cur.fetchall()
        cur.close()
        return render_template('Q1e5.html', partyname = no['no'], amt = total[0][0], dropdown_data = dropdown, tableq4 = table4)
    
@app.route('/Q1e6',methods = ["GET","POST"])
def Q1e6():
    cur = mysql.connection.cursor()
    cur.execute("SELECT pd.`Name of the Political Party`, SUM(pd.Denominations) AS total_denomination FROM purchase_redemption_details AS pd GROUP BY pd.`Name of the Political Party`")
    dropdown = cur.fetchall()
    # dropdown = dropdown[0]
    cur.close()
    # print(dropdown)
    label_party = []
    donated = []
    for i in range(len(dropdown)):
        label_party.append(dropdown[i][0])
        donated.append(int(dropdown[i][1]))
    print(label_party)
    return render_template('Q1e6.html',dropdown_data=[label_party,donated])

@app.route('/a_0', methods = ["POST", "GET"])
def a_0():
    if request.method == "GET":
        print("HI")
        print(request.method)
        # print(request.form["box"])  

        print("TEST")

        cursor = mysql.connection.cursor()
        cursor.execute("select * from purchase_details)", (request.form["box"],))

        data = cursor.fetchone()

        cursor.close()

    return render_template("index.html", a_0_data = data) 

@app.route('/a_1', methods = ["POST", "GET"])
def a_1():
    if request.method == "POST":
        print("HI")
        print(request.method)
        print(request.form["box"])  

        print("TEST")

        cursor = mysql.connection.cursor()
        cursor.execute("select * from genre where movie_id like (select id from movie where title like %s)", (request.form["box"],))

        data = cursor.fetchone()

        cursor.close()

    return render_template("index.html", a_1_data = data) 


@app.route('/a_2', methods = ["POST", "GET"])
def a_2():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("select title from movie join genre on movie.id = genre.movie_id where genre = %s limit 10", (request.form["box"],))

        data = cursor.fetchall()

        cursor.close()
        
    return render_template("index.html", a_2_data = data) 


@app.route('/a_3', methods = ["POST", "GET"])
def a_3():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("select title from movie where id in (select movie_id from director_mapping where name_id in (select id from `names` where `name` like %s)) limit 5;", (request.form["box"],))

        data = cursor.fetchall()

        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", a_3_data = [["Not Found !!!"]]) 

    return render_template("index.html", a_3_data = data) 



if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 
