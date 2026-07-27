from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

player_score = 0
computer_score = 0
tie_score = 0

html = """
<!DOCTYPE html>
<html>
<head>
<title>Rock Paper Scissors</title>

<style>

body{
    margin:0;
    font-family:Arial;
    background:linear-gradient(135deg,#4facfe,#00f2fe);
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}

.container{
    width:500px;
    background:rgba(255,255,255,.2);
    backdrop-filter:blur(15px);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0 10px 25px rgba(0,0,0,.3);
}

h1{
    margin-bottom:20px;
}

button{
    padding:15px 20px;
    margin:10px;
    font-size:18px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    transition:.3s;
    background:#ff9800;
    color:white;
}

button:hover{
    transform:scale(1.08);
    background:#ff6f00;
}

.choice{
    font-size:60px;
}

.result{
    font-size:28px;
    margin-top:20px;
}

.score{
    margin-top:25px;
    font-size:20px;
    background:rgba(255,255,255,.2);
    padding:10px;
    border-radius:10px;
}

</style>

</head>

<body>

<div class="container">

<h1>🎮 Rock Paper Scissors 🎮</h1>

<form method="POST">

<button name="choice" value="rock">🪨 Rock</button>

<button name="choice" value="paper">📄 Paper</button>

<button name="choice" value="scissors">✂️ Scissors</button>

</form>

{% if user %}

<hr>

<h2>Your Choice</h2>
<div class="choice">{{ user_emoji }}</div>

<h2>Computer Choice</h2>
<div class="choice">{{ computer_emoji }}</div>

<div class="result">{{ result }}</div>

{% endif %}

<div class="score">

🏆 Player : {{ player }} <br><br>

💻 Computer : {{ computer }} <br><br>

🤝 Tie : {{ tie }}

</div>

</div>

</body>

</html>
"""

@app.route("/", methods=["GET","POST"])
def home():

    global player_score
    global computer_score
    global tie_score

    user = None
    computer = None
    result = None
    user_emoji = ""
    computer_emoji = ""

    if request.method == "POST":

        user = request.form["choice"]
        computer = random.choice(list(choices.keys()))

        user_emoji = choices[user]
        computer_emoji = choices[computer]

        if user == computer:
            result = "🤝 It's a Tie!"
            tie_score += 1

        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):

            result = "🎉 You Win!"
            player_score += 1

        else:
            result = "💻 Computer Wins!"
            computer_score += 1

    return render_template_string(
        html,
        user=user,
        computer=computer_score,
        player=player_score,
        tie=tie_score,
        result=result,
        user_emoji=user_emoji,
        computer_emoji=computer_emoji
    )

if __name__ == "__main__":
    app.run(debug=True)