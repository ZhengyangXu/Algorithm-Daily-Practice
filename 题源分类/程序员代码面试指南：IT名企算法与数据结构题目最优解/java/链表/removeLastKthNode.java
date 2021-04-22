// # 在单链表和双链表中删除倒数第K个节点
// # 【题目】分别实现两个函数，一个可以删除单链表中倒数第K个节点，
// # 另一个可以删除双链表中倒数第K个节点。
// # 【要求】如果链表长度为N，时间复杂度达到O（N），
// # 额外空间复杂度达到O（1）。
// # 【难度】士 ★☆☆☆

public class removeLastKthNode {

    class Node {
        public int value;
        public Node next; //

        public Node(int value) {
            this.value = value;
        }
    }

    public Node removeLastKthNode(Node head, int k) {
        
        if (head == null || k < 1){
            return head;
        }
        
        Node cur = head;
        
        while (cur != null){
            k--;
            cur = cur.next;
        }
        
        if(k == 0){
            head = head.next;
        }
        if (k > 0){
            cur = head;
            while (++k != 0){
                cur = cur.next;
            }
            cur.next = cur.next.next;
        }
        return head;
    }
    
    class DoubleNode{
        public int value;
        public DoubleNode last;
        public DoubleNode next;
        
        public DoubleNode(int value){
            this.value = value;
        }
    }
    
    public DoubleNode removeLastKthDoubleNode(DoubleNode head,int k){
        if(head == null || k < 1){
            return head;
        }
        DoubleNode cur = head;
        while (cur != null){
            --k;
            cur = cur.next;
        }
        if (k == 0){
            head = head.next;
            head.last = null;
            
        }
        if (k < 0){
            cur = head;
            while(++k != 0){
                cur = cur.next;
            }
            DoubleNode newNext = cur.next.next;
            cur.next = newNext;
            if (newNext != null){
                newNext.last = cur;
            }
        }
        return head;
    }

}
