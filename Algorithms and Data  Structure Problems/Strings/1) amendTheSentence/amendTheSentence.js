function amendTheSentence(s) {
    for(var i = 0; i < s.length; i++){
        if(s[i] == s[i].toUpperCase()){
            if(i != 0){
                var space = " ";
                console.log(s);
                s = [s.slice(0, i) + space + s.slice(i)].join("");
                i++
            }
        }
    }
    s = s.toLowerCase();
    return s;
}