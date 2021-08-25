package BinarySearch;
//1111222222444444查找不小于2的数的最左侧位置
public class BSNearLeft {
    public static void main(String[] Args){

    }

    public static int bsNearLeft(int[] arr,int value){
        int left = 0;
        int right = arr.length - 1;
        int index = -1; //

        while (left < right){
            int mid = left +((right - left))>>2;

            if (arr[mid] >= value){
                index = mid; 
                right = mid-1;
            } else {
                left = mid + 1; 
            }
            
        }

        return index;
    }
}
