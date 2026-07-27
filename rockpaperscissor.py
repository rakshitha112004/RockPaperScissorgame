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

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,Helvetica,sans-serif;
}

body{
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:linear-gradient(-45deg,#4facfe,#00f2fe,#43e97b,#38f9d7);
background-size:400% 400%;
animation:bg 10s ease infinite;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.container{
width:700px;
max-width:95%;
background:rgba(255,255,255,.15);
backdrop-filter:blur(18px);
padding:35px;
border-radius:25px;
text-align:center;
color:white;
box-shadow:0 20px 50px rgba(0,0,0,.3);
}

h1{
font-size:40px;
margin-bottom:10px;
}

.subtitle{
margin-bottom:30px;
font-size:18px;
}

.buttons{
display:flex;
justify-content:center;
gap:20px;
flex-wrap:wrap;
}

button{
width:150px;
height:150px;
font-size:60px;
border:none;
border-radius:20px;
cursor:pointer;
transition:.3s;
background:white;
}

button:hover{
transform:translateY(-8px) scale(1.05);
box-shadow:0 10px 20px rgba(0,0,0,.4);
}

.choice-box{
display:flex;
justify-content:space-around;
margin-top:35px;
}

.card{
width:220px;
background:rgba(255,255,255,.15);
padding:20px;
border-radius:20px;
}

.emoji{
font-size:80px;
margin-top:15px;
}

.result{
margin-top:30px;
font-size:32px;
font-weight:bold;
}

.win{
color:#00ff88;
}

.lose{
color:#ff5252;
}

.tie{
color:#ffe082;
}

.score{
margin-top:35px;
display:flex;
justify-content:space-around;
}

.score div{
background:rgba(255,255,255,.2);
padding:15px;
border-radius:15px;
width:150px;
font-size:22px;
}

.play{
margin-top:30px;
padding:12px 25px;
font-size:18px;
background:#ff9800;
color:white;
border:none;
border-radius:10px;
cursor:pointer;
}

.play:hover{
background:#fb8c00;
}

</style>

</head>

<body>

<div class="container">

<h1>🎮 Rock Paper Scissors</h1>
<p class="subtitle">Choose your weapon!</p>

<form method="POST">

<div class="buttons">

<button name="choice" value="rock">🪨</button>

<button name="choice" value="paper">📄</button>

<button name="choice" value="scissors">✂️</button>

</div>

</form>

{% if user %}

<div class="choice-box">

<div class="card">
<h2>You</h2>
<div class="emoji">{{user_emoji}}</div>
</div>

<div class="card">
<h2>Computer</h2>
<div class="emoji">{{computer_emoji}}</div>
</div>

</div>

<div class="result
{% if 'Win' in result %}
win
{% elif 'Tie' in result %}
tie
{% else %}
lose
{% endif %}
">
{{result}}
</div>

<form action="/">
<button class="play">Play Again</button>
</form>

{% endif %}

<div class="score">

<div>
🏆<br>
Player<br>
<b>{{player}}</b>
</div>

<div>
💻<br>
Computer<br>
<b>{{computer}}</b>
</div>

<div>
🤝<br>
Tie<br>
<b>{{tie}}</b>
</div>

</div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    global player_score, computer_score, tie_score

    user = None
    user_emoji = ""
    computer_emoji = ""
    result = ""

    if request.method == "POST":

        user = request.form["choice"]
        computer = random.choice(list(choices.keys()))

        user_emoji = choices[user]
        computer_emoji = choices[computer]

        if user == computer:
            result = "🤝 It's a Tie!"
            tie_score += 1

        elif (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
        ):
            result = "🎉 You Win!"
            player_score += 1

        else:
            result = "💻 Computer Wins!"
            computer_score += 1

    return render_template_string(
        html,
        user=user,
        user_emoji=user_emoji,
        computer_emoji=computer_emoji,
        result=result,
        player=player_score,
        computer=computer_score,
        tie=tie_score
    )

if __name__ == "__main__":
    app.run(debug=True)
