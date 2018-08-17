function Bogosort(flag){
    var arrLen = flag.length;

    var attemptArr = [];

    while (!arraysEqual(attemptArr,flag)) {
        attemptArr=genArr(arrLen);
    }

    flagString = "";

    for(var i = 0; i < attemptArr.length; i++) {
        flagString += String.fromCharCode(attemptArr[i]);
    }

    console.log(flagString);
}

    function genArr(lenArr){
        var arr = [];

        for(var i = 0; i < lenArr; i++) {
            arr.push(Math.floor(Math.random() * (125 - 45 + 1)) + 45);
        }

        return arr;
    }

    function arraysEqual(arr1, arr2) {
        if(arr1.length !== arr2.length)
            return false;
        for(var i = arr1.length; i--;) {
            if(arr1[i] !== arr2[i])
                return false;
        }
    
        return true;
    }


var flag = [102,108,97,103,123,115,52,118,51,100,95,109,121,95,98,114,52,105,110,95,102,114,48,109,95,98,48,103,48,125];
Bogosort(flag);