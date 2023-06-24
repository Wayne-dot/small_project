// search, add, edit, and delete items

// let add = document.getElementById("add");
// add.addEventListener("click"), function(){
//     console.log("Hello worl")
// };


// javascript object
const car1 = {



    // properties
    model: "Honda",
    color: "blue",

    // this keyword
    // this in this context is car1
    drive : function(){
        console.log(`You are driving ${this.model}now`);
    },
}

// javascript class
class Player{
    // static keyword - properties for the class
    // static function_name(){}
    static number_of_player = 0;

    // each object, unique value for each object
    constructor(age){
        this.age = age;
        Player.number_of_player += 1;
        console.log(Player.number_of_player);
    }
    score = 0;

    showage(){
        console.log(`The age of the car is ${this.age}`)
    }

    pause(){
        console.log("You pause the game");
    }

    exit(){
        console.log("You exit the game");
    }
}


const player1 = new Player(34);
const player2 = new Player(34);
const player3 = new Player(34);
const player4 = new Player(34);
player1.score += 1


console.log(player1.score)
player1.showage()



class animal{
    alive = true;

    constructor(age){
        this.age = age;
    }

    eat(){
        console.log(`This ${this.name} is eating`)
    }
}

// inherace from animal class
class fish extends animal{
    name = "fish";

    constructor(age){
        // use constructer of the parent class
        super(age);
    }
}


const Fish = new fish;
Fish.eat()





class Car{
    constructor(power){
        this._gas = 25;
        this._power = power;
    }
    get power(){
        return `${this._power}hp`;
    }
    get gas(){
        return `${this._gas} (${this._gas / 50 * 100}%)`
    }
    set gas(value){
        this._gas = value;
    }
}

// don't have to be name, can be just new Car(400)
let car = new Car(400);
// 400 will un change

console.log(car.power)



// Error and handling
try{
    let x = window.prompt("Enter a #");

    if (isNaN(x)) throw "That wasn't a number";
    if(x == "") throw "That was empty!";

    console.log(`${x} is not a number`);
}

catch(error){
    console.log(error);
}

finally{
    console.log("This always execute");
}


// Synchronous vs asynchronous



// track how long synchronous method take
console.time("Response time")

alert("click")
console.timeEnd("Response time")


// Promise
const promise = new Promise((resolve, reject) => {
    let fileload = true;
    if(fileload){
        resolve("file loaded")
    }
    else{
        reject("file NOT loaded")
    }
});

promise.then(
    function(value) { /* code if successful */ },
    function(error) { /* code if some error */ }
);





// async funcction
async function loadFile(){
    let fileload = true;
    if(fileload){
        return "file loaded";
        // if asyn function is just function
        // return Promise.resolve("File loaded")
    }
    else{
        return "file NOT loaded";
    }
}

loadFile().then(value => console.log(value))
        .catch(error => console.log(error));





// await keyword
// wait for the resolve promise before execute
async function myDisplay() {
    let myPromise = new Promise(function(resolve) {
      setTimeout(function() {resolve("I love You !!");}, 3000);
    });
    document.getElementById("demo").innerHTML = await myPromise;
  }
  
myDisplay();
  
  

import { pi, getCircumference } from "./math.js";
// import * as Mathutil from "./math.js";
// Mathutil.pi
console.log(pi);

let circumference = getCircumference(10);
console.log(circumference)


// document.title = "this is a cool title"

// querySelector("#classname")

// use textContent, not innerHTML (XSS attacks)
// const nameTag = document.createElement("h1")
// nameTag.textContent = "Bro hello world"

// change CSS properties
// nameTag.style.something

const myButton = document.getElementById("myButton");
const myAnimation = document.getElementById("myDiv");

myButton.addEventListener("click", begin)

function begin(){
    let timerID = null;
    let x = 0;
    let y = 0;

    timerID = setInterval(frame, 5);

    function frame(){
        if(x> 200){
            clearInterval(timerID)
        }
        else{
            x += 1;
            myAnimation.style.left = x + "px";
        }

    }
}


