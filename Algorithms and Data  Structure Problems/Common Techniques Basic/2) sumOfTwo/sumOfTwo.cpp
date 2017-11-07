bool sumOfTwo(std::vector<int> a, std::vector<int> b, int v) {
    int neededValue;
    std::unordered_map<int, int> nums;
    for (int i = 0; i < a.size(); i++) {
        neededValue = v - a[i];
        nums[neededValue] = 1;
    }
    for(int j = 0; j < b.size(); j++){
        if(nums.find(b[j]) != nums.end()){
            return true;
        }
    }
    return false;  
}