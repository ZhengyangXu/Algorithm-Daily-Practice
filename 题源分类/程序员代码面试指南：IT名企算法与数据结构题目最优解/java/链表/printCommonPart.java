public class printCommonPart {
    
    Class Node {
        public int val;
        public Node next;
        public Node(int val){
            this.val = val;
        }
    }
    
    public void printCommonPart(Node node1,Node node2){
        
        System.out.println("common part:");
        
        while (head1 != null && head2 != null){
            if (head1.val < head2.val){
                head1 = head1.next;
            } else if (head.val > head2.val){
                head2 = head.next;
            }  else{
                System.out.println(head1.val+"");
                head1 = head1.next;
                head2 = head2.next;
            }
        }        
    }
    
}
