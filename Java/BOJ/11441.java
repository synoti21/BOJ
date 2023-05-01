import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static int sol(int start, int end, int[] arr){
        int sum = 0;
        for (int i = start-1; i < end; i++){
            sum += arr[i];
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i =0 ;i < n ;i ++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int m = Integer.parseInt(br.readLine());

        int start, end;
        for (int i =0 ;i < m ; i ++){
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            System.out.println(Integer.toString(sol(start, end, arr)));
        }
        bw.flush();
        br.close();
        bw.close();
    }
}