import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CSC372_GUI {
    // Connection to BankAccount 
    private BankAccount account = new BankAccount();
    // GUI Componenets 
    private JFrame frame;
    private JPanel panel;
    private JLabel balanceLabel;
    private JTextField amountField;
    private JButton depositButton;
    private JButton withdrawButton;
    private JButton exitButton;

    public CSC372_GUI() {
        // Main window
        frame = new JFrame( "Bank Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        // Panel that holds everything
        panel = new JPanel();
        panel.setLayout(new FlowLayout());
        // Activates components
        balanceLabel = new JLabel("Balance: $" + account.getBalance());
        amountField = new JTextField(10);
        depositButton = new JButton("Deposit");
        withdrawButton = new JButton("Withdraw");
        exitButton = new JButton("Exit");
        // Adds the components to the panel
        panel.add(balanceLabel);
        panel.add(new JLabel("Amount:"));
        panel.add(amountField);
        panel.add(depositButton);
        panel.add(withdrawButton);
        panel.add(exitButton);
        // Logic for deposit button
        depositButton.addActionListener(new ActionListener() {
            @Override 
            public void actionPerformed(ActionEvent e) {
                double amount = Double.parseDouble(amountField.getText());
                account.deposit(amount);
                balanceLabel.setText("Balamce: $" + account.getBalance());
                amountField.setText("");
            }
        });
        // Logic for withdraw button
        withdrawButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                double amount = Double.parseDouble(amountField.getText());
                account.withdraw(amount);
                balanceLabel.setText("Balance: $" + account.getBalance());
                amountField.setText("");
            }
        });
        // Logic for exit button
        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(frame, "FInal Balance: $" + account.getBalance(), "Exiting", JOptionPane.INFORMATION_MESSAGE);
                System.exit(0);
            }  
        });
        // connects panel to the frame and makes it visible
        frame.add(panel);
        frame.setVisible(true);

    }
    // Runs GUI Application
    public static void main(String[] args) {

        new CSC372_GUI();  
    }
}