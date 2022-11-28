//create the template for our objects 
//the template should always be the knows 
function areaTriangle(base,height){
     this.base = base;
     this.height = height;
}

//formulae 
areaTriangle.prototype.Area = function(){
    let area  = 0.5 * this.base * this.height;
    return area;
}


let newTriangle = new areaTriangle(10,20);
console.log(newTriangle.Area().toFixed(4))