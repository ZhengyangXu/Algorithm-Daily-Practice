import java.util.LinkedList;

import org.junit.Test;

public class MaxMin{
    
    @Test
    public int test(){
        int[] arr = {1,2,3,4,5,6,7,8};
        int num = 4;
        
        return getNum(arr,num);
    }
    
    public static int getNum(int[] arr, int num){
        if (arr == null || arr.length == 0 || num < 0){
            return 0;
        }
        
        LinkedList<Integer> qmin = new LinkedList<Integer>();
        LinkedList<Integer> qmax = new LinkedList<Integer>();
        
        int i = 0;
        int j = 0;
        
        int res = 0;
        
        while (i < arr.length){
            while (j < arr.length){
                if(qmin.isEmpty() || amin.peekLast() != j ){
                    while (!qmin.isEmpty() && arr[qmin.peekLast()] >= arr[j]){
                        qmin.pollLast();
                    }
                    qmin.addLast(j);
                    while(!qmax.isEmpty() && arrr[qmax.peekLast()] <= arr[j]){
                        qmax.pollLast();
                    }
                    qmax.pollLast();
                }
                if (arr[qmax.getFirst()] - arr[qmin.getFirst()] > num){
                    break;
                }
                j++;
            }
                   res += j -i;
                   if (qmin.peekFirst() == i){
                       qmin.pollFirst();
                   } 
                   if (qmax.peekFirst() == i){
                       qmax.pollFirst();
                   }
                   i++;
        }
                   return res;
        
    }
    
}