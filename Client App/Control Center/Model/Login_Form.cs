using System;
using System.Windows.Controls;
using System.Windows;


namespace Control_Center.Model
{
    namespace LoginPopup
    {
        public class LoginWindow : Window
        {
            private TextBox txtUsername;
            private PasswordBox txtPassword;

            public string Username { get; private set; }
            public string Password { get; private set; }

            public LoginWindow()
            {
                InitializeComponents();
            }

            private void InitializeComponents()
            {
                Title = "Login";
                Width = 300;
                Height = 200;

                Grid grid = new Grid();
                grid.Margin = new Thickness(10);

                RowDefinition rowDef1 = new RowDefinition();
                RowDefinition rowDef2 = new RowDefinition();
                RowDefinition rowDef3 = new RowDefinition();
                RowDefinition rowDef4 = new RowDefinition();
                RowDefinition rowDef5 = new RowDefinition();
                RowDefinition rowDef6 = new RowDefinition();
                grid.RowDefinitions.Add(rowDef1);
                grid.RowDefinitions.Add(rowDef2);
                grid.RowDefinitions.Add(rowDef3);
                grid.RowDefinitions.Add(rowDef4);
                grid.RowDefinitions.Add(rowDef5);
                grid.RowDefinitions.Add(rowDef6);

                TextBlock lblUsername = new TextBlock();
                lblUsername.Text = "Username:";
                Grid.SetRow(lblUsername, 0);

                txtUsername = new TextBox();
                Grid.SetRow(txtUsername, 1);

                TextBlock lblPassword = new TextBlock();
                lblPassword.Text = "Password:";
                Grid.SetRow(lblPassword, 2);

                txtPassword = new PasswordBox();
                Grid.SetRow(txtPassword, 3);

                Button btnLogin = new Button();
                btnLogin.Content = "Login";
                btnLogin.Click += btnLogin_Click;
                Grid.SetRow(btnLogin, 4);

                Button btnCancel = new Button();
                btnCancel.Content = "Cancel";
                btnCancel.Click += btnCancel_Click;
                Grid.SetRow(btnCancel, 5);

                grid.Children.Add(lblUsername);
                grid.Children.Add(txtUsername);
                grid.Children.Add(lblPassword);
                grid.Children.Add(txtPassword);
                grid.Children.Add(btnLogin);
                grid.Children.Add(btnCancel);

                Content = grid;
            }

            private void btnLogin_Click(object sender, RoutedEventArgs e)
            {
                // Get the entered username and password
                Username = txtUsername.Text;
                Password = txtPassword.Password;

                // Close the dialog box
                DialogResult = true;
            }

            private void btnCancel_Click(object sender, RoutedEventArgs e)
            {
                // Close the dialog box without setting any values
                DialogResult = false;
            }
        }

        public class RegisterWindow : Window
        {
            private TextBox txtUsername;
            private PasswordBox txtPassword;

            public string Username { get; private set; }
            public string Password { get; private set; }

            public RegisterWindow()
            {
                InitializeComponents();
            }

            private void InitializeComponents()
            {

                Title = "Register";
                Width = 300;
                Height = 200;

                Grid grid = new Grid();
                grid.Margin = new Thickness(10);

                RowDefinition rowDef1 = new RowDefinition();
                RowDefinition rowDef2 = new RowDefinition();
                RowDefinition rowDef3 = new RowDefinition();
                RowDefinition rowDef4 = new RowDefinition();
                RowDefinition rowDef5 = new RowDefinition();
                RowDefinition rowDef6 = new RowDefinition();
                grid.RowDefinitions.Add(rowDef1);
                grid.RowDefinitions.Add(rowDef2);
                grid.RowDefinitions.Add(rowDef3);
                grid.RowDefinitions.Add(rowDef4);
                grid.RowDefinitions.Add(rowDef5);
                grid.RowDefinitions.Add(rowDef6);

                TextBlock lblUsername = new TextBlock();
                lblUsername.Text = "Username:";
                Grid.SetRow(lblUsername, 0);

                txtUsername = new TextBox();
                Grid.SetRow(txtUsername, 1);

                TextBlock lblPassword = new TextBlock();
                lblPassword.Text = "Password:";
                Grid.SetRow(lblPassword, 2);

                txtPassword = new PasswordBox();
                Grid.SetRow(txtPassword, 3);

                Button btnRegister = new Button();
                btnRegister.Content = "Register";
                btnRegister.Click += btnRegister_Click;
                Grid.SetRow(btnRegister, 4);

                Button btnCancel = new Button();
                btnCancel.Content = "Cancel";
                btnCancel.Click += btnCancel_Click;
                Grid.SetRow(btnCancel, 5);

                grid.Children.Add(lblUsername);
                grid.Children.Add(txtUsername);
                grid.Children.Add(lblPassword);
                grid.Children.Add(txtPassword);
                grid.Children.Add(btnRegister);
                grid.Children.Add(btnCancel);

                Content = grid;
            }

            private void btnRegister_Click(object sender, RoutedEventArgs e)
            {
                // Get the entered username and password
                Username = txtUsername.Text;
                Password = txtPassword.Password;

                // Close the dialog box
                DialogResult = true;
            }

            private void btnCancel_Click(object sender, RoutedEventArgs e)
            {
                // Close the dialog box without setting any values
                DialogResult = false;
            }
        }
    }
}
