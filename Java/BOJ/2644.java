import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Pair{
    private int x;
    private int y;

    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
    public int getX(){
        return this.x;
    }
    public int getY(){
        return this.y;
    }
}

public class Main{
    static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    static int n, f_target, s_target,m;
    static Queue<Pair> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n+1; i++){
            arr.add(new ArrayList<Integer>());
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        f_target = Integer.parseInt(st.nextToken());
        s_target = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(br.readLine());

        for (int i =0 ;i < m ; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(a).add(b);
            arr.get(b).add(a);
        }
        System.out.println(sol());
    }

    public static int sol(){
        int ans = 0;
        Pair new_node, now_node;
        boolean[] visited = new boolean[n+1];
        queue.add(new Pair(f_target,ans));
        visited[f_target] = true;

        while (!queue.isEmpty()){
            now_node = queue.poll();
            int now = now_node.getX();
            int count = now_node.getY();

            if (now == s_target){
                return count;
            }
            for (int i =0 ;i < arr.get(now).size(); i++){
                int new_n = arr.get(now).get(i);
                new_node = new Pair(new_n,count+1);
                if (!visited[new_n]){
                    queue.add(new_node);
                    visited[new_n] = true;
                }
            }
        }
        return -1;
    }
}