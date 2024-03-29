// Key concepts covered:

// objects
// DOMContentLoaded
// addEventListener()
// array.length
// textContent

const persons1 = {
    author: "James weldon",
    job: "backend engineer",
    info: "As a seasoned software backend engineer, I excel in designing robust architectures, optimizing performance, and implementing scalable solutions. My expertise lies in crafting efficient code that powers seamless and reliable applications.",
}

const persons2 = {
    author: "Adin Johnson",
    job: "frontend engineer",
    info: "My job title is junior software backend engineer and I know C++ and C#",
}



const forward = document.getElementById("forward")
forward.addEventListener("click", function(){
    console.log("forward click");
    let author = document.getElementById("author").textContent;
    console.log(`${author}`);
})

const backward = document.getElementById("backward")
backward.addEventListener("click", function(){
    console.log("backward click");
})