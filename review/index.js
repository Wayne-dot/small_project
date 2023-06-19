// Key concepts covered:

// objects
// DOMContentLoaded
// addEventListener()
// array.length
// textContent


const forward = document.getElementById("forward")
forward.addEventListener("click", function(){
    console.log("forward click");
})

const backward = document.getElementById("backward")
backward.addEventListener("click", function(){
    console.log("backward click");
})