int firstDuplicate(int[] a) {
    int value = -1;
    Dictionary<int, int> nums = new Dictionary<int,int>();
    for(int i = 0; i < a.Length; i++){
        if(nums.ContainsKey(a[i])){
            value = a[i];
            break;
        }
        nums.Add(a[i], 1);
    }
    return value;
}