import java.util.Arrays;
import java.util.List;
import java.util.Stack;

import org.junit.Test;

public class GetNearLess {
    
    @Test
    public void getNearLessNoRepeatTest(){
        int[] arr = {3,4,1,5,6,2,7};
        
        int[][] res = null;
        res = getNearLessNoRepeat(arr);
        
        for(int[] lis:res){
            System.out.print(Arrays.toString(res));
        }
        
        
    }
    
    
    public int[][] getNearLessNoRepeat(int[] arr){
        int[][] res = new int[arr.length][2];
        
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0;i<arr.length;i++){
            while(!stack.isEmpty() && arr[i] < arr[stack.peek()]){
                int popIndex = stack.pop();
                int left = stack.isEmpty() ? -1:stack.peek();
                res[popIndex][0] = left;
                res[popIndex][1] = i;
            }
            stack.push(i);
        }
        
        while (!stack.isEmpty()){
            int popIndex = stack.pop();
            int left = stack.isEmpty() ? -1:stack.peek();
            res[popIndex][0] = left;
            res[popIndex][1] = -1;
        }
        return res;
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    public int[][] getNearLessRepeat(int[] arr){
        int[][] res = new int[arr.length][2];
        
        Stack<List<Integer>> stack = new Stack<>(); 
        
        for(int i = 0; i < arr.length; i++){
            while(!stack.isEmpty() && arr[stack.peek().get(0)] > arr[i]){
                List<Integer> PopIs = stack.pop(); 
                int leftLessIndex = stack.isEmpty() ? -1:stack.peek().get(stack.peek().size()-1);
                
                for(Integer popi:popIs){
                    res[popi][0] = leftLessIndex;
                    res[popi][1] = i;
                }
            }
            if(!stack.isEmpty() && arr[stack.peek().get(0)] == arr[i]){
                stack.peek().add(Integer.valueOf(i));
            } else {
                
            }
        }
        
    }
    
}
