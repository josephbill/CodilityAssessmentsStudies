const readline = require('readline');

let numerals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function computerguess(arr) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    let low = 0;
    let high = arr.length - 1;

    const askQuestion = (question) => {
        return new Promise((resolve) => {
            rl.question(question, answer => {
                resolve(answer);
            });
        });
    };

    const guessLoop = async () => {
        while (low <= high) {
            console.log("Operation low is", low, "Operation high is", high);

            let midvalue = Math.floor((low + high) / 2);
            console.log("The computer has guessed", arr[midvalue]);

            let usersInput = await askQuestion("Is the computer guess high, low, or correct? ");

            if (usersInput === 'c') {
                rl.close();
                return `The guess is correct, value is ${arr[midvalue]}`;
            }

            if (usersInput === 'h') {
                high = midvalue - 1;
            } else if (usersInput === 'l') {
                low = midvalue + 1;
            }
        }
        rl.close();
        return "No more guesses possible.";
    };

    return guessLoop();
}

computerguess(numerals).then(result => console.log(result));
