public class Two {
    public static void main (String[] args){
        String[] input = new String[]{

        };
        String [] sample = new String[]{
        };
        // input = sample;
        int aim = 0;
        int horizontal = 0;
        int depth = 0;
        for (String command: input) {
            String[] split = command.split(" ");
            int arg = Integer.parseInt(split[1]);
            switch(split[0]) {
                case "forward": 
                    horizontal += arg;
                    depth += aim * arg;
                    continue;
                case "down":
                    aim += arg;
                    continue;
                case "up":
                    aim -= arg;
                    continue;
            }
        }
        System.out.println(horizontal*depth);

    }
}
