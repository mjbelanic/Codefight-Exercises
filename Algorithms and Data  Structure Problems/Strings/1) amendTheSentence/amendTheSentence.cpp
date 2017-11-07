std::string amendTheSentence(std::string s) {
    string replacement;
    for(int i = 0 ;  i < s.size(); ++i){
        if(s[i]>='A' && s[i]<='Z'){
            if(i!= 0){
                replacement+=" ";
            }
            replacement+=char(s[i]+32);
            continue;
        }
        replacement += s[i];
    }
    return replacement;
}