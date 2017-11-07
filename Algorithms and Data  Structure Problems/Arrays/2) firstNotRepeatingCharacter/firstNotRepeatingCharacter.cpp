char firstNotRepeatingCharacter(std::string s) {
    char value = '_';
    std::unordered_map<char, int> letters;
    string copy = s;
    std::sort(s.begin() , s.end());
    for(int i = 0; i < s.size(); i++){
        if(s[i] != s[i-1] && s[i] != s[i+1]){
            letters[s[i]] = 1;
        }
    }
    for(int j = 0; j < copy.size(); j++){
        if(letters.find(copy[j]) != letters.end()){
            value = copy[j];
            return value;
        }
    }
    return value;
}