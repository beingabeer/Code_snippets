import java.time.Instant;
import java.time.format.DateTimeFormatter;

public class StackTraceGenerator {
    public static void main(String[] args) {
        try {
            generateStackTrace();
        } catch (Exception e) {
            logStackTrace(e);
        }
    }

    private static void generateStackTrace() {
        recursiveMethod(10);
    }

    private static void recursiveMethod(int count) {
        if (count <= 0) {
            throw new RuntimeException("Stack trace generation complete.");
        }
        recursiveMethod(count - 1);
    }

    private static void logStackTrace(Exception e) {
        Instant timestamp = Instant.now();
        String formattedTimestamp = DateTimeFormatter.ISO_INSTANT.format(timestamp);

        StringBuilder sb = new StringBuilder();
        sb.append(formattedTimestamp).append(" Stack trace:\n");
        StackTraceElement[] stackTrace = e.getStackTrace();
        for (StackTraceElement element : stackTrace) {
            sb.append("\tat ").append(element).append("\n");
        }
        
        System.out.println(sb.toString());
    }
}
