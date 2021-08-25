
public class BubbleSort {

    public static void main(String[] Args) {

        int[] arr = { 1, 5, 2, 3, 4, 6 };
        bubbleSort(arr);
        System.out.println(arr.toString());
        foreach ( int i : arr){
            System.out.print(i+'\t');
        }

        

    }

    public static void bubbleSort(int[] arr) {
        if (arr == null || arr.length < 2) {
            return;
        }

        for (int n = arr.length - 1; n > 0; n--) {
            for (int i = 0; i < n; i++) {
                if (arr[i] > arr[i + 1]) {
                    swap(arr, i, i + 1);
                }
            }
        }
    }

    public static void swap(int[] arr, int i, int j) {
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    }

}
