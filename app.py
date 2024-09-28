from flask import Flask,redirect, render_template, request, url_for, jsonify
import sqlite3 

app = Flask(__name__)

DATABASE = 'master.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()




@app.route('/ship_entry_data', methods=['POST'])
def ship_entry_data():
    PONO = request.form['PONO']
    indentor = request.form['indentor']
    suppliername = request.form['suppliername']
    origin = request.form['origin']
    confirmdate = request.form['confirmdate']
    materialname = request.form['materialname']
    materialqty = request.form['quantity']
    materialprice = request.form['price']
    materialname2 = request.form.get('materialname2','-')
    materialqty2 = request.form['quantity2']
    materialprice2 = request.form['price2']
    materialname3 = request.form.get('materialname3','-')
    materialqty3 = request.form['quantity3']
    materialprice3 = request.form['price3']
    contractsalesno = request.form['contractsalesno']
    contractsaledate = request.form['contractsaledate']
    totalquantity = request.form['totalquantity']
    totalprice = request.form['totalprice']
    lme1 = request.form['lme1']
    lmepercent1 = request.form['lmepercent1']
    lme2 = request.form['lme2']
    lmepercent2 = request.form['lmepercent2']
    lme3 = request.form['lme3']
    lmepercent3 = request.form['lmepercent3']
    paymentterms = request.form['paymentterms']

    status = "Booked"
    advance = (int(paymentterms)/100)*float(totalprice)
    pending = float(totalprice)-int(advance)
    # ClearanceData = 0
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO shipentry VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (PONO, indentor, suppliername, origin, confirmdate, materialname,materialqty,materialprice,materialname2, materialqty2,materialprice2,materialname3,materialqty3,materialprice3,
                      contractsalesno, contractsaledate,totalquantity, totalprice, lme1, lmepercent1,lme2, lmepercent2, lme3, lmepercent3, paymentterms,status,advance,pending))

    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)

@app.route('/update_ship_entry_data', methods=['POST'])
def update_ship_entry_data():
    PONO = request.form['PONO']
    indentor = request.form['indentor']
    suppliername = request.form['suppliername']
    origin = request.form['origin']
    confirmdate = request.form['confirmdate']
    materialname = request.form.get('materialname')
    materialqty = request.form['quantity']
    materialprice = request.form['price']
    materialname2 = request.form.get('materialname2','-')
    materialqty2 = request.form['quantity2']
    materialprice2 = request.form['price2']
    materialname3 = request.form.get('materialname3','-')
    materialqty3 = request.form['quantity3']
    materialprice3 = request.form['price3']
    contractsalesno = request.form['contractsalesno']
    contractsaledate = request.form['contractsaledate']
    totalquantity = request.form['totalquantity']
    totalprice = request.form['totalprice']
    lme1 = request.form['lme1']
    lmepercent1 = request.form['lmepercent1']
    lme2 = request.form['lme2']
    lmepercent2 = request.form['lmepercent2']
    lme3 = request.form['lme3']
    lmepercent3 = request.form['lmepercent3']
    paymentterms = request.form['paymentterms']

    status = "Booked"
    advance = (int(paymentterms)/100)*float(totalprice)
    pending = float(totalprice)-int(advance)
    # ClearanceData = 0
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("UPDATE shipentry SET indentor=?, suppliername=?, origin=?, confirmationdate=?, materialname=?, materialqty=?, materialprice=?, materialname2=?, materialqty2=?, materialprice2=?,materialname3=?, materialqty3=?, materialprice3=?,contractsalesno=?, contractsalesdate=?, TotalQuantity=?,price=?, lme1=?, lmepercent1=?,lme2=?, lmepercent2=?,lme3=?, lmepercent3=?, paymentterms=?, status=?, advance=?, pending=? WHERE PONO=?", (indentor, suppliername, origin, confirmdate,materialname,materialqty,materialprice,materialname2,materialqty2,materialprice2,materialname3,materialqty3,materialprice3,
                      contractsalesno, contractsaledate,totalquantity,totalprice, lme1, lmepercent1, lme2,lmepercent2, lme3,lmepercent3,paymentterms,status,advance,pending,PONO))

    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)


@app.route('/ad_pay', methods=['post'])
def ad_pay():
    PONO = request.form['PONO']
    adpayamt = request.form['pendingAmount']
    adpaydate = request.form['adpaydate']
    CoSN = request.form['CSN']
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO adpay VALUES(?,?,?,?)", (PONO,adpayamt, adpaydate,CoSN))
    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)

@app.route('/ship_doc_data', methods=['post'])
def ship_doc_data():
    pono = request.form['pono']
    invno = request.form['invno']
    invdate = request.form['invdate']
    invquantity = request.form['invquantity']
    invamt = request.form['invamt']
    pendingamt = request.form['pendingamt']
    containerno = request.form['containerno']
    shippingline = request.form['shippingline']
    blno = request.form['blno']
    eta = request.form['eta']
    etd = request.form['etd']
    detfreeday = request.form['detfreeday']
    detfreetill = request.form['detfreetill']
    transtime = request.form['transtime']
    portarr = request.form['portarr']
    portship = request.form['portship']
    asscha = request.form['asscha']
    status = 'Shipped'
    material = request.form['materialname']
    CoSN = request.form['CSN']
    ClearanceData = "NA"
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO shipdoc VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pono,invno, invdate, invquantity, invamt, pendingamt, containerno,
                      shippingline, blno, eta, etd, detfreeday, detfreetill, transtime, portarr, portship, asscha,status,material,CoSN,ClearanceData))
    my_cursor.execute("UPDATE shipentry SET pending = ? WHERE PONO = ?", (pendingamt,pono))


    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)

@app.route('/port_clear_data', methods=['post'])
def port_clear_data():
    PONO = request.form['pono']
    blno = request.form['blno']
    shipexp = request.form['shipexp']
    chaexp = request.form['chaexp']
    dutypaid = request.form['dutypaid']
    missexp = request.form['missexp']
    portexp = request.form['portexp']
    transport = request.form['transport']
    instampduty = request.form['instampduty']
    detention = request.form['detention']
    bankchg = request.form['bankchg']
    loadedprice = request.form['loadedprice']
    ClearanceDate = request.form.get('ClearanceDate')
    invinr = request.form['invinr']

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO portclear VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (PONO,blno,shipexp, chaexp, dutypaid, missexp, portexp, transport,
                      instampduty, detention, bankchg, loadedprice, ClearanceDate,invinr))
    my_cursor.execute("UPDATE shipdoc SET ClearanceDate = ? WHERE blno = ?",(ClearanceDate, blno))    

    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)

@app.route('/update_status', methods=['POST'])
def update_status():
    BLNO = request.form.get('BLNO')
    new_status = request.form.get('new_status')

    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE shipdoc SET status = ? WHERE BLNO = ?', (new_status, BLNO))
    abc = cursor.execute("SELECT se.PONO FROM shipentry se JOIN (SELECT sd.PONO, SUM(sd.invoicequantity) AS total_invoice_quantity FROM shipdoc sd WHERE sd.status = 'Cleared' GROUP BY sd.PONO) subquery ON se.PONO = subquery.PONO WHERE se.TotalQuantity = subquery.total_invoice_quantity").fetchall()
    # print(abc)
    
    pono_list = [item[0] for item in abc]
    # print(pono_list)
    # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    for pono_value in pono_list:
        cursor.execute("UPDATE shipentry SET status = 'Cleared' WHERE PONO = ?", (pono_value,))
    # cursor.execute('UPDATE shipentry SET status = ? WHERE PONO = ?', (new_status, shipment_id))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

