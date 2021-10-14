// var a = 'abc'  // var 声明变量，b=赋值
// a = 123
// console.log(a);

// let c = 'qwe' // let c 声明变量，ES6的新语法，推荐使用
// console.log(c);

// let e       // 只声明，未赋值，不会报错，会输出undefined
// console.log(e);

// const f = 200   // 声明常量，const在声明时必须赋初始值
// console.log(f);


// console.log("-----------分割线 --------------");
// console.log(a='a'+1,a+2);


// console.log("-----------字符串string--------------");
// console.log(a=3+'mage',typeof(a));
// console.log(a=null+'mage',typeof(a));
// console.log(a=undefined+'mage',typeof(a));
// console.log(a=true+'mage',typeof(a));  


// console.log("-----------数字number--------------");
// /**
//  * parseInt 截取整数部分，python int
//  * Math.floor 向下取整
//  * Math.ceil 向上取整
//  * Math.round  四舍六入，五右侧最近整数
//  */
// let numbers = [0.1,0.6,2.2,2.9,3.49999,3.500001]
// for (let x of numbers){
//     console.log(x,parseInt(x))
// }
// console.log("----------------------------");
// for (let x of numbers){
//     console.log(x,Math.floor(x));
//     console.log(x,Math.ceil(x));
// }



// console.log("-----------json 的in 属性--------------");

// let arr = [1, 2, 3, 4, 5] //下标索引：0-1，1-2……

// console.log(1 in arr)
// console.log(3 in arr)
// console.log(5 in arr)   // false , 因为arr 这个列表中没有下标为5的属性
// console.log('length' in arr) // json 中的in属性，是问有没有这个属性，而不是元素


// let obj ={
//     'a':1,
//     'b':'abc'
// }

// console.log('a' in obj)     // true
// console.log('b' in obj)     // true
// console.log('abc' in obj)   // false


// /**
//  * 和python 不一样的地方，js中通过索引删除列表元素，
//  * 列表长度不变，每个元素索引不变，
//  * 只不过被删除元素变为 undefined
// */
// for (var i=0;i<arr.length;i++){
//     console.log(i, arr[i])
// }

// console.log(delete arr[2]);  

// for (var i=0;i<arr.length;i++){
//     console.log(i, arr[i])
// }



// /**
//  * for 循环
//  * i++ 先用后加
//  * ++i 先加后用
//  */
// for (let i=0;i <5; i++){
//     console.log(++i)      
// }


let x = 10;
while (x--) {
    console.log(x);
}
console.log('=============')
do {
    console.log(x)
}while(x++<10)