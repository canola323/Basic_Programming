import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Random;

public class MenuApplication extends JFrame {

    private JTextArea textArea;
    private Random random = new Random();

    public MenuApplication() {
        setTitle("Menu Application");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Text Area
        textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        add(scrollPane, BorderLayout.CENTER);

        // Menu Bar
        JMenuBar menuBar = new JMenuBar();
        JMenu menu = new JMenu("Menu");

        JMenuItem dateTimeItem = new JMenuItem("Show Date and Time");
        JMenuItem saveItem = new JMenuItem("Save to log.txt");
        JMenuItem colorItem = new JMenuItem("Random Green Background");
        JMenuItem exitItem = new JMenuItem("Exit");

        // First Menu Item
        dateTimeItem.addActionListener(e -> {
            DateTimeFormatter formatter =
                    DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
            String currentDateTime =
                    LocalDateTime.now().format(formatter);

            textArea.setText(currentDateTime);
        });

        // Second Menu Item
        saveItem.addActionListener(e -> {
            try (FileWriter writer = new FileWriter("log.txt")) {
                writer.write(textArea.getText());
                JOptionPane.showMessageDialog(this,
                        "Text saved to log.txt");
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this,
                        "Error saving file.");
            }
        });

        // Third Menu Item
        colorItem.addActionListener(e -> {
            // Random green shade
            int red = random.nextInt(60);
            int green = 150 + random.nextInt(106);
            int blue = random.nextInt(60);

            getContentPane().setBackground(new Color(red, green, blue));
        });

        // Fourth Menu Item
        exitItem.addActionListener(e -> System.exit(0));

        // Add menu items
        menu.add(dateTimeItem);
        menu.add(saveItem);
        menu.add(colorItem);
        menu.add(exitItem);

        menuBar.add(menu);
        setJMenuBar(menuBar);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            MenuApplication app = new MenuApplication();
            app.setVisible(true);
        });
    }
}