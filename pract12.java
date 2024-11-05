import java.net.*;
import java.util.Scanner;

public class pract12 {

    public static void main(String[] args) {
        String host;
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("1. Enter Host Name\n2. Enter IP address\nChoice= ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character

            if (choice == 1) {
                System.out.print("\nEnter host name: ");
                host = scanner.nextLine();
                try {
                    InetAddress address = InetAddress.getByName(host);
                    System.out.println("IP address: " + address.getHostAddress());
                    System.out.println("Host name: " + address.getHostName());
                    System.out.println("Host name and IP address: " + address.toString());
                } catch (UnknownHostException ex) {
                    System.out.println("Could not find host: " + host);
                }
            } else if (choice == 2) {
                System.out.print("\nEnter IP address: ");
                host = scanner.nextLine();
                try {
                    InetAddress address = InetAddress.getByName(host);
                    System.out.println("Host name: " + address.getHostName());
                    System.out.println("IP address: " + address.getHostAddress());
                    System.out.println("Host name and IP address: " + address.toString());
                } catch (UnknownHostException ex) {
                    System.out.println("Could not find IP address: " + host);
                }
            } else {
                System.out.println("Invalid choice. Please enter 1 or 2.");
            }
        }
    }
}