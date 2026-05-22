let balance = 1000

function spin(){

    let symbols = ["🍒","💎","7️⃣","⭐","🍋"]

    let a = symbols[Math.floor(Math.random()*5)]
    let b = symbols[Math.floor(Math.random()*5)]
    let c = symbols[Math.floor(Math.random()*5)]

    document.getElementById("slot1").innerHTML = a
    document.getElementById("slot2").innerHTML = b
    document.getElementById("slot3").innerHTML = c

    let result = document.getElementById("result")

    if(a === b && b === c){

        balance += 500

        result.innerHTML = "🔥 JACKPOT +$500"

    } else {

        balance -= 100

        result.innerHTML = "😢 Lost $100"
    }

    document.querySelector(".balance").innerHTML =
        `Balance: $${balance}`
}