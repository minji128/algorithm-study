public class 음양더하기 {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;

        for(int i=0; i<signs.length; i++){
            if(!signs[i]){
                absolutes[i] = absolutes[i] * (-1);
            }
            answer += absolutes[i];
        }
        return answer;
    }
}
