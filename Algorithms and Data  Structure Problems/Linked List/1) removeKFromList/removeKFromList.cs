// Definition for singly-linked list:
// class ListNode<T> {
//   public T value { get; set; }
//   public ListNode<T> next { get; set; }
// }
//
ListNode<int> removeKFromList(ListNode<int> l, int k) {
    ListNode<int> prev = null;
    var current = l;
    
    if(current == null){
        return null;
    }
    while(current != null){
        if(current.value == k){
            if(prev == null){
                current = current.next;
                l = current;
            }else{
                prev.next = current.next;
                current = current.next;
            }
        }else{
            prev = current;
            current = current.next;
        }
    }
    return l;
}