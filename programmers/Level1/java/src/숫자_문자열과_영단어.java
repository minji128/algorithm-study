public class 숫자_문자열과_영단어 {
    public static int solution(String s) {
        String[] words ={"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for(int i=0; i<words.length; i++){
            s = s.replaceAll(words[i], Integer.toString(i));
        }
        return Integer.parseInt(s); }
}
