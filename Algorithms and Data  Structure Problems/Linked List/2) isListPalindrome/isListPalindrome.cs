// Definition for singly-linked list:
// class ListNode<T> {
//   public T value { get; set; }
//   public ListNode<T> next { get; set; }
// }

bool isListPalindrome(ListNode<int> l) {
    Stack<int> checker = new Stack<int>();
     var current = l;
    
    if(current == null){
        return true;
    }
    while(current != null){
        checker.Push(current.value);
        current = current.next;
    }
    while(l != null){
        if(l.value != checker.Pop()){
            return false;
        }
        l = l.next;
     }
    return true;
}