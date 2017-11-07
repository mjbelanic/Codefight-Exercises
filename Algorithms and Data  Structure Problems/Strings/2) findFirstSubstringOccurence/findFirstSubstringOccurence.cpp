int findFirstSubstringOccurrence(std::string s, std::string x) {
    if(x.size()>s.size())return -1;
    for(int i=0; i<s.size()-x.size()+1; ++i){
        if(s[i]==x[0] && s[i+x.size()-1]==x[x.size()-1]){
            string temp(s.begin()+i, s.begin()+i+x.size());
            if(temp==x)
                return i;
        }
    }
    return -1;
}