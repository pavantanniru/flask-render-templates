from flask  import Flask ,redirect ,url_for,render_template,request
app = Flask(__name__)


@app.route('/')

def home():
       
       return render_template('base.html')
    
@app.route('/signup')
def signup():
      return render_template('puppy.html')

@app.route('/tank_yo')

def tank_you():
       
       first = request.args.get('fna')
       last = request.args.get('lna')
       
       
       
       
       return render_template('tanku.html',first=first,last=last)
    
@app.errorhandler(404)
def page_not_found(error):
       return '<h1>page not Found !</h1>'
            
         
if __name__ == '__main__':
   app.run(debug=True)
   

