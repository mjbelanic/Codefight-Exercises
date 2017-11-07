bool containsDuplicates(std::vector<int> a) {
    if(a.size() == 0){
        return false;
    }
    std::unordered_map<int, int> nums;
    for (int i = 0; i < a.size(); i++) {
        if (nums.find(a[i]) != nums.end()){
            return true;
        }
        nums[a[i]] = 1;
    }
    return false;  
}