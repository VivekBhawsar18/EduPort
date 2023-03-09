from flask import render_template , Blueprint , request , flash , session
from config import Config

bp = Blueprint('authentication' , __name__ , static_folder='static' , template_folder='auth_temps')


"""Class for handling OTP generation and updates."""
class otp:
    def __init__(self, otp=000000):
        """Initialize the object with the given OTP value."""
        self.otp = otp

    def update_otp(self, new_otp):
        """Method to update the OTP value."""
        self.otp = new_otp
        return self.otp

# Creating an object of the otp class
obj = otp()

@bp.route('/sign-in')
def signIn():

    return render_template('sign-in.html')

@bp.route('/sign-up', methods=['GET' , 'POST'])
def signUp():

    if request.method=='POST':

        # Extract the user input data from the request form
        email = request.form.get('e-mail')
        password = request.form.get('password')
        cnf_password = request.form.get('cnf-password')

        print(email,password,cnf_password)

        # Confirm password
        if password==cnf_password:
            return '<h1>True</h1>'
        return '<h1>False</h1>'
        # # Convert the name to upper case
        # name = name.upper()

        # # Check if the email or contact is already registered in the database
        # userEmail= User.query.filter_by(email=email).first()
        # userContact= User.query.filter_by(contact=contact).first()

        # # If the email is already registered, send a flash message to the user
        # if  userEmail:
        #     flash("Email is already registered","warning")
        #     return redirect(url_for('user.user_signup'))
        
        # # If the contact is already registered, send a flash message to the user
        # if userContact:
        #     flash("Contact No. is already registered","warning")
        #     return redirect(url_for('user.user_signup'))           

        # # Generate a new OTP and send it to the user via email
        # new_otp = randint(000000,999999)
        # obj.update_otp(new_otp)


        # msg = Message(
        #                 f'Verify your email {new_otp}',
        #                 sender = var.MAIL_SENDER,
        #                 recipients = [email]
        #                 )

        # msg.html = render_template('email/signupOtp.html' , name=name , sentotp=new_otp)

        # mail.send(msg)

        # # Save the user input data to the session
        # session['data'] = 'secure_data'
        # session['name']=name
        # session['contact']=contact
        # session['email']=email
        # session['gender']=gender
        # session['address']=address

        # # Send a flash message to the user to indicate that the OTP has been sent
        # flash("OTP sent" , "success")
        # return render_template('verify/signupVerification.html')

    # If the request method is GET, return the userSignup.html template
    return render_template('sign-up.html')