def truncate_on_double_zero(number):
    # Convert the number to string
    num_str = str(number)
    
    # Split into integer and fractional parts
    if '.' in num_str:
        integer_part, fractional_part = num_str.split('.')
    else:
        return number  # No fractional part to process
    
    # Find the index of the first occurrence of "00"
    zero_index = fractional_part.find('00')
    
    # Truncate the fractional part if "00" is found
    if zero_index != -1:
        fractional_part = fractional_part[:zero_index]
    
    # Recombine the parts into a new number string
    if fractional_part:  # If there's still a fractional part left
        truncated_num_str = f"{integer_part}.{fractional_part}"
    else:
        truncated_num_str = integer_part  # Only the integer part remains

    # Convert back to float if possible
    truncated_number = float(truncated_num_str)
    
    return truncated_number

@app.route('/fetch_pending_amount', methods=['POST'])
def fetch_pending_amount():
    CSN = request.form.get('CSN')

    # Query the database to get the pending amount for the provided PONO
    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()
    payment = truncate_on_double_zero(cursor.execute('select advance from shipentry where contractsalesno=?',(CSN,)).fetchone()[0])
    PONO = cursor.execute('select PONO from shipentry where contractsalesno=?',(CSN,)).fetchone()[0]

    if payment:
        # Convert the tuple to a dictionary for JSON response
        return {'pendingAmount': payment,'PONO':PONO}
    else:
        return {'pendingAmount': None,'PONO':None} 
    
@app.route('/fetch_invamt', methods=['POST'])
def fetch_invamt():
    blno = request.form.get('blno')
    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()
    invamt = cursor.execute('select invoiceamt from shipdoc where BLNO=?',(blno,)).fetchone()[0]

    if invamt:
        # Convert the tuple to a dictionary for JSON response
        return {'invoiceAmount': invamt}
    else:
        return {'invoiceAmount': None} 
    
@app.route('/fetch_expenses', methods=['POST'])
def fetch_expenses():
    pono = request.form.get('pono')

    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()

    details = cursor.execute('SELECT shippingexpense, chaexpense, missexpense, portexpense, transport, detention, insurancestampduty, bankcharges FROM portclear WHERE PONO=?', (pono,)).fetchone()
    if details:
        shipexp, chaexp, missexp,portexp, transport, detention, instampduty, bankchg = details
    else:
        shipexp, chaexp, missexp, portexp, transport, detention, instampduty, bankchg = None, None, None

    conn.close()

    return {
        'shipexp': shipexp,
        'chaexp': chaexp,
        'missexp': missexp,
        'portexp': portexp,
        'transport': transport,
        'detention': detention,
        'instampduty': instampduty,
        'bankchg': bankchg
    }

@app.route('/fetch_materials', methods=['POST'])
def fetch_materials():

    PONO = request.form.get('PONO')
     
    # Query the database to get the pending amount for the provided PONO
    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()
    materials = cursor.execute('select materialname,materialname2,materialname3 from shipentry where PONO=?',(PONO,)).fetchall()
    print(materials)
    names = cursor.execute("Select * from shipline").fetchall()
    conn.close()
     # Convert data to a format suitable for JSON response
    materials_list = [{'materialname': m[0], 'materialname2': m[1], 'materialname3': m[2]} for m in materials]
    print("-----------materials_list-------------")
    print(materials_list)

    return jsonify({'materials': materials_list})
    
    

@app.route('/fetch_details', methods=['POST'])
def fetch_details():
    PONO = request.form.get('PONO')

    # Query the database to get the pending amount for the provided PONO
    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()
 
    adv = cursor.execute('select pending from shipentry where PONO=?',(PONO,)).fetchone()[0]
    print("ajax----------------------")
    pendingamt = adv
    conn.close()
    # print(payment)
    if pendingamt:
        return jsonify({'pendingamt': pendingamt})
    else:
        return jsonify({'pendingamt': 'Not found'})

@app.route('/fetch_LP', methods=['POST'])
def fetch_LP():
    blno = request.form.get('blno')
    print(blno)
    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()
    amount = cursor.execute('select invoiceamt from shipdoc where BLNO=?',(blno,)).fetchone()[0]
    qty = cursor.execute('select invoicequantity from shipdoc where BLNO=?',(blno,)).fetchone()[0]
    print(amount)
    conn.close()
    # print(payment)
    if amount and qty:
        return jsonify({'amount': amount},{'quantity':qty})
    else:
        return jsonify({'amount': 'Not found'},{'quantity':'Not found'})
   
@app.route('/new')
def newindex():
    return render_template("newindex.html")

