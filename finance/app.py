import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if not session["user_id"]:
        return render_template("login.html")
    try:
        stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])
        cash_db = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash_db[0]["cash"]
        total_value = cash
        for stock in stocks:
            stock_info = lookup(stock["symbol"])
            stock["name"] = stock_info["name"]
            stock["price"] = stock_info["price"]
            stock["value"] = stock["total_shares"]*stock["price"]
            total_value += stock["value"]
        return render_template("index.html", stocks=stocks, cash=cash, total_value=total_value)
    except:
        return apology("Error occurred, Please try again", 500)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        stock_info = {
                "symbol" : "",
                "name" : "",
                "price" : 0
            }
        return render_template("buy.html", stock_info=stock_info)

    if request.method == "POST":
        if request.form.get("symbol_search"):
            symbol = request.form.get("symbol_search").upper()
        else :
            symbol = request.form.get("symbol").upper()

        stock_info = lookup(symbol)

        if not stock_info:
            return apology("Invalid symbol", 400)
        print("int(request.form.get(shares)) :", request.form.get("shares"))

        if request.form.get("shares") != "":
            try:
                shares = int(request.form.get("shares"))
            except ValueError:
                return apology("Shares must be number", 400)

            if shares <= 0:
                return apology("Shares must be positive integer", 400)

            total_cost = stock_info["price"]*shares
            user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            user_cash = user_cash_db[0]["cash"]

            if total_cost > user_cash:
                return apology("Not enough cash", 400)

            db.execute("INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)", session["user_id"], symbol, shares, stock_info["price"], datetime.now())
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, session["user_id"])
            if db.execute("SELECT symbol FROM stocks WHERE symbol = ? AND user_id = ?", symbol, session["user_id"]):
                db.execute("UPDATE stocks SET shares = shares + ? WHERE symbol = ? AND user_id = ?", shares, symbol, session["user_id"])
            else:
                db.execute("INSERT INTO stocks (user_id, symbol, shares) VALUES (?, ?, ?)", session["user_id"], symbol, shares)

            return redirect("/")
        else:
            return render_template("buy.html", stock_info=stock_info)



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id = ? ORDER BY timestamp DESC", session["user_id"])
    for transaction in transactions:
        transaction["price"] = usd(transaction["price"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock_info = lookup(symbol)
        if not stock_info:
            return apology("Invalid symbol", 400)
        return render_template("quoted.html", name=stock_info["name"], symbol=stock_info["symbol"], price=usd(stock_info["price"]))
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Please provide username!", 400)
        elif not request.form.get("password"):
            return apology("Please provide password!", 400)
        elif not request.form.get("confirmation"):
            return apology("Please enter the password again to confirm it", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password does not match", 400)

        hashed_password = generate_password_hash(request.form.get("password"))
        username = request.form.get("username")
        username_exists = db.execute("SELECT * FROM users WHERE username = ?", username)

        if (len(username_exists) > 0):
            return apology("username already exists", 400)

        user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed_password)
        session["user_id"] = user_id
        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbols = db.execute("SELECT symbol FROM stocks WHERE user_id = ? AND shares > 0", session["user_id"])
        if not symbols:
            return apology("You dont have any stock to sell", 400)
        return render_template("sell.html", symbols=symbols)

    else:
        if not request.form.get("symbol"):
            return apology("Not valid symbol", 400)
        if not lookup(request.form.get("symbol")):
            return apology("Not valid symbol", 400)

        symbol = request.form.get("symbol")

        if not request.form.get("shares"):
            return apology("Nothing to sell", 400)
        if int(request.form.get("shares")) <= 0:
            return apology("Share must be 1 or greater", 400)

        shares_to_sell = int(request.form.get("shares"))

        shares_db = db.execute("SELECT shares FROM stocks WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        shares = shares_db[0]["shares"]

        if shares_to_sell > shares:
            print(f"shares_to_sell: {shares_to_sell}, shares: {shares}")
            return apology("You dont have enough stocks to sell", 400)

        stock_info = lookup(symbol)
        sell_price = stock_info["price"]
        sale_price = sell_price*shares_to_sell
        db.execute("UPDATE stocks SET shares = shares - ? WHERE symbol = ? AND user_id = ?", shares_to_sell, symbol, session["user_id"])
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", sale_price, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)", session["user_id"], symbol, (-1)*shares_to_sell, stock_info["price"], datetime.now())


    return redirect("/")