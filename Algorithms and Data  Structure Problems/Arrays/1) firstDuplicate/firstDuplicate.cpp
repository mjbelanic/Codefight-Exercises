int firstDuplicate(std::vector<int> a) {
    int value = -1;
    std::unordered_map<int,int>nums;
    for(int i = 0; i < a.size(); i++){
        if(nums.find(a[i]) != nums.end()){
                value = a[i];
                break;
            }
        nums[a[i]] = 1;
        }        
    return value;
}