@app.route('/button_clicked/<button_id>')
def button_clicked(button_id):

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    if(button_id=="Pending"):
        temp = my_cursor.execute("SELECT * FROM shipentry se LEFT JOIN adpay ap ON se.PONO = ap.PONO WHERE ap.PONO IS NULL;").fetchall()
    elif(button_id=="Booked"):
        my_cursor.execute("Select * from shipentry where status!='Cleared'")
        # print("booked done")
        # print('$$$$$$$$$$$$$$$$$$$$$$')
        temp = my_cursor.fetchall() 
        # print(temp)
    else:
        lala =  my_cursor.execute("""
        SELECT 
            shipdoc.BLNO, shipdoc.PONO, shipentry.suppliername,
            shipdoc.material, shipdoc.invoicequantity, shipentry.materialname, shipentry.materialprice, 
            shipentry.materialname2, shipentry.materialprice2, shipentry.materialname3, shipentry.materialprice3, 
            shipdoc.invoiceamt, strftime('%d-%m-%Y', shipdoc.eta) as eta, CASE WHEN shipdoc.ClearanceDate GLOB '[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]' THEN strftime('%d-%m-%Y',shipdoc.ClearanceDate) ELSE shipdoc.ClearanceDate END as clear_date, shipdoc.status, shipdoc.invoiceno
        FROM 
            shipdoc
        LEFT JOIN 
            shipentry 
        ON 
            shipdoc.pono = shipentry.pono
        WHERE
            shipdoc.status = ?
    """, (button_id,)).fetchall()
    combined_data = []

  
    for row in lala:
        material_name = row[3]
        price = None
        if material_name == row[5]:
            price = row[6]
        elif material_name == row[7]:
            price = row[8]
        elif material_name == row[9]:
            price = row[10]

        entry = {
            "bl_no": row[0],
            "pono": row[1],
            "invoiceno": row[15],
            "supp_name": row[2],
            "material_name": material_name,
            "inv_qty": row[4],
            "price": price,
            "value_of_goods": row[11],
            "eta": row[12],
            "clear_date": row[13],
            "status": row[14]
        }
        combined_data.append(entry)
    
    # print(combined_data)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    total=my_cursor.execute("Select count(*) from shipentry").fetchone()[0]
    totaladv = my_cursor.execute("Select count(*) from shipentry where advance!=0").fetchone()[0]
    advancedone = my_cursor.execute("Select count(*) from adpay").fetchone()[0]
    pending = totaladv-advancedone

    booked = my_cursor.execute("Select count(*) from shipentry where status!='Cleared'").fetchone()[0]
    bookedqty = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    bookedprice = round(my_cursor.execute("Select COALESCE(sum(price),0) from shipentry where status!='Cleared'").fetchone()[0])

    # total = my_cursor.execute("Select sum(TotalQuantity) from shipentry").fetchone()[0]
    advance = my_cursor.execute("Select sum(advance) from adpay").fetchone()[0]
    if advance is None:
        advance=0
    advanceprice = round((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry").fetchone()[0])-(advance))
    advsum = my_cursor.execute("Select COALESCE(sum(advance),1) from shipentry where status!='Cleared'").fetchone()[0]
    if advsum==0:
        pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(1))*100)
    else:
         pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(advsum))*100)
    
    if total==0:
        pendingqty = int((pending/1)*100)
    else:
        pendingqty = int((pending/total)*100)

    print(".............")
    print(pendingqty)
    print(".............")
    print(pendingper)

     #---------------------shipped---------------------------

    shipped = (my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Shipped'").fetchone()[0])
    if shipped is None:
        shipped=0
    shipped=round(shipped)

    shippedprice = (my_cursor.execute("Select sum(invoiceamt) from shipdoc where status='Shipped'").fetchone()[0])
    print("-------shipped---------------")
    print(advance)
    if shippedprice is None:
        shippedprice=0
    shippedprice = round(shippedprice)

    totalinpss = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    if totalinpss is None:
        totalinpss=1

    totalinpssprice = my_cursor.execute("Select sum(price) from shipentry where status!='Cleared'").fetchone()[0]
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    if totalinpssprice is None:
        totalinpssprice=1
    print(shippedprice)
    print(totalinpssprice)

    if(shipped==0):
        shippedqtyper = 0
    else:
        shippedqtyper = int((shipped/totalinpss)*100)
    if(shippedprice==0):
        shippedpriceper = 0
    else:
        shippedpriceper = int((shippedprice/totalinpssprice)*100)

#---------------------shipped ends---------------------------
    
#---------------------not shipped---------------------------
    presentshipped = my_cursor.execute("Select sum(invoicequantity) from shipdoc").fetchone()[0]
    if presentshipped is None:
        presentshipped=0
    notshipped = round((my_cursor.execute("Select COALESCE(sum(TotalQuantity),0) from shipentry").fetchone()[0])-(presentshipped))
    if notshipped is None:
        notshipped=0

    notshippedtotalqty = int((my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedqtyper = int((notshipped/notshippedtotalqty)*100)
    
    notshippedprice = round((my_cursor.execute("Select COALESCE(sum(pending),0) from shipentry where status!='Cleared'").fetchone()[0]))

    if notshippedprice is None:
        notshippedprice=0

    notshippedtotalprice = int((my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedpriceper = int((notshippedprice/notshippedtotalprice)*100)


#--------------------- not shippedends---------------------------

   
        
#---------------------arrived---------------------------

    arrived = my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Arrived'").fetchone()[0]
    if arrived is None:
        arrived=0

    arrivedqtyper = int((arrived/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)

    arrivedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Arrived'").fetchone()[0])



    arrivedpriceper = int(((arrivedprice)/(my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)
    
#---------------------arrived ends---------------------------


#---------------------cleared---------------------------
  
   


    cleared = my_cursor.execute("Select COALESCE(sum(invoicequantity),0) from shipdoc where status='Cleared'").fetchone()[0]
    clearedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Cleared'").fetchone()[0])

    clearedqtyper = int(((cleared)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

    clearedpriceper = int(((clearedprice)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

#---------------------cleared ends---------------------------

    
        
    if total==0:
        clearedper = int(cleared/1)
    else:
        clearedper = int(cleared/total)

    # demo=24
    connection.close()

    return render_template('index.html',combined_data=combined_data,booked=booked,notshipped=notshipped,shipped=shipped,arrived=arrived,cleared=cleared,pending=pending,bookedqty=bookedqty,bookedprice=bookedprice,advanceprice=advanceprice,clearedprice=clearedprice,clearedper=clearedper,pendingper=pendingper,pendingqty=pendingqty,shippedprice=shippedprice,shippedqtyper=shippedqtyper,shippedpriceper=shippedpriceper,notshippedprice=notshippedprice,notshippedqtyper=notshippedqtyper,notshippedpriceper=notshippedpriceper,arrivedprice=arrivedprice,arrivedqtyper=arrivedqtyper,arrivedpriceper=arrivedpriceper,clearedqtyper=clearedqtyper,clearedpriceper=clearedpriceper)










@app.route('/Booked')
def Booked():

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala= my_cursor.execute("Select * from shipentry where status!='Cleared'").fetchall()
    
    # print(combined_data)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    total=my_cursor.execute("Select count(*) from shipentry").fetchone()[0]
    totaladv = my_cursor.execute("Select count(*) from shipentry where advance!=0").fetchone()[0]
    advancedone = my_cursor.execute("Select count(*) from adpay").fetchone()[0]
    pending = totaladv-advancedone

    booked = my_cursor.execute("Select count(*) from shipentry where status!='Cleared'").fetchone()[0]
    bookedqty = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    bookedprice = round(my_cursor.execute("Select COALESCE(sum(price),0) from shipentry where status!='Cleared'").fetchone()[0])

    # total = my_cursor.execute("Select sum(TotalQuantity) from shipentry").fetchone()[0]
    advance = my_cursor.execute("Select sum(advance) from adpay").fetchone()[0]
    if advance is None:
        advance=0
    advanceprice = round((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry").fetchone()[0])-(advance))
    advsum = my_cursor.execute("Select COALESCE(sum(advance),1) from shipentry where status!='Cleared'").fetchone()[0]
    if advsum==0:
        pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(1))*100)
    else:
         pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(advsum))*100)
    
    if total==0:
        pendingqty = int((pending/1)*100)
    else:
        pendingqty = int((pending/total)*100)

    print(".............")
    print(pendingqty)
    print(".............")
    print(pendingper)

     #---------------------shipped---------------------------

    shipped = (my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Shipped'").fetchone()[0])
    if shipped is None:
        shipped=0
    shipped=round(shipped)

    shippedprice = (my_cursor.execute("Select sum(invoiceamt) from shipdoc where status='Shipped'").fetchone()[0])
    print("-------shipped---------------")
    print(advance)
    if shippedprice is None:
        shippedprice=0
    shippedprice = round(shippedprice)

    totalinpss = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    if totalinpss is None:
        totalinpss=1

    totalinpssprice = my_cursor.execute("Select sum(price) from shipentry where status!='Cleared'").fetchone()[0]
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    if totalinpssprice is None:
        totalinpssprice=1
    print(shippedprice)
    print(totalinpssprice)

    if(shipped==0):
        shippedqtyper = 0
    else:
        shippedqtyper = int((shipped/totalinpss)*100)
    if(shippedprice==0):
        shippedpriceper = 0
    else:
        shippedpriceper = int((shippedprice/totalinpssprice)*100)

#---------------------shipped ends---------------------------
    
#---------------------not shipped---------------------------
    presentshipped = my_cursor.execute("Select sum(invoicequantity) from shipdoc").fetchone()[0]
    if presentshipped is None:
        presentshipped=0
    notshipped = round((my_cursor.execute("Select COALESCE(sum(TotalQuantity),0) from shipentry").fetchone()[0])-(presentshipped))
    if notshipped is None:
        notshipped=0

    notshippedtotalqty = int((my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedqtyper = int((notshipped/notshippedtotalqty)*100)
    
    notshippedprice = round((my_cursor.execute("Select COALESCE(sum(pending),0) from shipentry where status!='Cleared'").fetchone()[0]))

    if notshippedprice is None:
        notshippedprice=0

    notshippedtotalprice = int((my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedpriceper = int((notshippedprice/notshippedtotalprice)*100)


#--------------------- not shippedends---------------------------

   
        
#---------------------arrived---------------------------

    arrived = my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Arrived'").fetchone()[0]
    if arrived is None:
        arrived=0

    arrivedqtyper = int((arrived/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)

    arrivedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Arrived'").fetchone()[0])



    arrivedpriceper = int(((arrivedprice)/(my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)
    
#---------------------arrived ends---------------------------


#---------------------cleared---------------------------
  
   


    cleared = my_cursor.execute("Select COALESCE(sum(invoicequantity),0) from shipdoc where status='Cleared'").fetchone()[0]
    clearedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Cleared'").fetchone()[0])

    clearedqtyper = int(((cleared)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

    clearedpriceper = int(((clearedprice)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

#---------------------cleared ends---------------------------

    
        
    if total==0:
        clearedper = int(cleared/1)
    else:
        clearedper = int(cleared/total)
    # demo=24
    connection.close()

    return render_template('bookedviewmore.html',booked=booked,lala=lala,notshipped=notshipped,shipped=shipped,arrived=arrived,cleared=cleared,pending=pending,bookedqty=bookedqty,bookedprice=bookedprice,advanceprice=advanceprice,clearedprice=clearedprice,clearedper=clearedper,pendingper=pendingper,pendingqty=pendingqty,shippedprice=shippedprice,shippedqtyper=shippedqtyper,shippedpriceper=shippedpriceper,notshippedprice=notshippedprice,notshippedqtyper=notshippedqtyper,notshippedpriceper=notshippedpriceper,arrivedprice=arrivedprice,arrivedqtyper=arrivedqtyper,arrivedpriceper=arrivedpriceper,clearedqtyper=clearedqtyper,clearedpriceper=clearedpriceper)




@app.route('/Advance')
def Advance():

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala= my_cursor.execute("SELECT se.* FROM shipentry se LEFT JOIN adpay ap ON se.PONO = ap.PONO WHERE ap.PONO IS NULL AND se.status != 'Cleared' AND se.advance!=0;").fetchall()
    
    # print(combined_data)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    total=my_cursor.execute("Select count(*) from shipentry").fetchone()[0]
    totaladv = my_cursor.execute("Select count(*) from shipentry where advance!=0").fetchone()[0]
    advancedone = my_cursor.execute("Select count(*) from adpay").fetchone()[0]
    pending = totaladv-advancedone

    booked = my_cursor.execute("Select count(*) from shipentry where status!='Cleared'").fetchone()[0]
    bookedqty = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    bookedprice = round(my_cursor.execute("Select COALESCE(sum(price),0) from shipentry where status!='Cleared'").fetchone()[0])

    # total = my_cursor.execute("Select sum(TotalQuantity) from shipentry").fetchone()[0]
    advance = my_cursor.execute("Select sum(advance) from adpay").fetchone()[0]
    if advance is None:
        advance=0
    advanceprice = round((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry").fetchone()[0])-(advance))
    advsum = my_cursor.execute("Select COALESCE(sum(advance),1) from shipentry where status!='Cleared'").fetchone()[0]
    if advsum==0:
        pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(1))*100)
    else:
         pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(advsum))*100)
    
    if total==0:
        pendingqty = int((pending/1)*100)
    else:
        pendingqty = int((pending/total)*100)

    print(".............")
    print(pendingqty)
    print(".............")
    print(pendingper)

     #---------------------shipped---------------------------

    shipped = (my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Shipped'").fetchone()[0])
    if shipped is None:
        shipped=0
    shipped=round(shipped)

    shippedprice = (my_cursor.execute("Select sum(invoiceamt) from shipdoc where status='Shipped'").fetchone()[0])
    print("-------shipped---------------")
    print(advance)
    if shippedprice is None:
        shippedprice=0
    shippedprice = round(shippedprice)

    totalinpss = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    if totalinpss is None:
        totalinpss=1

    totalinpssprice = my_cursor.execute("Select sum(price) from shipentry where status!='Cleared'").fetchone()[0]
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    if totalinpssprice is None:
        totalinpssprice=1
    print(shippedprice)
    print(totalinpssprice)

    if(shipped==0):
        shippedqtyper = 0
    else:
        shippedqtyper = int((shipped/totalinpss)*100)
    if(shippedprice==0):
        shippedpriceper = 0
    else:
        shippedpriceper = int((shippedprice/totalinpssprice)*100)

#---------------------shipped ends---------------------------
    
#---------------------not shipped---------------------------
    presentshipped = my_cursor.execute("Select sum(invoicequantity) from shipdoc").fetchone()[0]
    if presentshipped is None:
        presentshipped=0
    notshipped = round((my_cursor.execute("Select COALESCE(sum(TotalQuantity),0) from shipentry").fetchone()[0])-(presentshipped))
    if notshipped is None:
        notshipped=0

    notshippedtotalqty = int((my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedqtyper = int((notshipped/notshippedtotalqty)*100)
    
    notshippedprice = round((my_cursor.execute("Select COALESCE(sum(pending),0) from shipentry where status!='Cleared'").fetchone()[0]))

    if notshippedprice is None:
        notshippedprice=0

    notshippedtotalprice = int((my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedpriceper = int((notshippedprice/notshippedtotalprice)*100)


#--------------------- not shippedends---------------------------

   
        
#---------------------arrived---------------------------

    arrived = my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Arrived'").fetchone()[0]
    if arrived is None:
        arrived=0

    arrivedqtyper = int((arrived/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)

    arrivedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Arrived'").fetchone()[0])



    arrivedpriceper = int(((arrivedprice)/(my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)
    
#---------------------arrived ends---------------------------


#---------------------cleared---------------------------
  
   


    cleared = my_cursor.execute("Select COALESCE(sum(invoicequantity),0) from shipdoc where status='Cleared'").fetchone()[0]
    clearedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Cleared'").fetchone()[0])

    clearedqtyper = int(((cleared)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

    clearedpriceper = int(((clearedprice)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

#---------------------cleared ends---------------------------

    
        
    if total==0:
        clearedper = int(cleared/1)
    else:
        clearedper = int(cleared/total)

    # demo=24
    connection.close()

    return render_template('advanceviewmore.html',booked=booked,lala=lala,notshipped=notshipped,shipped=shipped,arrived=arrived,cleared=cleared,pending=pending,bookedqty=bookedqty,bookedprice=bookedprice,advanceprice=advanceprice,clearedprice=clearedprice,clearedper=clearedper,pendingper=pendingper,pendingqty=pendingqty,shippedprice=shippedprice,shippedqtyper=shippedqtyper,shippedpriceper=shippedpriceper,notshippedprice=notshippedprice,notshippedqtyper=notshippedqtyper,notshippedpriceper=notshippedpriceper,arrivedprice=arrivedprice,arrivedqtyper=arrivedqtyper,arrivedpriceper=arrivedpriceper,clearedqtyper=clearedqtyper,clearedpriceper=clearedpriceper)






@app.route('/NotShipped')
def NotShipped():

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala= my_cursor.execute("SELECT sd.PONO,sd.suppliername,sd.materialname,sd.materialname2,sd.materialname3, sd.TotalQuantity - COALESCE(SUM(invoicequantity), 0) AS remaining_quantity FROM shipentry sd LEFT JOIN (SELECT PONO, SUM(invoicequantity) AS invoicequantity FROM shipdoc GROUP BY PONO) id ON sd.PONO = id.PONO GROUP BY sd.PONO, sd.TotalQuantity HAVING remaining_quantity > 0;").fetchall()

    # print(lala)
    
    # print(combined_data)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    total=my_cursor.execute("Select count(*) from shipentry").fetchone()[0]
    totaladv = my_cursor.execute("Select count(*) from shipentry where advance!=0").fetchone()[0]
    advancedone = my_cursor.execute("Select count(*) from adpay").fetchone()[0]
    pending = totaladv-advancedone

    booked = my_cursor.execute("Select count(*) from shipentry where status!='Cleared'").fetchone()[0]
    bookedqty = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    bookedprice = round(my_cursor.execute("Select COALESCE(sum(price),0) from shipentry where status!='Cleared'").fetchone()[0])

    # total = my_cursor.execute("Select sum(TotalQuantity) from shipentry").fetchone()[0]
    advance = my_cursor.execute("Select sum(advance) from adpay").fetchone()[0]
    if advance is None:
        advance=0
    advanceprice = round((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry").fetchone()[0])-(advance))
    advsum = my_cursor.execute("Select COALESCE(sum(advance),1) from shipentry where status!='Cleared'").fetchone()[0]
    if advsum==0:
        pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(1))*100)
    else:
         pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(advsum))*100)
    
    if total==0:
        pendingqty = int((pending/1)*100)
    else:
        pendingqty = int((pending/total)*100)

    print(".............")
    print(pendingqty)
    print(".............")
    print(pendingper)

     #---------------------shipped---------------------------

    shipped = (my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Shipped'").fetchone()[0])
    if shipped is None:
        shipped=0
    shipped=round(shipped)

    shippedprice = (my_cursor.execute("Select sum(invoiceamt) from shipdoc where status='Shipped'").fetchone()[0])
    print("-------shipped---------------")
    print(advance)
    if shippedprice is None:
        shippedprice=0
    shippedprice = round(shippedprice)

    totalinpss = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    if totalinpss is None:
        totalinpss=1

    totalinpssprice = my_cursor.execute("Select sum(price) from shipentry where status!='Cleared'").fetchone()[0]
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    if totalinpssprice is None:
        totalinpssprice=1
    print(shippedprice)
    print(totalinpssprice)

    if(shipped==0):
        shippedqtyper = 0
    else:
        shippedqtyper = int((shipped/totalinpss)*100)
    if(shippedprice==0):
        shippedpriceper = 0
    else:
        shippedpriceper = int((shippedprice/totalinpssprice)*100)

#---------------------shipped ends---------------------------
    
#---------------------not shipped---------------------------
    presentshipped = my_cursor.execute("Select sum(invoicequantity) from shipdoc").fetchone()[0]
    if presentshipped is None:
        presentshipped=0
    notshipped = round((my_cursor.execute("Select COALESCE(sum(TotalQuantity),0) from shipentry").fetchone()[0])-(presentshipped))
    if notshipped is None:
        notshipped=0

    notshippedtotalqty = int((my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedqtyper = int((notshipped/notshippedtotalqty)*100)
    
    notshippedprice = round((my_cursor.execute("Select COALESCE(sum(pending),0) from shipentry where status!='Cleared'").fetchone()[0]))

    if notshippedprice is None:
        notshippedprice=0

    notshippedtotalprice = int((my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedpriceper = int((notshippedprice/notshippedtotalprice)*100)


#--------------------- not shippedends---------------------------

   
        
#---------------------arrived---------------------------

    arrived = my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Arrived'").fetchone()[0]
    if arrived is None:
        arrived=0

    arrivedqtyper = int((arrived/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)

    arrivedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Arrived'").fetchone()[0])



    arrivedpriceper = int(((arrivedprice)/(my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)
    
#---------------------arrived ends---------------------------


#---------------------cleared---------------------------
  
   


    cleared = my_cursor.execute("Select COALESCE(sum(invoicequantity),0) from shipdoc where status='Cleared'").fetchone()[0]
    clearedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Cleared'").fetchone()[0])

    clearedqtyper = int(((cleared)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

    clearedpriceper = int(((clearedprice)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

#---------------------cleared ends---------------------------

    
        
    if total==0:
        clearedper = int(cleared/1)
    else:
        clearedper = int(cleared/total)

    # demo=24
    connection.close()

    return render_template('NotShipmore.html',booked=booked,lala=lala,notshipped=notshipped,shipped=shipped,arrived=arrived,cleared=cleared,pending=pending,bookedqty=bookedqty,bookedprice=bookedprice,advanceprice=advanceprice,clearedprice=clearedprice,clearedper=clearedper,pendingper=pendingper,pendingqty=pendingqty,shippedprice=shippedprice,shippedqtyper=shippedqtyper,shippedpriceper=shippedpriceper,notshippedprice=notshippedprice,notshippedqtyper=notshippedqtyper,notshippedpriceper=notshippedpriceper,arrivedprice=arrivedprice,arrivedqtyper=arrivedqtyper,arrivedpriceper=arrivedpriceper,clearedqtyper=clearedqtyper,clearedpriceper=clearedpriceper)








@app.route('/')
def index():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("""
        SELECT 
            shipdoc.BLNO, shipdoc.PONO, shipentry.suppliername,
            shipdoc.material, shipdoc.invoicequantity, shipentry.materialname, shipentry.materialprice, 
            shipentry.materialname2, shipentry.materialprice2, shipentry.materialname3, shipentry.materialprice3, 
            shipdoc.invoiceamt, strftime('%d-%m-%Y', shipdoc.eta) as eta, CASE WHEN shipdoc.ClearanceDate GLOB '[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]' THEN strftime('%d-%m-%Y',shipdoc.ClearanceDate) ELSE shipdoc.ClearanceDate END as clear_date, shipdoc.status, shipdoc.invoiceno
        FROM 
            shipdoc
        LEFT JOIN 
            shipentry 
        ON 
            shipdoc.pono = shipentry.pono
    """)
    lala = my_cursor.fetchall()
    combined_data = []


  
    for row in lala:
        material_name = row[3]
        price = None
        if material_name == row[5]:
            price = row[6]
        elif material_name == row[7]:
            price = row[8]
        elif material_name == row[9]:
            price = row[10]

        entry = {
            "bl_no": row[0],
            "pono": row[1],
            "invoiceno": row[15],
            "supp_name": row[2],
            "material_name": material_name,
            "inv_qty": row[4],
            "price": price,
            "value_of_goods": row[11],
            "eta": row[12],
            "clear_date": row[13],
            "status": row[14]
        }
        combined_data.append(entry)
    # print(combined_data)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    total=my_cursor.execute("Select count(*) from shipentry").fetchone()[0]
    totaladv = my_cursor.execute("Select count(*) from shipentry where advance!=0").fetchone()[0]
    advancedone = my_cursor.execute("Select count(*) from adpay").fetchone()[0]
    pending = totaladv-advancedone

    booked = my_cursor.execute("Select count(*) from shipentry where status!='Cleared'").fetchone()[0]
    bookedqty = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    bookedprice = round(my_cursor.execute("Select COALESCE(sum(price),0) from shipentry where status!='Cleared'").fetchone()[0])

    # total = my_cursor.execute("Select sum(TotalQuantity) from shipentry").fetchone()[0]
    advance = my_cursor.execute("Select sum(advance) from adpay").fetchone()[0]
    if advance is None:
        advance=0
    advanceprice = round((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry").fetchone()[0])-(advance))
    advsum = my_cursor.execute("Select COALESCE(sum(advance),1) from shipentry where status!='Cleared'").fetchone()[0]
    if advsum==0:
        pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(1))*100)
    else:
         pendingper = int((((my_cursor.execute("Select COALESCE(sum(advance),0) from shipentry where status!='Cleared'").fetchone()[0])-(advance))/(advsum))*100)
    
    if total==0:
        pendingqty = int((pending/1)*100)
    else:
        pendingqty = int((pending/total)*100)

    print(".............")
    print(pendingqty)
    print(".............")
    print(pendingper)

     #---------------------shipped---------------------------

    shipped = my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Shipped'").fetchone()[0]
    if shipped is None:
        shipped=0
    shipped=round(shipped)

    shippedprice = (my_cursor.execute("Select sum(invoiceamt) from shipdoc where status='Shipped'").fetchone()[0])
    print("-------shipped---------------")
    print(advance)
    if shippedprice is None:
        shippedprice=0
    shippedprice = round(shippedprice)

    totalinpss = my_cursor.execute("Select sum(TotalQuantity) from shipentry where status!='Cleared'").fetchone()[0]
    if totalinpss is None:
        totalinpss=1

    totalinpssprice = my_cursor.execute("Select sum(price) from shipentry where status!='Cleared'").fetchone()[0]
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    if totalinpssprice is None:
        totalinpssprice=1
    print(shippedprice)
    print(totalinpssprice)

    if(shipped==0):
        shippedqtyper = 0
    else:
        shippedqtyper = int((shipped/totalinpss)*100)
    if(shippedprice==0):
        shippedpriceper = 0
    else:
        shippedpriceper = int((shippedprice/totalinpssprice)*100)

#---------------------shipped ends---------------------------
    
#---------------------not shipped---------------------------
    presentshipped = my_cursor.execute("Select sum(invoicequantity) from shipdoc").fetchone()[0]
    if presentshipped is None:
        presentshipped=0
    notshipped = round((my_cursor.execute("Select COALESCE(sum(TotalQuantity),0) from shipentry").fetchone()[0])-(presentshipped))
    if notshipped is None:
        notshipped=0

    notshippedtotalqty = int((my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedqtyper = int((notshipped/notshippedtotalqty)*100)
    
    notshippedprice = round((my_cursor.execute("Select COALESCE(sum(pending),0) from shipentry where status!='Cleared'").fetchone()[0]))

    if notshippedprice is None:
        notshippedprice=0

    notshippedtotalprice = int((my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))

    notshippedpriceper = int((notshippedprice/notshippedtotalprice)*100)


#--------------------- not shippedends---------------------------

   
        
#---------------------arrived---------------------------

    arrived = my_cursor.execute("Select sum(invoicequantity) from shipdoc where status='Arrived'").fetchone()[0]
    if arrived is None:
        arrived=0

    arrivedqtyper = int((arrived/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)

    arrivedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Arrived'").fetchone()[0])



    arrivedpriceper = int(((arrivedprice)/(my_cursor.execute("Select COALESCE(sum(price),1) from shipentry where status!='Cleared'").fetchone()[0]))*100)
    
#---------------------arrived ends---------------------------


#---------------------cleared---------------------------
  
   


    cleared = my_cursor.execute("Select COALESCE(sum(invoicequantity),0) from shipdoc where status='Cleared'").fetchone()[0]
    clearedprice = round(my_cursor.execute("Select COALESCE(sum(invoiceamt),0) from shipdoc where status='Cleared'").fetchone()[0])

    clearedqtyper = int(((cleared)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

    clearedpriceper = int(((clearedprice)/(my_cursor.execute("Select COALESCE(sum(TotalQuantity),1) from shipentry where status!='Cleared' ").fetchone()[0]))*100)

#---------------------cleared ends---------------------------

    
        
    if total==0:
        clearedper = int(cleared/1)
    else:
        clearedper = int(cleared/total)
        

    # demo=24
    connection.close()

    return render_template('index.html',combined_data=combined_data,booked=booked,notshipped=notshipped,shipped=shipped,arrived=arrived,cleared=cleared,pending=pending,bookedqty=bookedqty,bookedprice=bookedprice,advanceprice=advanceprice,clearedprice=clearedprice,clearedper=clearedper,pendingper=pendingper,pendingqty=pendingqty,shippedprice=shippedprice,shippedqtyper=shippedqtyper,shippedpriceper=shippedpriceper,notshippedprice=notshippedprice,notshippedqtyper=notshippedqtyper,notshippedpriceper=notshippedpriceper,arrivedprice=arrivedprice,arrivedqtyper=arrivedqtyper,arrivedpriceper=arrivedpriceper,clearedqtyper=clearedqtyper,clearedpriceper=clearedpriceper)

@app.route('/updateshipentry', methods=['POST'])
def updateshipentry():
    PONO = request.form.get('PONO')
    print(PONO)
    print('------------PONO------------------')
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala=my_cursor.execute('Select * from shipentry where PONO=?',(PONO,)).fetchall()
    print(lala)

    suppliers = my_cursor.execute("Select name from supplier").fetchall()
    indentors = my_cursor.execute("Select name from indentor").fetchall()
    materials = my_cursor.execute("Select name from material").fetchall()
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
        "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
        "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
        "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
        "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
        "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the",
        "Congo, Republic of the", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
        "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
        "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland",
        "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
        "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
        "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
        "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",
        "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
        "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
        "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
        "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
        "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
        "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
        "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
        "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
        "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
        "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
        "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
        "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
        "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
        "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
        "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
    print('$$$$$$$$$$$$$$$$$$')
    return render_template('updateshipentry.html',lala=lala,suppliers=suppliers,indentors=indentors,materials=materials,countries=countries)

@app.route('/updateadvance', methods=['POST'])
def updateadvance():
    CSN = request.form.get('CSN')
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala=my_cursor.execute('Select * from shipentry where contractsalesno=?',(CSN,)).fetchall()
    print(lala)
    print('$$$$$$$$$$$$$$$$$$')
    return render_template('updateadvancedet.html',lala=lala)

@app.route('/commitadvance', methods=['POST'])
def commitadvance():
    PONO = request.form['PONO']
    indentor = request.form['indentor']
    suppliername = request.form['suppliername']
    origin = request.form['origin']
    confirmdate = request.form['confirmdate']
    materialname = request.form['materialname']
    contractsalesno = request.form['contractsalesno']
    contractsaledate = request.form['contractsaledate']
    quantity = request.form['quantity']
    totalquantity = request.form['totalquantity']
    unit = request.form['unit']
    price = request.form['price']
    lme = request.form['lme']
    lmepercent = request.form['lmepercent']
    paymentterms = request.form['paymentterms']
    quantityleft = int(totalquantity)-int(quantity)
    status = "Booked"
    advance = request.form['advanceamt']
    pending = int(price)-int(advance)
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("UPDATE shipentry SET indentor=?, suppliername=?, origin=?, confirmationdate=?, materialname=?, contractsalesno=?, contractsalesdate=?, TotalQuantity=?, quantity=?, quantityleft=?, unit=?, price=?, LME=?, LMEper=?, paymentterms=?, status=?, advance=?, pending=? WHERE PONO=?", (indentor, suppliername, origin, confirmdate, materialname,
                      contractsalesno, contractsaledate,totalquantity,quantity, quantityleft, unit, price, lme, lmepercent, paymentterms,status,advance,pending,PONO))

    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)

@app.route('/updateShipArriv',methods=['POST'])
def updateShipArriv():
    BLNO = request.form.get('BLNO')
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    status = my_cursor.execute('Select status from shipdoc where BLNO=?',(BLNO,)).fetchone()[0]
    print(status)
    print('-----------status--------------------')
    if  status=='Cleared':
        lala=my_cursor.execute('Select * from portclear where BLNO=?',(BLNO,)).fetchall()
        return render_template('updateCleared.html',lala=lala)

    lala=my_cursor.execute('Select * from shipdoc where BLNO=?',(BLNO,)).fetchall()
    names = my_cursor.execute("Select * from shipline").fetchall()
    return render_template('updateShippedArrived.html',lala=lala,names=names)

@app.route('/commitShipArriv', methods=['POST'])
def commitShipArriv():
    invno = request.form['invno']
    invdate = request.form['invdate']
    invquantity = request.form['invquantity']
    invamt = request.form['invamt']
    pendingamt = request.form['pendingamt']
    containerno = request.form['containerno']
    shippingline = request.form.get('shippingline')
    blno = request.form['blno']
    eta = request.form['eta']
    etd = request.form['etd']
    detfreeday = request.form['detfreeday']
    detfreetill = request.form['detfreetill']
    transtime = request.form['transtime']
    portarr = request.form['portarr']
    portship = request.form['portship']
    asscha = request.form['asscha']

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("UPDATE shipdoc SET invoiceno=?, dateinvoice=?, invoicequantity=?, invoiceamt=?, pendingamount=?, containerno=?, shippingline=?, BLNO=?, ETA=?, ETD=?, detentionfreedays=?, detentionfreetill=?, transittime=?, portofarrival=?, portofshipment=?, CHAassigned=? WHERE BLNO=?", (invno, invdate, invquantity, invamt, pendingamt,
                      containerno, shippingline,blno,eta, etd, detfreeday, detfreetill, transtime, portarr, portship,asscha,blno))

    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)


@app.route('/commitCleared', methods=['POST'])
def commitCleared():
    pono = request.form['pono']
    BLNO = request.form['blno']
    shipexp = request.form['shipexp']
    chaexp = request.form['chaexp']
    dutypaid = request.form['dutypaid']
    missexp = request.form['missexp']
    portexp = request.form['portexp']
    transport = request.form['transport']
    instampduty = request.form['instampduty']
    detention = request.form['detention']
    bankchg = request.form['bankchg']
    loadedprice = request.form['loadedprice']
    ClearanceDate = request.form.get('ClearanceDate')
    invinr = request.form['invinr']

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("UPDATE portclear SET pono=?, BLNO=?, shippingexpense=?, chaexpense=?, dutypaid=?, missexpense=?, portexpense=?, trasnsport=?, insurancestampduty=?, detention=?, bankcharges=?, loadedprice=?,ClearanceDate=?,invinr=? WHERE BLNO=?", (pono,BLNO, shipexp, chaexp, dutypaid, missexp,
                      portexp, transport,instampduty,detention, bankchg, loadedprice, ClearanceDate,invinr,BLNO))
    my_cursor.execute("UPDATE shipdoc SET ClearanceDate = ? WHERE blno = ?",(ClearanceDate, BLNO)) 

    connection.commit()
    connection.close()
    return redirect(url_for('index'),code=303)




@app.route('/shipentry')
def shipentry():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala = my_cursor.execute("Select name from supplier").fetchall()
    indentors = my_cursor.execute("Select name from indentor").fetchall()
    materials = my_cursor.execute("Select name from material").fetchall()
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
        "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
        "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
        "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
        "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
        "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the",
        "Congo, Republic of the", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
        "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
        "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland",
        "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
        "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
        "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
        "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",
        "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
        "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
        "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
        "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
        "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
        "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
        "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
        "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
        "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
        "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
        "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
        "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
        "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
        "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
        "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
    return render_template('shipment_entry.html',lala=lala,countries=countries,indentors=indentors,materials=materials)
@app.route('/adpay')
def adpay():
    return render_template('ad_pay.html')
@app.route('/shipdoc')
def shipdoc():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    names = my_cursor.execute("Select * from shipline").fetchall()
    return render_template('ship_doc.html',names=names)
@app.route('/portclear')
def portclear():
    return render_template('port_clear.html')
@app.route('/reports')
def reports():
    return render_template('reports.html')
@app.route('/register')
def register():
    return render_template('pages-register.html')
@app.route('/login')
def login():
    return render_template('pages-login.html')

#Reports Route----------------------
# strftime('%d-%m-%Y', shipdoc.eta) as eta, CASE WHEN shipdoc.ClearanceDate = '0' THEN '0' ELSE strftime('%d-%m-%Y',shipdoc.ClearanceDate) END as clear_date

@app.route('/advpaid')
def advpaid():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT a.PONO, s.indentor, s.suppliername, s.origin, strftime('%d-%m-%Y', s.confirmationdate) as confirmationdate, s.contractsalesno, strftime('%d-%m-%Y', s.contractsalesdate) as contractsalesdate, s.materialname, s.totalquantity, s.price, s.paymentterms, s.advance, a.advance FROM adpay a JOIN shipentry s ON a.PONO = s.PONO")
    lala = my_cursor.fetchall()

    connection.close()

    return render_template('advpaid.html',lala=lala)

@app.route('/advpen')
def advpen():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT s.PONO, s.indentor, s.suppliername, s.origin, strftime('%d-%m-%Y', s.confirmationdate) as confirmationdate, s.contractsalesno, strftime('%d-%m-%Y', s.contractsalesdate) as contractsalesdate, s.materialname, s.totalquantity, s.price, s.paymentterms, s.advance, s.pending FROM shipentry s LEFT JOIN adpay a ON s.PONO = a.PONO WHERE a.PONO IS NULL AND s.advance!=0")
    lala = my_cursor.fetchall()

    connection.close()

    return render_template('advpen.html',lala=lala)

@app.route('/intransit')
def intransit():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("""
        SELECT 
            shipdoc.PONO,shipdoc.invoiceno, shipentry.suppliername,shipentry.origin,strftime('%d-%m-%Y', shipentry.confirmationdate) as confirmationdate,shipentry.contractsalesno,strftime('%d-%m-%Y', shipentry.contractsalesdate) as contractsalesdate,
            shipdoc.material, shipdoc.invoicequantity, shipentry.materialname, shipentry.materialprice, 
            shipentry.materialname2, shipentry.materialprice2, shipentry.materialname3, shipentry.materialprice3,shipdoc.invoicequantity, 
            shipdoc.invoiceamt,shipdoc.containerno,shipdoc.shippingline,strftime('%d-%m-%Y', shipdoc.etd) as etd, strftime('%d-%m-%Y',shipdoc.eta) as eta
        FROM 
            shipdoc
        LEFT JOIN 
            shipentry 
        ON 
            shipdoc.pono = shipentry.pono
        WHERE
            shipdoc.status = 'Shipped'
    """)
    lala = my_cursor.fetchall()
    combined_data = []

  
    for row in lala:
        material_name = row[7]
        price = None
        if material_name == row[9]:
            price = row[10]
        elif material_name == row[11]:
            price = row[12]
        elif material_name == row[13]:
            price = row[14]

        entry = {
            "pono": row[0],
            "invno": row[1],
            "supp_name": row[2],
            "origin": row[3],
            "confirmdate": row[4],
            "csn": row[5],
            "contdate": row[6],
            "material_name": material_name,
            "inv_qty": row[8],
            "price": price,
            "value_of_goods": row[16],
            "contno": row[17],
            "shipline": row[18],
            "etd": row[19],
            "eta": row[20]
        }
        combined_data.append(entry)

    connection.close()

    return render_template('intransit.html',combined_data=combined_data)

@app.route('/notshipped')
def notshipped():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala= my_cursor.execute("SELECT sd.PONO,sd.suppliername,sd.origin,strftime('%d-%m-%Y', sd.confirmationdate) as confirmationdate,sd.contractsalesno,strftime('%d-%m-%Y', sd.contractsalesdate) as contractsalesdate,sd.materialname,sd.materialname2,sd.materialname3,sd.price,sd.TotalQuantity - COALESCE(SUM(invoicequantity), 0) AS remaining_quantity FROM shipentry sd LEFT JOIN (SELECT PONO, SUM(invoicequantity) AS invoicequantity FROM shipdoc GROUP BY PONO) id ON sd.PONO = id.PONO GROUP BY sd.PONO, sd.TotalQuantity HAVING remaining_quantity > 0;").fetchall()

    connection.close()

    return render_template('notshipped.html',lala=lala)

@app.route('/ETA_ship')
def ETA_ship():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("""
        SELECT 
            shipdoc.PONO,shipdoc.invoiceno, shipentry.suppliername,shipentry.origin,strftime('%d-%m-%Y', shipentry.confirmationdate) as confirmationdate,shipentry.contractsalesno,strftime('%d-%m-%Y', shipentry.contractsalesdate) as contractsalesdate,
            shipdoc.material, shipdoc.invoicequantity, shipentry.materialname, shipentry.materialprice, 
            shipentry.materialname2, shipentry.materialprice2, shipentry.materialname3, shipentry.materialprice3,shipdoc.invoicequantity, 
            shipdoc.invoiceamt,shipdoc.containerno,shipdoc.shippingline,strftime('%d-%m-%Y', shipdoc.etd) as etd, strftime('%d-%m-%Y',shipdoc.eta) as eta,shipdoc.detentionfreedays,strftime('%d-%m-%Y',shipdoc.detentionfreetill) as detentionfreetill,shipdoc.transittime,shipdoc.portofarrival, shipdoc.CHAassigned
        FROM 
            shipdoc
        LEFT JOIN 
            shipentry 
        ON 
            shipdoc.pono = shipentry.pono
    """)
    lala = my_cursor.fetchall()
    combined_data = []

  
    for row in lala:
        material_name = row[7]
        price = None
        if material_name == row[9]:
            price = row[10]
        elif material_name == row[11]:
            price = row[12]
        elif material_name == row[13]:
            price = row[14]

        entry = {
            "pono": row[0],
            "invno": row[1],
            "supp_name": row[2],
            "origin": row[3],
            "confirmdate": row[4],
            "csn": row[5],
            "contdate": row[6],
            "material_name": material_name,
            "inv_qty": row[8],
            "price": price,
            "value_of_goods": row[16],
            "contno": row[17],
            "shipline": row[18],
            "etd": row[19],
            "eta": row[20],
            "dfd": row[21],
            "freedate": row[22],
            "time": row[23],
            "port": row[24],
            "cha": row[25]
        }
        combined_data.append(entry)

    connection.close()

    return render_template('ETA_ship.html',combined_data=combined_data)

@app.route('/mat_wise_ship')
def mat_wise_ship():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT PONO,suppliername,origin, strftime('%d-%m-%Y', confirmationdate) as confirmationdate, contractsalesno, strftime('%d-%m-%Y', contractsalesdate) as contractsalesdate, materialname,materialname2,materialname3,materialprice,materialprice2,materialprice3,materialqty,materialqty2,materialqty3 FROM shipentry")
    lala = my_cursor.fetchall()

    connection.close()

    return render_template('mat_wise_ship.html',lala=lala)

@app.route('/month_ship')
def month_ship():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("""
        SELECT 
            shipdoc.PONO,shipdoc.invoiceno, shipentry.suppliername,shipentry.origin,shipentry.contractsalesno,
            shipdoc.material, shipdoc.invoicequantity, shipentry.materialname,
            shipentry.materialname2, shipentry.materialname3,
            shipdoc.invoiceamt,shipdoc.containerno, strftime('%d-%m-%Y',shipdoc.eta) as eta, shipdoc.transittime, shipdoc.portofarrival
        FROM 
            shipdoc
        LEFT JOIN 
            shipentry 
        ON 
            shipdoc.pono = shipentry.pono
    """)
    lala = my_cursor.fetchall()
    combined_data = []

  
    for row in lala:
        material_name = row[5]
        price = None
        if material_name == row[7]:
            price = row[6]
        elif material_name == row[8]:
            price = row[8]
        elif material_name == row[9]:
            price = row[10]

        entry = {
            
            "pono": row[0],
            "invno": row[1],
            "supp_name": row[2],
            "origin": row[3],
            "csn": row[4],
            "material_name": material_name,
            "inv_qty": row[6],
            "invamt": row[10],
            "contno": row[11],
            "eta": row[12],
            "time": row[13],
            "port": row[14]
        }
        combined_data.append(entry)

    connection.close()

    return render_template('month_ship.html',combined_data=combined_data)

@app.route('/month_item')
def month_item():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("""
        SELECT 
            shipdoc.PONO,shipdoc.invoiceno, shipentry.suppliername,shipentry.origin,shipentry.contractsalesno,
            shipdoc.material, shipdoc.invoicequantity, shipentry.materialname,
            shipentry.materialname2, shipentry.materialname3,
            shipdoc.invoiceamt,shipdoc.containerno, strftime('%d-%m-%Y', shipentry.confirmationdate) as confirmationdate, shipdoc.transittime, shipdoc.portofarrival
        FROM 
            shipdoc
        LEFT JOIN 
            shipentry 
        ON 
            shipdoc.pono = shipentry.pono
    """)
    lala = my_cursor.fetchall()
    combined_data = []

  
    for row in lala:
        material_name = row[5]
        price = None
        if material_name == row[7]:
            price = row[6]
        elif material_name == row[8]:
            price = row[8]
        elif material_name == row[9]:
            price = row[10]

        entry = {
            
            "pono": row[0],
            "invno": row[1],
            "supp_name": row[2],
            "origin": row[3],
            "csn": row[4],
            "material_name": material_name,
            "inv_qty": row[6],
            "invamt": row[10],
            "contno": row[11],
            "confirmdate": row[12],
            "time": row[13],
            "port": row[14]
        }
        combined_data.append(entry)

    connection.close()

    return render_template('month_item.html',combined_data=combined_data)

@app.route('/LPR_month')
def LPR_month():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("""
        SELECT 
            shipdoc.PONO,shipdoc.invoiceno, shipdoc.BLNO, portclear.BLNO,shipentry.suppliername,shipentry.origin,shipentry.contractsalesno,
            shipdoc.material, shipdoc.invoicequantity, shipentry.materialname,
            shipentry.materialname2, shipentry.materialname3,
            shipdoc.invoiceamt,shipdoc.containerno, shipdoc.portofarrival,strftime('%d-%m-%Y', shipdoc.eta) as eta, portclear.loadedprice
        FROM 
            shipdoc
        INNER JOIN 
            portclear
        ON 
            shipdoc.BLNO = portclear.BLNO
        LEFT JOIN 
            shipentry 
        ON 
            shipdoc.pono = shipentry.pono
        AND 
            shipentry.pono = portclear.pono;
    """)
    lala = my_cursor.fetchall()
    combined_data = []

  
    for row in lala:
        material_name = row[7]
        price = None
        if material_name == row[9]:
            price = row[6]
        elif material_name == row[10]:
            price = row[8]
        elif material_name == row[11]:
            price = row[10]

        entry = {
            
            "pono": row[0],
            "blno": row[3],
            "invno": row[1],
            "supp_name": row[4],
            "origin": row[5],
            "csn": row[6],
            "material_name": material_name,
            "inv_qty": row[8],
            "invamt": row[12],
            "contno": row[13],
            "eta": row[15],
            "lpr": row[16],
            "port": row[14]
        }
        combined_data.append(entry)

    connection.close()

    return render_template('LPR_month.html',combined_data=combined_data)


# Master routes------------------------

@app.route('/supplierentry', methods=['POST'])
def supplierentry():

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    email2 = request.form['email2']
    email3 = request.form['email3']
    email4 = request.form['email4']
    email5 = request.form['email5']

    address = request.form['address']
    

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO supplier VALUES(?,?,?,?,?,?,?,?)", (name,phone,email,email2,email3,email4,email5,address))

    connection.commit()
    connection.close()
    return redirect(url_for('suppliermaster'))

@app.route('/suppliermaster')
def suppliermaster():

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala = my_cursor.execute("Select name,phone,email,email2,email3,email4,email5,address from supplier").fetchall()

    return render_template('suppliermaster.html',lala=lala)


@app.route('/indentorentry', methods=['POST'])
def indentorentry():

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']
    

    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO indentor VALUES(?,?,?,?)", (name,phone,email,address))

    connection.commit()
    connection.close()
    return redirect(url_for('indentormaster'))


@app.route('/indentormaster')
def indentormaster():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala = my_cursor.execute("Select * from indentor").fetchall()
    return render_template('indentormaster.html',lala=lala)


@app.route('/materialmaster')
def materialmaster():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala = my_cursor.execute("Select * from material").fetchall()
    return render_template('materialmaster.html',lala=lala)


@app.route('/materialentry', methods=['POST'])
def materialentry():

    name = request.form['name']
    hscode = request.form['hscode']
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO material VALUES(?,?)", (name,hscode))

    connection.commit()
    connection.close()
    return redirect(url_for('materialmaster'))

@app.route('/shiplinemaster')
def shiplinemaster():
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    lala = my_cursor.execute("Select * from shipline").fetchall()
    return render_template('shiplinemaster.html',lala=lala)

@app.route('/shiplineentry', methods=['POST'])
def shiplineentry():
    name = request.form['name']
    connection = sqlite3.connect('master.db')
    my_cursor = connection.cursor()
    my_cursor.execute("INSERT INTO shipline VALUES(?)", (name,))
    connection.commit()
    connection.close()
    return redirect(url_for('shiplinemaster'))

@app.context_processor
def utility_processor():
    def zip_lists(a, b, c):
        return zip(a, b, c)
    return dict(zip_lists=zip_lists)

@app.context_processor
def utility_processor():
    def zip_lists_2(a, b):
        return zip(a, b)
    return dict(zip_lists_2=zip_lists_2)


if __name__ == '__main__':
    app.run(debug=True)
