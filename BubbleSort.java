public class BubbleSort {

	public static void main(String[] args) {
		int i, j, temp;
        int[] array = {5, 6, 81, 55, 346, 151, 21, 21, 32, 65, 5, 666, 999};
        System.out.println("Unsorted array:");
        for(i = 0; i < array.length; i++)
            System.out.printf("%d ", array[i]);
        System.out.println();
        for(i = 0; i < array.length; i++)
        {
            for(j = 0; j < array.length; j++)
            {
                if(array[j + 1] < array[j])
                {
                    temp = array[j + 1];
                    array[j + 1] = array[j];
                    array[j] = temp;
                }
            }
        }
        System.out.println("Sorted array:");
        for(i = 0; i < array.length; i++)
            System.out.printf("%d ", array[i]);
	}

}
