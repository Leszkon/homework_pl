class Main {
    static float NWD(float a, float b) {
        float c;
        while (b != 0){
            c = a % b;
            a = b;
            b = c;
        }
        return a;
    }
    public static void main(String[] args) {
        System.out.println(NWD(10, 22));
    }
}
